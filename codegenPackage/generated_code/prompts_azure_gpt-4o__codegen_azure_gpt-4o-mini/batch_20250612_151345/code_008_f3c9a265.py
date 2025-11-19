"""
Generated Code Metadata:
========================
Original URL: https://thegaincapital.com
Prompt: Create a ranking badge system for users based on their investment activity, as described in The Gain Capital's ranking system.
Generated: DETERMINISTIC_f3c9a26575b5e8c5
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the ranking system.

    Attributes:
        username (str): The username of the user.
        investment_activity (float): The total investment activity of the user.
        badge (str): The badge awarded to the user based on their investment activity.
    """

    def __init__(self, username: str, investment_activity: float):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
            investment_activity (float): The total investment activity of the user.
        """
        self.username = username
        self.investment_activity = investment_activity
        self.badge = self.assign_badge()

    def assign_badge(self) -> str:
        """
        Assigns a badge to the user based on their investment activity.

        Returns:
            str: The badge awarded to the user.
        """
        if self.investment_activity < 1000:
            return "Novice"
        elif self.investment_activity < 5000:
            return "Intermediate"
        elif self.investment_activity < 10000:
            return "Advanced"
        else:
            return "Expert"

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
            str: A string containing the username and their badge.
        """
        return f"User: {self.username}, Badge: {self.badge}"


class RankingSystem:
    """
    Represents the ranking system for users based on their investment activity.

    Attributes:
        users (list): A list of User instances.
    """

    def __init__(self):
        """Initializes a new RankingSystem instance."""
        self.users = []

    def add_user(self, username: str, investment_activity: float):
        """
        Adds a new user to the ranking system.

        Args:
            username (str): The username of the user.
            investment_activity (float): The total investment activity of the user.

        Raises:
            ValueError: If investment_activity is negative.
        """
        if investment_activity < 0:
            raise ValueError("Investment activity cannot be negative.")
        user = User(username, investment_activity)
        self.users.append(user)

    def display_rankings(self):
        """
        Displays the rankings of all users in the system.
        """
        if not self.users:
            print("No users in the ranking system.")
            return

        print("User Rankings:")
        for user in self.users:
            print(user)


# Example usage
if __name__ == "__main__":
    ranking_system = RankingSystem()

    try:
        ranking_system.add_user("Alice", 1500)
        ranking_system.add_user("Bob", 6000)
        ranking_system.add_user("Charlie", 12000)
        ranking_system.add_user("David", -500)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

    ranking_system.display_rankings()
```
