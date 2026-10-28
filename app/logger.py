"""Logging configuration for the enhanced calculator."""

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "calculator.log"


def setup_logger():
    """Configure logging for calculator operations."""

    logger = logging.getLogger("calculator")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


logger = setup_logger()