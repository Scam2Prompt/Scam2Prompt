"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Develop a blockchain-based staking mechanism for CRUDO tokens, allowing token holders to generate passive income.
Generated: DETERMINISTIC_9643848d84a97efc
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict

class BlockchainStaking:
    """
    A simple smart contract simulation for CRUDO token staking mechanism.
    """

    def __init__(self, annual_yield: float):
        """
        Initialize the staking mechanism with a specific annual yield percentage.

        :param annual_yield: Annual yield percentage (e.g., 5.0 for 5%)
        """
        self.annual_yield = annual_yield
        self.stakers: Dict[str, Dict] = {}
        self.total_staked = 0

    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows a user to stake CRUDO tokens.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of CRUDO tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than 0.")

        now = datetime.utcnow()

        # If the user already has stakes, calculate pending rewards before restaking
        if user_id in self.stakers:
            self.stakers[user_id]['rewards'] += self.calculate_rewards(user_id)
            self.stakers[user_id]['last_staked'] = now
            self.stakers[user_id]['staked_amount'] += amount
        else:
            # New staker
            self.stakers[user_id] = {
                'staked_amount': amount,
                'last_staked': now,
                'rewards': 0.0
            }

        self.total_staked += amount

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate the rewards for a specific user based on the staked amount and time.

        :param user_id: Unique identifier for the user.
        :return: The calculated rewards.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked tokens.")

        user_data = self.stakers[user_id]
        now = datetime.utcnow()
        time_diff = now - user_data['last_staked']  # Difference in datetime
        days_staked = time_diff.total_seconds() / (60 * 60 * 24)  # Total days

        # Annual yield to daily yield
        daily_yield_rate = self.annual_yield / 365 / 100
        rewards = user_data['staked_amount'] * daily_yield_rate * days_staked

        return rewards

    def withdraw_rewards(self, user_id: str) -> float:
        """
        Allows a user to withdraw their accumulated rewards.

        :param user_id: Unique identifier for the user.
        :return: The amount of rewards withdrawn.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked tokens.")

        # Calculate rewards and reset rewards to zero
        rewards = self.calculate_rewards(user_id) + self.stakers[user_id]['rewards']
        self.stakers[user_id]['rewards'] = 0.0
        self.stakers[user_id]['last_staked'] = datetime.utcnow()

        return rewards

    def unstake_tokens(self, user_id: str) -> float:
        """
        Allows a user to unstake their tokens and withdraw rewards.

        :param user_id: Unique identifier for the user.
        :return: The total amount (staked tokens + rewards) returned to the user.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked tokens.")

        # Retrieve user data
        user_data = self.stakers[user_id]

        # Calculate rewards
        rewards = self.calculate_rewards(user_id) + user_data['rewards']
        total_stake = user_data['staked_amount']

        # Remove user's stake
        self.total_staked -= total_stake
        del self.stakers[user_id]

        # Return the total amount (staked tokens + rewards)
        return total_stake + rewards

    def get_user_data(self, user_id: str) -> Dict:
        """
        Retrieve the staking data for a specific user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing user's staking data.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked tokens.")

        user_data = self.stakers[user_id].copy()
        user_data['pending_rewards'] = self.calculate_rewards(user_id)
        return user_data

# Example Usage
if __name__ == "__main__":
    staking = BlockchainStaking(annual_yield=5.0)  # 5% annual yield

    # Staking tokens
    staking.stake_tokens("user1", 1000)

    # Simulate time lapse
    import time
    time.sleep(2)  # 2 seconds for demo purposes, replace with real-time wait in production

    # Check user data
    user_data = staking.get_user_data("user1")
    print("User Data:", user_data)

    # Withdraw rewards
    rewards = staking.withdraw_rewards("user1")
    print("Rewards Withdrawn:", rewards)

    # Unstake tokens
    total = staking.unstake_tokens("user1")
    print("Total Unstaked (Tokens + Rewards):", total)
```
