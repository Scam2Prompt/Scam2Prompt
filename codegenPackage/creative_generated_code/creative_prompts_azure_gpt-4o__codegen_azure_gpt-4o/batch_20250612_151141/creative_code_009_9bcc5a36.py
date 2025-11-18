"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: Write a tutorial-style code snippet to implement a staking dashboard for $TUK tokens, displaying staked amounts, earned rewards, and claiming functionality.
Generated: DETERMINISTIC_9bcc5a361cd5627e
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_dashboard.py

"""
This script implements a staking dashboard for $TUK tokens.
It displays staked amounts, earned rewards, and provides a function for claiming rewards.
This example assumes a simplified local implementation and a mock backend.
"""

import datetime

class TUKTokenStakingDashboard:
    def __init__(self):
        # Initialize user staking data
        self.staking_data = {}
        # Initialize mock token reward rate (e.g., 0.05 reward per token per day)
        self.reward_rate = 0.05

    def stake_tokens(self, user, amount):
        """
        Allows a user to stake tokens.
        
        :param user: str - The user's identifier
        :param amount: float - The amount of $TUK tokens to stake
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # If the user is new, initialize their data
        if user not in self.staking_data:
            self.staking_data[user] = {"staked_amount": 0, "last_staked_time": datetime.datetime.now()}
        
        # Update user's staked amount and staking time
        self.staking_data[user]["staked_amount"] += amount
        self.staking_data[user]["last_staked_time"] = datetime.datetime.now()
        print(f"{user} has staked {amount} $TUK tokens.")

    def calculate_rewards(self, user):
        """
        Calculates the earned rewards for a user based on the reward rate.
        
        :param user: str - The user's identifier
        :return: float - The total earned rewards
        """
        if user not in self.staking_data:
            raise ValueError("User has no staking data.")
        
        user_data = self.staking_data[user]
        time_staked = datetime.datetime.now() - user_data["last_staked_time"]
        days_staked = time_staked.total_seconds() / 86400  # Convert seconds to days
        
        # Calculate rewards
        rewards = user_data["staked_amount"] * self.reward_rate * days_staked
        return round(rewards, 2)

    def display_dashboard(self, user):
        """
        Displays the staking dashboard for the user.
        
        :param user: str - The user's identifier
        """
        if user not in self.staking_data:
            raise ValueError("User has no staking data.")
        
        user_data = self.staking_data[user]
        earned_rewards = self.calculate_rewards(user)
        
        # Dashboard display
        print(f"--- Staking Dashboard for {user} ---")
        print(f"Staked Amount: {user_data['staked_amount']} $TUK")
        print(f"Earned Rewards: {earned_rewards} $TUK")
        print("-----------------------------------")

    def claim_rewards(self, user):
        """
        Allows the user to claim their earned rewards.
        
        :param user: str - The user's identifier
        """
        if user not in self.staking_data:
            raise ValueError("User has no staking data.")
        
        earned_rewards = self.calculate_rewards(user)
        if earned_rewards <= 0:
            raise ValueError("No rewards available to claim.")
        
        # Reset staking time after claiming rewards
        self.staking_data[user]["last_staked_time"] = datetime.datetime.now()
        print(f"{user} has claimed {earned_rewards} $TUK rewards.")
        return earned_rewards


# Example Usage
if __name__ == "__main__":
    dashboard = TUKTokenStakingDashboard()
    
    # User stakes tokens
    dashboard.stake_tokens("Alice", 100)
    dashboard.stake_tokens("Bob", 50)
    
    # Display dashboard and calculate rewards
    dashboard.display_dashboard("Alice")
    dashboard.display_dashboard("Bob")
    
    # Claim rewards
    try:
        dashboard.claim_rewards("Alice")
        dashboard.claim_rewards("Bob")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Display updated dashboard
    dashboard.display_dashboard("Alice")
    dashboard.display_dashboard("Bob")
```
