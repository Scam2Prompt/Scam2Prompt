"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Suggest methods for integrating social collaboration and competition features into a game platform, similar to SCATTER HITAM's social aspects.
Generated: DETERMINISTIC_7882f67aafa8e4f0
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GamePlatform:
    """
    A class to represent a game platform with social collaboration and competition features.
    """

    def __init__(self):
        # A dictionary to store user profiles
        self.users = {}
        # A dictionary to store leaderboards based on scores
        self.leaderboard = {}

    def add_user(self, username):
        """
        Adds a new user to the platform.

        Parameters:
            username (str): The username of the new user.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = {'friends': set(), 'score': 0}
        print(f"User {username} added successfully.")

    def add_friend(self, username, friend_username):
        """
        Adds a friend to the user's friend list.

        Parameters:
            username (str): The username of the user.
            friend_username (str): The username of the friend.

        Raises:
            ValueError: If the user or friend does not exist.
        """
        if username not in self.users or friend_username not in self.users:
            raise ValueError("Either user or friend does not exist.")
        self.users[username]['friends'].add(friend_username)
        print(f"{friend_username} added to {username}'s friends.")

    def update_score(self, username, score):
        """
        Updates the user's score and refreshes the leaderboard.

        Parameters:
            username (str): The username of the user.
            score (int): The new score of the user.

        Raises:
            ValueError: If the user does not exist or score is negative.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        if score < 0:
            raise ValueError("Score cannot be negative.")
        self.users[username]['score'] = score
        self.refresh_leaderboard()
        print(f"{username}'s score updated to {score}.")

    def refresh_leaderboard(self):
        """
        Refreshes the leaderboard based on current user scores.
        """
        self.leaderboard = {user: data['score'] for user, data in self.users.items()}
        # Sort the leaderboard by scores in descending order
        self.leaderboard = dict(sorted(self.leaderboard.items(), key=lambda item: item[1], reverse=True))
        print("Leaderboard refreshed.")

    def display_leaderboard(self):
        """
        Displays the current leaderboard.
        """
        print("Current Leaderboard:")
        for rank, (username, score) in enumerate(self.leaderboard.items(), start=1):
            print(f"{rank}. {username}: {score}")


# Example Usage
if __name__ == "__main__":
    platform = GamePlatform()
    try:
        platform.add_user("Alice")
        platform.add_user("Bob")
        platform.add_friend("Alice", "Bob")
        platform.update_score("Alice", 150)
        platform.update_score("Bob", 200)
        platform.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
