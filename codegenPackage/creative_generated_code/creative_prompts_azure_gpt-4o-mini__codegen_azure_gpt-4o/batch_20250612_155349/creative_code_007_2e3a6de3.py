"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: How can developers leverage the IVI Token's utility in a sports club's loyalty program? Include a code example for tracking token usage.
Generated: DETERMINISTIC_2e3a6de37bae0ca8
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
IVI Token Loyalty Program Example
This code demonstrates how developers can leverage the IVI Token's utility in a sports club's loyalty program.
It tracks token usage for members and provides functionality to redeem tokens.
"""

import uuid
from datetime import datetime


class MemberToken:
    """
    Represents a sports club member and their associated IVI Token balance.
    """

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id  # Unique identifier for the member
        self.name = name  # Member's name
        self.token_balance = 0  # Initial IVI Token balance
        self.transaction_history = []  # List of token transactions

    def add_tokens(self, amount: int):
        """
        Adds IVI Tokens to the member's account.

        :param amount: Number of tokens to add (must be positive).
        """
        if amount <= 0:
            raise ValueError("Token amount must be positive.")
        self.token_balance += amount
        self.transaction_history.append({
            "transaction_id": str(uuid.uuid4()),
            "type": "add",
            "amount": amount,
            "date": datetime.now()
        })

    def redeem_tokens(self, amount: int):
        """
        Redeems IVI Tokens from the member's account.

        :param amount: Number of tokens to redeem (must be positive).
        """
        if amount <= 0:
            raise ValueError("Token amount must be positive.")
        if amount > self.token_balance:
            raise ValueError("Insufficient token balance.")
        self.token_balance -= amount
        self.transaction_history.append({
            "transaction_id": str(uuid.uuid4()),
            "type": "redeem",
            "amount": amount,
            "date": datetime.now()
        })

    def get_balance(self) -> int:
        """
        Returns the current token balance of the member.

        :return: Current token balance.
        """
        return self.token_balance

    def get_transaction_history(self) -> list:
        """
        Returns the transaction history of the member.

        :return: List of all token transactions.
        """
        return self.transaction_history


# Example Usage
if __name__ == "__main__":
    try:
        # Create a new member
        member = MemberToken(member_id="001", name="John Doe")

        # Add tokens to the member's account
        member.add_tokens(100)
        print(f"Token Balance after adding: {member.get_balance()}")

        # Redeem tokens
        member.redeem_tokens(30)
        print(f"Token Balance after redeeming: {member.get_balance()}")

        # Display transaction history
        print("Transaction History:")
        for transaction in member.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
