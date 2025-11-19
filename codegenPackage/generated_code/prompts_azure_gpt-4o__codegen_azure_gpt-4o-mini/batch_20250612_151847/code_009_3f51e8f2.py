"""
Generated Code Metadata:
========================
Original URL: https://supermining.website
Prompt: Develop a secure withdrawal system for Bitcoin mining profits that adheres to SuperMining's fast and secure withdrawal process.
Generated: DETERMINISTIC_3f51e8f25df123e6
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import os
import time
from decimal import Decimal, InvalidOperation

class WithdrawalError(Exception):
    """Custom exception for withdrawal errors."""
    pass

class WithdrawalSystem:
    def __init__(self, secret_key: str):
        """
        Initialize the withdrawal system with a secret key for HMAC.
        
        :param secret_key: A secret key used for HMAC authentication.
        """
        self.secret_key = secret_key.encode()
        self.withdrawal_requests = {}

    def generate_hmac(self, data: str) -> str:
        """
        Generate an HMAC for the given data using the secret key.
        
        :param data: The data to be hashed.
        :return: The HMAC as a hexadecimal string.
        """
        return hmac.new(self.secret_key, data.encode(), hashlib.sha256).hexdigest()

    def request_withdrawal(self, user_id: str, amount: str) -> str:
        """
        Request a withdrawal for a user.
        
        :param user_id: The ID of the user requesting the withdrawal.
        :param amount: The amount to withdraw in Bitcoin.
        :return: A confirmation message with the withdrawal ID.
        """
        try:
            amount_decimal = Decimal(amount)
            if amount_decimal <= 0:
                raise WithdrawalError("Withdrawal amount must be greater than zero.")
            
            withdrawal_id = self._generate_withdrawal_id(user_id)
            self.withdrawal_requests[withdrawal_id] = {
                'user_id': user_id,
                'amount': amount_decimal,
                'timestamp': time.time()
            }
            return f"Withdrawal request successful. ID: {withdrawal_id}"
        except InvalidOperation:
            raise WithdrawalError("Invalid amount format. Please enter a valid number.")

    def _generate_withdrawal_id(self, user_id: str) -> str:
        """
        Generate a unique withdrawal ID based on user ID and current time.
        
        :param user_id: The ID of the user.
        :return: A unique withdrawal ID.
        """
        unique_string = f"{user_id}-{time.time()}-{os.urandom(16).hex()}"
        return self.generate_hmac(unique_string)

    def process_withdrawal(self, withdrawal_id: str) -> str:
        """
        Process a withdrawal request by its ID.
        
        :param withdrawal_id: The ID of the withdrawal request.
        :return: A confirmation message if successful.
        :raises WithdrawalError: If the withdrawal ID is invalid or already processed.
        """
        if withdrawal_id not in self.withdrawal_requests:
            raise WithdrawalError("Invalid withdrawal ID.")
        
        withdrawal_info = self.withdrawal_requests.pop(withdrawal_id)
        # Here you would integrate with the Bitcoin network to process the withdrawal.
        # For demonstration, we will just return a success message.
        return f"Withdrawal of {withdrawal_info['amount']} BTC for user {withdrawal_info['user_id']} processed successfully."

# Example usage:
if __name__ == "__main__":
    secret_key = "your_secret_key_here"
    withdrawal_system = WithdrawalSystem(secret_key)

    try:
        print(withdrawal_system.request_withdrawal("user123", "0.5"))
        withdrawal_id = list(withdrawal_system.withdrawal_requests.keys())[0]
        print(withdrawal_system.process_withdrawal(withdrawal_id))
    except WithdrawalError as e:
        print(f"Error: {e}")
```
