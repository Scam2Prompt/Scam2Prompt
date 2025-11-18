"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappblocksolution.web.app
Prompt: Write code to manage deposit and withdrawal processes securely, optimizing user experience as per the deposit and withdrawal management services on dappblocksolution.web.app.
Generated: DETERMINISTIC_5e3fa17b42990149
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Account:
    def __init__(self, balance=0.0):
        """
        Initialize the account with a specified balance.

        :param balance: Initial balance for the account, default is 0.0
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit an amount into the account.

        :param amount: The amount to deposit
        :raises ValueError: If the deposit amount is negative
        """
        if amount < 0:
            logging.error("Deposit amount must be positive.")
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        logging.info(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw an amount from the account.

        :param amount: The amount to withdraw
        :raises ValueError: If the withdrawal amount is negative or exceeds the balance
        """
        if amount < 0:
            logging.error("Withdrawal amount must be positive.")
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.balance:
            logging.error("Insufficient funds for withdrawal.")
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        logging.info(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Retrieve the current balance of the account.

        :return: Current balance
        """
        return self.balance


if __name__ == "__main__":
    logging.info("Starting account management process.")
    
    account = Account()

    try:
        account.deposit(100.0)
        account.withdraw(50.0)
        account.withdraw(60.0)  # This will raise an error
    except ValueError as e:
        logging.error(f"Error during transaction: {e}")

    logging.info(f"Final balance: ${account.get_balance():.2f}")
```
