import ast
import typer
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
import tiktoken

app = typer.Typer(help="Token-Trim: Intelligently prune code to save LLM context window tokens.")
console = Console()

class DocstringAndCommentStripper(ast.NodeTransformer):
    """AST Visitor that removes docstrings and cleans up unnecessary AST nodes."""
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        # 1. Fixed ast.Str deprecation & checked if docstring is the only node in body
        if (node.body and isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)):
            if len(node.body) > 1:
                node.body.pop(0)
            else:
                # Keep 'pass' if docstring was the only statement in function
                node.body[0] = ast.Pass()
        return node

    def visit_AsyncFunctionDef(self, node):
        """2. Added support for async functions."""
        return self.visit_FunctionDef(node)

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        if (node.body and isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)):
            if len(node.body) > 1:
                node.body.pop(0)
            else:
                node.body[0] = ast.Pass()
        return node

    def visit_Module(self, node):
        """3. Added support for stripping module-level docstrings at the top of files."""
        self.generic_visit(node)
        if (node.body and isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)):
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
    file_path: str = typer.Argument(..., help="Path to the code or log file to prune"),
    model: str = typer.Option("gpt-4o", "--model", "-m", help="LLM model tokenizer target"),
):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File '{file_path}' not found.")
        raise typer.Exit(1)

    orig_tokens = count_tokens(original_code, model)
    pruned_code = prune_python_code(original_code)
    new_tokens = count_tokens(pruned_code, model)

    saved_tokens = orig_tokens - new_tokens
    pct_saved = (saved_tokens / orig_tokens * 100) if orig_tokens > 0 else 0

    console.print(Panel.fit("[bold green]Token-Trim Execution Complete[/bold green]"))
    console.print(f"[bold]Original Tokens:[/bold] {orig_tokens}")
    console.print(f"[bold]Pruned Tokens:[/bold]   {new_tokens}")
    console.print(f"[bold yellow]Tokens Saved:[/bold yellow]   {saved_tokens} ({pct_saved:.1f}% reduction)\n")

    console.print("[bold cyan]Pruned Output Preview:[/bold cyan]")
    syntax = Syntax(pruned_code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

if __name__ == "__main__":
    app()