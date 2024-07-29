import logging
import os

from dotenv import load_dotenv
from pythonjsonlogger import jsonlogger

# Load environment variables from a .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Custom function to configure the logger
def configure_logger(level: str = "INFO") -> None:
    log_format = os.getenv("LOG_MESSAGES_FORMAT", "text").lower()

    logger.setLevel(level.upper())

    # Create a handler for logging
    handler = logging.StreamHandler()

    if log_format == "json":
        # JSON format
        formatter = jsonlogger.JsonFormatter(
            fmt='%(asctime)s %(name)s %(levelname)s %(message)s %(filename)s %(lineno)d',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        # Text format
        formatter = logging.Formatter(
            fmt='[%(asctime)s] %(levelname)s {%(filename)s:%(lineno)d} - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    handler.setFormatter(formatter)
    logger.handlers = []  # Clear existing handlers
    logger.addHandler(handler)

# Call the configure logger function to set up the logger initially
configure_logger(level="INFO")

# Function to set log level
def set_log_level(level: str) -> None:
    """
    Set the log level for the logger.

    Parameters:
    - level (str): A logging level such as 'debug', 'info', 'warning', 'error', or 'critical'.
    """
    configure_logger(level)

# Set default log levels for other libraries
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("matplotlib.pyplot").setLevel(logging.WARNING)
logging.getLogger("PIL.PngImagePlugin").setLevel(logging.WARNING)
logging.getLogger("PIL.Image").setLevel(logging.WARNING)

# Re-export the logger for ease of use
__all__ = ["logger", "set_log_level"]
