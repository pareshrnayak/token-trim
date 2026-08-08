<p align="center">
  <img src="assets/token-trim-banner.svg" alt="token-trim banner" width="100%">
</p>

# token-trim

[![PyPI Version](https://img.shields.io/pypi/v/token-trim-cli.svg)](https://pypi.org/project/token-trim-cli/)
[![Python Versions](https://img.shields.io/pypi/pyversions/token-trim-cli.svg)](https://pypi.org/project/token-trim-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Intelligently prune Python code and log files to reduce LLM context window usage, save AI tokens, and lower API costs.

`token-trim` is a lightweight command-line utility for optimizing Python code and log files before sending them to Large Language Models (LLMs) and AI coding assistants. Built with **Python**, **AST**, **Typer**, **Rich**, and **tiktoken**, it removes unnecessary content such as docstrings, comments, blank lines, and excess whitespace while preserving valid Python syntax and reporting token savings.

## Overview

Large Language Models (LLMs) process text as tokens. When using AI APIs, token usage can directly affect cost, while large amounts of unnecessary text can consume valuable context window space.

Source code and log files often contain comments, documentation, blank lines, and formatting that may not be necessary when asking an AI assistant to analyze, debug, explain, or modify code.

`token-trim` removes this unnecessary content before you send your code to an LLM. This helps reduce token usage, lower API costs, and fit more useful code within an AI model's context window.

It can be useful when working with AI coding assistants, LLM APIs, and developer tools such as **ChatGPT, Claude, Gemini, OpenAI API, Anthropic API, OpenRouter, Cursor, and Claude Code**.

## Features

* AST-based Python code pruning
* Removes module, class, and function docstrings
* Removes unnecessary comments and blank lines
* Preserves valid Python syntax, including empty function bodies
* Falls back to line-based cleanup for non-Python files, such as logs
* Reports token counts before and after pruning
* Calculates token savings and percentage reduction
* Copies pruned output directly to the system clipboard (`-c`, `--copy`)
* Supports recursive directory and batch processing
* Supports in-place file overwriting (`-w`, `--write`)
* Uses `tiktoken` to measure token usage
* Clean and user-friendly command-line interface powered by **Rich** and **Typer**
* Designed for preparing source code and logs for LLM prompts and AI-assisted coding workflows

## Why Token Optimization Matters

AI coding tools are increasingly used for code generation, debugging, code review, refactoring, and documentation. However, the amount of code and text sent to an LLM can affect both context usage and API costs.

For example, a Python project may contain:

* Long docstrings
* Comments that are not relevant to the current task
* Large numbers of blank lines
* Unnecessary formatting
* Log output and repeated whitespace

When this information is not useful for the AI's task, sending it wastes part of the available context.

`token-trim` provides a simple way to clean this content before sending it to an LLM or AI coding assistant.

## How It Works

For Python files, `token-trim`:

1. Parses the source code using Python's built-in `ast` module.
2. Traverses the Abstract Syntax Tree (AST).
3. Removes module, class, and function docstrings.
4. Removes unnecessary comments and formatting.
5. Reconstructs valid Python code using `ast.unparse()`.
6. Calculates token counts before and after pruning using `tiktoken`.
7. Reports the number and percentage of tokens saved.

If the input is not valid Python, `token-trim` automatically switches to line-based cleanup that removes comments, blank lines, and unnecessary whitespace.

This makes the tool useful not only for Python source code but also for log files and other text-based files that may contain unnecessary content.

## Installation

### Install from PyPI

```bash
pip install token-trim-cli
```

Verify the installation:

```bash
token-trim --help
```

## Usage

### Basic Usage

Prune a Python file or log file.

```bash
token-trim path/to/file.py
```

This produces a cleaned version of the file and reports the original token count, pruned token count, and total token savings.

### Copy Output to the Clipboard

Copy the pruned output directly to your system clipboard.

```bash
token-trim path/to/file.py --copy
```

or

```bash
token-trim path/to/file.py -c
```

This is useful when preparing code to paste into an AI assistant such as ChatGPT, Claude, Gemini, Cursor, or Claude Code.

### Overwrite the Original File

Replace the original file with the pruned version.

```bash
token-trim path/to/file.py --write
```

or

```bash
token-trim path/to/file.py -w
```

### Specify a Tokenizer Model

By default, `token-trim` uses the `gpt-4o` tokenizer.

Use a different tokenizer model:

```bash
token-trim path/to/file.py --model gpt-3.5-turbo
```

or

```bash
token-trim path/to/file.py -m gpt-3.5-turbo
```

### Process an Entire Directory

Recursively prune all supported files within a directory.

```bash
token-trim path/to/folder/
```

This makes it possible to process multiple Python source files and supported text or log files in a single command.

### View Available Options

```bash
token-trim --help
```

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

## AI Coding and LLM Use Cases

`token-trim` is designed for developers who work with AI-assisted programming and Large Language Models.

It can be used before sending source code, logs, or other text to:

* **ChatGPT** for code analysis, debugging, refactoring, and code generation
* **Claude** for large codebase analysis and AI-assisted development
* **Gemini** for code analysis and development workflows
* **OpenAI API** applications where input token usage affects cost
* **Anthropic API** applications that process source code or logs
* **OpenRouter** workflows using different LLM providers
* **Cursor** and other AI-powered code editors
* **Claude Code** workflows where large amounts of source code may be provided to an AI coding agent

`token-trim` does not require a connection to these services. It works locally as a preprocessing tool: clean your code first, then send the resulting output to the AI tool or API of your choice.

## Tech Stack

* Python
* AST (`ast`)
* Typer
* Rich
* tiktoken

## Contributing

Contributions are welcome.

If you'd like to contribute, please read **CONTRIBUTING.md** for instructions on setting up a development environment, running tests, and submitting pull requests.

Ideas, bug reports, feature requests, documentation improvements, and code contributions are all welcome.

## License

This project is licensed under the MIT License. See the **LICENSE** file for more information.

