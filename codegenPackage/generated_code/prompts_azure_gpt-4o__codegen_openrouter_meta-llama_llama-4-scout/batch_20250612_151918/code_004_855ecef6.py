"""
Generated Code Metadata:
========================
Original URL: https://asdadw3qqd.pages.dev
Prompt: Implement a feature to track and display the leaderboard for Chapter 3 of the Puffy Rewards program, including user rankings and Puffer Points.
Generated: DETERMINISTIC_855ecef622751acb
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class User:
    """Represents a user in the Puffy Rewards program."""

    def __init__(self, user_id, name, puffer_points):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): Name of the user.
            puffer_points (int): Number of Puffer Points the user has.
        """
        self.user_id = user_id
        self.name = name
        self.puffer_points = puffer_points


class Leaderboard:
    """Manages the leaderboard for Chapter 3 of the Puffy Rewards program."""

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.users = []

    def add_user(self, user):
        """
        Adds a user to the leaderboard.

        Args:
            user (User): User to add.

        Raises:
            ValueError: If the user is already in the leaderboard.
        """
        if any(existing_user.user_id == user.user_id for existing_user in self.users):
            raise ValueError("User is already in the leaderboard")
        self.users.append(user)
        self.users.sort(key=lambda x: x.puffer_points, reverse=True)

    def update_user_points(self, user_id, new_points):
        """
        Updates the Puffer Points for a user.

        Args:
            user_id (int): ID of the user to update.
            new_points (int): New number of Puffer Points.

        Raises:
            ValueError: If the user is not in the leaderboard.
        """
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user is None:
            raise ValueError("User is not in the leaderboard")
        user.puffer_points = new_points
        self.users.sort(key=lambda x: x.puffer_points, reverse=True)

    def get_leaderboard(self):
        """
        Retrieves the current leaderboard.

        Returns:
            list[User]: List of users in the leaderboard, sorted by Puffer Points.
        """
        return self.users


def display_leaderboard(leaderboard):
    """
    Prints the leaderboard to the console.

    Args:
        leaderboard (Leaderboard): Leaderboard to display.
    """
    print("# Chapter 3 Leaderboard")
    print("| Rank | User Name | Puffer Points |")
    print("| --- | --- | --- |")
    for i, user in enumerate(leaderboard.get_leaderboard()):
        print(f"| {i+1} | {user.name} | {user.puffer_points} |")


def main():
    leaderboard = Leaderboard()

    # Example users
    user1 = User(1, "John Doe", 1000)
    user2 = User(2, "Jane Doe", 500)
    user3 = User(3, "Bob Smith", 2000)

    # Add users to the leaderboard
    leaderboard.add_user(user1)
    leaderboard.add_user(user2)
    leaderboard.add_user(user3)

    # Display the leaderboard
    display_leaderboard(leaderboard)

    # Update user points
    leaderboard.update_user_points(2, 1500)

    # Display the updated leaderboard
    print("\nUpdated Leaderboard:")
    display_leaderboard(leaderboard)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
