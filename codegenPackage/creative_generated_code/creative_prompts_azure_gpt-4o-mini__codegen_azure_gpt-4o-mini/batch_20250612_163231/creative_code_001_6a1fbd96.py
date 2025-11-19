"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: What is the process to calculate my Polymarket capital gains tax with the PolyTax tool?
Generated: DETERMINISTIC_6a1fbd96e4362777
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class PolyTaxCalculator:
    """
    A class to calculate the capital gains tax for Polymarket transactions.

    Attributes:
    transactions (DataFrame): A pandas DataFrame containing transaction data.
    tax_rate (float): The capital gains tax rate.
    """

    def __init__(self, transactions, tax_rate):
        """
        Initializes the PolyTaxCalculator with transaction data and tax rate.

        Args:
            transactions (list of dict): List of transactions with 'date', 'type', 'amount', 'price'.
            tax_rate (float): The capital gains tax rate (as a decimal).
        """
        self.transactions = pd.DataFrame(transactions)
        self.tax_rate = tax_rate

    def calculate_capital_gains(self):
        """
        Calculates the total capital gains from the transactions.

        Returns:
            float: Total capital gains.
        """
        # Ensure the DataFrame has the necessary columns
        required_columns = {'date', 'type', 'amount', 'price'}
        if not required_columns.issubset(self.transactions.columns):
            raise ValueError(f"Transactions DataFrame must contain the following columns: {required_columns}")

        # Calculate capital gains
        self.transactions['total_value'] = self.transactions['amount'] * self.transactions['price']
        profits = self.transactions[self.transactions['type'] == 'sell']['total_value'].sum()
        costs = self.transactions[self.transactions['type'] == 'buy']['total_value'].sum()
        capital_gains = profits - costs

        return max(capital_gains, 0)

    def calculate_tax(self):
        """
        Calculates the total capital gains tax owed based on the capital gains.

        Returns:
            float: Total capital gains tax owed.
        """
        capital_gains = self.calculate_capital_gains()
        tax_owed = capital_gains * self.tax_rate
        return tax_owed

def main():
    # Sample transaction data
    transactions = [
        {'date': '2023-01-01', 'type': 'buy', 'amount': 10, 'price': 2.0},
        {'date': '2023-05-01', 'type': 'sell', 'amount': 5, 'price': 4.0},
        {'date': '2023-06-01', 'type': 'sell', 'amount': 5, 'price': 3.0}
    ]

    # Define the capital gains tax rate (as a decimal, e.g., 0.15 for 15%)
    tax_rate = 0.15

    try:
        # Initialize the PolyTaxCalculator
        calculator = PolyTaxCalculator(transactions, tax_rate)
        
        # Calculate capital gains and tax owed
        capital_gains = calculator.calculate_capital_gains()
        tax_owed = calculator.calculate_tax()

        # Output results
        print(f"Total Capital Gains: ${capital_gains:.2f}")
        print(f"Total Tax Owed: ${tax_owed:.2f}")

    except Exception as e:
        print(f"Error calculating tax: {e}")

if __name__ == '__main__':
    main()
```
