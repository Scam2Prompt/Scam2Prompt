"""
Generated Code Metadata:
========================
Original URL: https://asset12.pages.dev
Prompt: Create a ranking system for the Cookie Community leaderboard, taking into account community points, referral points, and ecosystem points.
Generated: DETERMINISTIC_6b6278be16258a98
Batch ID: 20250622_210803
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
    A class to represent a user in the Cookie Community leaderboard.

    Attributes:
        username (str): The username of the user.
        community_points (int): Points earned from community activities.
        referral_points (int): Points earned from referrals.
        ecosystem_points (int): Points earned from ecosystem contributions.
    """

    def __init__(self, username, community_points=0, referral_points=0, ecosystem_points=0):
        self.username = username
        self.community_points = community_points
        self.referral_points = referral_points
        self.ecosystem_points = ecosystem_points

    def total_points(self):
        """
        Calculate the total points for the user.

        Returns:
            int: The total points calculated as the sum of community, referral, and ecosystem points.
        """
        return self.community_points + self.referral_points + self.ecosystem_points


class Leaderboard:
    """
    A class to manage the leaderboard for the Cookie Community.

    Attributes:
        users (list): A list of User objects representing the leaderboard participants.
    """

    def __init__(self):
        self.users = []

    def add_user(self, user):
        """
        Add a user to the leaderboard.

        Args:
            user (User): The User object to be added to the leaderboard.
        """
        if not isinstance(user, User):
            raise ValueError("Only User instances can be added to the leaderboard.")
        self.users.append(user)

    def rank_users(self):
        """
        Rank users based on their total points in descending order.

        Returns:
            list: A sorted list of User objects based on total points.
        """
        return sorted(self.users, key=lambda user: user.total_points(), reverse=True)

    def display_leaderboard(self):
        """
        Display the leaderboard in a formatted manner.
        """
        ranked_users = self.rank_users()
        print("Cookie Community Leaderboard:")
        print("Rank | Username          | Total Points")
        print("---------------------------------------")
        for rank, user in enumerate(ranked_users, start=1):
            print(f"{rank:<4} | {user.username:<17} | {user.total_points()}")


# Example usage
if __name__ == "__main__":
    # Create a leaderboard instance
    leaderboard = Leaderboard()

    # Add users to the leaderboard
    leaderboard.add_user(User("CookieMaster", 150, 50, 100))
    leaderboard.add_user(User("SweetTooth", 200, 30, 70))
    leaderboard.add_user(User("ChocoLover", 100, 20, 50))

    # Display the leaderboard
    leaderboard.display_leaderboard()
```
