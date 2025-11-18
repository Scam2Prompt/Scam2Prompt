"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Generate code to calculate short-term and long-term capital gains based on Immediate Helix V9’s descriptions. Include tax implications for both types of gains.
Generated: DETERMINISTIC_beafbbadaa58c918
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CapitalGainsCalculator:
    """
    A class to calculate short-term and long-term capital gains and their tax implications.
    """

    def __init__(self, purchase_price, sale_price, holding_period_days):
        """
        Initializes the calculator with purchase and sale prices and the holding period.

        :param purchase_price: The price at which the asset was purchased.
        :param sale_price: The price at which the asset was sold.
        :param holding_period_days: The duration in days the asset was held.
        """
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.holding_period_days = holding_period_days

    def calculate_gain(self):
        """
        Calculates the capital gain from the sale of the asset.

        :return: The capital gain.
        """
        return self.sale_price - self.purchase_price

    def determine_gain_type(self):
        """
        Determines if the gain is short-term or long-term based on the holding period.

        :return: 'short-term' or 'long-term'.
        """
        return 'short-term' if self.holding_period_days < 365 else 'long-term'

    def calculate_tax(self):
        """
        Calculates the tax implications based on the type of capital gain.

        :return: The tax amount payable.
        """
        gain = self.calculate_gain()
        gain_type = self.determine_gain_type()

        if gain_type == 'short-term':
            tax_rate = 0.22  # Example short-term capital gains tax rate
        else:
            tax_rate = 0.15  # Example long-term capital gains tax rate
        
        tax = gain * tax_rate
        return tax if gain > 0 else 0  # No tax on negative gains

    def report(self):
        """
        Reports the capital gain, type, and tax implications.

        :return: A dictionary with gain type, amount, and tax due.
        """
        gain = self.calculate_gain()
        gain_type = self.determine_gain_type()
        tax_due = self.calculate_tax()

        report = {
            'capital_gain': gain,
            'gain_type': gain_type,
            'tax_due': tax_due
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Example values for purchase price, sale price, and holding period
        purchase_price = 5000.00
        sale_price = 7000.00
        holding_period_days = 200

        # Create an instance of the calculator
        calculator = CapitalGainsCalculator(purchase_price, sale_price, holding_period_days)

        # Generate report
        result = calculator.report()
        print("Capital Gains Report:", result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
