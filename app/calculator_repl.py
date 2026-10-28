"""Enhanced calculator REPL with advanced design patterns and logging."""

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import MementoManager
from app.exceptions import CalculatorError
from app.history import HistoryManager
from app.input_validators import validate_arguments
from app.logger import logger
from colorama import Fore, Style, init

init(autoreset=True)


class HistoryObserver:
    """Observer that automatically saves calculation history."""

    def __init__(self, history, enabled=True):
        self.history = history
        self.enabled = enabled

    def update(self, event):
        if self.enabled:
            self.history.save()


class Calculator:
    """Facade providing a simplified calculator interface."""

    def __init__(self, config=None):
        self.config = config or CalculatorConfig.from_env()

        self.history = HistoryManager(
            self.config.history_file,
            self.config.max_history,
        )

        self.mementos = MementoManager()

        self.observers = [
            HistoryObserver(
                self.history,
                self.config.auto_save,
            )
        ]

        self.history.load()

    def notify(self, event):
        """Notify all registered observers."""
        for observer in self.observers:
            observer.update(event)

    def calculate(self, operation, a, b):
        """Perform a calculation and log the result."""
        try:
            calculation = Calculation.create(
                operation, a, b
            )

            self.mementos.save(
                self.history.get_records()
            )

            self.history.add(calculation)
            self.notify("calculation")

            logger.info(
                "Calculation successful: %s(%s, %s) = %s",
                operation,
                a,
                b,
                calculation.result,
            )

            return calculation.result

        except CalculatorError as exc:
            logger.warning(
                "Calculation failed: %s(%s, %s) - %s",
                operation,
                a,
                b,
                exc,
            )
            raise

    def clear(self):
        """Clear calculation history."""
        self.mementos.save(
            self.history.get_records()
        )

        self.history.clear()
        self.notify("clear")

        logger.info("Calculation history cleared.")

    def undo(self):
        """Undo the previous history change."""
        previous = self.mementos.undo(
            self.history.get_records()
        )

        if previous is None:
            logger.info("Undo requested with no available history.")
            return False

        self.history.restore(previous)
        self.notify("undo")

        logger.info("Undo operation completed successfully.")
        return True

    def redo(self):
        """Redo the last undone history change."""
        next_state = self.mementos.redo(
            self.history.get_records()
        )

        if next_state is None:
            logger.info("Redo requested with no available history.")
            return False

        self.history.restore(next_state)
        self.notify("redo")

        logger.info("Redo operation completed successfully.")
        return True

    def save(self):
        """Save calculation history."""
        self.history.save()
        logger.info("Calculation history saved.")

    def load(self):
        """Load calculation history."""
        self.mementos.save(
            self.history.get_records()
        )

        loaded = self.history.load()

        if loaded:
            logger.info("Calculation history loaded.")
        else:
            logger.warning("No history file found to load.")

        return loaded

    def help(self):
        """Display available calculator commands."""
        return """
Available Commands:
  add <a> <b>        Addition
  subtract <a> <b>   Subtraction
  multiply <a> <b>   Multiplication
  divide <a> <b>     Division
  power <a> <b>      Exponentiation
  root <a> <b>       Calculate the b-th root of a
  modulus <a> <b>    Remainder after division
  int_divide <a> <b> Integer division
  percent <a> <b>    Calculate a as a percentage of b
  abs_diff <a> <b>   Absolute difference between two numbers

  history            Display calculation history
  stats              Display calculation statistics
  clear              Clear calculation history
  undo               Undo last history change
  redo               Redo last undone change
  save               Save history to CSV
  load               Load history from CSV
  help               Display available commands
  exit               Exit the calculator
"""


def repl():
    """Run the interactive calculator."""
    calculator = Calculator()

    print(f"{Fore.CYAN}Enhanced Professional Calculator{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type 'help' for available commands.{Style.RESET_ALL}")

    logger.info("Calculator application started.")

    while True:
        try:
            user_input = input("\n>>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                logger.info("Calculator application exited.")
                print("Goodbye!")
                break

            if command == "help":
                print(calculator.help())
                continue

            if command == "history":
                print(calculator.history.display())
                continue

            if command == "stats":
                print(calculator.history.statistics())
                continue

            if command == "clear":
                calculator.clear()
                print("History cleared.")
                continue

            if command == "undo":
                print(
                    "Undo successful."
                    if calculator.undo()
                    else "Nothing to undo."
                )
                continue

            if command == "redo":
                print(
                    "Redo successful."
                    if calculator.redo()
                    else "Nothing to redo."
                )
                continue

            if command == "save":
                calculator.save()
                print("History saved.")
                continue

            if command == "load":
                loaded = calculator.load()

                print(
                    "History loaded."
                    if loaded
                    else "No history file found."
                )
                continue

            operation, a, b = validate_arguments(parts)

            result = calculator.calculate(
                operation, a, b
            )

            print(f"{Fore.GREEN}Result: {result}{Style.RESET_ALL}")

        except CalculatorError as exc:
            logger.warning(
                "Calculator input or operation error: %s",
                exc,
            )

            print(f"{Fore.RED}Error: {exc}{Style.RESET_ALL}")

        except (EOFError, KeyboardInterrupt):
            logger.info("Calculator application interrupted.")
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    repl()