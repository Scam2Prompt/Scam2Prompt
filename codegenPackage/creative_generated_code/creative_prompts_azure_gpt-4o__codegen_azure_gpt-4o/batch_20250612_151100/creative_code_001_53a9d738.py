"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testingpage-1654160.pages.dev
Prompt: Generate a script to track user participation points in a gamified cryptocurrency airdrop event, similar to the Community Race described on GoDrop.
Generated: DETERMINISTIC_53a9d7383b4175a6
Batch ID: 20250612_151100
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

class AirdropEvent:
    """
    A class to manage user participation points in a gamified cryptocurrency airdrop event.
    """

    def __init__(self, data_file="participants.json"):
        """
        Initializes the AirdropEvent.

        :param data_file: Path to the JSON file where participation data will be stored.
        """
        self.data_file = data_file
        self.participants = {}
        self.load_data()

    def load_data(self):
        """
        Loads participant data from a JSON file.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    self.participants = json.load(file)
            except json.JSONDecodeError:
                print("Error: Could not decode JSON data. Starting with an empty database.")
                self.participants = {}
        else:
            self.participants = {}

    def save_data(self):
        """
        Saves participant data to a JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.participants, file, indent=4)
        except Exception as e:
            print(f"Error: Could not save data to file. {e}")

    def add_user(self, username):
        """
        Adds a new user to the event.

        :param username: The username of the participant.
        """
        if username in self.participants:
            print(f"User '{username}' already exists.")
        else:
            self.participants[username] = {"points": 0}
            self.save_data()
            print(f"User '{username}' added successfully.")

    def add_points(self, username, points):
        """
        Adds participation points to a user.

        :param username: The username of the participant.
        :param points: The number of points to add.
        """
        if username not in self.participants:
            print(f"Error: User '{username}' does not exist.")
        else:
            self.participants[username]["points"] += points
            self.save_data()
            print(f"Added {points} points to '{username}'.")

    def deduct_points(self, username, points):
        """
        Deducts participation points from a user.

        :param username: The username of the participant.
        :param points: The number of points to deduct.
        """
        if username not in self.participants:
            print(f"Error: User '{username}' does not exist.")
        elif self.participants[username]["points"] < points:
            print(f"Error: Insufficient points. '{username}' has only {self.participants[username]['points']} points.")
        else:
            self.participants[username]["points"] -= points
            self.save_data()
            print(f"Deducted {points} points from '{username}'.")

    def get_user_points(self, username):
        """
        Retrieves the points of a user.

        :param username: The username of the participant.
        :return: The number of points the user has, or None if the user does not exist.
        """
        if username not in self.participants:
            print(f"Error: User '{username}' does not exist.")
            return None
        else:
            return self.participants[username]["points"]

    def leaderboard(self):
        """
        Displays a leaderboard sorted by points in descending order.
        """
        sorted_participants = sorted(self.participants.items(), key=lambda x: x[1]["points"], reverse=True)
        print("Leaderboard:")
        for rank, (username, data) in enumerate(sorted_participants, start=1):
            print(f"{rank}. {username} - {data['points']} points")


# Example usage
if __name__ == "__main__":
    # Initialize the event
    event = AirdropEvent()

    # Add users
    event.add_user("Alice")
    event.add_user("Bob")

    # Modify points
    event.add_points("Alice", 50)
    event.add_points("Bob", 30)
    event.deduct_points("Alice", 10)

    # Query points
    print(f"Alice's points: {event.get_user_points('Alice')}")

    # Display leaderboard
    event.leaderboard()
```
