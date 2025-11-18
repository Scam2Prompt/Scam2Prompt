"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Develop a program to simulate cryptocurrency price volatility and assess risk, based on the investment strategies for cryptocurrencies described on Petrolio Italiano.
Generated: DETERMINISTIC_b00fd186d35bf1e4
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

class CryptoSimulator:
    def __init__(self, initial_investment, price, volatility, days):
        """
        Initializes the cryptocurrency simulator with the specified parameters.

        :param initial_investment: Initial amount of investment in cryptocurrency
        :param price: Current price of the cryptocurrency
        :param volatility: Daily volatility as a percentage (e.g., 5 for 5%)
        :param days: Number of days to simulate
        """
        self.initial_investment = initial_investment
        self.price = price
        self.volatility = volatility / 100  # Convert percentage to decimal
        self.days = days
        self.prices = []
        self.investment_values = []

    def simulate_price(self):
        """
        Simulates the price of the cryptocurrency over the specified number of days based on its volatility.
        """
        for day in range(self.days):
            # Calculate daily price change based on volatility
            daily_change = np.random.normal(loc=0, scale=self.volatility)
            self.price *= (1 + daily_change)
            self.prices.append(self.price)

    def assess_risk(self):
        """
        Assesses the risk of the investment by calculating the maximum drawdown and volatility.
        """
        price_series = np.array(self.prices)
        # Calculate daily returns
        returns = np.diff(price_series) / price_series[:-1]
        
        # Calculate maximum drawdown
        peak = np.maximum.accumulate(price_series)
        drawdown = (peak - price_series) / peak
        max_drawdown = np.max(drawdown)
        
        # Calculate annualized volatility
        annualized_volatility = np.std(returns) * np.sqrt(252)  # Assuming 252 trading days in a year

        return max_drawdown, annualized_volatility

    def run_simulation(self):
        """
        Runs the full simulation, generates price data, and evaluates risk metrics.

        :return: A tuple containing maximum drawdown and annualized volatility
        """
        self.simulate_price()
        max_drawdown, annualized_volatility = self.assess_risk()
        self.investment_values = [self.initial_investment * (price / self.initial_investment) for price in self.prices]

        return max_drawdown, annualized_volatility

    def plot_results(self):
        """
        Plots the simulated prices and investment value over time.
        """
        plt.figure(figsize=(14, 7))
        plt.subplot(2, 1, 1)
        plt.plot(self.prices, label='Simulated Price', color='blue')
        plt.title('Cryptocurrency Price Simulation')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.investment_values, label='Investment Value', color='green')
        plt.title('Investment Value Over Time')
        plt.xlabel('Days')
        plt.ylabel('Value')
        plt.legend()

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Set parameters for simulation
        initial_investment = 10000  # Initial investment amount in USD
        initial_price = 30000  # Initial price of the cryptocurrency in USD
        daily_volatility = 5  # Daily volatility in percentage
        simulation_days = 30  # Number of days to simulate

        # Create a CryptoSimulator instance
        simulator = CryptoSimulator(initial_investment, initial_price, daily_volatility, simulation_days)

        # Run the simulation
        max_drawdown, annualized_volatility = simulator.run_simulation()

        # Output the risk assessment
        print(f"Maximum Drawdown: {max_drawdown:.2%}")
        print(f"Annualized Volatility: {annualized_volatility:.2%}")

        # Plot the results
        simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
