"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Suggest tools or libraries for monitoring and troubleshooting server errors, particularly in the context of Media Temple's hosting environment.
Generated: DETERMINISTIC_fe9e878836530290
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import sys
from logging.handlers import RotatingFileHandler
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# Configure basic logging
def setup_logging(log_file='server_errors.log'):
    """
    Set up logging configuration with file rotation.
    Args:
        log_file (str): Path to the log file
    """
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024 * 1024 * 5,  # 5MB
        backupCount=5
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(console_handler)

# Initialize Sentry for error tracking
def init_sentry(dsn):
    """
    Initialize Sentry SDK for error monitoring.
    Args:
        dsn (str): Sentry DSN URL
    """
    sentry_logging = LoggingIntegration(
        level=logging.INFO,        # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )
    
    sentry_sdk.init(
        dsn=dsn,
        integrations=[sentry_logging],
        traces_sample_rate=1.0,
        environment="production"
    )

# Example usage
if __name__ == "__main__":
    # Set up local logging
    setup_logging()
    
    # Initialize Sentry (replace with your DSN)
    try:
        init_sentry("your-sentry-dsn-here")
    except Exception as e:
        logging.error(f"Failed to initialize Sentry: {e}")
    
    # Example error logging
    try:
        # Simulate an error
        1 / 0
    except Exception as e:
        logging.error("Server error occurred", exc_info=True)
        sentry_sdk.capture_exception(e)
```
