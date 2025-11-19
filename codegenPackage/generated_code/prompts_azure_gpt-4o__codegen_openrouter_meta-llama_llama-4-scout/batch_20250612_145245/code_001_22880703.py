"""
Generated Code Metadata:
========================
Original URL: https://scam-sniffer.com
Prompt: Create a code snippet that simulates transactions to detect sell restrictions in a token contract using the features described on Scam Sniffer.
Generated: DETERMINISTIC_22880703484b904b
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class TokenContract:
    def __init__(self, name: str, total_supply: int):
        """
        Initialize a token contract.

        Args:
        - name (str): The name of the token.
        - total_supply (int): The total supply of the token.
        """
        self.name = name
        self.total_supply = total_supply
        self.balances: Dict[str, int] = {}  # User balances
        self.sell_restrictions: Dict[str, bool] = {}  # Sell restrictions

    def add_user(self, user: str, balance: int):
        """
        Add a user to the token contract.

        Args:
        - user (str): The user's address.
        - balance (int): The user's initial balance.
        """
        self.balances[user] = balance
        self.sell_restrictions[user] = False  # Initialize sell restriction to False

    def transfer(self, from_user: str, to_user: str, amount: int):
        """
        Simulate a transfer transaction.

        Args:
        - from_user (str): The sender's address.
        - to_user (str): The recipient's address.
        - amount (int): The transfer amount.

        Raises:
        - ValueError: If the sender has insufficient balance or sell restriction is enabled.
        """
        if self.balances[from_user] < amount:
            raise ValueError("Insufficient balance")
        if self.sell_restrictions[from_user]:
            raise ValueError("Sell restriction is enabled for this user")

        self.balances[from_user] -= amount
        self.balances[to_user] = self.balances.get(to_user, 0) + amount

    def enable_sell_restriction(self, user: str):
        """
        Enable sell restriction for a user.

        Args:
        - user (str): The user's address.
        """
        self.sell_restrictions[user] = True

    def disable_sell_restriction(self, user: str):
        """
        Disable sell restriction for a user.

        Args:
        - user (str): The user's address.
        """
        self.sell_restrictions[user] = False


def simulate_transactions(contract: TokenContract, transactions: List[Dict]):
    """
    Simulate a list of transactions to detect sell restrictions.

    Args:
    - contract (TokenContract): The token contract.
    - transactions (List[Dict]): A list of transactions.

    Returns:
    - A list of users with sell restrictions.
    """
    restricted_users = []
    for transaction in transactions:
        try:
            contract.transfer(transaction["from"], transaction["to"], transaction["amount"])
        except ValueError as e:
            if "Sell restriction is enabled" in str(e):
                restricted_users.append(transaction["from"])
            elif "Insufficient balance" in str(e):
                print(f"Insufficient balance for user {transaction['from']}")
            else:
                print(f"Error: {str(e)}")
    return restricted_users


# Example usage
if __name__ == "__main__":
    contract = TokenContract("Example Token", 1000)
    contract.add_user("User1", 100)
    contract.add_user("User2", 50)
    contract.enable_sell_restriction("User1")

    transactions = [
        {"from": "User1", "to": "User2", "amount": 20},
        {"from": "User2", "to": "User1", "amount": 10},
        {"from": "User1", "to": "User2", "amount": 80},  # This should trigger sell restriction
    ]

    restricted_users = simulate_transactions(contract, transactions)
    print(f"Users with sell restrictions: {restricted_users}")
```
