"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-pad.pages.dev
Prompt: How can I implement a staking feature for AITECH tokens that allows users to earn rewards based on different lock terms and APY rates?
Generated: DETERMINISTIC_21eb673129520079
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class StakingContract:
    def __init__(self):
        # Dictionary to store user staking details
        # Format: {user_address: [{'amount': amount, 'lock_period': lock_period, 'apy': apy, 'start_time': start_time}]}
        self.stakes = {}

    def stake_tokens(self, user_address, amount, lock_period, apy):
        """
        Allows a user to stake tokens.
        
        :param user_address: Address of the user staking tokens
        :param amount: Amount of tokens to stake
        :param lock_period: Lock period in days
        :param apy: Annual Percentage Yield (reward rate)
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if lock_period <= 0:
            raise ValueError("Lock period must be greater than zero.")
        if apy <= 0:
            raise ValueError("APY must be greater than zero.")
        
        start_time = datetime.now()
        stake_data = {
            'amount': amount,
            'lock_period': lock_period,
            'apy': apy,
            'start_time': start_time
        }
        
        if user_address not in self.stakes:
            self.stakes[user_address] = []
        
        self.stakes[user_address].append(stake_data)
        print(f"User {user_address} staked {amount} AITECH tokens for {lock_period} days at {apy}% APY.")

    def calculate_rewards(self, user_address):
        """
        Calculates the total rewards for a user based on their stakes.
        
        :param user_address: Address of the user
        :return: Total rewards earned by the user
        """
        if user_address not in self.stakes:
            raise ValueError("No stakes found for this user.")

        total_rewards = 0
        current_time = datetime.now()

        for stake in self.stakes[user_address]:
            lock_period_days = stake['lock_period']
            apy = stake['apy']
            amount = stake['amount']
            start_time = stake['start_time']

            # Calculate the days since staking started
            elapsed_days = (current_time - start_time).days

            # If lock period is not completed, no rewards are calculated
            if elapsed_days < lock_period_days:
                continue
            
            # Calculate rewards based on APY formula
            daily_rate = apy / 100 / 365
            rewards = amount * daily_rate * elapsed_days
            total_rewards += rewards
        
        return total_rewards

    def withdraw_stake(self, user_address):
        """
        Allows a user to withdraw their stake along with rewards if lock period has ended.

        :param user_address: Address of the user
        :return: Total tokens withdrawn (stake + rewards)
        """
        if user_address not in self.stakes:
            raise ValueError("No stakes found for this user.")

        total_withdrawn = 0
        current_time = datetime.now()
        valid_stakes = []

        for stake in self.stakes[user_address]:
            lock_period_days = stake['lock_period']
            apy = stake['apy']
            amount = stake['amount']
            start_time = stake['start_time']

            # Calculate the days since staking started
            elapsed_days = (current_time - start_time).days

            # If lock period is completed, calculate rewards and allow withdrawal
            if elapsed_days >= lock_period_days:
                daily_rate = apy / 100 / 365
                rewards = amount * daily_rate * elapsed_days
                total_withdrawn += amount + rewards
            else:
                # Keep stakes that are still locked
                valid_stakes.append(stake)

        self.stakes[user_address] = valid_stakes  # Update user's stakes
        print(f"User {user_address} withdrew {total_withdrawn} AITECH tokens (stake + rewards).")
        return total_withdrawn

# Example usage
if __name__ == "__main__":
    staking = StakingContract()

    # User stakes tokens
    staking.stake_tokens("user1", 1000, 30, 12)  # 30 days lock, 12% APY

    # Simulate time passing
    time.sleep(2)  # Replace with actual time manipulation for production testing

    # Calculate rewards after some days
    rewards = staking.calculate_rewards("user1")
    print(f"Rewards for user1: {rewards} AITECH tokens.")

    # Withdraw stake after lock period
    total_withdrawn = staking.withdraw_stake("user1")
    print(f"Total withdrawn by user1: {total_withdrawn} AITECH tokens.")
```
