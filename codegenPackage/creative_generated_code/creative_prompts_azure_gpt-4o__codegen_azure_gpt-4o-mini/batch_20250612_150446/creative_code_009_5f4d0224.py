"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultimateexperttrade24.com
Prompt: Develop a Python script to simulate the performance of industry ETFs in sectors like energy or biotechnology, as described on Ultimateexperttrade24.com.
Generated: DETERMINISTIC_5f4d022471ebfccb
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

class ETFPerformanceSimulator:
    def __init__(self, tickers, start_date, end_date):
        """
        Initializes the ETFPerformanceSimulator with the specified parameters.

        :param tickers: List of ETF tickers to simulate
        :param start_date: Start date for historical data in 'YYYY-MM-DD' format
        :param end_date: End date for historical data in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        """
        Fetch historical price data for the specified ETFs using the Yahoo Finance API.

        :raises Exception: If data fetching fails
        """
        try:
            self.data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
            print("Data fetched successfully.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_returns(self):
        """
        Calculate daily returns from the historical price data.

        :return: DataFrame of daily returns
        """
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")
        returns = self.data.pct_change().dropna()
        print("Daily returns calculated.")
        return returns

    def simulate_performance(self, initial_investment=10000):
        """
        Simulate the performance of the ETFs over the specified period.

        :param initial_investment: Initial investment amount for the simulation
        :return: DataFrame containing the simulated portfolio value over time
        """
        returns = self.calculate_returns()
        simulated_portfolio = (returns + 1).cumprod() * initial_investment
        print("Simulation completed.")
        return simulated_portfolio

    def plot_performance(self, simulated_portfolio):
        """
        Plot the simulated performance of the ETFs.

        :param simulated_portfolio: DataFrame containing the simulated portfolio values
        """
        plt.figure(figsize=(14, 7))
        for ticker in simulated_portfolio.columns:
            plt.plot(simulated_portfolio.index, simulated_portfolio[ticker], label=ticker)

        plt.title("ETF Performance Simulation")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value")
        plt.legend()
        plt.grid()
        plt.show()

def main():
    # Define the ETFs, start date, and end date for the simulation
    etfs = ['XLE', 'XBI']  # Example: Energy and Biotechnology ETFs
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # Create an instance of the simulator
    simulator = ETFPerformanceSimulator(etfs, start_date, end_date)

    # Fetch data, simulate performance, and plot results
    try:
        simulator.fetch_data()
        portfolio_values = simulator.simulate_performance()
        simulator.plot_performance(portfolio_values)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    main()
```
