"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-i6-folex.com
Prompt: Create a Python script to simulate the process of funding a trading account and pairing users with investment education companies, inspired by the workflow described on the Trade i6 Folex platform.
Generated: DETERMINISTIC_bc3ac58d0667392e
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate funding a trading account and pairing users with investment education companies.
Inspired by the Trade i6 Folex platform workflow.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import uuid
import random

# Define constants
MIN_FUND_AMOUNT = 100  # Minimum funding amount in USD
EDUCATION_COMPANIES = ["InvestSmart Co.", "TradeLearn Inc.", "ProfitWise Academy", "MarketMasters LLC"]

class TradingAccount:
    """
    Represents a trading account for a user.
    """
    def __init__(self, user_name):
        self.user_name = user_name
        self.account_id = str(uuid.uuid4())
        self.balance = 0.0
        self.education_partner = None

    def fund_account(self, amount):
        """
        Funds the trading account with the specified amount.
        :param amount: Amount in USD to fund the account.
        :raises ValueError: If the funding amount is below the minimum threshold.
        """
        if amount < MIN_FUND_AMOUNT:
            raise ValueError(f"Funding amount must be at least ${MIN_FUND_AMOUNT}.")
        self.balance += amount
        print(f"Account funded successfully. Current balance: ${self.balance:.2f}")

    def pair_with_education_company(self):
        """
        Pairs the user with a random investment education company.
        """
        self.education_partner = random.choice(EDUCATION_COMPANIES)
        print(f"Paired with investment education company: {self.education_partner}")


def main():
    """
    Main function to simulate the trading account funding workflow.
    """
    print("Welcome to the Trading Account Funding Platform!")
    
    # Step 1: Get user input for account creation
    user_name = input("Enter your name to create a trading account: ").strip()
    if not user_name:
        print("Error: User name cannot be empty.")
        return

    # Create a trading account
    account = TradingAccount(user_name)
    print(f"Trading account created successfully. Account ID: {account.account_id}")

    # Step 2: Fund the trading account
    try:
        fund_amount = float(input(f"Enter the amount to fund your account (minimum ${MIN_FUND_AMOUNT}): "))
        account.fund_account(fund_amount)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Step 3: Pair with an investment education company
    account.pair_with_education_company()

    # Step 4: Display final account details
    print("\nAccount Details:")
    print(f"User Name: {account.user_name}")
    print(f"Account ID: {account.account_id}")
    print(f"Balance: ${account.balance:.2f}")
    print(f"Education Partner: {account.education_partner}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
