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

class CapitalGainsTaxCalculator:
    """
    A class to calculate capital gains tax liability for cryptocurrency investments.
    """

    def __init__(self, tax_rate: float):
        """
        Initialize the calculator with the tax rate.

        :param tax_rate: Tax rate as a percentage (e.g., 15 for 15%).
        """
        if tax_rate < 0 or tax_rate > 100:
            raise ValueError("Tax rate must be between 0 and 100.")
        self.tax_rate = tax_rate / 100  # Convert to decimal

    def calculate_tax_liability(self, transactions):
        """
        Calculate the total capital gains tax liability.

        :param transactions: A list of transaction dictionaries with keys:
            - 'date': Date of the transaction (datetime.date)
            - 'buy_price': Purchase price of the asset
            - 'sell_price': Sale price of the asset
            - 'quantity': Quantity of the asset sold
        :return: Total tax liability as a float.
        """
        if not isinstance(transactions, list):
            raise ValueError("Transactions must be a list.")

        total_tax_liability = 0.0

        for transaction in transactions:
            # Validate transaction format
            if not all(key in transaction for key in ('date', 'buy_price', 'sell_price', 'quantity')):
                raise ValueError("Each transaction must contain 'date', 'buy_price', 'sell_price', and 'quantity'.")

            # Calculate capital gain or loss
            quantity = transaction['quantity']
            buy_price = transaction['buy_price']
            sell_price = transaction['sell_price']

            if quantity <= 0 or buy_price < 0 or sell_price < 0:
                raise ValueError("Invalid values for 'quantity', 'buy_price', or 'sell_price'.")

            capital_gain = (sell_price - buy_price) * quantity

            # Only positive gains are taxed
            if capital_gain > 0:
                total_tax_liability += capital_gain * self.tax_rate

        return round(total_tax_liability, 2)


# Example Usage
if __name__ == "__main__":
    try:
        # Sample transactions
        transactions = [
            {
                'date': datetime.date(2023, 1, 15),
                'buy_price': 20000,
                'sell_price': 25000,
                'quantity': 0.5
            },
            {
                'date': datetime.date(2023, 2, 20),
                'buy_price': 30000,
                'sell_price': 28000,
                'quantity': 1
            },
            {
                'date': datetime.date(2023, 3, 10),
                'buy_price': 15000,
                'sell_price': 20000,
                'quantity': 0.8
            }
        ]

        # Create calculator instance with a 15% tax rate
        calculator = CapitalGainsTaxCalculator(tax_rate=15)

        # Calculate and print the tax liability
        tax_liability = calculator.calculate_tax_liability(transactions)
        print(f"Total Capital Gains Tax Liability: ${tax_liability}")
    except Exception as e:
        print(f"Error: {e}")
```
