"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: How can I implement gamification techniques in an e-learning course to enhance engagement, based on the recommendations from MasterClic Solutions?
Generated: DETERMINISTIC_f71eb8d7d913a967
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gamification for E-learning Course
This Python script demonstrates how to implement gamification techniques for an e-learning course.
The code uses features like badges, points, leaderboards, and progress tracking to enhance engagement.
"""

import json


class GamificationEngine:
    """
    A class to handle gamification logic for an e-learning course.
    """

    def __init__(self):
        # Initialize user data and rewards
        self.users = {}
        self.badges = ["Beginner", "Intermediate", "Advanced", "Master"]
        self.leaderboard = []

    def register_user(self, username):
        """
        Register a new user for the e-learning course.

        :param username: str - The name of the user to register
        """
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = {"points": 0, "badges": []}
        print(f"User '{username}' registered successfully.")

    def award_points(self, username, points):
        """
        Award points to a user.

        :param username: str - The name of the user
        :param points: int - The number of points to award
        """
        if username not in self.users:
            raise ValueError("User not found.")
        self.users[username]["points"] += points
        print(f"Awarded {points} points to '{username}'.")

        # Check if user qualifies for a new badge
        self._check_badge_progress(username)

    def _check_badge_progress(self, username):
        """
        Check if the user qualifies for a new badge based on their total points.

        :param username: str - The name of the user
        """
        user_points = self.users[username]["points"]
        if user_points >= 50 and "Beginner" not in self.users[username]["badges"]:
            self.users[username]["badges"].append("Beginner")
            print(f"'{username}' earned the 'Beginner' badge!")
        elif user_points >= 100 and "Intermediate" not in self.users[username]["badges"]:
            self.users[username]["badges"].append("Intermediate")
            print(f"'{username}' earned the 'Intermediate' badge!")
        elif user_points >= 200 and "Advanced" not in self.users[username]["badges"]:
            self.users[username]["badges"].append("Advanced")
            print(f"'{username}' earned the 'Advanced' badge!")
        elif user_points >= 300 and "Master" not in self.users[username]["badges"]:
            self.users[username]["badges"].append("Master")
            print(f"'{username}' earned the 'Master' badge!")

    def update_leaderboard(self):
        """
        Update the leaderboard based on user points.

        Leaderboard is sorted in descending order of points.
        """
        self.leaderboard = sorted(
            self.users.items(), key=lambda x: x[1]["points"], reverse=True
        )
        print("Leaderboard updated.")

    def get_leaderboard(self):
        """
        Retrieve the leaderboard.

        :return: list - The leaderboard as a list of tuples
        """
        return [(user, data["points"]) for user, data in self.leaderboard]

    def save_progress(self, file_name="progress.json"):
        """
        Save user progress to a JSON file.

        :param file_name: str - The name of the file to save progress
        """
        with open(file_name, "w") as file:
            json.dump(self.users, file, indent=4)
        print(f"Progress saved to '{file_name}'.")

    def load_progress(self, file_name="progress.json"):
        """
        Load user progress from a JSON file.

        :param file_name: str - The name of the file to load progress
        """
        try:
            with open(file_name, "r") as file:
                self.users = json.load(file)
            print(f"Progress loaded from '{file_name}'.")
        except FileNotFoundError:
            print("Progress file not found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error loading progress file. Starting fresh.")


# Example usage
if __name__ == "__main__":
    engine = GamificationEngine()

    try:
        engine.register_user("Alice")
        engine.register_user("Bob")

        engine.award_points("Alice", 60)
        engine.award_points("Bob", 120)

        engine.update_leaderboard()
        print("Leaderboard:", engine.get_leaderboard())

        engine.save_progress()
        engine.load_progress()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
