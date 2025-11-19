"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoons.web.app
Prompt: Explain how to implement a leaderboard feature for the Kangamoon community, rewarding users based on their participation and $KANG earnings.
Generated: DETERMINISTIC_7f06438a8c293889
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the Kangamoon community.
    Attributes:
        username (str): The username of the user.
        participation_score (int): The score based on community participation.
        kang_earnings (float): The amount of $KANG earned by the user.
    """
    def __init__(self, username, participation_score=0, kang_earnings=0.0):
        self.username = username
        self.participation_score = participation_score
        self.kang_earnings = kang_earnings

    def __repr__(self):
        return f"User(username='{self.username}', participation_score={self.participation_score}, kang_earnings={self.kang_earnings})"


class Leaderboard:
    """
    A leaderboard to manage and display user rankings based on their participation and $KANG earnings.
    """
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """
        Adds a new user to the leaderboard.
        Args:
            user (User): The User object to add.
        Raises:
            ValueError: If user already exists on the leaderboard.
        """
        if self.get_user(user.username) is not None:
            raise ValueError(f"User {user.username} already exists on the leaderboard.")
        self.users.append(user)

    def get_user(self, username):
        """
        Retrieves a user by username.
        Args:
            username (str): The username of the user to retrieve.
        Returns:
            User: The User object if found, else None.
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update_user(self, username, participation_score=0, kang_earnings=0.0):
        """
        Updates user's scores and earnings.
        Args:
            username (str): The username of the user to update.
            participation_score (int): New participation score to add.
            kang_earnings (float): New $KANG earnings to add.
        Raises:
            ValueError: If user is not found.
        """
        user = self.get_user(username)
        if user is None:
            raise ValueError(f"User {username} not found on the leaderboard.")
        
        user.participation_score += participation_score
        user.kang_earnings += kang_earnings

    def get_leaderboard(self):
        """
        Returns the leaderboard sorted by participation score and $KANG earnings.
        Returns:
            list: List of users sorted by their scores and earnings.
        """
        return sorted(self.users, key=lambda user: (user.participation_score, user.kang_earnings), reverse=True)

    def display_leaderboard(self):
        """
        Displays the leaderboard in a readable format.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, user in enumerate(leaderboard, start=1):
            print(f"{rank}. {user.username} - Participation: {user.participation_score}, $KANG Earned: {user.kang_earnings:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()

        # Adding users
        user1 = User("Alice", participation_score=10, kang_earnings=150.0)
        user2 = User("Bob", participation_score=20, kang_earnings=100.0)
        user3 = User("Charlie", participation_score=15, kang_earnings=200.0)

        leaderboard.add_user(user1)
        leaderboard.add_user(user2)
        leaderboard.add_user(user3)

        # Updating user scores
        leaderboard.update_user("Alice", participation_score=5, kang_earnings=50.0)

        # Displaying the leaderboard
        leaderboard.display_leaderboard()

    except ValueError as e:
        print(f"Error: {e}")
```
