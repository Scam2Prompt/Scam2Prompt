"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Write a script to track user activity and calculate rewards in a loyalty program for an online casino, including cashback on losses as described in BaxBet's features.
Generated: DETERMINISTIC_28e6e50fec360351
Batch ID: 20250612_154239
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
from typing import Dict, Any, List


class UserActivityTracker:
    """
    A class to track user activity and calculate rewards in a loyalty program.
    """

    def __init__(self):
        self.user_data: Dict[str, Dict[str, Any]] = {}
        self.cashback_percentage = 0.1  # 10% cashback on losses

    def add_user(self, username: str) -> None:
        """
        Add a new user to the tracker.

        :param username: The username of the new user.
        :raises ValueError: If the username already exists.
        """
        if username in self.user_data:
            raise ValueError(f"User '{username}' already exists.")
        
        self.user_data[username] = {
            "activity": [],
            "total_losses": 0.0,
            "cashback": 0.0,
        }

    def log_activity(self, username: str, activity_type: str, amount: float) -> None:
        """
        Log a user's activity, either a win or a loss.

        :param username: The username of the user.
        :param activity_type: The type of activity ('win' or 'loss').
        :param amount: The amount of money associated with the activity.
        :raises ValueError: If the user does not exist or if the amount is negative.
        """
        if username not in self.user_data:
            raise ValueError(f"User '{username}' does not exist.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.user_data[username]["activity"].append({
            "timestamp": datetime.now().isoformat(),
            "activity_type": activity_type,
            "amount": amount,
        })

        # Update total losses and calculate cashback if the activity is a loss
        if activity_type == 'loss':
            self.user_data[username]["total_losses"] += amount
            self.user_data[username]["cashback"] += amount * self.cashback_percentage

    def get_user_report(self, username: str) -> Dict[str, Any]:
        """
        Retrieve a report of the user's activity including total losses and cashback.

        :param username: The username of the user.
        :return: A dictionary containing user activity report.
        :raises ValueError: If the user does not exist.
        """
        if username not in self.user_data:
            raise ValueError(f"User '{username}' does not exist.")

        user_info = self.user_data[username]
        return {
            "username": username,
            "total_losses": user_info["total_losses"],
            "cashback": user_info["cashback"],
            "activity_log": user_info["activity"],
        }

    def save_to_file(self, file_path: str) -> None:
        """
        Save the user data to a JSON file.

        :param file_path: The path to the file where the data will be saved.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load user data from a JSON file.

        :param file_path: The path to the file from which the data will be loaded.
        :raises IOError: If there is an error reading the file or if the file is invalid.
        """
        try:
            with open(file_path, 'r') as f:
                self.user_data = json.load(f)
        except IOError as e:
            raise IOError(f"Error loading data from file: {e}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in the file.")


# Example usage
if __name__ == "__main__":
    tracker = UserActivityTracker()
    tracker.add_user("john_doe")
    tracker.log_activity("john_doe", "loss", 100)
    tracker.log_activity("john_doe", "win", 50)
    
    report = tracker.get_user_report("john_doe")
    print(report)

    # Save data to a file
    tracker.save_to_file("user_data.json")

    # Load data from a file
    tracker.load_from_file("user_data.json")
```
