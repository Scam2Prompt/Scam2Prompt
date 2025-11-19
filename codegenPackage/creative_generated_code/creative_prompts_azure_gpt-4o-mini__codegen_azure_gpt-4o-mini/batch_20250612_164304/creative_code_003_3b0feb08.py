"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbank.pages.dev
Prompt: Generate a function to verify withdrawals from a decentralized wallet as described in the DApp Bank content.
Generated: DETERMINISTIC_3b0feb08885b7213
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DecentralizedWallet:
    def __init__(self):
        # Initialize the wallet with a balance of 0
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount into the wallet.
        
        :param amount: The amount to be deposited (must be positive).
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the wallet if sufficient balance exists.
        
        :param amount: The amount to be withdrawn (must be positive).
        :raises ValueError: If the amount is negative or zero.
        :raises InsufficientFundsError: If the balance is insufficient for the withdrawal.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current balance of the wallet.
        
        :return: The current balance.
        """
        return self.balance


class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the available balance."""
    pass


# Example usage:
if __name__ == "__main__":
    wallet = DecentralizedWallet()

    try:
        wallet.deposit(100.0)
        print("Balance after deposit: ", wallet.get_balance())
        
        wallet.withdraw(50.0)
        print("Balance after withdrawal: ", wallet.get_balance())
        
        wallet.withdraw(60.0)  # This will raise an InsufficientFundsError
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except InsufficientFundsError as ife:
        print(f"InsufficientFundsError: {ife}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
