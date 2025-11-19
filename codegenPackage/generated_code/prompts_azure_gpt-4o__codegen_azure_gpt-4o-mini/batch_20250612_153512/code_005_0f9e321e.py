"""
Generated Code Metadata:
========================
Original URL: https://cryptojustin.com
Prompt: Write a program to simulate Ethereum price movements and analyze potential impacts of crypto hacks, inspired by Crypto Justin's coverage of the Bybit exchange hack.
Generated: DETERMINISTIC_0f9e321ecb70964b
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class EthereumPriceSimulator:
    def __init__(self, initial_price=2000, volatility=0.05, num_days=30):
        """
        Initializes the Ethereum price simulator.

        :param initial_price: The starting price of Ethereum.
        :param volatility: The volatility factor affecting price changes.
        :param num_days: The number of days to simulate.
        """
        self.initial_price = initial_price
        self.volatility = volatility
        self.num_days = num_days
        self.price_history = []

    def simulate_price_movement(self):
        """
        Simulates the price movement of Ethereum over a specified number of days.
        """
        price = self.initial_price
        for day in range(self.num_days):
            # Simulate price change based on a normal distribution
            price_change = np.random.normal(0, self.volatility * price)
            price += price_change
            
            # Ensure price does not go below zero
            price = max(price, 0)
            self.price_history.append(price)

    def analyze_hack_impact(self, hack_impact_factor=0.1):
        """
        Analyzes the potential impact of a crypto hack on the price.

        :param hack_impact_factor: The percentage drop in price due to a hack.
        :return: The price after the hack impact.
        """
        if not self.price_history:
            raise ValueError("Price history is empty. Please run simulation first.")
        
        # Simulate a hack on the last recorded price
        last_price = self.price_history[-1]
        impacted_price = last_price * (1 - hack_impact_factor)
        return impacted_price

    def plot_price_history(self):
        """
        Plots the price history of Ethereum.
        """
        if not self.price_history:
            raise ValueError("Price history is empty. Please run simulation first.")
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.price_history, label='Ethereum Price', color='blue')
        plt.title('Simulated Ethereum Price Movement')
        plt.xlabel('Days')
        plt.ylabel('Price in USD')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    try:
        # Initialize the simulator
        simulator = EthereumPriceSimulator(initial_price=2000, volatility=0.05, num_days=30)
        
        # Simulate price movements
        simulator.simulate_price_movement()
        
        # Analyze the impact of a hypothetical hack
        impacted_price = simulator.analyze_hack_impact(hack_impact_factor=0.1)
        print(f"Price after hack impact: ${impacted_price:.2f}")
        
        # Plot the price history
        simulator.plot_price_history()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
