"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbabak.info
Prompt: How can I implement a deposit feature using bank transfers and e-wallets for a gambling platform like PANSOS4D?
Generated: DETERMINISTIC_8d0db1bd1a616a30
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class InsufficientFundsError(Exception):
    """Custom exception raised when the user has insufficient funds."""
    pass

class PaymentMethodNotSupportedError(Exception):
    """Custom exception raised when a payment method is unsupported."""
    pass

class GamblingPlatform:
    def __init__(self):
        # Dummy user data for simulation purposes
        self.users = {
            "user1": {
                "balance": 100.0,  # User's gambling platform balance
                "bank_balance": 500.0,  # User's external bank balance
                "e_wallet_balance": 300.0,  # User's external e-wallet balance
            }
        }
        self.transaction_history = []  # A record of all transactions
    
    def generate_transaction_id(self):
        """Generate a unique transaction ID."""
        return str(uuid.uuid4())
    
    def deposit(self, username, amount, payment_method):
        """
        Deposit money into the user's gambling platform account.

        Args:
            username (str): The username of the user making the deposit.
            amount (float): The amount to deposit.
            payment_method (str): The payment method ('bank' or 'e-wallet').

        Returns:
            str: Success message indicating the deposit was made.

        Raises:
            ValueError: If the amount is not valid (e.g., negative or zero).
            InsufficientFundsError: If the external source has insufficient funds.
            PaymentMethodNotSupportedError: If the payment method is not supported.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        user = self.users[username]
        
        if payment_method == "bank":
            if user["bank_balance"] < amount:
                raise InsufficientFundsError("Insufficient funds in bank account.")
            user["bank_balance"] -= amount  # Deduct from bank balance
            user["balance"] += amount  # Add to gambling platform balance
        elif payment_method == "e-wallet":
            if user["e_wallet_balance"] < amount:
                raise InsufficientFundsError("Insufficient funds in e-wallet.")
            user["e_wallet_balance"] -= amount  # Deduct from e-wallet balance
            user["balance"] += amount  # Add to gambling platform balance
        else:
            raise PaymentMethodNotSupportedError("Payment method not supported.")
        
        # Log transaction
        transaction_id = self.generate_transaction_id()
        self.transaction_history.append({
            "transaction_id": transaction_id,
            "username": username,
            "amount": amount,
            "payment_method": payment_method,
            "status": "success"
        })
        
        return f"Deposit successful. Transaction ID: {transaction_id}"

    def get_user_balance(self, username):
        """
        Get the current balance of a user.

        Args:
            username (str): The username of the user.

        Returns:
            dict: User's balances (gambling platform, bank, and e-wallet).
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        return {
            "platform_balance": self.users[username]["balance"],
            "bank_balance": self.users[username]["bank_balance"],
            "e_wallet_balance": self.users[username]["e_wallet_balance"]
        }

    def get_transaction_history(self, username):
        """
        Get the transaction history for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            list: A list of transactions made by the user.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        return [tx for tx in self.transaction_history if tx["username"] == username]


# Example usage
if __name__ == "__main__":
    platform = GamblingPlatform()
    
    try:
        # Deposit to the platform using bank transfer
        print(platform.deposit("user1", 50.0, "bank"))
        
        # Deposit to the platform using e-wallet
        print(platform.deposit("user1", 100.0, "e-wallet"))
        
        # Get user balances
        print(platform.get_user_balance("user1"))
        
        # Get user transaction history
        print(platform.get_transaction_history("user1"))
    
    except ValueError as e:
        print(f"Error: {e}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    except PaymentMethodNotSupportedError as e:
        print(f"Error: {e}")
```
