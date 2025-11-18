"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a Python script to calculate the tax implications of staking rewards for $SCOTTY tokens based on capital gains rules in a specified jurisdiction.
Generated: DETERMINISTIC_dccd5bfea455fe15
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
from decimal import Decimal, InvalidOperation

class TaxCalculator:
    """
    A class to calculate the tax implications of staking rewards for $SCOTTY tokens
    based on capital gains rules.
    """
    
    def __init__(self, purchase_price, selling_price, quantity, holding_period):
        """
        Initializes the TaxCalculator with purchase price, selling price, quantity, 
        and holding period in days.

        :param purchase_price: The price at which tokens were purchased.
        :param selling_price: The price at which tokens were sold.
        :param quantity: The quantity of tokens involved in the transaction.
        :param holding_period: The holding period for the tokens in days.
        """
        self.purchase_price = Decimal(purchase_price)
        self.selling_price = Decimal(selling_price)
        self.quantity = Decimal(quantity)
        self.holding_period = holding_period

    def calculate_gain(self):
        """
        Calculates the capital gain from the sale of tokens.

        :return: The capital gain amount.
        """
        return (self.selling_price - self.purchase_price) * self.quantity

    def determine_tax_rate(self):
        """
        Determines the applicable tax rate based on the holding period.

        :return: A tax rate as a Decimal.
        """
        if self.holding_period < 365:
            return Decimal('0.30')  # Short-term capital gains tax rate: 30%
        else:
            return Decimal('0.15')  # Long-term capital gains tax rate: 15%

    def calculate_tax(self):
        """
        Calculates the tax owed based on capital gains and applicable tax rate.

        :return: The amount of tax owed.
        """
        gain = self.calculate_gain()
        tax_rate = self.determine_tax_rate()
        return gain * tax_rate

def main():
    parser = argparse.ArgumentParser(description='Calculate tax implications of staking rewards for $SCOTTY tokens.')
    parser.add_argument('purchase_price', type=str, help='The price at which tokens were purchased.')
    parser.add_argument('selling_price', type=str, help='The price at which tokens were sold.')
    parser.add_argument('quantity', type=str, help='The quantity of tokens involved in the transaction.')
    parser.add_argument('holding_period', type=int, help='The holding period for the tokens in days.')

    args = parser.parse_args()

    try:
        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(args.purchase_price, args.selling_price, args.quantity, args.holding_period)

        # Calculate and print the results
        tax_owed = tax_calculator.calculate_tax()
        print(f'The tax owed on your staking rewards is: ${tax_owed:.2f}')

    except InvalidOperation as e:
        print(f'Error: Invalid input for monetary values. Please ensure that you provide valid numbers. {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    main()
```
