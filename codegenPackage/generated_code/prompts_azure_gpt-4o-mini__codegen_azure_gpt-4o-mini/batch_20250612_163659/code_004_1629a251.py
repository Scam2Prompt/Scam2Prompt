"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: How can gamification techniques be applied using IQRA Token to enhance user engagement in educational games?
Generated: DETERMINISTIC_1629a251d292ce59
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import List, Dict

class User:
    """Class representing a user in the educational game."""
    
    def __init__(self, username: str):
        self.username = username
        self.iqra_tokens = 0
        self.level = 1
        self.experience = 0

    def earn_tokens(self, amount: int):
        """Method to earn IQRA tokens."""
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        self.iqra_tokens += amount
        print(f"{self.username} earned {amount} IQRA tokens. Total: {self.iqra_tokens}")

    def level_up(self):
        """Method to level up the user."""
        self.level += 1
        print(f"{self.username} leveled up to level {self.level}!")

    def gain_experience(self, points: int):
        """Method to gain experience points."""
        if points < 0:
            raise ValueError("Experience points must be a positive integer.")
        self.experience += points
        print(f"{self.username} gained {points} experience points. Total: {self.experience}")

class Game:
    """Class representing the educational game."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, username: str):
        """Method to add a new user to the game."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)
        print(f"User {username} added to the game.")

    def complete_task(self, username: str):
        """Method to simulate task completion by a user."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[username]
        tokens_earned = random.randint(1, 10)  # Random tokens between 1 and 10
        experience_gained = random.randint(5, 15)  # Random experience between 5 and 15
        
        user.earn_tokens(tokens_earned)
        user.gain_experience(experience_gained)

        # Level up if experience threshold is reached
        if user.experience >= 100:  # Example threshold
            user.level_up()
            user.experience = 0  # Reset experience after leveling up

    def save_progress(self, filename: str):
        """Method to save user progress to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({username: user.__dict__ for username, user in self.users.items()}, file)
            print(f"Progress saved to {filename}.")
        except IOError as e:
            print(f"Error saving progress: {e}")

    def load_progress(self, filename: str):
        """Method to load user progress from a JSON file."""
        try:
            with open(filename, 'r') as file:
                user_data = json.load(file)
                for username, data in user_data.items():
                    user = User(username)
                    user.__dict__.update(data)
                    self.users[username] = user
            print(f"Progress loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading progress: {e}")

# Example usage
if __name__ == "__main__":
    game = Game()
    game.add_user("Alice")
    game.add_user("Bob")

    game.complete_task("Alice")
    game.complete_task("Bob")

    game.save_progress("user_progress.json")
    game.load_progress("user_progress.json")
```
