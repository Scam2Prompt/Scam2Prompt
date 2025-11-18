"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-atomcapital.com
Prompt: Write code to simulate the impact of economic shifts on capital markets, referencing Atom Capital's educational content on aligning financial strategies with market conditions.
Generated: DETERMINISTIC_dc7a95c011a2df2e
Batch ID: 20250612_150048
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

class MarketSimulator:
    """
    A class to simulate the impact of economic shifts on capital markets.
    The simulation is based on historical economic factors and their effects on market indices.
    """

    def __init__(self, initial_investment: float, economic_factors: dict):
        """
        Initialize the MarketSimulator with an initial investment and economic factors.
        
        Parameters:
        initial_investment (float): The initial amount of capital to invest.
        economic_factors (dict): A dictionary containing economic factors affecting the market.
        """
        self.initial_investment = initial_investment
        self.economic_factors = economic_factors
        self.portfolio_value = initial_investment
        self.history = []

    def apply_economic_shift(self, shift: str):
        """
        Apply an economic shift to the market simulation.
        
        Parameters:
        shift (str): The type of economic shift ('recession', 'growth', 'stability').
        
        Raises:
        ValueError: If the shift type is not recognized.
        """
        if shift not in self.economic_factors:
            raise ValueError(f"Unrecognized economic shift: {shift}. Valid shifts are: {list(self.economic_factors.keys())}")

        # Simulate market impact based on the economic shift
        impact_factor = self.economic_factors[shift]
        self.portfolio_value *= (1 + impact_factor)
        self.history.append(self.portfolio_value)

    def simulate(self, shifts: list):
        """
        Simulate a series of economic shifts on the capital market.
        
        Parameters:
        shifts (list): A list of economic shifts to simulate.
        """
        for shift in shifts:
            self.apply_economic_shift(shift)

    def plot_results(self):
        """
        Plot the results of the simulation showing portfolio value over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.history, marker='o')
        plt.title('Capital Market Simulation Results')
        plt.xlabel('Time Steps')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.axhline(y=self.initial_investment, color='r', linestyle='--', label='Initial Investment')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define economic factors affecting the capital markets
    economic_factors = {
        'recession': -0.15,  # 15% loss during recession
        'growth': 0.10,      # 10% gain during growth
        'stability': 0.02     # 2% gain during stable conditions
    }

    # Initialize the market simulator with an initial investment of $10,000
    simulator = MarketSimulator(initial_investment=10000, economic_factors=economic_factors)

    # Define a sequence of economic shifts to simulate
    shifts = ['growth', 'stability', 'recession', 'growth', 'stability']

    # Run the simulation
    simulator.simulate(shifts)

    # Plot the results
    simulator.plot_results()
```
