"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummyh.pages.dev
Prompt: Explain how to create your own version of the $Gummy token using the principles discussed in Gummynomics101.
Generated: DETERMINISTIC_4bdcb87bc73a78ff
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import time
from typing import List, Dict, Any

class GummyToken:
    def __init__(self, name: str, symbol: str, total_supply: int, owner: str):
        """
        Initializes a new GummyToken instance.

        :param name: The name of the token.
        :param symbol: The symbol of the token.
        :param total_supply: The total supply of tokens.
        :param owner: The owner of the token contract.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.owner = owner
        self.balances: Dict[str, int] = {owner: total_supply}  # Initialize owner's balance
        self.transactions: List[Dict[str, Any]] = []  # Record of transactions
        self.current_time = time.time()  # Current timestamp

    def _hash_transaction(self, transaction: Dict[str, Any]) -> str:
        """
        Creates a SHA256 hash of the transaction.

        :param transaction: The transaction data to hash.
        :return: The SHA256 hash of the transaction.
        """
        transaction_string = json.dumps(transaction, sort_keys=True).encode()
        return hashlib.sha256(transaction_string).hexdigest()

    def transfer(self, to: str, amount: int) -> str:
        """
        Transfers tokens from the owner to a recipient.

        :param to: The address of the recipient.
        :param amount: The amount of tokens to transfer.
        :return: Transaction hash if successful.
        :raises ValueError: If the transfer amount is invalid or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if self.balances[self.owner] < amount:
            raise ValueError("Insufficient balance for transfer.")

        # Deduct from sender's balance
        self.balances[self.owner] -= amount
        # Add to recipient's balance
        self.balances[to] = self.balances.get(to, 0) + amount

        # Create transaction record
        transaction = {
            'from': self.owner,
            'to': to,
            'amount': amount,
            'timestamp': self.current_time
        }
        transaction_hash = self._hash_transaction(transaction)
        self.transactions.append(transaction)

        return transaction_hash

    def get_balance(self, address: str) -> int:
        """
        Retrieves the balance of a specific address.

        :param address: The address to check the balance of.
        :return: The balance of the address.
        :raises KeyError: If the address does not exist.
        """
        if address not in self.balances:
            raise KeyError("Address does not exist.")
        return self.balances[address]

    def get_total_supply(self) -> int:
        """
        Returns the total supply of the token.

        :return: Total supply of the token.
        """
        return self.total_supply

    def get_token_info(self) -> Dict[str, Any]:
        """
        Retrieves information about the token.

        :return: A dictionary containing the token's name, symbol, and total supply.
        """
        return {
            'name': self.name,
            'symbol': self.symbol,
            'total_supply': self.total_supply,
            'owner': self.owner
        }

# Example usage
if __name__ == "__main__":
    try:
        gummy_token = GummyToken(name="Gummy", symbol="GUM", total_supply=1000000, owner="0xOwnerAddress")
        print(gummy_token.get_token_info())
        print("Initial Balance:", gummy_token.get_balance("0xOwnerAddress"))
        
        # Transfer some tokens
        transaction_hash = gummy_token.transfer("0xRecipientAddress", 100)
        print("Transaction Hash:", transaction_hash)
        
        print("Balance after transfer:", gummy_token.get_balance("0xOwnerAddress"))
        print("Recipient Balance:", gummy_token.get_balance("0xRecipientAddress"))

    except Exception as e:
        print(f"An error occurred: {e}")
```
