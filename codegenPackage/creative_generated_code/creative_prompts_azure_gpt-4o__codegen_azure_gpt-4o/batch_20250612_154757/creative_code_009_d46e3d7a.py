"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Write a Python script to track and display the referral rewards earned by a user, including the total number of referrals and the corresponding $INIT token balance.
Generated: DETERMINISTIC_d46e3d7a9ae31b51
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ReferralRewardsTracker:
    """
    A class to track and display referral rewards earned by a user.
    """

    def __init__(self, initial_token_value=10):
        """
        Initialize the referral tracker with a default token value for each referral.
        
        :param initial_token_value: Value in $INIT tokens for each referral (default is 10).
        """
        self.referrals = {}  # Dictionary to store user referrals and their token balances.
        self.initial_token_value = initial_token_value

    def add_referral(self, user_id, referred_user_id):
        """
        Add a referral for a user and update the token balance.
        
        :param user_id: ID of the user who referred someone.
        :param referred_user_id: ID of the user who was referred.
        :return: None
        """
        if user_id not in self.referrals:
            self.referrals[user_id] = {"total_referrals": 0, "token_balance": 0}

        # Update referral count and token balance.
        self.referrals[user_id]["total_referrals"] += 1
        self.referrals[user_id]["token_balance"] += self.initial_token_value
        
        print(f"Referral added: {user_id} referred {referred_user_id}.")
        print(f"Updated token balance: {self.referrals[user_id]['token_balance']} $INIT.")
    
    def get_rewards_summary(self, user_id):
        """
        Retrieve the referral rewards summary for a user.
        
        :param user_id: ID of the user whose summary is requested.
        :return: Dictionary containing total referrals and token balance.
        """
        if user_id not in self.referrals:
            raise ValueError(f"No referrals found for user ID: {user_id}")
        
        return self.referrals[user_id]

    def save_to_file(self, filename="referral_rewards.json"):
        """
        Save referral rewards data to a JSON file.
        
        :param filename: Name of the file to save data to.
        :return: None
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.referrals, file, indent=4)
            print(f"Referral rewards saved to {filename}.")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, filename="referral_rewards.json"):
        """
        Load referral rewards data from a JSON file.
        
        :param filename: Name of the file to load data from.
        :return: None
        """
        try:
            with open(filename, "r") as file:
                self.referrals = json.load(file)
            print(f"Referral rewards loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty dataset.")
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage:
if __name__ == "__main__":
    tracker = ReferralRewardsTracker()

    # Adding referrals
    tracker.add_referral("user1", "ref_userA")
    tracker.add_referral("user1", "ref_userB")
    tracker.add_referral("user2", "ref_userC")

    # Displaying rewards summary
    try:
        user1_summary = tracker.get_rewards_summary("user1")
        print("User1 Rewards Summary:", user1_summary)
    except ValueError as e:
        print(e)

    # Save to file
    tracker.save_to_file()

    # Load from file
    tracker.load_from_file()

    # Displaying rewards summary after loading data
    try:
        user2_summary = tracker.get_rewards_summary("user2")
        print("User2 Rewards Summary:", user2_summary)
    except ValueError as e:
        print(e)
```
