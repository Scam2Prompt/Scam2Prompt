"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Outline the steps to implement a referral program that rewards users with CRUDO tokens for bringing in new customers to the platform.
Generated: DETERMINISTIC_ef1e574b8949bc31
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self):
        # Initialize an empty dictionary to store user referrals
        self.referrals = {}
        # Initialize a rewards pool for CRUDO tokens
        self.rewards_pool = 100000  # Example starting token amount
        self.reward_per_referral = 10  # Tokens awarded per successful referral

    def register_user(self, user_id):
        """
        Registers a new user into the referral program.
        
        :param user_id: Unique identifier for the user
        """
        if user_id in self.referrals:
            raise ValueError(f"User {user_id} is already registered.")
        self.referrals[user_id] = {'referrals': 0, 'total_rewards': 0}

    def refer_user(self, referrer_id, new_user_id):
        """
        Allows a user to refer a new user.
        
        :param referrer_id: User ID of the referrer
        :param new_user_id: Unique identifier for the new user
        :raises ValueError: If the referrer is not registered or if the new user is already registered
        """
        if referrer_id not in self.referrals:
            raise ValueError(f"Referrer {referrer_id} is not registered.")
        if new_user_id in self.referrals:
            raise ValueError(f"User {new_user_id} is already registered.")

        # Register the new user
        self.register_user(new_user_id)
        # Update referral count for the referrer
        self.referrals[referrer_id]['referrals'] += 1
        # Award tokens to the referrer
        self.award_tokens(referrer_id)

    def award_tokens(self, user_id):
        """
        Awards tokens to a user for a successful referral.
        
        :param user_id: Unique identifier for the user
        """
        if self.rewards_pool < self.reward_per_referral:
            raise ValueError("Insufficient rewards pool to award tokens.")
        
        self.referrals[user_id]['total_rewards'] += self.reward_per_referral
        self.rewards_pool -= self.reward_per_referral

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards of a user.
        
        :param user_id: Unique identifier for the user
        :return: Total rewards of the user
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.referrals:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.referrals[user_id]['total_rewards']

    def get_referral_count(self, user_id):
        """
        Retrieves the number of referrals made by a user.
        
        :param user_id: Unique identifier for the user
        :return: Number of referrals made by the user
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.referrals:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.referrals[user_id]['referrals']

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        # Register users
        referral_program.register_user("user_1")
        referral_program.register_user("user_2")
        
        # User_1 refers User_2
        referral_program.refer_user("user_1", "user_2")
        
        # Print rewards and referral counts
        print("User 1 Rewards:", referral_program.get_user_rewards("user_1"))
        print("User 1 Referral Count:", referral_program.get_referral_count("user_1"))
    except ValueError as e:
        print(f"Error: {e}")
```
