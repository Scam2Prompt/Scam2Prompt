"""
Generated Code Metadata:
========================
Original URL: https://panccokesowpaflnace.com
Prompt: Write a code snippet that demonstrates how to log activities using the 'logs/' directory structure mentioned on panccokesowpaflnace.com.
Generated: DETERMINISTIC_db1b86524ee251f9
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime
from pathlib import Path

def setup_logger(log_name: str, log_dir: str = "logs") -> logging.Logger:
    """
    Sets up a logger with file and console handlers.
    
    Args:
        log_name: Name of the logger and the log file (without extension).
        log_dir: Directory where logs will be stored. Defaults to "logs".
    
    Returns:
        Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    
    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Create file handler
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_path / f"{log_name}_{timestamp}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Example usage
if __name__ == "__main__":
    try:
        logger = setup_logger("sample_app")
        logger.info("Logger setup complete")
        logger.debug("This is a debug message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
    except Exception as e:
        print(f"Failed to setup logger: {str(e)}")
```
