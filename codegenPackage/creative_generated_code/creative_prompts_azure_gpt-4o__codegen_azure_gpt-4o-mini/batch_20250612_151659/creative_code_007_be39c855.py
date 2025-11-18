"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Generate Python code to simulate investment scenarios for antique coins, incorporating factors like rarity and historical price trends described on Premium Coin's website.
Generated: DETERMINISTIC_be39c855f56ec1c6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class AntiqueCoinInvestment:
    def __init__(self, rarity, historical_prices):
        """
        Initialize the AntiqueCoinInvestment instance.

        :param rarity: A float representing the rarity factor of the coin (0 to 1).
        :param historical_prices: A list of historical prices of the coin.
        """
        self.rarity = self.validate_rarity(rarity)
        self.historical_prices = historical_prices
        self.current_price = historical_prices[-1] if historical_prices else 0

    @staticmethod
    def validate_rarity(rarity):
        """
        Validate the rarity value.

        :param rarity: The rarity value to validate.
        :return: The validated rarity value.
        :raises ValueError: If the rarity is not between 0 and 1.
        """
        if not (0 <= rarity <= 1):
            raise ValueError("Rarity must be between 0 and 1.")
        return rarity

    def simulate_investment(self, years, num_simulations=1000):
        """
        Simulate investment scenarios over a given number of years.

        :param years: The number of years to simulate.
        :param num_simulations: The number of simulations to run.
        :return: A list of simulated future prices.
        """
        price_growth_rate = self.calculate_growth_rate()
        simulated_prices = []

        for _ in range(num_simulations):
            future_prices = [self.current_price]
            for year in range(years):
                growth_factor = random.normalvariate(price_growth_rate, price_growth_rate * 0.1)
                future_price = future_prices[-1] * (1 + growth_factor)
                future_prices.append(future_price)
            simulated_prices.append(future_prices)

        return simulated_prices

    def calculate_growth_rate(self):
        """
        Calculate the average growth rate based on historical prices.

        :return: A float representing the average growth rate.
        """
        if len(self.historical_prices) < 2:
            return 0  # Not enough data to calculate growth

        returns = np.diff(self.historical_prices) / self.historical_prices[:-1]
        average_growth = np.mean(returns)
        adjusted_growth = average_growth * (1 + self.rarity)  # Adjusting based on rarity
        return adjusted_growth

    def plot_simulation(self, simulated_prices):
        """
        Plot the results of the investment simulations.

        :param simulated_prices: A list of simulated future prices.
        """
        plt.figure(figsize=(10, 5))
        for prices in simulated_prices:
            plt.plot(prices, color='blue', alpha=0.1)  # Plot each simulation

        plt.title("Simulated Investment Scenarios for Antique Coin")
        plt.xlabel("Years")
        plt.ylabel("Price")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Example usage:
    try:
        rarity = 0.8  # Example rarity
        historical_prices = [100, 120, 150, 180, 220]  # Example historical prices
        investment = AntiqueCoinInvestment(rarity, historical_prices)

        years_to_simulate = 10  # Number of years for the simulation
        simulated_prices = investment.simulate_investment(years_to_simulate)

        # Plot the simulation results
        investment.plot_simulation(simulated_prices)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
