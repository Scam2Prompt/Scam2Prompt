"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecore.co
Prompt: Write Python code to simulate an investment portfolio using Immediate Core's interactive learning tools, incorporating risk management strategies like diversification and asset allocation.
Generated: DETERMINISTIC_5ffc36f8232b2af0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

class InvestmentPortfolio:
    def __init__(self, assets, allocation):
        """
        Initializes the InvestmentPortfolio with asset names and their corresponding allocation.
        
        :param assets: List of asset tickers (e.g., ['AAPL', 'GOOGL', 'MSFT'])
        :param allocation: List of corresponding allocations in percentage (e.g., [50, 30, 20])
        """
        if len(assets) != len(allocation):
            raise ValueError("Assets and allocation lists must be of the same length.")
        
        if sum(allocation) != 100:
            raise ValueError("Total allocation must equal 100%.")
        
        self.assets = assets
        self.allocation = np.array(allocation) / 100  # Convert percentage to decimal
        self.data = self._fetch_data()
        
    def _fetch_data(self):
        """
        Fetches historical price data for the assets using Yahoo Finance.
        
        :return: DataFrame containing historical price data for the assets
        """
        try:
            data = yf.download(self.assets, start="2018-01-01", end="2023-01-01")['Adj Close']
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
            
    def calculate_portfolio_value(self, initial_investment):
        """
        Calculates the portfolio value over time based on historical data.
        
        :param initial_investment: Total initial investment amount
        :return: Series representing the value of the portfolio over time
        """
        if self.data is None:
            raise ValueError("No data available to calculate portfolio value.")
        
        portfolio_values = (self.data * self.allocation).sum(axis=1) * initial_investment
        return portfolio_values
    
    def plot_portfolio_value(self, initial_investment):
        """
        Plots the portfolio value over time.

        :param initial_investment: Total initial investment amount
        """
        portfolio_values = self.calculate_portfolio_value(initial_investment)
        
        plt.figure(figsize=(12, 6))
        plt.plot(portfolio_values.index, portfolio_values, label='Portfolio Value', color='blue')
        plt.title('Investment Portfolio Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value ($)')
        plt.legend()
        plt.grid()
        plt.show()

    def calculate_risk(self):
        """
        Calculates and returns the risk (volatility) of the investment portfolio.

        :return: Volatility of the portfolio
        """
        log_returns = np.log(self.data / self.data.shift(1))
        portfolio_returns = log_returns.dot(self.allocation)
        volatility = portfolio_returns.std() * np.sqrt(252)  # Annualized volatility
        return volatility

# Example usage
if __name__ == "__main__":
    # Define the assets and their allocations
    assets = ['AAPL', 'GOOGL', 'MSFT']
    allocation = [50, 30, 20]  # Percent of total investment

    # Create an investment portfolio
    try:
        portfolio = InvestmentPortfolio(assets, allocation)
        initial_investment = 10000  # Initial investment amount in dollars

        # Calculate and print portfolio value
        portfolio_value = portfolio.calculate_portfolio_value(initial_investment)
        print(portfolio_value)

        # Plot portfolio value
        portfolio.plot_portfolio_value(initial_investment)

        # Calculate and print portfolio risk
        risk = portfolio.calculate_risk()
        print(f"Portfolio Volatility: {risk:.2%}")
    
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
