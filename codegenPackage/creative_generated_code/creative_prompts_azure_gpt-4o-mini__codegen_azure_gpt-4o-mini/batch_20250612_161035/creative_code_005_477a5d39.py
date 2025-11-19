"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jm3-dapp.pages.dev
Prompt: Write a function to handle the staking and harvesting of assets in a DApp, based on the guidelines provided in the content.
Generated: DETERMINISTIC_477a5d3960855749
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import List, Dict

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds when staking."""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid staking or harvesting amounts."""
    pass

class StakingManager:
    def __init__(self):
        # Initialize an empty dictionary to hold user balances
        self.user_balances: Dict[str, Decimal] = {}
        # Initialize an empty dictionary to hold user stakes
        self.user_stakes: Dict[str, Decimal] = {}

    def stake_assets(self, user_id: str, amount: Decimal) -> None:
        """
        Allows a user to stake a specified amount of assets.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount to be staked.
        :raises InsufficientFundsError: If the user does not have enough assets to stake.
        :raises InvalidAmountError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        
        user_balance = self.user_balances.get(user_id, Decimal('0'))

        if user_balance < amount:
            raise InsufficientFundsError("Insufficient funds to stake.")

        # Deduct the staked amount from the user's balance
        self.user_balances[user_id] -= amount
        # Add the staked amount to the user's stakes
        self.user_stakes[user_id] = self.user_stakes.get(user_id, Decimal('0')) + amount

    def harvest_assets(self, user_id: str, amount: Decimal) -> None:
        """
        Allows a user to withdraw a specified amount of staked assets.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount to be harvested.
        :raises InvalidAmountError: If the amount is less than or equal to zero.
        :raises InsufficientFundsError: If the user does not have enough staked assets to harvest.
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        
        user_stake = self.user_stakes.get(user_id, Decimal('0'))

        if user_stake < amount:
            raise InsufficientFundsError("Insufficient staked assets to harvest.")

        # Deduct the harvested amount from the user's stakes
        self.user_stakes[user_id] -= amount
        # Add the harvested amount back to the user's balance
        self.user_balances[user_id] += amount

    def add_user_balance(self, user_id: str, amount: Decimal) -> None:
        """
        Adds an amount to the user's balance.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount to add to the user's balance.
        :raises InvalidAmountError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        
        self.user_balances[user_id] = self.user_balances.get(user_id, Decimal('0')) + amount

    def get_user_balance(self, user_id: str) -> Decimal:
        """
        Retrieves the current balance of the user.
        
        :param user_id: Unique identifier for the user.
        :return: User's current balance.
        """
        return self.user_balances.get(user_id, Decimal('0'))

    def get_user_stake(self, user_id: str) -> Decimal:
        """
        Retrieves the current staked amount of the user.
        
        :param user_id: Unique identifier for the user.
        :return: User's current staked amount.
        """
        return self.user_stakes.get(user_id, Decimal('0'))
```
