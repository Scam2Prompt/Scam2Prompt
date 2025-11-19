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
# capital_gains_tax_calculator.py

from datetime import datetime
from typing import List, Dict

class CapitalGainsTaxCalculator:
    """
    Calculates capital gains tax liability for cryptocurrency investments.
    """

    def __init__(self, tax_rate: float, long_term_rate: float, 
                 short_term_rate: float, annual_exemption: float):
        """
        Initializes the calculator with tax rates and exemption.

        Args:
        - tax_rate (float): General tax rate.
        - long_term_rate (float): Long-term capital gains tax rate.
        - short_term_rate (float): Short-term capital gains tax rate.
        - annual_exemption (float): Annual exemption amount.
        """
        self.tax_rate = tax_rate
        self.long_term_rate = long_term_rate
        self.short_term_rate = short_term_rate
        self.annual_exemption = annual_exemption

    def calculate_gains(self, transactions: List[Dict]) -> float:
        """
        Calculates total capital gains from a list of transactions.

        Args:
        - transactions (List[Dict]): List of transactions.
            Each transaction is a dictionary with 'buy_date', 'buy_price', 
            'sell_date', 'sell_price', and 'amount' keys.

        Returns:
        - float: Total capital gains.
        """
        total_gains = 0.0
        for transaction in transactions:
            buy_date = datetime.strptime(transaction['buy_date'], '%Y-%m-%d')
            sell_date = datetime.strptime(transaction['sell_date'], '%Y-%m-%d')
            holding_period = (sell_date - buy_date).days

            gain = transaction['sell_price'] * transaction['amount'] - \
                   transaction['buy_price'] * transaction['amount']

            if gain > 0:
                if holding_period > 365:  # Long-term gain
                    total_gains += gain * self.long_term_rate
                else:  # Short-term gain
                    total_gains += gain * self.short_term_rate

        return total_gains

    def calculate_tax_liability(self, transactions: List[Dict]) -> float:
        """
        Calculates tax liability from a list of transactions.

        Args:
        - transactions (List[Dict]): List of transactions.

        Returns:
        - float: Tax liability.
        """
        total_gains = self.calculate_gains(transactions)
        taxable_gains = max(0, total_gains - self.annual_exemption)
        tax_liability = taxable_gains * self.tax_rate

        return tax_liability


def main():
    try:
        calculator = CapitalGainsTaxCalculator(
            tax_rate=0.20, 
            long_term_rate=0.15, 
            short_term_rate=0.30, 
            annual_exemption=10000.0
        )

        transactions = [
            {
                'buy_date': '2022-01-01',
                'buy_price': 1000.0,
                'sell_date': '2022-01-15',
                'sell_price': 1200.0,
                'amount': 1.0
            },
            {
                'buy_date': '2022-06-01',
                'buy_price': 500.0,
                'sell_date': '2023-06-01',
                'sell_price': 800.0,
                'amount': 2.0
            }
        ]

        tax_liability = calculator.calculate_tax_liability(transactions)
        print(f'Tax Liability: ${tax_liability:.2f}')

    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
```
