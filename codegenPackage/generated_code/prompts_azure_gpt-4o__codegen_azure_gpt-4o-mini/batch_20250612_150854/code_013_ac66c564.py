"""
Generated Code Metadata:
========================
Original URL: https://immediatefrontier.app
Prompt: Write code to calculate capital gains tax liability for cryptocurrency investments, considering Immediate Frontier's emphasis on legal compliance and tax awareness.
Generated: DETERMINISTIC_ac66c5642c2b7acb
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CryptoInvestment:
    def __init__(self, purchase_price, sale_price, purchase_date, sale_date, quantity):
        """
        Initialize a CryptoInvestment instance.

        :param purchase_price: Price at which the cryptocurrency was purchased.
        :param sale_price: Price at which the cryptocurrency was sold.
        :param purchase_date: Date of purchase (YYYY-MM-DD).
        :param sale_date: Date of sale (YYYY-MM-DD).
        :param quantity: Quantity of cryptocurrency bought and sold.
        """
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.purchase_date = self._parse_date(purchase_date)
        self.sale_date = self._parse_date(sale_date)
        self.quantity = quantity

    @staticmethod
    def _parse_date(date_str):
        """
        Parse a date string into a datetime object.

        :param date_str: Date string in YYYY-MM-DD format.
        :return: datetime object.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.") from e

    def calculate_capital_gains(self):
        """
        Calculate the capital gains from the investment.

        :return: Capital gains as a float.
        """
        if self.sale_price < self.purchase_price:
            return 0.0  # No capital gains if sold at a loss
        return (self.sale_price - self.purchase_price) * self.quantity

    def calculate_tax_liability(self, tax_rate):
        """
        Calculate the capital gains tax liability.

        :param tax_rate: Tax rate as a decimal (e.g., 0.15 for 15%).
        :return: Tax liability as a float.
        """
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        capital_gains = self.calculate_capital_gains()
        return capital_gains * tax_rate

def main():
    """
    Main function to demonstrate the calculation of capital gains tax liability.
    """
    try:
        # Example investment data
        investment = CryptoInvestment(
            purchase_price=1000.0,
            sale_price=1500.0,
            purchase_date="2022-01-01",
            sale_date="2023-01-01",
            quantity=1.0
        )

        # Define tax rate (e.g., 15%)
        tax_rate = 0.15

        # Calculate tax liability
        tax_liability = investment.calculate_tax_liability(tax_rate)
        print(f"Capital Gains Tax Liability: ${tax_liability:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
