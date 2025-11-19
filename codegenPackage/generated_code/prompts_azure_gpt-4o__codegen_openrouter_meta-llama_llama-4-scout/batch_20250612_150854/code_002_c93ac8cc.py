"""
Generated Code Metadata:
========================
Original URL: https://immediate-neupro.co
Prompt: Create a program that generates real-time reports on investment progress, inspired by the "informes instantáneos" feature described on Portefeuille Vexo.
Generated: DETERMINISTIC_c93ac8cccc166bd4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_report_generator.py

import datetime
import pandas as pd
import yfinance as yf

class InvestmentReportGenerator:
    """
    Generates real-time reports on investment progress.
    """

    def __init__(self, portfolio):
        """
        Initializes the InvestmentReportGenerator with a portfolio.

        Args:
            portfolio (dict): A dictionary of investments with their respective tickers and quantities.
        """
        self.portfolio = portfolio

    def get_investment_data(self):
        """
        Retrieves the current data for each investment in the portfolio.

        Returns:
            dict: A dictionary of investments with their respective data.
        """
        investment_data = {}
        for ticker, quantity in self.portfolio.items():
            try:
                data = yf.Ticker(ticker)
                info = data.info
                investment_data[ticker] = {
                    'name': info['shortName'],
                    'current_price': info['currentPrice'],
                    'market_cap': info['marketCap'],
                    'quantity': quantity
                }
            except Exception as e:
                print(f"Error retrieving data for {ticker}: {str(e)}")
        return investment_data

    def calculate_investment_values(self, investment_data):
        """
        Calculates the current value of each investment in the portfolio.

        Args:
            investment_data (dict): A dictionary of investments with their respective data.

        Returns:
            dict: A dictionary of investments with their respective values.
        """
        investment_values = {}
        for ticker, data in investment_data.items():
            current_value = data['current_price'] * data['quantity']
            investment_values[ticker] = {
                'name': data['name'],
                'current_value': current_value,
                'market_cap': data['market_cap']
            }
        return investment_values

    def generate_report(self):
        """
        Generates a real-time report on investment progress.

        Returns:
            pd.DataFrame: A DataFrame containing the investment report.
        """
        investment_data = self.get_investment_data()
        investment_values = self.calculate_investment_values(investment_data)

        # Create a DataFrame from the investment values
        df = pd.DataFrame({
            'Investment': list(investment_values.keys()),
            'Name': [data['name'] for data in investment_values.values()],
            'Current Value': [data['current_value'] for data in investment_values.values()],
            'Market Cap': [data['market_cap'] for data in investment_values.values()]
        })

        # Calculate the total portfolio value
        total_portfolio_value = df['Current Value'].sum()

        # Add a summary row to the DataFrame
        summary_row = pd.DataFrame({
            'Investment': ['Total Portfolio'],
            'Name': [''],
            'Current Value': [total_portfolio_value],
            'Market Cap': ['']
        })

        # Append the summary row to the DataFrame
        df = pd.concat([df, summary_row], ignore_index=True)

        return df

def main():
    # Example usage
    portfolio = {
        'AAPL': 10,
        'GOOGL': 5,
        'MSFT': 20
    }

    generator = InvestmentReportGenerator(portfolio)
    report = generator.generate_report()

    print(report)

if __name__ == "__main__":
    main()
```
