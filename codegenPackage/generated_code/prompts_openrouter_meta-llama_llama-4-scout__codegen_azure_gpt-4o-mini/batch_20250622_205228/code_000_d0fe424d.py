"""
Generated Code Metadata:
========================
Original URL: https://tradefx.co
Prompt: Write a Python script to calculate the margin required for a Forex trade using TradeFX's account types and leverage.
Generated: DETERMINISTIC_d0fe424d8316f7be
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ForexTradeMarginCalculator:
    """
    A class to calculate the margin required for a Forex trade based on account type and leverage.
    """

    ACCOUNT_TYPES = {
        'standard': 100000,
        'mini': 10000,
        'micro': 1000
    }

    def __init__(self, account_type: str, leverage: float):
        """
        Initializes the ForexTradeMarginCalculator with the specified account type and leverage.

        :param account_type: The type of account (standard, mini, micro).
        :param leverage: The leverage ratio (e.g., 100 for 1:100).
        """
        self.account_type = account_type.lower()
        self.leverage = leverage

        if self.account_type not in self.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type: {self.account_type}. "
                             f"Valid options are: {', '.join(self.ACCOUNT_TYPES.keys())}")

        if self.leverage <= 0:
            raise ValueError("Leverage must be a positive number.")

    def calculate_margin(self, trade_size: float) -> float:
        """
        Calculates the margin required for a given trade size.

        :param trade_size: The size of the trade in the base currency.
        :return: The margin required in the account currency.
        """
        if trade_size <= 0:
            raise ValueError("Trade size must be a positive number.")

        # Calculate the contract size based on account type
        contract_size = self.ACCOUNT_TYPES[self.account_type]

        # Calculate the margin required
        margin_required = (trade_size / self.leverage) * contract_size
        return margin_required

def main():
    """
    Main function to execute the margin calculation based on user input.
    """
    try:
        account_type = input("Enter account type (standard, mini, micro): ")
        leverage = float(input("Enter leverage (e.g., 100 for 1:100): "))
        trade_size = float(input("Enter trade size in base currency: "))

        # Create an instance of the margin calculator
        calculator = ForexTradeMarginCalculator(account_type, leverage)

        # Calculate the margin required
        margin = calculator.calculate_margin(trade_size)

        print(f"Margin required for a {trade_size} trade on a {account_type} account with "
              f"{leverage}: {margin:.2f} in account currency.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
