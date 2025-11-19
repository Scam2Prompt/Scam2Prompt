"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.aqanu.org
Prompt: Create a code snippet that simulates the training portal setup for BASF's new pest control product, Selontra, and tracks user qualifications.
Generated: DETERMINISTIC_0fe3e34a8b08c617
Batch ID: 20250612_135940
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

class TrainingPortal:
    """
    A class to simulate a training portal for BASF's Selontra pest control product.
    Tracks user qualifications and training progress.
    """

    def __init__(self):
        # Initialize the portal with an empty list of users and exercises
        self.users = {}
        self.exercises = []

    def add_user(self, user_id, name, email):
        """
        Add a new user to the training portal.
        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param email: Email address of the user
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = {
            "name": name,
            "email": email,
            "completed_exercises": [],
            "qualification_status": False,
            "last_updated": str(datetime.now())
        }

    def add_exercise(self, exercise_id, title, description):
        """
        Add a new exercise to the training portal.
        :param exercise_id: Unique identifier for the exercise
        :param title: Exercise title
        :param description: Exercise description
        """
        for exercise in self.exercises:
            if exercise["exercise_id"] == exercise_id:
                raise ValueError("Exercise ID already exists.")
        self.exercises.append({
            "exercise_id": exercise_id,
            "title": title,
            "description": description
        })

    def complete_exercise(self, user_id, exercise_id):
        """
        Mark an exercise as completed for a user.
        :param user_id: Unique identifier for the user
        :param exercise_id: Unique identifier for the exercise
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        if not any(ex["exercise_id"] == exercise_id for ex in self.exercises):
            raise ValueError("Exercise not found.")
        
        user = self.users[user_id]
        if exercise_id in user["completed_exercises"]:
            raise ValueError("Exercise already completed by this user.")
        user["completed_exercises"].append(exercise_id)

        # Update qualification status if all exercises are completed
        if len(user["completed_exercises"]) == len(self.exercises):
            user["qualification_status"] = True
        user["last_updated"] = str(datetime.now())

    def export_user_data(self, user_id):
        """
        Export user data as a JSON string.
        :param user_id: Unique identifier for the user
        :return: JSON string of the user data
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        return json.dumps(self.users[user_id], indent=4)

    def list_exercises(self):
        """
        List all exercises available in the portal.
        :return: List of exercises
        """
        return self.exercises

    def list_users(self):
        """
        List all users in the portal.
        :return: Dictionary of users
        """
        return self.users


# Example usage
if __name__ == "__main__":
    try:
        portal = TrainingPortal()

        # Add some exercises
        portal.add_exercise("EX001", "Introduction to Selontra", "Learn the basics of pest control using Selontra.")
        portal.add_exercise("EX002", "Advanced Techniques", "Explore advanced strategies for effective pest control.")

        # Add some users
        portal.add_user("U001", "John Doe", "john.doe@example.com")
        portal.add_user("U002", "Jane Smith", "jane.smith@example.com")

        # User completes exercises
        portal.complete_exercise("U001", "EX001")
        portal.complete_exercise("U001", "EX002")

        # Export user data
        print("John Doe's Data:")
        print(portal.export_user_data("U001"))

        # List all exercises
        print("\nAvailable Exercises:")
        print(portal.list_exercises())

        # List all users
        print("\nUsers:")
        print(portal.list_users())

    except Exception as e:
        print(f"Error: {e}")
```
