"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdappwallet.web.app
Prompt: Develop a program to manage deposit and withdrawal processes securely, enhancing user experience as described on WebDappWallet's platform.
Generated: DETERMINISTIC_d26765dd4f187ed7
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Wallet:
    """A class to manage deposits and withdrawals in a digital wallet."""

    def __init__(self):
        """Initialize the wallet with a balance of 0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit a specified amount into the wallet.
        
        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        logging.info(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw a specified amount from the wallet.
        
        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not a positive number or exceeds the balance.
        """
        if amount <= 0:
            logging.error("Withdrawal amount must be positive.")
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        logging.info(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """Retrieve the current balance of the wallet.
        
        Returns:
            float: The current balance.
        """
        return self.balance

def main():
    """Main function to demonstrate wallet operations."""
    wallet = Wallet()
    
    try:
        # Example usage
        wallet.deposit(100.00)
        wallet.withdraw(50.00)
        print(f"Current balance: ${wallet.get_balance():.2f}")
        
        # Attempting to withdraw more than the current balance
        wallet.withdraw(60.00)
        
    except ValueError as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
