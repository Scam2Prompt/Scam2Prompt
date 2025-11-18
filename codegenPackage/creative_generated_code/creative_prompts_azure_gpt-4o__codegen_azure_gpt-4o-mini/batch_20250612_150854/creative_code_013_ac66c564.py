"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefrontier.app
Prompt: Write code to calculate capital gains tax liability for cryptocurrency investments, considering Immediate Frontier's emphasis on legal compliance and tax awareness.
Generated: DETERMINISTIC_ac66c5642c2b7acb
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CryptoInvestment:
    def __init__(self, purchase_price, sell_price, quantity, purchase_date, sell_date):
        """
        Initialize a CryptoInvestment instance.
        
        :param purchase_price: Price at which the cryptocurrency was purchased.
        :param sell_price: Price at which the cryptocurrency was sold.
        :param quantity: Quantity of cryptocurrency bought and sold.
        :param purchase_date: Date of purchase (YYYY-MM-DD).
        :param sell_date: Date of sale (YYYY-MM-DD).
        """
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.purchase_date = self._parse_date(purchase_date)
        self.sell_date = self._parse_date(sell_date)

    @staticmethod
    def _parse_date(date_string):
        """
        Parses a date string in YYYY-MM-DD format into a datetime object.
        
        :param date_string: Date in string format.
        :return: Parsed date as a datetime object.
        """
        try:
            return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD.") from e

    def calculate_gain(self):
        """
        Calculate the capital gain from the investment.
        
        :return: Capital gain as a float.
        """
        total_purchase_cost = self.purchase_price * self.quantity
        total_sell_value = self.sell_price * self.quantity
        capital_gain = total_sell_value - total_purchase_cost
        return capital_gain

    def calculate_tax_liability(self, tax_rate):
        """
        Calculate the tax liability based on the capital gain and tax rate.
        
        :param tax_rate: Applicable tax rate as a decimal (e.g., 0.15 for 15%).
        :return: Tax liability as a float.
        :raises ValueError: If tax_rate is not between 0 and 1.
        """
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1.")

        capital_gain = self.calculate_gain()
        tax_liability = capital_gain * tax_rate
        return tax_liability

# Example usage:
if __name__ == "__main__":
    try:
        investment = CryptoInvestment(
            purchase_price=10000,      # Price per unit when purchased
            sell_price=15000,          # Price per unit when sold
            quantity=1,                # Quantity of the cryptocurrency
            purchase_date="2023-01-01", # Date of purchase
            sell_date="2023-12-01"      # Date of sale
        )

        tax_rate = 0.15  # Example tax rate of 15%
        tax_liability = investment.calculate_tax_liability(tax_rate)

        print(f"Capital Gain: ${investment.calculate_gain():,.2f}")
        print(f"Tax Liability: ${tax_liability:,.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
