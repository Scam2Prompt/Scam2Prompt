"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.nl
Prompt: Write code to calculate the impact of tax regulations on cryptocurrency investments, referencing Immediate Peak's acknowledgment of the connection between investments and taxation.
Generated: DETERMINISTIC_87583c14efbf05fd
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_crypto_calculator.py

import enum

class TaxStatus(enum.Enum):
    """Enum for tax status"""
    SHORT_TERM = 1
    LONG_TERM = 2

class CryptoInvestment:
    """Class to represent a cryptocurrency investment"""
    def __init__(self, purchase_price, purchase_date, sale_price, sale_date):
        """
        Initialize a CryptoInvestment object.

        Args:
        - purchase_price (float): The price at which the cryptocurrency was purchased.
        - purchase_date (str): The date on which the cryptocurrency was purchased (YYYY-MM-DD).
        - sale_price (float): The price at which the cryptocurrency was sold.
        - sale_date (str): The date on which the cryptocurrency was sold (YYYY-MM-DD).
        """
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.sale_price = sale_price
        self.sale_date = sale_date

    def calculate_gain(self):
        """
        Calculate the gain from the investment.

        Returns:
        - float: The gain from the investment.
        """
        return self.sale_price - self.purchase_price

    def determine_tax_status(self):
        """
        Determine the tax status of the investment based on the holding period.

        Returns:
        - TaxStatus: The tax status of the investment.
        """
        from datetime import datetime

        purchase_date = datetime.strptime(self.purchase_date, "%Y-%m-%d")
        sale_date = datetime.strptime(self.sale_date, "%Y-%m-%d")

        holding_period = (sale_date - purchase_date).days

        if holding_period <= 365:
            return TaxStatus.SHORT_TERM
        else:
            return TaxStatus.LONG_TERM

class TaxCalculator:
    """Class to calculate the impact of tax regulations on cryptocurrency investments"""
    def __init__(self, tax_rate_short_term, tax_rate_long_term):
        """
        Initialize a TaxCalculator object.

        Args:
        - tax_rate_short_term (float): The tax rate for short-term gains.
        - tax_rate_long_term (float): The tax rate for long-term gains.
        """
        self.tax_rate_short_term = tax_rate_short_term
        self.tax_rate_long_term = tax_rate_long_term

    def calculate_tax(self, investment):
        """
        Calculate the tax on a cryptocurrency investment.

        Args:
        - investment (CryptoInvestment): The investment to calculate tax for.

        Returns:
        - float: The tax on the investment.
        """
        gain = investment.calculate_gain()
        if gain <= 0:
            return 0

        tax_status = investment.determine_tax_status()

        if tax_status == TaxStatus.SHORT_TERM:
            return gain * self.tax_rate_short_term
        else:
            return gain * self.tax_rate_long_term

def main():
    try:
        # Example usage
        investment = CryptoInvestment(
            purchase_price=1000,
            purchase_date="2022-01-01",
            sale_price=1500,
            sale_date="2023-01-01"
        )

        tax_calculator = TaxCalculator(
            tax_rate_short_term=0.24,
            tax_rate_long_term=0.20
        )

        tax = tax_calculator.calculate_tax(investment)

        print(f"Tax on investment: ${tax:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
