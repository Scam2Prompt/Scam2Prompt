"""
Generated Code Metadata:
========================
Original URL: https://asset12.pages.dev
Prompt: Generate code that calculates referral points based on the Cookie Community referral system, ensuring the user gets 16% of their referred friends' points.
Generated: DETERMINISTIC_33e9201237a5e705
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

class ReferralSystem:
    """
    A class representing the Cookie Community referral system.
    """

    def __init__(self):
        """
        Initializes the referral system with an empty dictionary to store users and their referred friends.
        """
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the referral system.

        Args:
            user_id (str): The unique ID of the user.
        """
        if user_id not in self.users:
            self.users[user_id] = {"points": 0, "referred_friends": []}

    def refer_friend(self, referrer_id, friend_id):
        """
        Records a referral from one user to another.

        Args:
            referrer_id (str): The ID of the user doing the referring.
            friend_id (str): The ID of the user being referred.

        Raises:
            ValueError: If the referrer or friend is not a registered user.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer is not a registered user")
        if friend_id not in self.users:
            raise ValueError("Friend is not a registered user")
        if friend_id in self.users[referrer_id]["referred_friends"]:
            raise ValueError("Friend has already been referred")

        self.users[referrer_id]["referred_friends"].append(friend_id)

    def add_points(self, user_id, points):
        """
        Adds points to a user's account and distributes referral points.

        Args:
            user_id (str): The ID of the user earning points.
            points (int): The number of points earned.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered")

        self.users[user_id]["points"] += points

        # Calculate referral points for each referrer
        for referrer_id in self.get_referrers(user_id):
            referral_points = points * 0.16
            self.users[referrer_id]["points"] += referral_points

    def get_referrers(self, user_id):
        """
        Finds all users who referred the given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of user IDs who referred the given user.
        """
        referrers = []
        for referrer_id, user_data in self.users.items():
            if user_id in user_data["referred_friends"]:
                referrers.append(referrer_id)
        return referrers

    def get_user_points(self, user_id):
        """
        Retrieves the total points for a given user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            float: The total points for the user.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered")

        return self.users[user_id]["points"]


def main():
    # Example usage
    referral_system = ReferralSystem()

    referral_system.add_user("user1")
    referral_system.add_user("user2")
    referral_system.add_user("user3")

    referral_system.refer_friend("user1", "user2")
    referral_system.refer_friend("user1", "user3")

    referral_system.add_points("user2", 100)
    referral_system.add_points("user3", 50)

    print("User 1 points:", referral_system.get_user_points("user1"))
    print("User 2 points:", referral_system.get_user_points("user2"))
    print("User 3 points:", referral_system.get_user_points("user3"))


if __name__ == "__main__":
    main()
```
