"""Unit tests for the calculator app."""
import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, _ = capfd.readouterr()

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Hello World. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World. Type 'exit' to exit." in out
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_add_command(capfd, monkeypatch):
    """Test adding numbers using the 'add' command."""
    inputs = iter(['add 2 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Result: 7" in out

def test_subtract_command(capfd, monkeypatch):
    """Test subtracting numbers using the 'subtract' command."""
    inputs = iter(['subtract 10 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Result: 7" in out

def test_multiply_command(capfd, monkeypatch):
    """Test multiplying numbers using the 'multiply' command."""
    inputs = iter(['multiply 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Result: 6" in out

def test_divide_command(capfd, monkeypatch):
    """Test dividing numbers using the 'divide' command."""
    inputs = iter(['divide 6 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Result: 3" in out

def test_menu_command(capfd, monkeypatch):
    """Test displaying the menu using the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Available commands:" in out

def test_divide_by_zero(capfd, monkeypatch):
    """Test divide by zero error handling."""
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: Division by zero is not allowed." in out

def test_invalid_number(capfd, monkeypatch):
    """Test error handling for non-numeric input."""
    inputs = iter(['add 10 two', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numbers." in out

def test_exit_command(capfd, monkeypatch):
    """Test the exit command triggers application exit."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Exiting..." in out

def test_unrecognized_command(capfd, monkeypatch):
    """Test handling of an unrecognized command."""
    inputs = iter(['fake_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Hello World. Type 'exit' to exit." in out

def test_divide_by_zero_command(capfd, monkeypatch):
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: Division by zero is not allowed." in out

def test_multiply_with_invalid_number(capfd, monkeypatch):
    inputs = iter(['multiply 10 two', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numbers." in out

def test_subtract_less_than_two_numbers(capfd, monkeypatch):
    inputs = iter(['subtract 10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: Need at least two numbers to perform subtraction." in out

def test_add_command_with_invalid_arguments(capfd, monkeypatch):
    """
    Test add command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['add 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numbers." in out

def test_subtract_command_with_invalid_arguments(capfd, monkeypatch):
    """
    Test subtract command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['subtract 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numbers." in out

def test_divide_command_with_invalid_arguments(capfd, monkeypatch):
    """
    Test divide command execution with invalid arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['divide 10 two', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numbers." in out

def test_divide_command_with_insufficient_arguments(capfd, monkeypatch):
    """
    Test divide command execution with insufficient arguments.
    Ensure the application exits by providing 'exit' command after the test command.
    """
    inputs = iter(['divide 10', 'exit'])  # Assuming 'add' command as an example
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()  # Start the application, which should now process the invalid command and then exit
    out, _ = capfd.readouterr()
    assert "Error: Need at least two numbers to perform division." in out
