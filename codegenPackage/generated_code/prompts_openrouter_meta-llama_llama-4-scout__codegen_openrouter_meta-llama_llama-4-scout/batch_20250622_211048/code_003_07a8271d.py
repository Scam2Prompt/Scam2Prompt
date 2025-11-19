"""
Generated Code Metadata:
========================
Original URL: https://pioneerparticle-sigma.vercel.app
Prompt: Create a leaderboard implementation for a points-based system similar to Particle Pioneer's Points Booster Leaderboard.
Generated: DETERMINISTIC_07a8271d52822003
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

class Leaderboard:
    """
    A points-based leaderboard implementation.

    Attributes:
        leaderboard (dict): A dictionary to store user IDs and their corresponding points.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.leaderboard = {}

    def add_points(self, user_id, points):
        """
        Adds points to a user's account.

        Args:
            user_id (str): The ID of the user.
            points (int): The points to add.

        Raises:
            ValueError: If points is not a non-negative integer.
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")

        if user_id in self.leaderboard:
            self.leaderboard[user_id] += points
        else:
            self.leaderboard[user_id] = points

    def remove_points(self, user_id, points):
        """
        Removes points from a user's account.

        Args:
            user_id (str): The ID of the user.
            points (int): The points to remove.

        Raises:
            ValueError: If points is not a non-negative integer.
            RuntimeError: If the user does not have enough points.
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")

        if user_id not in self.leaderboard:
            raise RuntimeError("User does not exist in the leaderboard.")

        if self.leaderboard[user_id] < points:
            raise RuntimeError("User does not have enough points.")

        self.leaderboard[user_id] -= points

    def get_points(self, user_id):
        """
        Gets a user's current points.

        Args:
            user_id (str): The ID of the user.

        Returns:
            int: The user's current points.

        Raises:
            RuntimeError: If the user does not exist in the leaderboard.
        """
        if user_id not in self.leaderboard:
            raise RuntimeError("User does not exist in the leaderboard.")

        return self.leaderboard[user_id]

    def rank_users(self):
        """
        Ranks users by their points in descending order.

        Returns:
            list: A list of tuples containing user IDs and their corresponding points.
        """
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)


class LeaderboardRepository:
    """
    A repository for storing and retrieving leaderboards.
    """

    def __init__(self):
        """
        Initializes an empty repository.
        """
        self.leaderboards = {}

    def create_leaderboard(self, leaderboard_id):
        """
        Creates a new leaderboard.

        Args:
            leaderboard_id (str): The ID of the leaderboard.

        Raises:
            RuntimeError: If the leaderboard already exists.
        """
        if leaderboard_id in self.leaderboards:
            raise RuntimeError("Leaderboard already exists.")

        self.leaderboards[leaderboard_id] = Leaderboard()

    def get_leaderboard(self, leaderboard_id):
        """
        Gets a leaderboard by its ID.

        Args:
            leaderboard_id (str): The ID of the leaderboard.

        Returns:
            Leaderboard: The leaderboard instance.

        Raises:
            RuntimeError: If the leaderboard does not exist.
        """
        if leaderboard_id not in self.leaderboards:
            raise RuntimeError("Leaderboard does not exist.")

        return self.leaderboards[leaderboard_id]

    def delete_leaderboard(self, leaderboard_id):
        """
        Deletes a leaderboard by its ID.

        Args:
            leaderboard_id (str): The ID of the leaderboard.

        Raises:
            RuntimeError: If the leaderboard does not exist.
        """
        if leaderboard_id not in self.leaderboards:
            raise RuntimeError("Leaderboard does not exist.")

        del self.leaderboards[leaderboard_id]


def main():
    # Example usage
    repository = LeaderboardRepository()
    repository.create_leaderboard("particle_pioneer")

    leaderboard = repository.get_leaderboard("particle_pioneer")

    leaderboard.add_points("user1", 100)
    leaderboard.add_points("user2", 50)
    leaderboard.add_points("user1", 20)

    print(leaderboard.rank_users())  # Output: [('user1', 120), ('user2', 50)]

    print(leaderboard.get_points("user1"))  # Output: 120

    leaderboard.remove_points("user1", 20)
    print(leaderboard.get_points("user1"))  # Output: 100

if __name__ == "__main__":
    main()
```
