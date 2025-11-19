"""
Generated Code Metadata:
========================
Original URL: https://meme-index.pages.dev
Prompt: What steps are involved in staking $MEMEX and what benefits does it provide to holders?
Generated: DETERMINISTIC_9050cf42c8128bf7
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines the steps involved in staking $MEMEX tokens and the benefits it provides to holders.
The code simulates a staking mechanism, including depositing tokens, calculating rewards, and withdrawing tokens.
"""

import time

class MemexStaking:
    def __init__(self, annual_reward_rate: float):
        """
        Initialize the staking contract.

        :param annual_reward_rate: Annual reward rate (e.g., 0.10 for 10% annual rewards)
        """
        self.annual_reward_rate = annual_reward_rate
        self.stakers = {}  # Dictionary to store staker information

    def deposit_tokens(self, user: str, amount: float):
        """
        Deposit $MEMEX tokens for staking.

        :param user: The user's identifier (e.g., wallet address)
        :param amount: The amount of $MEMEX tokens to stake
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        current_time = time.time()
        if user in self.stakers:
            # Update existing staker's information
            self._update_rewards(user)
            self.stakers[user]['balance'] += amount
        else:
            # Add new staker
            self.stakers[user] = {
                'balance': amount,
                'last_stake_time': current_time,
                'pending_rewards': 0.0
            }
        print(f"{amount} $MEMEX tokens successfully staked by {user}.")

    def _update_rewards(self, user: str):
        """
        Update the pending rewards for a staker.

        :param user: The user's identifier
        """
        current_time = time.time()
        staker = self.stakers[user]
        time_elapsed = current_time - staker['last_stake_time']
        annual_seconds = 365 * 24 * 60 * 60  # Total seconds in a year

        # Calculate rewards based on time elapsed and annual reward rate
        rewards = (staker['balance'] * self.annual_reward_rate * time_elapsed) / annual_seconds
        staker['pending_rewards'] += rewards
        staker['last_stake_time'] = current_time

    def withdraw_tokens(self, user: str):
        """
        Withdraw staked tokens and rewards.

        :param user: The user's identifier
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")

        self._update_rewards(user)
        staker = self.stakers[user]
        total_withdrawal = staker['balance'] + staker['pending_rewards']

        # Reset staker's information
        del self.stakers[user]

        print(f"{total_withdrawal} $MEMEX tokens successfully withdrawn by {user}.")
        return total_withdrawal

    def check_rewards(self, user: str):
        """
        Check the pending rewards for a staker.

        :param user: The user's identifier
        :return: The amount of pending rewards
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")

        self._update_rewards(user)
        return self.stakers[user]['pending_rewards']

    def get_staked_balance(self, user: str):
        """
        Get the staked balance for a user.

        :param user: The user's identifier
        :return: The staked balance
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")

        return self.stakers[user]['balance']


# Example usage
if __name__ == "__main__":
    staking_contract = MemexStaking(annual_reward_rate=0.10)  # 10% annual reward rate

    try:
        # User deposits tokens
        staking_contract.deposit_tokens(user="user1", amount=1000)

        # Simulate time passing
        time.sleep(2)  # Wait for 2 seconds

        # Check rewards
        rewards = staking_contract.check_rewards(user="user1")
        print(f"Pending rewards for user1: {rewards} $MEMEX")

        # Withdraw tokens and rewards
        total_withdrawn = staking_contract.withdraw_tokens(user="user1")
        print(f"Total withdrawn by user1: {total_withdrawn} $MEMEX")
    except ValueError as e:
        print(f"Error: {e}")
```
