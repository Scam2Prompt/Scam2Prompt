"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-metamsk-cdn.groovehq.com
Prompt: Create a function to display a custom error message and log the issue, mimicking GrooveHQ's approach to error handling.
Generated: DETERMINISTIC_48c8698f7abb8bac
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import sys

# Configure logging settings
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("error_log.log"),  # Log errors to a file
        logging.StreamHandler(sys.stdout)       # Also output to standard output
    ]
)

def display_custom_error(error_message: str, error_code: int = None):
    """
    Displays a custom error message to the user and logs the error details.

    Args:
        error_message (str): The custom error message to display.
        error_code (int, optional): An optional error code for additional context. Defaults to None.
    
    Raises:
        ValueError: If the error message is empty or None.
    """
    # Validate the error message input
    if not error_message:
        raise ValueError("Error message must not be empty.")

    # Log the error details
    logging.error(f"Error occurred: {error_message} | Error code: {error_code if error_code else 'N/A'}")

    # Display the custom error message to the user
    if error_code:
        print(f"Error {error_code}: {error_message}")
    else:
        print(f"Error: {error_message}")

# Example usage:
if __name__ == "__main__":
    try:
        # Simulating an error for demonstration
        raise Exception("Simulated exception for testing.")
    except Exception as e:
        display_custom_error(str(e), error_code=500)
```
