"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: Create a function in Python to simulate the impact of mold, mildew, and algae on deck deterioration over time, using insights from "How Mold, Mildew, and Algae Affect Your Deck Over Time" on Real and Origin.
Generated: DETERMINISTIC_b4d2a64120af0c3f
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class DeckDeteriorationSimulator:
    """
    A class to simulate the impact of mold, mildew, and algae on deck deterioration over time.
    """

    def __init__(self, initial_condition: float, mold_growth_rate: float, mildew_growth_rate: float, algae_growth_rate: float):
        """
        Initializes the simulator with the initial condition of the deck and growth rates for mold, mildew, and algae.

        :param initial_condition: Initial condition of the deck (0 to 100 scale).
        :param mold_growth_rate: Growth rate of mold (percentage per time unit).
        :param mildew_growth_rate: Growth rate of mildew (percentage per time unit).
        :param algae_growth_rate: Growth rate of algae (percentage per time unit).
        """
        if not (0 <= initial_condition <= 100):
            raise ValueError("Initial condition must be between 0 and 100.")
        if any(rate < 0 for rate in [mold_growth_rate, mildew_growth_rate, algae_growth_rate]):
            raise ValueError("Growth rates must be non-negative.")

        self.initial_condition = initial_condition
        self.mold_growth_rate = mold_growth_rate
        self.mildew_growth_rate = mildew_growth_rate
        self.algae_growth_rate = algae_growth_rate

    def simulate_deterioration(self, time_period: int) -> np.ndarray:
        """
        Simulates the deterioration of the deck over a specified time period.

        :param time_period: The number of time units to simulate.
        :return: An array of deck conditions over time.
        """
        if time_period <= 0:
            raise ValueError("Time period must be a positive integer.")

        # Initialize the condition array
        conditions = np.zeros(time_period)
        conditions[0] = self.initial_condition

        # Simulate deterioration over time
        for t in range(1, time_period):
            mold_effect = conditions[t-1] * (self.mold_growth_rate / 100)
            mildew_effect = conditions[t-1] * (self.mildew_growth_rate / 100)
            algae_effect = conditions[t-1] * (self.algae_growth_rate / 100)

            # Update the condition based on the growth effects
            conditions[t] = max(0, conditions[t-1] - (mold_effect + mildew_effect + algae_effect))

        return conditions

    def plot_deterioration(self, time_period: int):
        """
        Plots the deterioration of the deck over the specified time period.

        :param time_period: The number of time units to simulate and plot.
        """
        conditions = self.simulate_deterioration(time_period)

        plt.figure(figsize=(10, 5))
        plt.plot(range(time_period), conditions, marker='o')
        plt.title('Deck Deterioration Over Time')
        plt.xlabel('Time (units)')
        plt.ylabel('Deck Condition (%)')
        plt.ylim(0, 100)
        plt.grid()
        plt.axhline(0, color='red', linestyle='--', label='Critical Condition')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        simulator = DeckDeteriorationSimulator(initial_condition=100, mold_growth_rate=5, mildew_growth_rate=3, algae_growth_rate=2)
        simulator.plot_deterioration(time_period=20)
    except ValueError as e:
        print(f"Error: {e}")
```
