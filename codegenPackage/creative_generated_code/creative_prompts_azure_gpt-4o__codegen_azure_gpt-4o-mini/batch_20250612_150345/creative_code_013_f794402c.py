"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatrades-proexch.com
Prompt: Write code to simulate investment growth based on the minimum deposit and profit structures for different account types on MetaTradesPro Exchange.
Generated: DETERMINISTIC_f794402c5182d4d9
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentAccount:
    """
    A class to represent an investment account on the MetaTradesPro Exchange.
    """

    def __init__(self, account_type, initial_deposit):
        """
        Initializes the investment account with a specific account type and initial deposit.

        :param account_type: str - Type of the account ('Basic', 'Standard', 'Premium').
        :param initial_deposit: float - Minimum deposit required to open the account.
        :raises ValueError: If the account type is not valid or initial deposit is less than account type minimum.
        """
        self.account_type = account_type
        self.initial_deposit = initial_deposit
        self.validate_account()

    def validate_account(self):
        """
        Validates the account type and ensures the initial deposit meets the minimum requirement.
        """
        account_types = {
            'Basic': 1000,
            'Standard': 5000,
            'Premium': 10000
        }

        if self.account_type not in account_types:
            raise ValueError(f"Invalid account type. Choose from: {', '.join(account_types.keys())}")

        if self.initial_deposit < account_types[self.account_type]:
            raise ValueError(f"Initial deposit must be at least {account_types[self.account_type]} for {self.account_type} account.")

    def calculate_growth(self, years, annual_rate):
        """
        Calculates the future value of the investment based on the annual growth rate.

        :param years: int - Number of years for investment growth.
        :param annual_rate: float - Annual growth rate as a percentage (e.g., 5 for 5%).
        :return: float - Future value of the investment after the specified number of years.
        :raises ValueError: If years is negative or annual_rate is negative.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        if annual_rate < 0:
            raise ValueError("Annual growth rate cannot be negative.")

        future_value = self.initial_deposit * ((1 + annual_rate / 100) ** years)
        return future_value


def main():
    """
    Main function to run the investment growth simulation.
    """
    try:
        account_type = input("Enter account type (Basic, Standard, Premium): ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        years = int(input("Enter number of years for growth: "))
        annual_rate = float(input("Enter annual growth rate (in %): "))

        # Create investment account
        account = InvestmentAccount(account_type, initial_deposit)

        # Calculate future value
        future_value = account.calculate_growth(years, annual_rate)
        print(f"Future value of your investment: ${future_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
