"""
Generated Code Metadata:
========================
Original URL: https://polymarket.tax
Prompt: Write a function to calculate gambling income from Polymarket trades and format it for Schedule 1, Line 8b reporting, based on the guidelines provided by PolyTax.
Generated: DETERMINISTIC_5c885f63d3c75d1f
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class PolymarketTrade:
    def __init__(self, trade_data: Dict):
        """
        Initialize a PolymarketTrade instance.

        :param trade_data: A dictionary containing trade information.
        """
        self.trade_data = trade_data
        self.validate_trade_data()

    def validate_trade_data(self):
        """
        Validate the trade data to ensure it contains necessary fields.
        Raises ValueError if validation fails.
        """
        required_fields = ['amount', 'outcome', 'price', 'trade_type']
        for field in required_fields:
            if field not in self.trade_data:
                raise ValueError(f"Missing required field: {field}")

    def calculate_income(self) -> float:
        """
        Calculate the income from the trade.

        :return: The income from the trade.
        """
        amount = self.trade_data['amount']
        price = self.trade_data['price']
        trade_type = self.trade_data['trade_type']

        if trade_type == 'buy':
            return -amount  # Loss when buying
        elif trade_type == 'sell':
            return amount * price  # Profit when selling
        else:
            raise ValueError(f"Invalid trade type: {trade_type}")

def calculate_total_income(trades: List[PolymarketTrade]) -> float:
    """
    Calculate the total income from a list of Polymarket trades.

    :param trades: A list of PolymarketTrade instances.
    :return: The total income from all trades.
    """
    total_income = 0.0
    for trade in trades:
        total_income += trade.calculate_income()
    return total_income

def format_for_schedule_1(income: float) -> str:
    """
    Format the income for Schedule 1, Line 8b reporting.

    :param income: The total income to format.
    :return: A formatted string for reporting.
    """
    return f"${income:,.2f}"

def main(trade_data_list: List[Dict]) -> str:
    """
    Main function to process trade data and return formatted income.

    :param trade_data_list: A list of dictionaries containing trade data.
    :return: A formatted string representing total income for reporting.
    """
    trades = []
    for trade_data in trade_data_list:
        try:
            trade = PolymarketTrade(trade_data)
            trades.append(trade)
        except ValueError as e:
            print(f"Error processing trade data: {e}")

    total_income = calculate_total_income(trades)
    return format_for_schedule_1(total_income)

# Example usage
if __name__ == "__main__":
    # Sample trade data
    sample_trade_data = [
        {"amount": 100, "outcome": "yes", "price": 1.2, "trade_type": "sell"},
        {"amount": 50, "outcome": "no", "price": 0.8, "trade_type": "buy"},
        {"amount": 200, "outcome": "yes", "price": 1.5, "trade_type": "sell"},
    ]

    formatted_income = main(sample_trade_data)
    print(f"Total Income for Schedule 1, Line 8b: {formatted_income}")
```
