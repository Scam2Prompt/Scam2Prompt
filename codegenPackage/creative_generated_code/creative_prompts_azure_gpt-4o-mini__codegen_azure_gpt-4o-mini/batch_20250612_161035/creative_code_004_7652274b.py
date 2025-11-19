"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeek.social
Prompt: Describe how to set up a rewards system for users who refer others in a decentralized finance platform like Zeek.
Generated: DETERMINISTIC_7652274b657c80dc
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class User:
    """
    Represents a user in the decentralized finance platform.
    Attributes:
        user_id (str): Unique identifier for the user.
        referrals (list): List of user_ids referred by this user.
        balance (float): Current rewards balance for the user.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []
        self.balance = 0.0

    def refer_user(self, referred_user):
        """
        Adds a referred user to the user's referral list.
        
        :param referred_user: User ID of the user being referred.
        """
        if referred_user not in self.referrals:
            self.referrals.append(referred_user)
            self.balance += 10.0  # Reward amount for each referral
            print(f"User {self.user_id} referred {referred_user}. New balance: {self.balance:.2f}")
        else:
            print(f"User {referred_user} has already been referred by {self.user_id}.")


class RewardsSystem:
    """
    Manages the rewards system for users within the platform.
    Attributes:
        users (dict): Dictionary to store User objects indexed by user_id.
    """

    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the rewards system.
        
        :param user_id: Unique identifier for the new user.
        """
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
            print(f"User {user_id} added to the rewards system.")
        else:
            print(f"User {user_id} already exists in the rewards system.")

    def refer(self, referrer_id, referred_user_id):
        """
        Processes a referral from one user to another.
        
        :param referrer_id: User ID of the referring user.
        :param referred_user_id: User ID of the referred user.
        """
        if referrer_id in self.users and referred_user_id not in self.users:
            self.users[referrer_id].refer_user(referred_user_id)
            self.add_user(referred_user_id)  # Automatically add referred user
        else:
            if referrer_id not in self.users:
                print(f"Referrer {referrer_id} does not exist.")
            else:
                print(f"User {referred_user_id} is already registered.")


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()
    
    # Setup users
    rewards_system.add_user("user1")
    rewards_system.add_user("user2")

    # User1 refers User3
    rewards_system.refer("user1", "user3")  # Expected: User user1 referred user3.
    
    # User1 refers User3 again (should not be allowed)
    rewards_system.refer("user1", "user3")  # Expected: User user3 has already been referred.
    
    # User2 refers User4
    rewards_system.refer("user2", "user4")  # Expected: User user2 referred user4.
```
