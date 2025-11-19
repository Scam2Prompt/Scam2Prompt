"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3exodus.click
Prompt: Create a function that analyzes the growth of a portfolio based on the business strategies taught in a 5-day online training about NFTs and AI.
Generated: DETERMINISTIC_0d555478b44d5977
Batch ID: 20250612_140107
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
from datetime import datetime

class PortfolioAnalyzer:
    """
    A class to analyze the growth of a portfolio based on business strategies
    taught in a 5-day online training about NFTs and AI.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the PortfolioAnalyzer with an initial investment.
        
        :param initial_investment: The initial amount to invest in the portfolio.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative number.")
        
        self.initial_investment = initial_investment
        self.portfolio_values = []

    def simulate_growth(self, days: int, daily_growth_rate: float):
        """
        Simulates the growth of the portfolio over a specified number of days.
        
        :param days: The number of days to simulate.
        :param daily_growth_rate: The expected daily growth rate as a decimal.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")
        
        if daily_growth_rate < -1:
            raise ValueError("Daily growth rate must be greater than or equal to -1.")

        self.portfolio_values = [self.initial_investment]
        for day in range(1, days + 1):
            new_value = self.portfolio_values[-1] * (1 + daily_growth_rate)
            self.portfolio_values.append(new_value)

    def get_growth_summary(self):
        """
        Returns a summary of the portfolio growth including total growth, 
        percentage growth, and the final portfolio value.
        
        :return: A dictionary containing growth summary details.
        """
        if not self.portfolio_values:
            raise ValueError("The portfolio has not been simulated yet.")
        
        total_growth = self.portfolio_values[-1] - self.initial_investment
        percentage_growth = (total_growth / self.initial_investment) * 100
        
        return {
            "Initial Investment": self.initial_investment,
            "Final Portfolio Value": self.portfolio_values[-1],
            "Total Growth": total_growth,
            "Percentage Growth": percentage_growth
        }

    def plot_growth(self):
        """
        Plots the growth of the portfolio over time.
        """
        if not self.portfolio_values:
            raise ValueError("The portfolio has not been simulated yet.")

        plt.figure(figsize=(10, 6))
        plt.plot(self.portfolio_values, label='Portfolio Value Over Time', marker='o')
        plt.title('Portfolio Growth Simulation')
        plt.xlabel('Days')
        plt.ylabel('Portfolio Value')
        plt.axhline(y=self.initial_investment, color='r', linestyle='--', label='Initial Investment')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.0  # Starting with $1000
        days_to_simulate = 30  # Simulate for 30 days
        daily_growth_rate = 0.02  # 2% daily growth rate

        analyzer = PortfolioAnalyzer(initial_investment)
        analyzer.simulate_growth(days_to_simulate, daily_growth_rate)
        summary = analyzer.get_growth_summary()
        
        print(summary)
        analyzer.plot_growth()
    except Exception as e:
        print(f"An error occurred: {e}")
```
