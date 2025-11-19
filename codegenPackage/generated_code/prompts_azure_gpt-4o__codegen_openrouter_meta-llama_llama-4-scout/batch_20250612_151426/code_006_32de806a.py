"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Create a Python script that incorporates gamification elements, such as leaderboards and challenges, to encourage users to stay on track with their weight loss goals, as described on myneel.com.
Generated: DETERMINISTIC_32de806af13aba2e
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# weight_loss_gamification.py

import datetime
import json
import os

class User:
    """Represents a user with weight loss goals."""

    def __init__(self, user_id, name, goal_weight):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): User's name.
            goal_weight (float): User's goal weight in kg.
        """
        self.user_id = user_id
        self.name = name
        self.goal_weight = goal_weight
        self.current_weight = None
        self.progress = []

    def update_weight(self, weight):
        """
        Updates the user's current weight and adds progress entry.

        Args:
            weight (float): User's current weight in kg.
        """
        self.current_weight = weight
        self.progress.append({
            'date': datetime.date.today().isoformat(),
            'weight': weight
        })

    def get_progress(self):
        """Returns the user's progress as a list of dictionaries."""
        return self.progress


class Challenge:
    """Represents a weight loss challenge."""

    def __init__(self, challenge_id, name, target_weight_loss):
        """
        Initializes a Challenge object.

        Args:
            challenge_id (int): Unique identifier for the challenge.
            name (str): Challenge name.
            target_weight_loss (float): Target weight loss in kg.
        """
        self.challenge_id = challenge_id
        self.name = name
        self.target_weight_loss = target_weight_loss
        self.users = {}

    def add_user(self, user):
        """
        Adds a user to the challenge.

        Args:
            user (User): User object.
        """
        self.users[user.user_id] = user

    def get_leaderboard(self):
        """
        Returns the leaderboard for the challenge.

        Returns:
            list: List of tuples containing user ID, name, and progress.
        """
        leaderboard = []
        for user_id, user in self.users.items():
            progress = user.get_progress()
            if progress:
                weight_loss = user.progress[0]['weight'] - user.progress[-1]['weight']
                leaderboard.append((user_id, user.name, weight_loss))
        leaderboard.sort(key=lambda x: x[2], reverse=True)
        return leaderboard


class WeightLossGamification:
    """Manages users, challenges, and leaderboards."""

    def __init__(self, data_file):
        """
        Initializes a WeightLossGamification object.

        Args:
            data_file (str): File path to store data.
        """
        self.data_file = data_file
        self.users = {}
        self.challenges = {}
        self.load_data()

    def load_data(self):
        """Loads data from the file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for user_data in data.get('users', []):
                    user = User(user_data['user_id'], user_data['name'], user_data['goal_weight'])
                    user.progress = user_data['progress']
                    self.users[user.user_id] = user
                for challenge_data in data.get('challenges', []):
                    challenge = Challenge(challenge_data['challenge_id'], challenge_data['name'], challenge_data['target_weight_loss'])
                    for user_id in challenge_data.get('users', []):
                        challenge.add_user(self.users[user_id])
                    self.challenges[challenge.challenge_id] = challenge

    def save_data(self):
        """Saves data to the file."""
        data = {
            'users': [
                {
                    'user_id': user.user_id,
                    'name': user.name,
                    'goal_weight': user.goal_weight,
                    'progress': user.progress
                } for user in self.users.values()
            ],
            'challenges': [
                {
                    'challenge_id': challenge.challenge_id,
                    'name': challenge.name,
                    'target_weight_loss': challenge.target_weight_loss,
                    'users': [user.user_id for user in challenge.users.values()]
                } for challenge in self.challenges.values()
            ]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def create_user(self, user_id, name, goal_weight):
        """
        Creates a new user.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): User's name.
            goal_weight (float): User's goal weight in kg.
        """
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, goal_weight)
            self.save_data()

    def create_challenge(self, challenge_id, name, target_weight_loss):
        """
        Creates a new challenge.

        Args:
            challenge_id (int): Unique identifier for the challenge.
            name (str): Challenge name.
            target_weight_loss (float): Target weight loss in kg.
        """
        if challenge_id not in self.challenges:
            self.challenges[challenge_id] = Challenge(challenge_id, name, target_weight_loss)
            self.save_data()

    def add_user_to_challenge(self, user_id, challenge_id):
        """
        Adds a user to a challenge.

        Args:
            user_id (int): User ID.
            challenge_id (int): Challenge ID.
        """
        if user_id in self.users and challenge_id in self.challenges:
            self.challenges[challenge_id].add_user(self.users[user_id])
            self.save_data()

    def update_user_weight(self, user_id, weight):
        """
        Updates a user's weight.

        Args:
            user_id (int): User ID.
            weight (float): User's current weight in kg.
        """
        if user_id in self.users:
            self.users[user_id].update_weight(weight)
            self.save_data()

    def get_challenge_leaderboard(self, challenge_id):
        """
        Returns the leaderboard for a challenge.

        Args:
            challenge_id (int): Challenge ID.

        Returns:
            list: List of tuples containing user ID, name, and progress.
        """
        if challenge_id in self.challenges:
            return self.challenges[challenge_id].get_leaderboard()
        return []


def main():
    gamification = WeightLossGamification('weight_loss_data.json')

    while True:
        print("1. Create user")
        print("2. Create challenge")
        print("3. Add user to challenge")
        print("4. Update user weight")
        print("5. Get challenge leaderboard")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            goal_weight = float(input("Enter goal weight (kg): "))
            gamification.create_user(user_id, name, goal_weight)
        elif choice == "2":
            challenge_id = int(input("Enter challenge ID: "))
            name = input("Enter challenge name: ")
            target_weight_loss = float(input("Enter target weight loss (kg): "))
            gamification.create_challenge(challenge_id, name, target_weight_loss)
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            challenge_id = int(input("Enter challenge ID: "))
            gamification.add_user_to_challenge(user_id, challenge_id)
        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            weight = float(input("Enter user weight (kg): "))
            gamification.update_user_weight(user_id, weight)
        elif choice == "5":
            challenge_id = int(input("Enter challenge ID: "))
            leaderboard = gamification.get_challenge_leaderboard(challenge_id)
            for user_id, name, weight_loss in leaderboard:
                print(f"{name}: {weight_loss} kg")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
