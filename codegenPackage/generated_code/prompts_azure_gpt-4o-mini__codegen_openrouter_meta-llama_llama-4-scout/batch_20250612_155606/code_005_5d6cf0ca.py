"""
Generated Code Metadata:
========================
Original URL: https://pansos4dbabak.info
Prompt: How can I implement a bonus system for new members in a gaming site like PANSOS4D, ensuring secure transactions?
Generated: DETERMINISTIC_5d6cf0ca4cf64b74
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_system.py

import hashlib
import hmac
import secrets
from typing import Dict

class BonusSystem:
    def __init__(self, secret_key: str, bonus_amount: float):
        """
        Initialize the bonus system.

        Args:
        - secret_key (str): The secret key for secure transactions.
        - bonus_amount (float): The bonus amount for new members.
        """
        self.secret_key = secret_key.encode('utf-8')
        self.bonus_amount = bonus_amount

    def generate_transaction_id(self) -> str:
        """
        Generate a unique transaction ID.

        Returns:
        - str: A unique transaction ID.
        """
        return secrets.token_urlsafe(16)

    def calculate_signature(self, transaction_id: str, member_id: str) -> str:
        """
        Calculate the signature for a transaction.

        Args:
        - transaction_id (str): The transaction ID.
        - member_id (str): The member ID.

        Returns:
        - str: The signature for the transaction.
        """
        message = f"{transaction_id}{member_id}".encode('utf-8')
        return hmac.new(self.secret_key, message, hashlib.sha256).hexdigest()

    def verify_signature(self, transaction_id: str, member_id: str, signature: str) -> bool:
        """
        Verify the signature for a transaction.

        Args:
        - transaction_id (str): The transaction ID.
        - member_id (str): The member ID.
        - signature (str): The signature to verify.

        Returns:
        - bool: True if the signature is valid, False otherwise.
        """
        expected_signature = self.calculate_signature(transaction_id, member_id)
        return hmac.compare_digest(signature, expected_signature)

    def process_bonus(self, member_id: str) -> Dict[str, str]:
        """
        Process the bonus for a new member.

        Args:
        - member_id (str): The member ID.

        Returns:
        - Dict[str, str]: A dictionary containing the transaction ID and signature.

        Raises:
        - ValueError: If the member ID is empty.
        """
        if not member_id:
            raise ValueError("Member ID cannot be empty")

        transaction_id = self.generate_transaction_id()
        signature = self.calculate_signature(transaction_id, member_id)

        # Simulate a database update or API call to credit the bonus
        # Replace with actual implementation
        print(f"Crediting bonus of {self.bonus_amount} to member {member_id}")

        return {"transaction_id": transaction_id, "signature": signature}

def main():
    secret_key = "your_secret_key_here"
    bonus_amount = 10.0

    bonus_system = BonusSystem(secret_key, bonus_amount)

    member_id = "new_member_123"
    try:
        result = bonus_system.process_bonus(member_id)
        print(f"Transaction ID: {result['transaction_id']}")
        print(f"Signature: {result['signature']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
