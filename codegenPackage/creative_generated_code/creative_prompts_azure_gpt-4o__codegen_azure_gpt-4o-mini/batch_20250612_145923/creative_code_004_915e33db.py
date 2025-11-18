"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Develop a staking protocol for a decentralized platform like Pushd, allowing users to earn interest ranging from 7% to 17% based on the number of tokens staked.
Generated: DETERMINISTIC_915e33dbdb81f4bc
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_protocol.py

from decimal import Decimal
from datetime import datetime, timedelta
import json

class StakingProtocol:
    """
    A simple staking protocol that allows users to stake tokens and earn interest.
    The interest rate is based on the amount of tokens staked.
    """

    # Constants for interest rates
    MIN_INTEREST_RATE = Decimal('0.07')  # 7%
    MAX_INTEREST_RATE = Decimal('0.17')  # 17%
    STAKING_PERIOD = timedelta(days=30)   # Minimum staking period

    def __init__(self):
        self.stakes = {}  # Dictionary to store user stakes
        self.interest_earned = {}  # Dictionary to store interest earned per user

    def stake_tokens(self, user_id: str, amount: Decimal):
        """
        Allows user to stake tokens.

        :param user_id: Unique identifier for the user
        :param amount: Amount of tokens to stake
        :raises ValueError: If amount is negative or user has already staked
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        
        if user_id in self.stakes:
            raise ValueError("User has already staked tokens.")

        self.stakes[user_id] = {
            'amount': amount,
            'timestamp': datetime.now()
        }
        self.interest_earned[user_id] = Decimal('0.00')

    def calculate_interest(self, user_id: str):
        """
        Calculates interest earned for the user based on staked amount and time.

        :param user_id: Unique identifier for the user
        :return: The total interest earned
        :raises ValueError: If user has not staked tokens
        """
        if user_id not in self.stakes:
            raise ValueError("User has not staked any tokens.")

        stake_info = self.stakes[user_id]
        staked_amount = stake_info['amount']
        staking_duration = datetime.now() - stake_info['timestamp']

        # Determine interest rate based on staked amount
        if staked_amount < Decimal('1000'):
            interest_rate = self.MIN_INTEREST_RATE
        elif staked_amount < Decimal('5000'):
            interest_rate = self.MIN_INTEREST_RATE + (self.MAX_INTEREST_RATE - self.MIN_INTEREST_RATE) * Decimal('0.5')
        else:
            interest_rate = self.MAX_INTEREST_RATE

        # Calculate interest only if the staking period has passed
        if staking_duration >= self.STAKING_PERIOD:
            interest = staked_amount * interest_rate * (staking_duration.days / 365)
            self.interest_earned[user_id] += interest

            # Reset staking info after calculating interest
            self.reset_stake(user_id)
            return self.interest_earned[user_id]

        return Decimal('0.00')

    def reset_stake(self, user_id: str):
        """
        Resets the user's stake after calculating interest.

        :param user_id: Unique identifier for the user
        """
        if user_id in self.stakes:
            del self.stakes[user_id]

    def to_json(self):
        """ Serializes the stakes and interest earned to JSON format. """
        return json.dumps({
            'stakes': self.stakes,
            'interest_earned': self.interest_earned
        }, default=str)

# Example usage
if __name__ == '__main__':
    staking = StakingProtocol()

    try:
        staking.stake_tokens("user123", Decimal('1500.00'))
        interest = staking.calculate_interest("user123")
        print(f"Interest earned: {interest}")
    except ValueError as e:
        print(f"Error: {e}")
```

This code defines a simple staking protocol that allows users to stake tokens and earn interest based on the amount staked. It includes proper error handling, comments, and follows best practices to ensure clean and maintainable code.
