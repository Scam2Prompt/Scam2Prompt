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
# Python code to calculate referral points based on the Cookie Community referral system.

class ReferralSystem:
    """
    A class to represent the Cookie Community referral system.
    """

    def __init__(self):
        """
        Initializes the referral system with an empty user database.
        """
        self.user_points = {}  # Dictionary to store user points (user_id -> points)
        self.referrals = {}    # Dictionary to store referrals (user_id -> [referral_user_ids])

    def add_user(self, user_id, points=0):
        """
        Adds a new user to the system.
        
        Parameters:
        user_id (str): Unique identifier for the user.
        points (int): Initial points for the user (default is 0).
        """
        if user_id in self.user_points:
            raise ValueError("User already exists.")
        self.user_points[user_id] = points
        self.referrals[user_id] = []

    def add_referral(self, user_id, referral_id):
        """
        Adds a referral relationship between a user and a referred friend.

        Parameters:
        user_id (str): The user who referred someone.
        referral_id (str): The user who was referred.
        """
        if user_id not in self.user_points:
            raise ValueError("Referring user does not exist.")
        if referral_id not in self.user_points:
            raise ValueError("Referred user does not exist.")
        self.referrals[user_id].append(referral_id)

    def update_points(self, user_id, points):
        """
        Updates the points for a given user.

        Parameters:
        user_id (str): Unique identifier for the user.
        points (int): The new points to set for the user.
        """
        if user_id not in self.user_points:
            raise ValueError("User does not exist.")
        self.user_points[user_id] = points

    def calculate_referral_points(self, user_id):
        """
        Calculates referral points for a user based on their referred friends' points.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        float: Total referral points earned by the user.
        """
        if user_id not in self.user_points:
            raise ValueError("User does not exist.")

        referral_points = 0
        for referral_id in self.referrals.get(user_id, []):
            referral_points += self.user_points[referral_id] * 0.16  # 16% of referred friend's points

        return referral_points

    def display_user_info(self, user_id):
        """
        Displays information about a user including their points and referral points.

        Parameters:
        user_id (str): Unique identifier for the user.
        """
        if user_id not in self.user_points:
            raise ValueError("User does not exist.")

        user_points = self.user_points[user_id]
        referral_points = self.calculate_referral_points(user_id)

        print(f"User ID: {user_id}")
        print(f"Points: {user_points}")
        print(f"Referral Points: {referral_points:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral system
        system = ReferralSystem()

        # Add users
        system.add_user("user1", 100)
        system.add_user("user2", 200)
        system.add_user("user3", 300)

        # Create referral relationships
        system.add_referral("user1", "user2")
        system.add_referral("user1", "user3")

        # Update points for referred users (optional example)
        system.update_points("user2", 250)
        system.update_points("user3", 320)

        # Display user information
        system.display_user_info("user1")
        system.display_user_info("user2")
        system.display_user_info("user3")

    except Exception as e:
        print(f"Error: {e}")
```
