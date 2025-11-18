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
# Import necessary modules
from collections import defaultdict

class ReferralSystem:
    """
    A class to manage the referral system, track referral counts, 
    and calculate rewards for users.
    """
    def __init__(self, reward_per_referral=10):
        """
        Initializes the referral system.
        
        :param reward_per_referral: The reward amount for each successful referral (default is 10).
        """
        self.referral_counts = defaultdict(int)  # Stores the count of referrals per user
        self.user_rewards = defaultdict(float)   # Stores the rewards earned by each user
        self.reward_per_referral = reward_per_referral  # Reward per successful referral

    def add_referral(self, referrer_username):
        """
        Adds a referral for the given user and updates their rewards.
        
        :param referrer_username: The username of the user who made the referral.
        """
        try:
            # Increment the referral count for the user
            self.referral_counts[referrer_username] += 1
            
            # Calculate the reward for the user
            self.user_rewards[referrer_username] = (
                self.referral_counts[referrer_username] * self.reward_per_referral
            )
        except Exception as e:
            print(f"Error adding referral for {referrer_username}: {e}")

    def get_user_referral_info(self, username):
        """
        Retrieves the referral count and rewards for a specific user.
        
        :param username: The username of the user.
        :return: A dictionary containing the user's referral count and rewards.
        """
        try:
            return {
                "username": username,
                "referral_count": self.referral_counts[username],
                "reward": self.user_rewards[username],
            }
        except KeyError:
            return {"error": f"User {username} not found."}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

    def display_all_users(self):
        """
        Displays the referral counts and rewards for all users in the system.
        """
        print("Referral System Summary:")
        print("-------------------------------------")
        for user, count in self.referral_counts.items():
            reward = self.user_rewards[user]
            print(f"User: {user}, Referrals: {count}, Rewards: ${reward:.2f}")
        print("-------------------------------------")

# Example usage of ReferralSystem
if __name__ == "__main__":
    # Initialize the referral system with a reward of $15 per referral
    system = ReferralSystem(reward_per_referral=15)

    # Adding referrals
    system.add_referral("alice")
    system.add_referral("bob")
    system.add_referral("alice")
    system.add_referral("alice")
    system.add_referral("bob")
    
    # Get individual user referral info
    print(system.get_user_referral_info("alice"))
    print(system.get_user_referral_info("bob"))
    print(system.get_user_referral_info("charlie"))  # Non-existing user

    # Display referral counts and rewards for all users
    system.display_all_users()
```
