"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Develop a program in Python to track user activity logs, including deposits, withdrawals, and events, based on the structure provided on the webpage.
Generated: DETERMINISTIC_01083d0cb26bc564
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class ActivityLogger:
    """
    A class to track user activity logs such as deposits, withdrawals, and other events.

    Methods:
        log_activity(activity_type, amount=None, event_description=None): Logs an activity.
        save_logs(output_file): Saves the logs to a JSON file.
        load_logs(input_file): Loads logs from a JSON file.
        display_logs(): Displays all logged activities.
    """

    def __init__(self):
        """
        Initializes the ActivityLogger with an empty activity list.
        """
        self.activity_log = []

    def log_activity(self, activity_type, amount=None, event_description=None):
        """
        Logs user activity such as deposits, withdrawals, or custom events.

        Parameters:
            activity_type (str): Type of activity ('deposit', 'withdrawal', or 'event').
            amount (float, optional): Amount involved in the activity (for deposits and withdrawals).
            event_description (str, optional): Description of the event (for custom events).

        Raises:
            ValueError: If an invalid activity type is provided.
            ValueError: If amount is not provided for deposits or withdrawals.
        """
        if activity_type not in ['deposit', 'withdrawal', 'event']:
            raise ValueError("Invalid activity type. Must be 'deposit', 'withdrawal', or 'event'.")

        if activity_type in ['deposit', 'withdrawal'] and amount is None:
            raise ValueError("Amount is required for deposits and withdrawals.")

        activity_entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'activity_type': activity_type,
            'amount': amount if amount is not None else None,
            'event_description': event_description if event_description else None
        }

        self.activity_log.append(activity_entry)

    def save_logs(self, output_file):
        """
        Saves the activity logs to a JSON file.

        Parameters:
            output_file (str): Path to the file where logs should be saved.

        Raises:
            Exception: If there is an error saving the logs.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(self.activity_log, file, indent=4)
        except Exception as e:
            raise Exception(f"Error saving logs to file: {e}")

    def load_logs(self, input_file):
        """
        Loads activity logs from a JSON file.

        Parameters:
            input_file (str): Path to the file from which logs should be loaded.

        Raises:
            Exception: If there is an error loading the logs.
        """
        try:
            with open(input_file, 'r') as file:
                self.activity_log = json.load(file)
        except Exception as e:
            raise Exception(f"Error loading logs from file: {e}")

    def display_logs(self):
        """
        Displays all logged activities in a readable format.
        """
        if not self.activity_log:
            print("No activity logs available.")
            return

        print("User Activity Logs:")
        for log in self.activity_log:
            print(json.dumps(log, indent=4))


# Example usage
if __name__ == "__main__":
    logger = ActivityLogger()

    try:
        # Logging activities
        logger.log_activity('deposit', amount=500.0)
        logger.log_activity('withdrawal', amount=200.0)
        logger.log_activity('event', event_description='User logged in')
        
        # Display logs
        logger.display_logs()
        
        # Save logs to file
        logger.save_logs('activity_logs.json')
        
        # Load logs from file
        logger.load_logs('activity_logs.json')
        
        # Display logs again after loading
        logger.display_logs()
    except Exception as error:
        print(f"An error occurred: {error}")
```
