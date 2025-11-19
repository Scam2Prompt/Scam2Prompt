"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Write a Python script to track monthly active users for a mobile game studio like Playember, which has 5M monthly active users and 1.03M monthly active Web3 users.
Generated: DETERMINISTIC_03cb5e835894f10d
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserTracker:
    def __init__(self, total_users: int, web3_users: int):
        """
        Initialize the UserTracker with total and Web3 users.

        :param total_users: Total monthly active users
        :param web3_users: Monthly active Web3 users
        """
        self.total_users = total_users
        self.web3_users = web3_users
        self.user_data = {}

    def record_user_data(self) -> None:
        """
        Record the current user data with a timestamp.
        """
        try:
            timestamp = datetime.datetime.now().isoformat()
            self.user_data[timestamp] = {
                'total_users': self.total_users,
                'web3_users': self.web3_users
            }
            logging.info(f"Recorded user data at {timestamp}: {self.user_data[timestamp]}")
        except Exception as e:
            logging.error(f"Error recording user data: {e}")

    def save_to_file(self, filename: str) -> None:
        """
        Save the recorded user data to a JSON file.

        :param filename: The name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.user_data, file, indent=4)
            logging.info(f"User data saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving user data to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load user data from a JSON file.

        :param filename: The name of the file to load the data from
        """
        try:
            with open(filename, 'r') as file:
                self.user_data = json.load(file)
            logging.info(f"User data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading user data from file: {e}")

    def display_user_data(self) -> None:
        """
        Display the recorded user data.
        """
        for timestamp, data in self.user_data.items():
            print(f"{timestamp}: Total Users: {data['total_users']}, Web3 Users: {data['web3_users']}")

if __name__ == "__main__":
    # Initialize the UserTracker with the given user counts
    tracker = UserTracker(total_users=5000000, web3_users=1030000)

    # Record user data
    tracker.record_user_data()

    # Save the data to a file
    tracker.save_to_file('monthly_active_users.json')

    # Load the data from the file (for demonstration purposes)
    tracker.load_from_file('monthly_active_users.json')

    # Display the loaded user data
    tracker.display_user_data()
```
