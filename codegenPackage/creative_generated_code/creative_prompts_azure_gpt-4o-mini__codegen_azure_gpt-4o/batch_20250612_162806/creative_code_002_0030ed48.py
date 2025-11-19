"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrax.io
Prompt: What are the steps to create a multi-collateral trading system that allows users to deposit various cryptocurrencies as collateral?
Generated: DETERMINISTIC_0030ed48e32d3e6c
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Multi-collateral Trading System
Allows users to deposit various cryptocurrencies as collateral.

Key features:
1. Deposit cryptocurrencies as collateral
2. Track collateral balance by user
3. Basic error handling for deposits
4. Extendable structure for future functionalities

Dependencies:
- Python >= 3.8
"""

from typing import Dict, DefaultDict
from collections import defaultdict

class MultiCollateralTradingSystem:
    def __init__(self):
        """
        Initialize the trading system with an empty collateral balance ledger.
        """
        self.collateral_balances: DefaultDict[str, DefaultDict[str, float]] = defaultdict(lambda: defaultdict(float))

    def deposit_collateral(self, user_id: str, crypto_symbol: str, amount: float) -> None:
        """
        Allows a user to deposit cryptocurrency as collateral.

        :param user_id: Unique identifier for the user
        :param crypto_symbol: Symbol of the cryptocurrency (e.g., BTC, ETH)
        :param amount: Amount of cryptocurrency to deposit
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Update user's collateral balance
        self.collateral_balances[user_id][crypto_symbol] += amount
        print(f"Successfully deposited {amount} {crypto_symbol} for user {user_id}.")

    def get_collateral_balance(self, user_id: str) -> Dict[str, float]:
        """
        Retrieves the collateral balances of a specific user.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing cryptocurrency symbols and their respective balances
        """
        return dict(self.collateral_balances[user_id])

    def display_all_balances(self) -> None:
        """
        Displays the collateral balances of all users in the system.
        """
        print("All Collateral Balances:")
        for user_id, balances in self.collateral_balances.items():
            print(f"User {user_id}: {dict(balances)}")

# Example usage
if __name__ == "__main__":
    # Instantiate the trading system
    trading_system = MultiCollateralTradingSystem()

    # Simulate deposits
    try:
        trading_system.deposit_collateral("user1", "BTC", 0.5)
        trading_system.deposit_collateral("user1", "ETH", 2.0)
        trading_system.deposit_collateral("user2", "USDT", 1000)
        trading_system.deposit_collateral("user2", "BTC", 1.2)

        # Retrieve and display balances
        print("\nUser 1 Balances:", trading_system.get_collateral_balance("user1"))
        print("User 2 Balances:", trading_system.get_collateral_balance("user2"))

        # Display all balances
        trading_system.display_all_balances()
    except ValueError as e:
        print(f"Error: {e}")
```
