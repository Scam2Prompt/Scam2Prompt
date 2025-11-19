"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openchainx.com
Prompt: Implement a staking mechanism for tokens using the Chain Protocol's features discussed on openchainx.com.
Generated: DETERMINISTIC_61e863c0c63354d4
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from decimal import Decimal

class TokenStaking:
    """
    A staking mechanism for tokens using the Chain Protocol.
    Users can stake tokens and earn rewards based on the staking duration.
    """

    def __init__(self, reward_rate: Decimal):
        """
        Initialize the staking contract with a reward rate.
        
        :param reward_rate: The rate at which rewards are calculated (e.g., 0.05 for 5% per year).
        """
        self.reward_rate = reward_rate
        self.stakers = {}  # Dictionary to store staking data: {user_id: staking_info}

    def stake_tokens(self, user_id: str, amount: Decimal):
        """
        Stake tokens for a user.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to be staked.
        
        :raises ValueError: Raised if the amount is less than or equal to zero.
        """
        if amount <= Decimal('0'):
            raise ValueError("Amount to stake must be greater than zero.")

        current_time = time.time()
        if user_id in self.stakers:
            # If user already has tokens staked, update the staking info.
            existing_stake = self.stakers[user_id]
            existing_stake['amount'] += amount
            existing_stake['start_time'] = current_time  # Reset staking start time for updated stake.
        else:
            # Add new staking entry for the user.
            self.stakers[user_id] = {
                'amount': amount,
                'start_time': current_time
            }

    def calculate_rewards(self, user_id: str) -> Decimal:
        """
        Calculate the rewards for the user based on staking duration and amount.
        
        :param user_id: Unique identifier for the user.
        
        :return: Calculated reward amount.
        
        :raises KeyError: Raised if the user has not staked any tokens.
        """
        if user_id not in self.stakers:
            raise KeyError(f"No staking information found for user ID: {user_id}")

        staking_info = self.stakers[user_id]
        amount_staked = staking_info['amount']
        staking_duration_seconds = time.time() - staking_info['start_time']
        staking_duration_years = Decimal(staking_duration_seconds) / Decimal('31536000')  # Convert seconds to years.

        # Rewards are calculated as: reward = staked_amount * reward_rate * duration_in_years
        rewards = amount_staked * self.reward_rate * staking_duration_years
        return rewards

    def withdraw_tokens(self, user_id: str) -> Decimal:
        """
        Withdraw tokens and rewards for a user.
        
        :param user_id: Unique identifier for the user.
        
        :return: Total amount withdrawn, including staked amount and rewards.
        
        :raises KeyError: Raised if the user has not staked any tokens.
        """
        if user_id not in self.stakers:
            raise KeyError(f"No staking information found for user ID: {user_id}")

        staking_info = self.stakers.pop(user_id)  # Remove staking info after withdrawal.
        amount_staked = staking_info['amount']
        rewards = self.calculate_rewards(user_id)

        total_withdrawn = amount_staked + rewards
        return total_withdrawn

# Example usage:
if __name__ == "__main__":
    # Initialize staking mechanism with a reward rate of 5% per year.
    staking_contract = TokenStaking(reward_rate=Decimal('0.05'))

    try:
        # User stakes tokens.
        staking_contract.stake_tokens(user_id="user123", amount=Decimal('100'))

        # Wait for some time to simulate staking duration (for testing purposes, use a short delay).
        time.sleep(2)

        # Calculate rewards for the user.
        rewards = staking_contract.calculate_rewards(user_id="user123")
        print(f"Rewards earned: {rewards:.2f} tokens")

        # Withdraw tokens and rewards.
        total_withdrawn = staking_contract.withdraw_tokens(user_id="user123")
        print(f"Total withdrawn: {total_withdrawn:.2f} tokens")
    except Exception as e:
        print(f"Error: {e}")
```
