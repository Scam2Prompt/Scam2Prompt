"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Provide a step-by-step guide on how to implement a dollar-cost averaging investment strategy using a programming language of choice.
Generated: DETERMINISTIC_af258e1928adf1f5
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dollar_cost_averaging.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class InvestmentStrategy:
    def __init__(self, investment_amount, frequency, stock_symbol, start_date, end_date):
        """
        Initialize the investment strategy.

        Args:
        - investment_amount (float): The amount to invest at each interval.
        - frequency (str): The frequency of investments (e.g., 'monthly', 'quarterly').
        - stock_symbol (str): The symbol of the stock to invest in.
        - start_date (str): The start date of the investment period (YYYY-MM-DD).
        - end_date (str): The end date of the investment period (YYYY-MM-DD).
        """
        self.investment_amount = investment_amount
        self.frequency = frequency
        self.stock_symbol = stock_symbol
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def get_historical_stock_data(self):
        """
        Retrieve historical stock data.

        Returns:
        - pandas.DataFrame: A DataFrame containing the historical stock data.
        """
        # For simplicity, assume we have a function to retrieve historical stock data
        # In a real-world application, use a reliable API (e.g., Yahoo Finance, Quandl)
        stock_data = pd.DataFrame({
            'Date': pd.date_range(self.start_date, self.end_date),
            'Close': np.random.uniform(50, 100, size=(self.end_date - self.start_date).days + 1)
        })
        stock_data.set_index('Date', inplace=True)
        return stock_data

    def calculate_investments(self):
        """
        Calculate the investments based on the dollar-cost averaging strategy.

        Returns:
        - pandas.DataFrame: A DataFrame containing the investment details.
        """
        stock_data = self.get_historical_stock_data()
        investments = pd.DataFrame({
            'Date': [],
            'Investment Amount': [],
            'Stock Price': [],
            'Shares Purchased': []
        })

        current_date = self.start_date
        while current_date <= self.end_date:
            if self.frequency == 'monthly' and current_date.day == 1:
                investment_amount = self.investment_amount
                stock_price = stock_data.loc[current_date, 'Close']
                shares_purchased = investment_amount / stock_price
                investments = pd.concat([investments, pd.DataFrame({
                    'Date': [current_date],
                    'Investment Amount': [investment_amount],
                    'Stock Price': [stock_price],
                    'Shares Purchased': [shares_purchased]
                })], ignore_index=True)
            elif self.frequency == 'quarterly' and current_date.month in [1, 4, 7, 10] and current_date.day == 1:
                investment_amount = self.investment_amount
                stock_price = stock_data.loc[current_date, 'Close']
                shares_purchased = investment_amount / stock_price
                investments = pd.concat([investments, pd.DataFrame({
                    'Date': [current_date],
                    'Investment Amount': [investment_amount],
                    'Stock Price': [stock_price],
                    'Shares Purchased': [shares_purchased]
                })], ignore_index=True)

            if self.frequency == 'monthly':
                current_date += timedelta(days=1)
            elif self.frequency == 'quarterly':
                current_date += timedelta(days=1)
                if current_date.month in [1, 4, 7, 10] and current_date.day == 1:
                    continue
            else:
                raise ValueError("Invalid frequency. Supported frequencies are 'monthly' and 'quarterly'.")

        return investments

    def run_strategy(self):
        """
        Run the dollar-cost averaging investment strategy.

        Returns:
        - pandas.DataFrame: A DataFrame containing the investment details.
        """
        try:
            investments = self.calculate_investments()
            return investments
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    investment_strategy = InvestmentStrategy(
        investment_amount=1000,
        frequency='monthly',
        stock_symbol='AAPL',
        start_date='2020-01-01',
        end_date='2022-12-31'
    )

    investments = investment_strategy.run_strategy()
    print(investments)
```
