"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Write a function to track and display referral counts and rewards for users, as per the referral system described on Rift Swap.
Generated: DETERMINISTIC_a50bd2a065396ae5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    def __init__(self):
        # Dictionary to hold user referral data
        self.referrals = {}
        # Dictionary to hold rewards for each user
        self.rewards = {}
        # Default reward per referral
        self.reward_per_referral = 10

    def add_referral(self, referrer, referred):
        """
        Adds a referral from the referrer to the referred user.
        Increments the referrer's referral count and updates rewards.
        
        :param referrer: The user who is referring others
        :param referred: The user being referred
        :raises ValueError: If either user does not exist or if the referred user is the same as the referrer
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = 0
        if referred not in self.referrals and referred != referrer:
            # Increment the referral count for the referrer
            self.referrals[referrer] += 1
            # Update the rewards for the referrer
            self.rewards[referrer] = self.rewards.get(referrer, 0) + self.reward_per_referral
            self.referrals[referred] = 0  # Initialize referred user
        else:
            raise ValueError("Invalid referral: Users must be distinct or referred user already exists.")

    def get_referral_count(self, user):
        """
        Returns the referral count for the specified user.
        
        :param user: The user whose referral count is requested
        :return: The number of referrals for the user
        :raises KeyError: If the user does not exist in the referral system
        """
        if user not in self.referrals:
            raise KeyError(f"User '{user}' not found.")
        return self.referrals[user]

    def get_rewards(self, user):
        """
        Returns the total rewards for the specified user.
        
        :param user: The user whose rewards are requested
        :return: The total rewards for the user
        :raises KeyError: If the user does not exist in the referral system
        """
        if user not in self.rewards:
            raise KeyError(f"User '{user}' not found.")
        return self.rewards[user]

    def display_referral_stats(self):
        """
        Displays the referral counts and rewards for all users in the system.
        """
        print("Referral Stats:")
        for user in self.referrals:
            print(f"User: {user}, Referrals: {self.referrals[user]}, Rewards: {self.rewards.get(user, 0)}")

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users and referrals
    try:
        referral_system.add_referral("Alice", "Bob")
        referral_system.add_referral("Alice", "Charlie")
        referral_system.add_referral("Bob", "David")
        
        # Displaying stats
        referral_system.display_referral_stats()
        
        # Fetching specific counts and rewards
        print(f"Alice's referrals: {referral_system.get_referral_count('Alice')}")
        print(f"Alice's rewards: {referral_system.get_rewards('Alice')}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
