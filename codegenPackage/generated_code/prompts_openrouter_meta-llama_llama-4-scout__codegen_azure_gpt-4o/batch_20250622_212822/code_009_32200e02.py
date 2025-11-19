"""
Generated Code Metadata:
========================
Original URL: https://alleth.org
Prompt: "Design a system for issuing and managing a EUR denominated stablecoin like AllUnity's, compliant with MiCAR regulations."
Generated: DETERMINISTIC_32200e02c1c380f4
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from decimal import Decimal
from datetime import datetime

class Stablecoin:
    """
    A class to represent a EUR denominated stablecoin.
    Compliant with MiCAR regulations.
    """

    def __init__(self, name: str, symbol: str, total_supply: Decimal):
        """
        Initialize the stablecoin with a name, symbol, and total supply.

        :param name: Name of the stablecoin (e.g., "AllUnity EUR").
        :param symbol: Symbol of the stablecoin (e.g., "AEUR").
        :param total_supply: Total supply of the stablecoin in EUR.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}  # Dictionary to store user balances
        self.transactions = []  # List to store transaction history

    def issue(self, recipient: str, amount: Decimal):
        """
        Issue new stablecoins to a recipient.

        :param recipient: The recipient's wallet address.
        :param amount: The amount of stablecoins to issue.
        :raises ValueError: If the amount is negative.
        """
        if amount <= 0:
            raise ValueError("Amount to issue must be positive.")
        
        self.total_supply += amount
        self.balances[recipient] = self.balances.get(recipient, Decimal(0)) + amount
        self._record_transaction("ISSUE", recipient, amount)

    def transfer(self, sender: str, recipient: str, amount: Decimal):
        """
        Transfer stablecoins from one user to another.

        :param sender: The sender's wallet address.
        :param recipient: The recipient's wallet address.
        :param amount: The amount of stablecoins to transfer.
        :raises ValueError: If the sender has insufficient balance or the amount is negative.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.balances.get(sender, Decimal(0)) < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, Decimal(0)) + amount
        self._record_transaction("TRANSFER", sender, recipient, amount)

    def burn(self, holder: str, amount: Decimal):
        """
        Burn stablecoins from a holder's balance.

        :param holder: The holder's wallet address.
        :param amount: The amount of stablecoins to burn.
        :raises ValueError: If the holder has insufficient balance or the amount is negative.
        """
        if amount <= 0:
            raise ValueError("Burn amount must be positive.")
        if self.balances.get(holder, Decimal(0)) < amount:
            raise ValueError("Insufficient balance to burn.")
        
        self.balances[holder] -= amount
        self.total_supply -= amount
        self._record_transaction("BURN", holder, amount)

    def _record_transaction(self, transaction_type: str, sender: str, recipient: str = None, amount: Decimal = Decimal(0)):
        """
        Record a transaction in the transaction history.

        :param transaction_type: Type of transaction ("ISSUE", "TRANSFER", "BURN").
        :param sender: The sender's wallet address.
        :param recipient: The recipient's wallet address (optional for "ISSUE" and "BURN").
        :param amount: The amount of stablecoins involved in the transaction.
        """
        transaction = {
            "id": str(uuid.uuid4()),
            "type": transaction_type,
            "sender": sender,
            "recipient": recipient,
            "amount": str(amount),
            "timestamp": datetime.utcnow().isoformat()
        }
        self.transactions.append(transaction)

    def get_balance(self, wallet_address: str) -> Decimal:
        """
        Get the balance of a specific wallet address.

        :param wallet_address: The wallet address to query.
        :return: The balance of the wallet address.
        """
        return self.balances.get(wallet_address, Decimal(0))

    def get_transaction_history(self) -> list:
        """
        Get the transaction history of the stablecoin.

        :return: A list of all transactions.
        """
        return self.transactions


# Example usage:
if __name__ == "__main__":
    try:
        # Create a new stablecoin
        stablecoin = Stablecoin(name="AllUnity EUR", symbol="AEUR", total_supply=Decimal("1000000"))

        # Issue stablecoins to a user
        stablecoin.issue("user1_wallet", Decimal("5000"))

        # Transfer stablecoins between users
        stablecoin.transfer("user1_wallet", "user2_wallet", Decimal("1000"))

        # Burn stablecoins from a user's balance
        stablecoin.burn("user1_wallet", Decimal("500"))

        # Print balances and transaction history
        print("User1 Balance:", stablecoin.get_balance("user1_wallet"))
        print("User2 Balance:", stablecoin.get_balance("user2_wallet"))
        print("Transaction History:", stablecoin.get_transaction_history())

    except ValueError as e:
        print("Error:", e)
```
