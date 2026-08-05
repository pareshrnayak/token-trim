# token-trim

Intelligently prune Python code and log files to reduce LLM context window usage and lower API costs.

`token-trim` is a lightweight command-line tool built with Python, `ast`, `typer`, and `rich`. It removes docstrings, strips comments, normalizes whitespace, and calculates token savings using OpenAI's `tiktoken`.

---

## Overview

Large Language Models (LLMs) have limited context windows and charge based on the number of input tokens. Source code often contains docstrings, comments, and formatting that increase token usage without affecting execution.

`token-trim` removes this unnecessary content while preserving the program's behavior, helping reduce token consumption before sending code to an LLM.

## Features

* AST-based Python code pruning
* Removes module, class, and function docstrings
* Preserves valid Python syntax, including empty function bodies
* Falls back to line-based cleaning for non-Python files (such as logs)
* Reports token counts before and after pruning
* Calculates percentage of tokens saved
* Clean command-line interface powered by `rich`

---

## How It Works

1. Parses Python source code using the built-in `ast` module.
2. Traverses the Abstract Syntax Tree to remove module, class, and function docstrings.
3. Reconstructs valid Python code using `ast.unparse()`.
4. Uses `tiktoken` to measure token counts before and after pruning.

If the input is not valid Python, `token-trim` automatically falls back to a line-based cleanup that removes comments, blank lines, and unnecessary whitespace.

---

## Installation

### Requirements

* Python 3.9 or later

### Clone the Repository

```bash
git clone https://github.com/your-username/token-trim.git
cd token-trim
```

### Create a Virtual Environment (Recommended)

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Usage

Prune a Python file or log file and display token savings.

```bash
python app.py path/to/file.py
```

### Specify a Tokenizer Model

By default, `token-trim` uses the `gpt-4o` tokenizer.

```bash
python app.py path/to/file.py --model gpt-3.5-turbo
```

or

```bash
python app.py path/to/file.py -m gpt-3.5-turbo
```

### View Available Options

```bash
python app.py --help
```

---

## Example Output

```text
╭────────────────────── Token-Trim Execution Complete ──────────────────────╮
Original Tokens: 758
Pruned Tokens:   670
Tokens Saved:    88 (11.6% reduction)

Pruned Output Preview:

  1 | import ast
  2 | import typer
  3 | from rich.console import Console
  ...
╰────────────────────────────────────────────────────────────────────────────╯
```

---

## Tech Stack

* Python
* ast
* typer
* rich
* tiktoken
