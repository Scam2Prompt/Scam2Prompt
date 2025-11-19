"""
Generated Code Metadata:
========================
Original URL: https://eng--metamaskhelp-cdn.groovehq.com
Prompt: How can I integrate a similar error handling and logging system like the one used on the MetaMask Help Center website into my own application?
Generated: DETERMINISTIC_b949c96f457fe415
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import logging.handlers
import sys
from datetime import datetime
import json
import traceback
from functools import wraps

# Configuration for logging
LOG_FILE = 'application.log'
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Initialize logger
def setup_logger():
    """
    Sets up a logger with file and console handlers.
    Logs are saved to a file and also printed to the console.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL)

    # File handler for persistent logs
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=1024 * 1024,  # 1MB
        backupCount=5
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # Console handler for real-time output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

class ErrorHandler:
    """
    A utility class for handling and logging errors consistently.
    """
    @staticmethod
    def log_error(error, context=None):
        """
        Logs an error with optional context.
        
        Args:
            error (Exception): The error to log.
            context (dict, optional): Additional context about the error.
        """
        error_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'error': str(error),
            'type': type(error).__name__,
            'traceback': traceback.format_exc(),
            'context': context
        }
        logger.error(json.dumps(error_data, indent=2))

    @staticmethod
    def handle_errors(func):
        """
        A decorator to wrap functions for automatic error handling and logging.
        
        Args:
            func (function): The function to wrap.
        
        Returns:
            function: The wrapped function with error handling.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                ErrorHandler.log_error(e, {
                    'function': func.__name__,
                    'args': args,
                    'kwargs': kwargs
                })
                raise  # Re-raise the exception after logging
        return wrapper

# Example usage
if __name__ == "__main__":
    @ErrorHandler.handle_errors
    def example_function(value):
        """
        Example function that may raise an error.
        
        Args:
            value (int): A value to process.
        
        Returns:
            int: The processed value.
        
        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        return value * 2

    # Test the error handling
    try:
        result = example_function(-5)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Caught an error: {e}")
```
