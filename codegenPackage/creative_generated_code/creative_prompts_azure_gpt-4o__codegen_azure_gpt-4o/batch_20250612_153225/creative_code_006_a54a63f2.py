"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperhanded-orbs.pages.dev
Prompt: Suggest a method to generate visualizations (e.g., graphs and charts) for tracking key metrics of cryptocurrency portfolios, inspired by HALO's data visualization features.
Generated: DETERMINISTIC_a54a63f2c9d19274
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import random

# Class for cryptocurrency portfolio visualization
class CryptoPortfolioVisualizer:
    def __init__(self, portfolio_data):
        """
        Initializes the visualizer with portfolio data.

        Args:
            portfolio_data (dict): A dictionary where keys are cryptocurrency names
                                   and values are lists of historical prices.
        """
        self.portfolio_data = portfolio_data

    def generate_price_trends(self):
        """
        Generates line charts to visualize historical price trends for each cryptocurrency.
        """
        try:
            plt.figure(figsize=(12, 6))
            for crypto, prices in self.portfolio_data.items():
                plt.plot(prices, label=crypto)
            
            plt.title("Cryptocurrency Price Trends")
            plt.xlabel("Time (Days)")
            plt.ylabel("Price (USD)")
            plt.legend(loc="upper left")
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error generating price trends visualization: {e}")

    def generate_portfolio_distribution(self):
        """
        Generates a pie chart to visualize the portfolio allocation.
        Allocation is based on the latest value of each cryptocurrency.
        """
        try:
            latest_prices = {crypto: data[-1] for crypto, data in self.portfolio_data.items()}
            total_value = sum(latest_prices.values())
            allocations = {crypto: (value / total_value) * 100 for crypto, value in latest_prices.items()}
            
            plt.figure(figsize=(8, 8))
            plt.pie(
                allocations.values(),
                labels=allocations.keys(),
                autopct='%1.1f%%',
                startangle=140
            )
            plt.title("Portfolio Allocation")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error generating portfolio distribution visualization: {e}")

# Example usage
if __name__ == "__main__":
    # Sample cryptocurrency portfolio data (randomly generated for demonstration purposes)
    portfolio_data = {
        "Bitcoin": [random.uniform(20000, 60000) for _ in range(30)],
        "Ethereum": [random.uniform(1000, 4000) for _ in range(30)],
        "Cardano": [random.uniform(0.3, 3) for _ in range(30)],
        "Solana": [random.uniform(10, 250) for _ in range(30)]
    }

    # Initialize the visualizer
    visualizer = CryptoPortfolioVisualizer(portfolio_data)

    # Generate visualizations
    visualizer.generate_price_trends()
    visualizer.generate_portfolio_distribution()
```
