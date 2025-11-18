"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoprohashings.vip
Prompt: Create a secure investment planning tool in Python that calculates potential profits based on the minimum deposit and profit margins for the Silver, Gold, and Premium accounts listed on cryptoprohashings.vip.
Generated: DETERMINISTIC_19b255deb8664a95
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentAccount:
    """Class representing an investment account and its profit calculation."""

    def __init__(self, name, min_deposit, profit_margin):
        """
        Initialize the investment account.

        :param name: Name of the account (e.g., Silver, Gold, Premium)
        :param min_deposit: Minimum deposit required for the account
        :param profit_margin: Expected profit margin as a percentage
        """
        self.name = name
        self.min_deposit = min_deposit
        self.profit_margin = profit_margin / 100  # Convert percentage to decimal

    def calculate_profit(self, deposit):
        """
        Calculate potential profit based on the deposit amount.

        :param deposit: Amount of money deposited in the account
        :return: Potential profit from the deposit
        """
        if deposit < self.min_deposit:
            raise ValueError(f"Deposit must be at least {self.min_deposit} for {self.name} account.")
        return deposit * self.profit_margin


def main():
    """Main function to execute the investment planning tool."""
    
    # Define the investment accounts with their minimum deposits and profit margins
    accounts = [
        InvestmentAccount("Silver", 100, 5),    # 5% profit margin
        InvestmentAccount("Gold", 500, 10),      # 10% profit margin
        InvestmentAccount("Premium", 1000, 15)   # 15% profit margin
    ]

    # User input for deposit amount
    try:
        deposit = float(input("Enter your deposit amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the deposit amount.")
        sys.exit(1)

    # Calculate and display potential profits for each account
    for account in accounts:
        try:
            profit = account.calculate_profit(deposit)
            print(f"Potential profit for {account.name} account with a deposit of {deposit}: {profit:.2f}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
```
