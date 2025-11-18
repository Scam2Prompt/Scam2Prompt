"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawfury-token.pages.dev
Prompt: Write a script to calculate capital gains taxes on cryptocurrency rewards earned from staking $PAW tokens, as mentioned in PawFury's disclaimer.
Generated: DETERMINISTIC_de6a228b7add84b3
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from decimal import Decimal

class CapitalGainsCalculator:
    def __init__(self, purchase_price: Decimal, selling_price: Decimal, amount_staked: Decimal,
                 acquisition_date: str, selling_date: str):
        """
        Initializes the CapitalGainsCalculator with the necessary parameters.

        :param purchase_price: The price at which the $PAW tokens were acquired.
        :param selling_price: The price at which the $PAW tokens were sold.
        :param amount_staked: The amount of $PAW tokens that were staked.
        :param acquisition_date: The date when the tokens were acquired (YYYY-MM-DD).
        :param selling_date: The date when the tokens were sold (YYYY-MM-DD).
        """
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.amount_staked = amount_staked
        self.acquisition_date = self.validate_date(acquisition_date)
        self.selling_date = self.validate_date(selling_date)

    @staticmethod
    def validate_date(date_str: str) -> datetime.date:
        """
        Validates and parses the date string into a datetime.date object.

        :param date_str: The date string to validate.
        :return: A datetime.date object.
        :raises ValueError: If the date_str is not a valid date.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def calculate_capital_gains(self) -> Decimal:
        """
        Calculates the capital gains from the sale of staked $PAW tokens.

        :return: The capital gains as a Decimal.
        """
        gain_per_token = self.selling_price - self.purchase_price
        total_gains = gain_per_token * self.amount_staked
        return total_gains if total_gains > 0 else Decimal('0.00')

    def calculate_tax(self) -> Decimal:
        """
        Calculates the tax on the capital gains. 
        For the sake of this example, we will assume a flat tax rate of 15%.

        :return: The tax amount as a Decimal.
        """
        capital_gains = self.calculate_capital_gains()
        tax_rate = Decimal('0.15')  # 15% tax rate
        return capital_gains * tax_rate

    def display_results(self):
        """
        Displays the calculated capital gains and tax in a user-friendly format.
        """
        try:
            capital_gains = self.calculate_capital_gains()
            tax = self.calculate_tax()
            print(f"Total Capital Gains: ${capital_gains:.2f}")
            print(f"Estimated Capital Gains Tax (15%): ${tax:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating results: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Replace the following values with actual data
        purchase_price = Decimal('0.05')  # Price at which $PAW was acquired
        selling_price = Decimal('0.10')    # Price at which $PAW was sold
        amount_staked = Decimal('1000')     # Amount of $PAW tokens staked
        acquisition_date = '2023-01-01'     # Acquisition date
        selling_date = '2023-06-01'         # Selling date

        calculator = CapitalGainsCalculator(purchase_price, selling_price, amount_staked,
                                             acquisition_date, selling_date)
        calculator.display_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
