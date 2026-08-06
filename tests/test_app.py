import ast
import pytest
from typer.testing import CliRunner
from app import app, count_tokens, prune_python_code

runner = CliRunner()


def test_remove_docstrings_and_comments():
    raw_code = '''
def calculate_sum(a, b):
    """This function adds two numbers together."""
    # Add a and b
    return a + b
'''
    pruned_code = prune_python_code(raw_code)

    assert "This function adds two numbers" not in pruned_code
    assert "return a + b" in pruned_code


def test_preserve_valid_syntax_empty_function():
    raw_code = '''
def empty_function():
    """Docstring only function."""
'''
    pruned_code = prune_python_code(raw_code)

    # Verify that AST visitor added ast.Pass() and code remains valid syntax
    compiled_ast = ast.parse(pruned_code)
    assert compiled_ast is not None
    assert "def empty_function():" in pruned_code
    assert "pass" in pruned_code


def test_count_tokens():
    text = "def hello(): print('world')"
    token_count = count_tokens(text)

    assert isinstance(token_count, int)
    assert token_count > 0


def test_cli_prune_command(tmp_path):
    # Create a temporary test python file
    test_file = tmp_path / "sample.py"
    test_file.write_text('def add(a, b):\n    """Adds a and b"""\n    return a + b\n')

    result = runner.invoke(app, [str(test_file)])
    assert result.exit_code == 0
    assert "Token-Trim Execution Complete" in result.output