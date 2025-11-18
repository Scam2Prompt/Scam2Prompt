"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asset12.pages.dev
Prompt: Generate code that calculates referral points based on the Cookie Community referral system, ensuring the user gets 16% of their referred friends' points.
Generated: DETERMINISTIC_33e9201237a5e705
Batch ID: 20250612_153400
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
    Class representing a user in the referral system.
    """

    def __init__(self, user_id):
        """
        Initialize a User instance.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.referral_points = 0
        self.referred_friends = []

    def add_referred_friend(self, friend):
        """
        Add a friend to the user's list of referred friends.

        :param friend: User instance representing the referred friend
        """
        if friend not in self.referred_friends:
            self.referred_friends.append(friend)

    def calculate_referral_points(self):
        """
        Calculate the referral points earned based on referred friends' points.

        The user earns 16% of the total points accrued by referred friends.
        """
        total_points_from_friends = sum(friend.referral_points for friend in self.referred_friends)
        self.referral_points = total_points_from_friends * 0.16
        return self.referral_points


class ReferralSystem:
    """
    Class representing the referral system that manages users and their referrals.
    """

    def __init__(self):
        """
        Initialize a ReferralSystem instance with an empty user registry.
        """
        self.users = {}

    def add_user(self, user_id):
        """
        Add a new user to the referral system.

        :param user_id: Unique identifier for the user
        :raises ValueError: If user_id is already taken
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id)

    def refer_friend(self, referrer_id, referred_id):
        """
        Handle the action of a user referring a friend.

        :param referrer_id: ID of the user who is referring
        :param referred_id: ID of the user being referred
        :raises KeyError: If the referrer or referred user does not exist
        """
        if referrer_id not in self.users or referred_id not in self.users:
            raise KeyError("Both referrer and referred user must exist in the system.")

        referrer = self.users[referrer_id]
        referred = self.users[referred_id]
        referrer.add_referred_friend(referred)

    def update_points(self, user_id, points):
        """
        Update the referral points of a user.

        :param user_id: ID of the user whose points are being updated
        :param points: New points to assign to the user
        :raises KeyError: If the user does not exist
        """
        if user_id not in self.users:
            raise KeyError("User does not exist in the system.")
        self.users[user_id].referral_points = points

    def calculate_all_referral_points(self):
        """
        Calculate referral points for all users based on their referred friends.
        """
        for user in self.users.values():
            user.calculate_referral_points()


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        # Adding users
        referral_system.add_user("user1")
        referral_system.add_user("user2")
        referral_system.add_user("user3")

        # Updating referred users points
        referral_system.update_points("user2", 100)  # user2 has 100 points
        referral_system.update_points("user3", 200)  # user3 has 200 points

        # Referring friends
        referral_system.refer_friend("user1", "user2")
        referral_system.refer_friend("user1", "user3")

        # Calculate referral points
        referral_system.calculate_all_referral_points()

        # Output referral points for user1
        print(f"User {referral_system.users['user1'].user_id} has referral points: {referral_system.users['user1'].referral_points}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
