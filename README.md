# IS601 Enhanced Calculator — Midterm Project

## Overview

This project is an enhanced Python command-line calculator developed for IS601 at the New Jersey Institute of Technology (NJIT).

The application was originally developed during Module 5 and expanded for the midterm project with additional arithmetic operations, improved error handling, and comprehensive logging.

The project demonstrates object-oriented programming, software design patterns, persistent calculation history, and automated testing.

## Features

### Calculator Operations

The calculator supports 10 arithmetic operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Root
7. Modulus
8. Integer Division
9. Percentage
10. Absolute Difference

### Additional Features

- Interactive command-line interface (REPL)
- Factory and Strategy design patterns
- Observer pattern for automatic history saving
- Memento pattern for undo and redo
- Facade pattern for simplified calculator interaction
- Pandas DataFrame history management
- CSV saving and loading
- Environment-based configuration
- Custom exception handling and input validation
- Logging for successful calculations and errors
- Automated testing with pytest
- 100% test coverage
- GitHub Actions continuous integration

### Optional Feature: Color-Coded Outputs

The calculator uses Colorama to improve the command-line interface.

- Green displays successful calculation results.
- Red displays error messages.
- Cyan displays welcome messages and instructions.

This feature improves readability and helps users distinguish successful operations from errors.

## Installation

Clone the GitHub repository:

```bash
git clone https://github.com/sandhuharnoor/IS601-Midterm-Enhanced-Calculator.git
```

Navigate to the project directory:

```bash
cd IS601-Midterm-Enhanced-Calculator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Calculator

Start the calculator using:

```bash
python -m app.calculator_repl
```

The application displays:

```text
Enhanced Professional Calculator
Type 'help' for available commands.
```

Enter commands to perform calculations.

## Example Commands

### Basic Operations

```text
add 10 5
subtract 10 5
multiply 10 5
divide 10 5
```

### Advanced Operations

```text
power 2 3
root 16 2
modulus 10 3
int_divide 10 3
percent 25 200
abs_diff 10 25
```

### Example Results

```text
>>> modulus 10 3
Result: 1.0

>>> int_divide 10 3
Result: 3.0

>>> percent 25 200
Result: 12.5

>>> abs_diff 10 25
Result: 15.0
```

### History Commands

```text
history
undo
redo
clear
save
load
help
exit
```

These commands allow users to manage calculation history, undo or redo changes, save calculations, and exit the application.

## Error Handling

The calculator uses custom exceptions to handle invalid inputs and arithmetic errors.

Examples include:

- Division by zero
- Modulus by zero
- Invalid calculator operations
- Invalid numerical inputs
- Unsupported mathematical operations
- Invalid root calculations

Instead of crashing, the application displays an appropriate error message.

## Logging Implementation

The midterm project includes logging using Python's built-in `logging` module.

Logging configuration is implemented in:

```text
app/logger.py
```

Logs are saved to:

```text
logs/calculator.log
```

The application records information about calculator operations and errors.

### Logging Levels

**INFO:** Records successful calculations and other normal application activities.

**WARNING:** Records failed calculations and handled errors.

### Example Log Entries

```text
2026-10-28 12:00:00,000 - INFO - Calculation successful: add(10.0, 5.0) = 15.0

2026-10-28 12:01:00,000 - WARNING - Calculation failed: divide(10.0, 0.0) - Cannot divide by zero
```

These examples illustrate the expected log format.

## Design Patterns

The calculator uses several software design patterns.

**Factory Pattern:** Creates arithmetic operation objects based on the user's selected command.

**Strategy Pattern:** Allows different arithmetic operations to use a common interface.

**Observer Pattern:** Automatically saves calculation history when changes occur.

**Memento Pattern:** Supports undo and redo functionality by storing previous history states.

**Facade Pattern:** Provides a simplified interface for interacting with the calculator.

These patterns help organize the code and make the application easier to maintain and expand.

## Testing

The project uses pytest for automated testing.

Tests cover:

- Basic arithmetic operations
- Advanced arithmetic operations
- Invalid inputs
- Division and modulus by zero
- Operation factory functionality
- Calculator history
- Undo and redo functionality
- Logging behavior
- Exception handling
- Command-line interface functionality

Run the test suite:

```bash
pytest -q
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Enforce 100% coverage:

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=100
```

### Test Results

The latest local test run completed with:

- **198 tests passed**
- **100% code coverage**
- **0 failed tests**

One runtime warning was reported during testing, but it did not cause any test failures.

## Continuous Integration

GitHub Actions automatically runs the project's test workflow when code is pushed to the main branch or a pull request is opened.

The workflow verifies that the tests pass and enforces the required coverage threshold.

The latest GitHub Actions workflow completed successfully.

## Technologies

- Python 3.12
- pandas
- python-dotenv
- pytest
- pytest-cov
- Python logging module
- Git and GitHub
- GitHub Actions
- Visual Studio Code

## Author

Harnoor Sandhu  
New Jersey Institute of Technology (NJIT)  
IS601 — Python for Web APIs