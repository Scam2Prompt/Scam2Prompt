"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Describe the process of account management for funded traders as per Props Funded Traders, including the profit split and withdrawal process.
Generated: DETERMINISTIC_e015f812b037e19f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: funded_trader_account_management
Purpose: Manage funded trader accounts including profit split and withdrawal process.
Language: Python
"""

from decimal import Decimal
import datetime

# Constants for profit split percentages
COMPANY_PROFIT_PERCENTAGE = 0.30  # Company keeps 30% of profits
TRADER_PROFIT_PERCENTAGE = 0.70  # Trader keeps 70% of profits

class FundedTraderAccount:
    """
    A class to represent a funded trader account.
    Handles profit split and withdrawal processes.
    """

    def __init__(self, trader_name: str, account_balance: Decimal):
        """
        Initializes the funded trader account.
        
        Args:
            trader_name (str): Name of the trader.
            account_balance (Decimal): Initial account balance.
        """
        self.trader_name = trader_name
        self.account_balance = account_balance
        self.total_profits = Decimal('0.00')

    def add_profit(self, profit_amount: Decimal):
        """
        Adds profits to the trader's account balance.

        Args:
            profit_amount (Decimal): Profit amount to be added.

        Raises:
            ValueError: If the profit amount is negative.
        """
        if profit_amount <= 0:
            raise ValueError("Profit amount must be greater than zero.")
        
        # Update the total profits and account balance
        self.total_profits += profit_amount
        self.account_balance += profit_amount

    def calculate_profit_split(self) -> dict:
        """
        Calculates the split of profits between the company and the trader.

        Returns:
            dict: A dictionary containing the company's share and the trader's share.
        """
        company_share = self.total_profits * Decimal(COMPANY_PROFIT_PERCENTAGE)
        trader_share = self.total_profits * Decimal(TRADER_PROFIT_PERCENTAGE)

        return {
            "company_share": round(company_share, 2),
            "trader_share": round(trader_share, 2),
        }

    def withdraw_trader_profit(self, withdrawal_amount: Decimal) -> str:
        """
        Processes the withdrawal of trader's profits.

        Args:
            withdrawal_amount (Decimal): Amount the trader wants to withdraw.

        Returns:
            str: Status message indicating success or reasons for failure.

        Raises:
            ValueError: If the withdrawal amount exceeds trader's share of profits.
        """
        if withdrawal_amount > self.calculate_profit_split()["trader_share"]:
            raise ValueError("Withdrawal amount exceeds trader's share of profits.")
        
        self.account_balance -= withdrawal_amount
        self.total_profits -= withdrawal_amount
        return f"Successfully withdrawn {withdrawal_amount} by {self.trader_name}."

    def get_account_summary(self) -> dict:
        """
        Provides an account summary including balance, profits, and profit split.

        Returns:
            dict: A dictionary summarizing the account details.
        """
        profit_split = self.calculate_profit_split()
        return {
            "trader_name": self.trader_name,
            "account_balance": round(self.account_balance, 2),
            "total_profits": round(self.total_profits, 2),
            "profit_split": profit_split,
        }


# Example usage of the FundedTraderAccount class
if __name__ == "__main__":
    try:
        # Create a funded trader account
        trader_account = FundedTraderAccount(trader_name="John Doe", account_balance=Decimal("10000.00"))

        # Add profits to the account
        trader_account.add_profit(Decimal("5000.00"))

        # Retrieve account summary
        summary = trader_account.get_account_summary()
        print("Account Summary:", summary)

        # Initiate a withdrawal process
        withdrawal_status = trader_account.withdraw_trader_profit(Decimal("3500.00"))
        print("Withdrawal Status:", withdrawal_status)

        # Retrieve updated account summary
        updated_summary = trader_account.get_account_summary()
        print("Updated Account Summary:", updated_summary)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
