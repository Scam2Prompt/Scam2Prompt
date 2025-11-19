"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-vallet.groovehq.com
Prompt: What strategies can I use to improve user experience when encountering errors, based on the insights from Rabby Wallet's approach to bugs?
Generated: DETERMINISTIC_308ed1579035a3a3
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class ErrorHandler:
    """
    A class to handle errors in a user-friendly manner.
    It integrates logging for tracking issues and user notifications for a better user experience.
    """

    def __init__(self):
        # Configure logging to a file with appropriate format
        logging.basicConfig(filename='app_errors.log', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_error(self, error_message):
        """
        Log the error message to a file for debugging purposes.

        Args:
            error_message (str): The error message to log.
        """
        logging.error(error_message)

    def notify_user(self, user_message):
        """
        Notify the user about the error in a friendly manner.

        Args:
            user_message (str): The message to display to the user.
        """
        # In a production application, this could be a UI notification or an alert dialog.
        print(f"User Notification: {user_message}")

    def handle_error(self, error):
        """
        Handle the error by logging it and notifying the user.

        Args:
            error (Exception): The exception that occurred.
        """
        # Log the error details for further investigation
        self.log_error(str(error))

        # Notify the user with a generic message
        self.notify_user("Oops! Something went wrong. Please try again or contact support.")

def perform_action():
    """
    Simulate an action that may raise an error.
    """
    try:
        # Simulate an action that may fail
        result = 10 / 0  # This will raise a ZeroDivisionError
        return result
    except Exception as e:
        error_handler = ErrorHandler()
        error_handler.handle_error(e)

if __name__ == "__main__":
    perform_action()
```
