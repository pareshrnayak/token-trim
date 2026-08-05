import ast
import os
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
import tiktoken

try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False

app = typer.Typer(
    help="Token-Trim: Intelligently prune code to save LLM context window tokens.",
    add_completion=False
)
console = Console()

class DocstringAndCommentStripper(ast.NodeTransformer):
    """AST Visitor that removes docstrings and cleans up unnecessary AST nodes."""
    
    def _strip_docstring(self, node):
        if (node.body and isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and 
            isinstance(node.body[0].value.value, str)):
            if len(node.body) > 1:
                node.body.pop(0)
            else:
                node.body[0] = ast.Pass()
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return self._strip_docstring(node)

    def visit_AsyncFunctionDef(self, node):
        self.generic_visit(node)
        return self._strip_docstring(node)

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        return self._strip_docstring(node)

    def visit_Module(self, node):
        self.generic_visit(node)
        if (node.body and isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and 
            isinstance(node.body[0].value.value, str)):
            node.body.pop(0)
        return node

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def prune_python_code(source_code: str) -> str:
    try:
        tree = ast.parse(source_code)
        stripper = DocstringAndCommentStripper()
        cleaned_tree = stripper.visit(tree)
        ast.fix_missing_locations(cleaned_tree)
        return ast.unparse(cleaned_tree)
    except SyntaxError:
        lines = source_code.splitlines()
        non_empty = [line for line in lines if line.strip() and not line.strip().startswith("#")]
        return "\n".join(non_empty)

@app.command()
def prune(
    target: str = typer.Argument(..., help="Path to a Python file or directory to prune"),
    model: str = typer.Option("gpt-4o", "--model", "-m", help="LLM model tokenizer target"),
    copy: bool = typer.Option(False, "--copy", "-c", help="Copy pruned code directly to system clipboard"),
    write: bool = typer.Option(False, "--write", "-w", help="Overwrite the original file with pruned code"),
):
    """Prune Python files/directories and display token savings."""
    target_path = Path(target)

    if not target_path.exists():
        console.print(f"[bold red]Error:[/bold red] Path '{target}' does not exist.")
        raise typer.Exit(1)

    files_to_process = []
    if target_path.is_file():
        files_to_process.append(target_path)
    elif target_path.is_dir():
        files_to_process.extend([p for p in target_path.rglob("*.py") if p.is_file()])

    if not files_to_process:
        console.print(f"[bold yellow]Warning:[/bold yellow] No Python files found at '{target}'.")
        raise typer.Exit(0)

    total_orig = 0
    total_new = 0
    last_pruned_code = ""

    table = Table(title="Token Savings Summary", show_header=True, header_style="bold magenta")
    table.add_column("File", style="dim", width=30)
    table.add_column("Original", justify="right")
    table.add_column("Pruned", justify="right")
    table.add_column("Savings", justify="right", style="green")

    for file_p in files_to_process:
        try:
            with open(file_p, "r", encoding="utf-8") as f:
                original_code = f.read()
        except Exception as e:
            console.print(f"[red]Failed to read {file_p}: {e}[/red]")
            continue

        orig_tokens = count_tokens(original_code, model)
        pruned_code = prune_python_code(original_code)
        new_tokens = count_tokens(pruned_code, model)

        total_orig += orig_tokens
        total_new += new_tokens
        last_pruned_code = pruned_code

        saved = orig_tokens - new_tokens
        pct = (saved / orig_tokens * 100) if orig_tokens > 0 else 0
        table.add_row(file_p.name, str(orig_tokens), str(new_tokens), f"{saved} ({pct:.1f}%)")

        if write:
            with open(file_p, "w", encoding="utf-8") as f:
                f.write(pruned_code)

    saved_tokens = total_orig - total_new
    pct_saved = (saved_tokens / total_orig * 100) if total_orig > 0 else 0

    console.print(Panel.fit("[bold green]Token-Trim Execution Complete[/bold green]"))
    console.print(table)
    console.print(f"\n[bold yellow]Total Tokens Saved:[/bold yellow] {saved_tokens} ({pct_saved:.1f}% reduction)\n")

    if copy:
        if HAS_PYPERCLIP:
            pyperclip.copy(last_pruned_code)
            console.print("[bold green]✓ Pruned code copied to system clipboard![/bold green]\n")
        else:
            console.print("[bold red]x Pyperclip is not installed. Run 'pip install pyperclip' to enable clipboard support.[/bold red]\n")

    if len(files_to_process) == 1 and not write:
        console.print("[bold cyan]Pruned Output Preview:[/bold cyan]")
        syntax = Syntax(last_pruned_code, "python", theme="monokai", line_numbers=True)
        console.print(syntax)

if __name__ == "__main__":
    app()