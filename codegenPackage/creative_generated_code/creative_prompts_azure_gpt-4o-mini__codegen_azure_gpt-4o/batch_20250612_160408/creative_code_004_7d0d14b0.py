"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Write a function that simulates the investment process (deposit, invest, withdraw) as outlined in the Astragoldbitx.org workflow.
Generated: DETERMINISTIC_7d0d14b0848cefdd
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging


class InvestmentError(Exception):
    """Custom exception for investment-related errors."""
    pass


class Account:
    def __init__(self, initial_balance=0):
        """
        Initializes an account with an initial balance.
        
        :param initial_balance: Starting balance for the account (default is 0).
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Adds funds to the account.

        :param amount: The amount to deposit.
        """
        if amount <= 0:
            raise InvestmentError("Deposit amount must be greater than zero.")
        self.balance += amount
        logging.info(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def invest(self, amount):
        """
        Invests a portion of the account balance.

        :param amount: The amount to invest.
        """
        if amount <= 0:
            raise InvestmentError("Investment amount must be greater than zero.")
        if amount > self.balance:
            raise InvestmentError("Insufficient balance for the investment.")
        self.balance -= amount
        logging.info(f"Invested ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws funds from the account.

        :param amount: The amount to withdraw.
        """
        if amount <= 0:
            raise InvestmentError("Withdraw amount must be greater than zero.")
        if amount > self.balance:
            raise InvestmentError("Insufficient balance for the withdrawal.")
        self.balance -= amount
        logging.info(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")


def simulate_investment_process():
    """
    Simulates a general investment process:
    1. Deposit funds into the account.
    2. Invest a portion of the funds.
    3. Withdraw funds.
    """
    try:
        # Step 1: Initialize account
        account = Account(initial_balance=1000)  # Start with $1000
        print(f"Initial balance: ${account.balance:.2f}")

        # Step 2: Deposit funds
        deposit_amount = 500
        account.deposit(deposit_amount)
        print(f"Deposited ${deposit_amount:.2f}")

        # Step 3: Invest funds
        invest_amount = 300
        account.invest(invest_amount)
        print(f"Invested ${invest_amount:.2f}")

        # Step 4: Withdraw funds
        withdraw_amount = 200
        account.withdraw(withdraw_amount)
        print(f"Withdrew ${withdraw_amount:.2f}")

        # Final balance
        print(f"Final balance: ${account.balance:.2f}")

    except InvestmentError as e:
        logging.error(f"Investment process error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Run the investment simulation
    simulate_investment_process()
```
