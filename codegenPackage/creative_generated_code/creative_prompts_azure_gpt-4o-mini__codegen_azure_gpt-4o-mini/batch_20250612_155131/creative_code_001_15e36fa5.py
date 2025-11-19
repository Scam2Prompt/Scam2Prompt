"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Write a code snippet to handle incorrect access data notifications in Map-OS as described on conext.info.
Generated: DETERMINISTIC_15e36fa5d6cc39cf
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AccessDataError(Exception):
    """Custom exception for handling access data errors."""
    pass

class MapOSDataHandler:
    """Class to handle access data notifications for Map-OS."""

    def __init__(self):
        self.access_data = {}

    def add_access_data(self, user_id, data):
        """
        Add access data for a user.

        Args:
            user_id (str): Unique identifier for the user.
            data (dict): Access data to be associated with the user.

        Raises:
            ValueError: If access data is invalid.
        """
        if not isinstance(data, dict):
            logging.error(f"Invalid data type for user {user_id}: expected dict, got {type(data).__name__}")
            raise ValueError("Access data must be a dictionary.")

        self.access_data[user_id] = data
        logging.info(f"Access data added for user {user_id}.")

    def notify_incorrect_access(self, user_id, expected_data):
        """
        Notify incorrect access data.

        Args:
            user_id (str): Unique identifier for the user.
            expected_data (dict): The expected access data for validation.

        Raises:
            AccessDataError: If the user access data does not match expected data.
        """
        if user_id not in self.access_data:
            logging.warning(f"No access data found for user {user_id}.")
            return

        actual_data = self.access_data[user_id]

        if actual_data != expected_data:
            error_message = f"Incorrect access data for user {user_id}. Expected: {expected_data}, Actual: {actual_data}"
            logging.error(error_message)
            raise AccessDataError(error_message)

        logging.info(f"Access data for user {user_id} is correct.")

# Example usage
if __name__ == "__main__":
    handler = MapOSDataHandler()

    try:
        # Adding sample access data
        handler.add_access_data("user123", {"location": "office", "time": "9 AM"})
        
        # Notifying incorrect access data
        handler.notify_incorrect_access("user123", {"location": "home", "time": "9 AM"})
    except (ValueError, AccessDataError) as e:
        logging.exception("An error occurred while handling access data.")
```
