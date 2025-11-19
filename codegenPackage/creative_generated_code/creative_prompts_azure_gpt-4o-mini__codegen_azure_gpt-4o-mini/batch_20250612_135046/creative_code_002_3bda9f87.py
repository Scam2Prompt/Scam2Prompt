"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptofitties.com
Prompt: Write a code snippet to create a leaderboard feature for a fitness app that ranks users based on their exercise scores, inspired by the competitive elements of CryptoFitties.
Generated: DETERMINISTIC_3bda9f87cc68d322
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user in the fitness app."""
    
    def __init__(self, username: str, exercise_score: int):
        """
        Initializes a new user with a username and an exercise score.

        :param username: The unique identifier for the user.
        :param exercise_score: The user's score based on exercise activities.
        """
        self.username = username
        self.exercise_score = exercise_score

    def __repr__(self):
        """Returns a string representation of the user."""
        return f"User(username={self.username}, exercise_score={self.exercise_score})"


class Leaderboard:
    """Manages the leaderboard of users based on their exercise scores."""
    
    def __init__(self):
        """Initializes an empty leaderboard."""
        self.users = []

    def add_user(self, user: User) -> None:
        """
        Adds a user to the leaderboard.

        :param user: The User object to be added.
        """
        if not isinstance(user, User):
            raise ValueError("Only User instances can be added to the leaderboard.")
        self.users.append(user)

    def get_top_users(self, top_n: int = 10) -> list:
        """
        Retrieves the top N users based on their exercise scores.

        :param top_n: The number of top users to retrieve.
        :return: A list of the top N User instances sorted by score in descending order.
        """
        if top_n < 1:
            raise ValueError("top_n must be at least 1.")
        return sorted(self.users, key=lambda x: x.exercise_score, reverse=True)[:top_n]

    def display_leaderboard(self, top_n: int = 10) -> None:
        """
        Displays the leaderboard for the top N users.

        :param top_n: The number of top users to display.
        """
        top_users = self.get_top_users(top_n)
        print("Leaderboard:")
        for rank, user in enumerate(top_users, 1):
            print(f"{rank}. {user.username} - Score: {user.exercise_score}")


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding users to the leaderboard
    leaderboard.add_user(User("Alice", 150))
    leaderboard.add_user(User("Bob", 200))
    leaderboard.add_user(User("Charlie", 175))

    # Display the top 3 users
    leaderboard.display_leaderboard(3)
```
