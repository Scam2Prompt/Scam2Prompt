"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Generate code to implement a referral system that tracks points earned by referred users and calculates the 16% commission for the referrer, as described in the Cookie Community referral program.
Generated: DETERMINISTIC_6f75762a02102ab2
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Referral System Implementation
# Tracks points earned by referred users and calculates a 16% commission for the referrer.
# Language: Python

class ReferralSystem:
    def __init__(self):
        """
        Initializes the referral system with empty data structures to store user and referral information.
        """
        self.users = {}  # Dictionary to store user data: {user_id: {"points": int, "referrer_id": str}}
        self.referral_commissions = {}  # Dictionary to store total commissions earned by referrers: {referrer_id: float}

    def add_user(self, user_id, referrer_id=None):
        """
        Adds a new user to the system.

        Args:
            user_id (str): Unique identifier for the new user.
            referrer_id (str, optional): Unique identifier for the referrer. Defaults to None.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists!")
        
        self.users[user_id] = {"points": 0, "referrer_id": referrer_id}
        if referrer_id and referrer_id not in self.referral_commissions:
            self.referral_commissions[referrer_id] = 0.0

    def add_points(self, user_id, points):
        """
        Adds points to a user's account and calculates commission for the referrer if applicable.

        Args:
            user_id (str): Unique identifier for the user earning points.
            points (int): Points to be added.

        Raises:
            ValueError: If the user_id does not exist or points are negative.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist!")
        if points < 0:
            raise ValueError("Points cannot be negative!")

        # Update user's points
        self.users[user_id]["points"] += points

        # Calculate and distribute commission to referrer, if applicable
        referrer_id = self.users[user_id]["referrer_id"]
        if referrer_id:
            commission = points * 0.16  # 16% commission
            self.referral_commissions[referrer_id] += commission

    def get_user_points(self, user_id):
        """
        Retrieves points for a given user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: Points earned by the user.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist!")
        return self.users[user_id]["points"]

    def get_referral_commission(self, referrer_id):
        """
        Retrieves total commission earned by a referrer.

        Args:
            referrer_id (str): Unique identifier for the referrer.

        Returns:
            float: Total commission earned by the referrer.

        Raises:
            ValueError: If the referrer_id does not exist.
        """
        if referrer_id not in self.referral_commissions:
            raise ValueError("Referrer ID does not exist!")
        return self.referral_commissions[referrer_id]

    def display_summary(self):
        """
        Displays a summary of all users, their points, and referral commissions.
        """
        print("User Summary:")
        for user_id, data in self.users.items():
            print(f"User ID: {user_id}, Points: {data['points']}, Referrer: {data['referrer_id']}")
        
        print("\nReferral Commissions:")
        for referrer_id, commission in self.referral_commissions.items():
            print(f"Referrer ID: {referrer_id}, Total Commission: {commission:.2f}")


# Example Usage (Uncomment for testing)
# --------------------------
# Create referral system instance
# referral_system = ReferralSystem()

# Add users
# referral_system.add_user("user1")
# referral_system.add_user("user2", "user1")
# referral_system.add_user("user3", "user1")
# referral_system.add_user("user4", "user2")

# Add points to users
# referral_system.add_points("user2", 100)
# referral_system.add_points("user3", 200)
# referral_system.add_points("user4", 150)

# Retrieve individual data
# print(referral_system.get_user_points("user2"))  # Output: 100
# print(referral_system.get_referral_commission("user1"))  # Output: 48.0

# Display summary
# referral_system.display_summary()
```
