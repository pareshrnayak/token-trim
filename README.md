<p align="center">
  <img src="assets/token-trim-banner.svg" alt="token-trim banner" width="100%">
</p>

# token-trim

Intelligently prune Python code and log files to reduce LLM context window usage and lower API costs.

`token-trim` is a lightweight command-line utility built with **Python**, **AST**, **Typer**, **Rich**, and **tiktoken**. It removes docstrings, strips comments, normalizes whitespace, and measures token savings while preserving valid Python syntax.

---

## Overview

Large Language Models (LLMs) have limited context windows and typically charge based on the number of input tokens. Python source files often contain docstrings, comments, blank lines, and formatting that increase token usage without affecting program execution.

`token-trim` removes unnecessary content while preserving the behavior of your code, making it ideal for preparing files before sending them to an LLM.

---

## Features

- AST-based Python code pruning
- Removes module, class, and function docstrings
- Preserves valid Python syntax, including empty function bodies
- Falls back to line-based cleaning for non-Python files (such as logs)
- Reports token counts before and after pruning
- Calculates token savings and percentage reduction
- Supports copying pruned output directly to the clipboard (`-c`, `--copy`)
- Supports recursive directory and batch processing
- Supports overwriting files in place (`-w`, `--write`)
- Clean command-line interface powered by **Rich** and **Typer**

---

## How It Works

For Python files, `token-trim`:

1. Parses source code using Python's built-in `ast` module.
2. Traverses the Abstract Syntax Tree (AST).
3. Removes module, class, and function docstrings.
4. Reconstructs valid Python code using `ast.unparse()`.
5. Calculates token counts before and after pruning using `tiktoken`.

If the input is not valid Python, `token-trim` automatically switches to a line-based cleanup that removes comments, blank lines, and unnecessary whitespace.

---

## Installation

### Requirements

- Python 3.8 or later

### Clone the Repository

```bash
git clone https://github.com/pareshrnayak/token-trim.git
cd token-trim
```

### Create a Virtual Environment (Recommended)

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Install the Package

Install `token-trim` in editable mode:

```bash
pip install -e .
```

Install with development dependencies:

```bash
pip install -e .[dev]
```

---

## Usage

### Basic Usage

Prune a Python file or log file:

```bash
token-trim path/to/file.py
```

### Copy Output to the Clipboard

Copy the pruned output directly to your system clipboard.

```bash
token-trim path/to/file.py --copy
```

or

```bash
token-trim path/to/file.py -c
```

---

### Overwrite the Original File

Replace the original file with the pruned version.

```bash
token-trim path/to/file.py --write
```

or

```bash
token-trim path/to/file.py -w
```

---

### Specify a Tokenizer Model

By default, `token-trim` uses the `gpt-4o` tokenizer.

Use a different tokenizer:

```bash
token-trim path/to/file.py --model gpt-3.5-turbo
```

or

```bash
token-trim path/to/file.py -m gpt-3.5-turbo
```

---

### Process an Entire Directory

Recursively prune all supported files in a directory.

```bash
token-trim path/to/folder/
```

---

### View Available Options

```bash
token-trim --help
```

---

## Example Output

```text
╭────────────────────── Token-Trim Execution Complete ──────────────────────╮
│ Original Tokens: 758                                                      │
│ Pruned Tokens:   670                                                      │
│ Tokens Saved:    88 (11.6% reduction)                                     │
│                                                                           │
│ Pruned Output Preview:                                                    │
│                                                                           │
│   1 │ import ast                                                          │
│   2 │ import typer                                                        │
│   3 │ from rich.console import Console                                    │
│   ...                                                                     │
╰───────────────────────────────────────────────────────────────────────────╯
```

---

## Development

### Run Unit Tests

```bash
pytest
```

### Run the Linter

```bash
ruff check .
```

### Format the Code

```bash
black .
```

### Build Package Distributions

```bash
python -m build
```

---

## Tech Stack

- Python
- AST (`ast`)
- Typer
- Rich
- tiktoken

---

## Contributing

Contributions are welcome.

Please read the project's **CONTRIBUTING.md** before opening an issue or submitting a pull request.

---

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.

