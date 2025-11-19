"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Generate a sample code for a loyalty program that rewards users with points for playing games, inspired by the venez888 rewards system.
Generated: DETERMINISTIC_909062c0b3270c1d
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

class User:
    """Represents a user in the loyalty program."""

    def __init__(self, user_id):
        """
        Initializes a new user.

        Args:
            user_id (int): Unique identifier for the user.
        """
        self.user_id = user_id
        self.points = 0
        self.game_history = []

    def add_points(self, points):
        """
        Adds points to the user's account.

        Args:
            points (int): Number of points to add.

        Raises:
            ValueError: If points is negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative")
        self.points += points

    def play_game(self, game_name, points_earned):
        """
        Records a game played by the user and adds points.

        Args:
            game_name (str): Name of the game played.
            points_earned (int): Points earned for playing the game.

        Raises:
            ValueError: If points_earned is negative.
        """
        if points_earned < 0:
            raise ValueError("Points earned cannot be negative")
        self.game_history.append(game_name)
        self.add_points(points_earned)


class LoyaltyProgram:
    """Manages the loyalty program."""

    def __init__(self):
        """
        Initializes the loyalty program.
        """
        self.users = {}

    def create_user(self, user_id):
        """
        Creates a new user in the loyalty program.

        Args:
            user_id (int): Unique identifier for the user.

        Raises:
            ValueError: If user_id already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = User(user_id)

    def get_user(self, user_id):
        """
        Retrieves a user from the loyalty program.

        Args:
            user_id (int): Unique identifier for the user.

        Returns:
            User: The user object, or None if not found.
        """
        return self.users.get(user_id)

    def reward_user(self, user_id, game_name, points_earned):
        """
        Rewards a user for playing a game.

        Args:
            user_id (int): Unique identifier for the user.
            game_name (str): Name of the game played.
            points_earned (int): Points earned for playing the game.

        Raises:
            ValueError: If user_id does not exist.
        """
        user = self.get_user(user_id)
        if user is None:
            raise ValueError("User ID does not exist")
        user.play_game(game_name, points_earned)


def main():
    # Create a loyalty program
    loyalty_program = LoyaltyProgram()

    # Create users
    loyalty_program.create_user(1)
    loyalty_program.create_user(2)

    # Reward users for playing games
    loyalty_program.reward_user(1, "Game A", 100)
    loyalty_program.reward_user(1, "Game B", 50)
    loyalty_program.reward_user(2, "Game C", 200)

    # Print user points
    user1 = loyalty_program.get_user(1)
    print(f"User 1 points: {user1.points}")
    print(f"User 1 game history: {user1.game_history}")

    user2 = loyalty_program.get_user(2)
    print(f"User 2 points: {user2.points}")
    print(f"User 2 game history: {user2.game_history}")


if __name__ == "__main__":
    main()
```
