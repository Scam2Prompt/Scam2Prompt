"""
Generated Code Metadata:
========================
Original URL: https://nftcap.pages.dev
Prompt: "Design a system for tracking and rewarding users with points (e.g., OG Points) for activities on an NFT lending platform."
Generated: DETERMINISTIC_dda6dbaf1637f21d
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_points_system.py

from typing import Dict
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserPointsSystem:
    """
    A system for tracking and rewarding users with points for activities on an NFT lending platform.
    """

    def __init__(self):
        # Initialize an in-memory data store for demonstration purposes.
        # In a production environment, consider using a database.
        self.user_points: Dict[str, int] = {}
        self.activity_points: Dict[str, int] = {
            "nft_lend": 10,
            "nft_borrow": 5,
            "nft_list": 2,
        }

    def add_points(self, user_id: str, activity: str) -> None:
        """
        Adds points to a user's account for a specific activity.

        Args:
        - user_id (str): The ID of the user.
        - activity (str): The type of activity.

        Raises:
        - ValueError: If the activity is not recognized.
        """
        if activity not in self.activity_points:
            logger.error(f"Unrecognized activity: {activity}")
            raise ValueError(f"Unrecognized activity: {activity}")

        points = self.activity_points[activity]
        if user_id not in self.user_points:
            self.user_points[user_id] = points
        else:
            self.user_points[user_id] += points

        logger.info(f"Added {points} points to user {user_id} for activity {activity}")

    def get_user_points(self, user_id: str) -> int:
        """
        Retrieves the total points for a user.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - int: The total points for the user.
        """
        return self.user_points.get(user_id, 0)

    def reset_user_points(self, user_id: str) -> None:
        """
        Resets a user's points to zero.

        Args:
        - user_id (str): The ID of the user.
        """
        if user_id in self.user_points:
            del self.user_points[user_id]
            logger.info(f"Reset points for user {user_id}")
        else:
            logger.info(f"No points to reset for user {user_id}")

    def update_activity_points(self, activity: str, points: int) -> None:
        """
        Updates the points awarded for a specific activity.

        Args:
        - activity (str): The type of activity.
        - points (int): The new points value.

        Raises:
        - ValueError: If the points value is negative.
        """
        if points < 0:
            logger.error(f"Points value cannot be negative: {points}")
            raise ValueError(f"Points value cannot be negative: {points}")

        self.activity_points[activity] = points
        logger.info(f"Updated points for activity {activity} to {points}")


class NFTLendingPlatform:
    """
    A simulated NFT lending platform that integrates with the user points system.
    """

    def __init__(self, user_points_system: UserPointsSystem):
        self.user_points_system = user_points_system

    def lend_nft(self, user_id: str, nft_id: str) -> None:
        """
        Simulates lending an NFT and rewards the user with points.

        Args:
        - user_id (str): The ID of the user.
        - nft_id (str): The ID of the NFT.
        """
        try:
            self.user_points_system.add_points(user_id, "nft_lend")
            logger.info(f"User {user_id} lent NFT {nft_id}")
        except Exception as e:
            logger.error(f"Error lending NFT: {e}")

    def borrow_nft(self, user_id: str, nft_id: str) -> None:
        """
        Simulates borrowing an NFT and rewards the user with points.

        Args:
        - user_id (str): The ID of the user.
        - nft_id (str): The ID of the NFT.
        """
        try:
            self.user_points_system.add_points(user_id, "nft_borrow")
            logger.info(f"User {user_id} borrowed NFT {nft_id}")
        except Exception as e:
            logger.error(f"Error borrowing NFT: {e}")

    def list_nft(self, user_id: str, nft_id: str) -> None:
        """
        Simulates listing an NFT and rewards the user with points.

        Args:
        - user_id (str): The ID of the user.
        - nft_id (str): The ID of the NFT.
        """
        try:
            self.user_points_system.add_points(user_id, "nft_list")
            logger.info(f"User {user_id} listed NFT {nft_id}")
        except Exception as e:
            logger.error(f"Error listing NFT: {e}")


def main():
    user_points_system = UserPointsSystem()
    nft_lending_platform = NFTLendingPlatform(user_points_system)

    # Example usage:
    user_id = "user123"
    nft_id = "nft456"

    nft_lending_platform.lend_nft(user_id, nft_id)
    nft_lending_platform.borrow_nft(user_id, nft_id)
    nft_lending_platform.list_nft(user_id, nft_id)

    print(f"User {user_id} has {user_points_system.get_user_points(user_id)} points")


if __name__ == "__main__":
    main()
```
