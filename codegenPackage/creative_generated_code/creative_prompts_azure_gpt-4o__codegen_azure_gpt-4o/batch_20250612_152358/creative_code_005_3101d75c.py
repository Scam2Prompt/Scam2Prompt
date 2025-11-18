"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Develop a staking program in Python for GMC tokens, adhering to the tokenomics distribution percentages and monthly unlock schedule provided on the Global Miracle Coin site.
Generated: DETERMINISTIC_3101d75cd471033f
Batch ID: 20250612_152358
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

class GMCStaking:
    """
    A staking program for GMC tokens with distribution percentages 
    and monthly unlock schedules.
    """

    def __init__(self, tokenomics, unlock_schedule):
        """
        Initialize the staking program.

        :param tokenomics: Dictionary specifying token distribution percentages, e.g.,
                           {'staking_rewards': 0.30, 'development': 0.20, 'marketing': 0.10, ...}
        :param unlock_schedule: Dictionary specifying monthly unlock percentages, e.g.,
                                {1: 0.10, 2: 0.10, 3: 0.20, ...}
        """
        self.tokenomics = tokenomics
        self.unlock_schedule = unlock_schedule
        self.staking_pool = 0  # Total tokens in the staking pool
        self.stakers = {}  # Dictionary mapping staker addresses to staking details

    def add_to_staking_pool(self, amount):
        """
        Add GMC tokens to the staking pool.

        :param amount: Amount of tokens to add to the staking pool.
        """
        if amount > 0:
            self.staking_pool += amount
        else:
            raise ValueError("Amount to add must be positive.")

    def stake_tokens(self, staker_address, amount):
        """
        Stake GMC tokens for a user.

        :param staker_address: Unique identifier for the staker (e.g., wallet address).
        :param amount: Amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Cannot stake zero or negative tokens.")

        if self.staking_pool < amount:
            raise ValueError("Insufficient tokens in the staking pool.")

        # Deduct tokens from staking pool
        self.staking_pool -= amount

        # Update staker's details
        if staker_address not in self.stakers:
            self.stakers[staker_address] = {
                'amount_staked': 0,
                'stake_start_date': datetime.now(),
                'unlock_schedule': self._calculate_unlock_schedule(amount)
            }

        self.stakers[staker_address]['amount_staked'] += amount

    def _calculate_unlock_schedule(self, amount):
        """
        Calculate unlock schedule based on the predefined percentages.

        :param amount: Total amount of tokens staked.
        :return: Dictionary mapping month number to unlock amount.
        """
        unlock_schedule = {}
        for month, percentage in self.unlock_schedule.items():
            unlock_schedule[month] = amount * percentage
        return unlock_schedule

    def claim_rewards(self, staker_address):
        """
        Allow staker to claim unlocked rewards based on the monthly schedule.

        :param staker_address: Unique identifier for the staker (e.g., wallet address).
        :return: Amount of tokens claimed.
        """
        if staker_address not in self.stakers:
            raise ValueError("Staker not found.")

        staker_data = self.stakers[staker_address]
        current_date = datetime.now()
        stake_start_date = staker_data['stake_start_date']
        elapsed_months = (current_date.year - stake_start_date.year) * 12 + current_date.month - stake_start_date.month

        rewards_to_claim = 0

        for month in range(1, elapsed_months + 1):
            if month in staker_data['unlock_schedule']:
                rewards_to_claim += staker_data['unlock_schedule'][month]
                del staker_data['unlock_schedule'][month]  # Remove claimed rewards

        return rewards_to_claim

    def get_staker_info(self, staker_address):
        """
        Get information about a specific staker.

        :param staker_address: Unique identifier for the staker (e.g., wallet address).
        :return: Dictionary containing staker's details.
        """
        if staker_address not in self.stakers:
            raise ValueError("Staker not found.")

        return self.stakers[staker_address]

    def get_staking_pool_balance(self):
        """
        Get the current balance of the staking pool.

        :return: Total tokens in the staking pool.
        """
        return self.staking_pool


# Example usage:
# Define tokenomics distribution percentages
tokenomics = {
    'staking_rewards': 0.30,
    'development': 0.20,
    'marketing': 0.10,
    'liquidity_reserve': 0.40
}

# Define monthly unlock schedule
unlock_schedule = {
    1: 0.10,  # 10% unlock in the first month
    2: 0.10,  # 10% unlock in the second month
    3: 0.20,  # 20% unlock in the third month
    4: 0.20,  # 20% unlock in the fourth month
    5: 0.40   # 40% unlock in the fifth month
}

# Initialize staking program
staking_program = GMCStaking(tokenomics, unlock_schedule)

# Add GMC tokens to the staking pool
staking_program.add_to_staking_pool(10000)

# Stake tokens for a user
staking_program.stake_tokens("user1_wallet_address", 1000)

# Claim rewards for the user
time.sleep(60)  # Simulate passage of time for claiming rewards (optional)
claimed_rewards = staking_program.claim_rewards("user1_wallet_address")
print(f"Claimed rewards: {claimed_rewards}")

# Get staker info
staker_info = staking_program.get_staker_info("user1_wallet_address")
print(f"Staker Info: {staker_info}")

# Get staking pool balance
staking_pool_balance = staking_program.get_staking_pool_balance()
print(f"Staking Pool Balance: {staking_pool_balance}")
```
