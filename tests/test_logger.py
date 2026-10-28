"""Tests for calculator logging and history loading."""

import logging
from unittest.mock import patch

from app.calculator_repl import Calculator
from app.logger import logger


def test_logger_configuration():
    """Verify that the calculator logger is configured."""
    assert logger.name == "calculator"
    assert logger.level == logging.INFO
    assert logger.hasHandlers()


def test_successful_calculation_logging(tmp_path):
    """Verify successful calculations are logged."""
    with patch.dict(
        "os.environ",
        {
            "CALCULATOR_HISTORY_FILE": str(
                tmp_path / "history.csv"
            )
        },
    ):
        calculator = Calculator()

        with patch.object(logger, "info") as mock_info:
            result = calculator.calculate("add", 10, 5)

            assert result == 15
            mock_info.assert_called()


def test_history_load_success_logging():
    """Verify successful history loading is logged."""
    calculator = Calculator()

    with patch.object(
        calculator.history,
        "load",
        return_value=True,
    ):
        with patch.object(logger, "info") as mock_info:
            assert calculator.load() is True
            mock_info.assert_called_with(
                "Calculation history loaded."
            )


def test_history_load_failure_logging():
    """Verify missing history files are logged."""
    calculator = Calculator()

    with patch.object(
        calculator.history,
        "load",
        return_value=False,
    ):
        with patch.object(logger, "warning") as mock_warning:
            assert calculator.load() is False
            mock_warning.assert_called_with(
                "No history file found to load."
            )
def test_failed_calculation_logging(tmp_path):
    """Verify failed calculations are logged correctly."""
    import pytest

    from app.exceptions import OperationError

    calculator = Calculator()

    with patch.object(logger, "warning") as mock_warning:
        with pytest.raises(OperationError, match="divide by zero"):
            calculator.calculate("divide", 10, 0)

        mock_warning.assert_called_once_with(
            "Calculation failed: %s(%s, %s) - %s",
            "divide",
            10,
            0,
            mock_warning.call_args.args[4],
        )
