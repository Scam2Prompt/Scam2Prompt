"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: Create a Python program to simulate risk scenarios in cryptocurrency trading, incorporating Immediate Peak's emphasis on understanding inherent risks.
Generated: DETERMINISTIC_3977013d1a4652ae
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
import matplotlib.pyplot as plt

class CryptoRiskSimulator:
    """
    A class to simulate risk scenarios in cryptocurrency trading.
    """
    
    def __init__(self, initial_investment: float, volatility: float, days: int):
        """
        Initialize the simulation with key parameters.

        :param initial_investment: The starting investment amount in USD.
        :param volatility: Daily price volatility (percentage as a decimal, e.g., 0.05 for 5%).
        :param days: Number of days to simulate.
        """
        self.initial_investment = initial_investment
        self.volatility = volatility
        self.days = days
        self.simulated_prices = []

    def simulate_price_movement(self):
        """
        Simulates daily price fluctuations based on volatility.

        :return: A list of simulated daily prices.
        """
        price = self.initial_investment
        self.simulated_prices.append(price)

        for _ in range(self.days):
            daily_change = np.random.normal(0, self.volatility)  # Normal distribution for daily change
            price *= (1 + daily_change)  # Update price
            price = max(price, 0)  # Ensure price doesn't go negative
            self.simulated_prices.append(price)

        return self.simulated_prices

    def plot_simulation(self):
        """
        Plots the simulated price movements over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.simulated_prices, label='Simulated Price Movement')
        plt.title('Cryptocurrency Price Simulation')
        plt.xlabel('Days')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    """
    Main function to execute the risk simulation.
    """
    try:
        # User input
        initial_investment = float(input("Enter initial investment amount (USD): "))
        volatility = float(input("Enter daily volatility (as a decimal, e.g., 0.05 for 5%): "))
        days = int(input("Enter number of days to simulate: "))
        
        # Validate inputs
        if initial_investment <= 0 or volatility <= 0 or days <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Create simulator instance
        simulator = CryptoRiskSimulator(initial_investment, volatility, days)
        
        # Simulate and plot
        simulator.simulate_price_movement()
        simulator.plot_simulation()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry-point of the program
if __name__ == "__main__":
    main()
```
