"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-shibabudz.pages.dev
Prompt: Explain how to implement a referral program for the Shibabudz token that allows users to earn up to 5% from their friends' first purchases.
Generated: DETERMINISTIC_140c308ac8b03ab9
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    A class to implement a referral program for the Shibabudz token.
    Users can earn a percentage from their friends' first purchases.
    """

    def __init__(self):
        # Initialize a dictionary to store users and their referrals
        self.users = {}
        self.referral_rewards = {}

    def register_user(self, user_id, referrer_id=None):
        """
        Register a new user in the referral program.
        
        Parameters:
            user_id (str): The unique identifier for the user.
            referrer_id (str): The ID of the user who referred this new user.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        
        # Register user with optional referrer
        self.users[user_id] = {
            'referrer': referrer_id,
            'first_purchase': False
        }

        # Initialize referral reward for the referrer if applicable
        if referrer_id and referrer_id in self.users:
            self.referral_rewards[referrer_id] = self.referral_rewards.get(referrer_id, 0)

    def record_purchase(self, user_id, purchase_amount):
        """
        Record a purchase made by a user and allocate referral rewards if applicable.
        
        Parameters:
            user_id (str): The ID of the user making the purchase.
            purchase_amount (float): The amount of the purchase.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")

        if self.users[user_id]['first_purchase']:
            raise ValueError(f"User {user_id} has already made a purchase.")

        # Mark the user's first purchase as completed
        self.users[user_id]['first_purchase'] = True

        # Allocate referral rewards
        self._allocate_referral_reward(user_id, purchase_amount)

    def _allocate_referral_reward(self, user_id, purchase_amount):
        """
        Private method to allocate referral rewards to the referrer.
        
        Parameters:
            user_id (str): The ID of the user who made the purchase.
            purchase_amount (float): The amount of the purchase.
        """
        referrer_id = self.users[user_id]['referrer']
        if referrer_id:
            reward = min(0.05 * purchase_amount, purchase_amount)  # User earns up to 5% of purchase amount
            self.referral_rewards[referrer_id] += reward

    def get_referral_rewards(self, user_id):
        """
        Get the referral rewards of a specific user.
        
        Parameters:
            user_id (str): The ID of the user.

        Returns:
            float: The total referral rewards earned by the user.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.referral_rewards.get(user_id, 0)


# Example usage
def main():
    referral_program = ReferralProgram()

    # Register users
    referral_program.register_user("Alice")
    referral_program.register_user("Bob", "Alice")  # Bob is referred by Alice

    # Record purchases
    referral_program.record_purchase("Bob", 100)  # Bob makes a first purchase of 100

    # Get referral rewards
    alice_rewards = referral_program.get_referral_rewards("Alice")
    print(f"Alice's referral rewards: {alice_rewards}")  # Expected output: 5.0


if __name__ == "__main__":
    main()
```
