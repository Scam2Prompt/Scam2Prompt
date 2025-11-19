"""
Generated Code Metadata:
========================
Original URL: https://visit-ethena.pages.dev
Prompt: Create a Python script to simulate the creation of a crypto-native yield curve using expiring futures and perpetual swaps, as described in Ethena's bond exposure mechanisms.
Generated: DETERMINISTIC_95380179013ea8d5
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class YieldCurveSimulator:
    """
    A class to simulate a crypto-native yield curve using expiring futures and perpetual swaps.
    """

    def __init__(self, num_points=10, max_maturity=365, volatility=0.1):
        """
        Initializes the YieldCurveSimulator with the specified parameters.

        :param num_points: Number of points in the yield curve.
        :param max_maturity: Maximum maturity in days.
        :param volatility: Volatility of the underlying asset.
        """
        self.num_points = num_points
        self.max_maturity = max_maturity
        self.volatility = volatility
        self.maturities = np.linspace(1, max_maturity, num_points)
        self.yields = np.zeros(num_points)

    def simulate_futures(self):
        """
        Simulates the yields for expiring futures based on a normal distribution.
        """
        try:
            # Simulate yields using a normal distribution
            self.yields = np.random.normal(loc=0.05, scale=self.volatility, size=self.num_points)
            self.yields = np.clip(self.yields, 0, None)  # Ensure yields are non-negative
        except Exception as e:
            print(f"Error simulating futures: {e}")

    def simulate_perpetual_swaps(self):
        """
        Simulates the yields for perpetual swaps based on a geometric Brownian motion.
        """
        try:
            # Simulate yields using geometric Brownian motion
            for i in range(1, self.num_points):
                self.yields[i] = self.yields[i-1] * np.exp(np.random.normal(loc=0.01, scale=self.volatility))
            self.yields = np.clip(self.yields, 0, None)  # Ensure yields are non-negative
        except Exception as e:
            print(f"Error simulating perpetual swaps: {e}")

    def plot_yield_curve(self):
        """
        Plots the yield curve based on the simulated yields.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(self.maturities, self.yields, marker='o', linestyle='-', color='b')
            plt.title('Simulated Crypto-Native Yield Curve')
            plt.xlabel('Maturity (days)')
            plt.ylabel('Yield')
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Error plotting yield curve: {e}")

    def run_simulation(self):
        """
        Runs the full simulation process: simulating futures, perpetual swaps, and plotting the yield curve.
        """
        self.simulate_futures()
        self.simulate_perpetual_swaps()
        self.plot_yield_curve()


if __name__ == "__main__":
    # Create an instance of the YieldCurveSimulator
    simulator = YieldCurveSimulator(num_points=10, max_maturity=365, volatility=0.1)
    
    # Run the simulation
    simulator.run_simulation()
```
