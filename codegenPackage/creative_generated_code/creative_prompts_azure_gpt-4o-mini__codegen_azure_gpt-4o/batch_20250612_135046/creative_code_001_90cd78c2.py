"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Write a Python script that integrates OSI-type coaching methods into a wellness app, focusing on emotional regulation and self-esteem enhancement.
Generated: DETERMINISTIC_90cd78c2500cc550
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime


class WellnessApp:
    """
    A class representing a wellness application that integrates OSI-type coaching methods.
    Focuses on emotional regulation and self-esteem enhancement.
    """

    def __init__(self, user_data_file="user_data.json"):
        """
        Initialize the WellnessApp instance.

        :param user_data_file: Path to the JSON file for storing user data.
        """
        self.user_data_file = user_data_file
        self.user_data = self.load_user_data()

    def load_user_data(self):
        """
        Load user data from the JSON file if it exists, otherwise initialize as an empty dictionary.
        """
        if os.path.exists(self.user_data_file):
            try:
                with open(self.user_data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error reading user data file. Initializing with empty data.")
                return {}
        else:
            return {}

    def save_user_data(self):
        """
        Save the user data into a JSON file.
        """
        try:
            with open(self.user_data_file, "w") as file:
                json.dump(self.user_data, file, indent=4)
        except IOError as e:
            print(f"Error saving user data: {e}")

    def add_user(self, username):
        """
        Add a new user to the application.

        :param username: The name of the user to add.
        """
        if username not in self.user_data:
            self.user_data[username] = {
                "self_esteem_logs": [],
                "emotional_regulation_logs": [],
            }
            self.save_user_data()
            print(f"User '{username}' has been added successfully.")
        else:
            print(f"User '{username}' already exists.")

    def log_self_esteem(self, username, activity, rating, notes=""):
        """
        Log a self-esteem enhancement activity.

        :param username: The name of the user logging the activity.
        :param activity: The activity performed (e.g., "Positive Affirmation").
        :param rating: A rating from 1-10 for how impactful the activity was.
        :param notes: Optional notes about the activity.
        """
        if username not in self.user_data:
            print(f"User '{username}' does not exist.")
            return

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "activity": activity,
            "rating": rating,
            "notes": notes,
        }
        self.user_data[username]["self_esteem_logs"].append(log_entry)
        self.save_user_data()
        print(f"Self-esteem activity logged for user '{username}'.")

    def log_emotional_regulation(self, username, technique, effectiveness, notes=""):
        """
        Log an emotional regulation activity.

        :param username: The name of the user logging the activity.
        :param technique: The emotional regulation technique used (e.g., "Deep Breathing").
        :param effectiveness: A rating from 1-10 for technique effectiveness.
        :param notes: Optional notes about the activity.
        """
        if username not in self.user_data:
            print(f"User '{username}' does not exist.")
            return

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "technique": technique,
            "effectiveness": effectiveness,
            "notes": notes,
        }
        self.user_data[username]["emotional_regulation_logs"].append(log_entry)
        self.save_user_data()
        print(f"Emotional regulation technique logged for user '{username}'.")

    def view_logs(self, username):
        """
        View all logs (self-esteem and emotional regulation) for a user.

        :param username: The name of the user whose logs are to be viewed.
        """
        if username not in self.user_data:
            print(f"User '{username}' does not exist.")
            return

        print(f"Logs for user '{username}':")
        print("\nSelf-Esteem Logs:")
        for log in self.user_data[username]["self_esteem_logs"]:
            print(f"  - {log}")

        print("\nEmotional Regulation Logs:")
        for log in self.user_data[username]["emotional_regulation_logs"]:
            print(f"  - {log}")


# Example usage
if __name__ == "__main__":
    app = WellnessApp()

    # Add users
    app.add_user("JohnDoe")
    app.add_user("JaneDoe")

    # Log activities
    app.log_self_esteem("JohnDoe", "Positive Affirmation", 8, "Felt great after affirming my worth.")
    app.log_emotional_regulation("JaneDoe", "Deep Breathing", 9, "Helped calm me down after a stressful day.")

    # View logs
    app.view_logs("JohnDoe")
    app.view_logs("JaneDoe")
```
