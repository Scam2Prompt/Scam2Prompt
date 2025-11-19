"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write a script to calculate the expected lifecycle of AlphaTest µ HELIX ® probes in aerospace component testing, considering their ability to last hundreds of thousands of test cycles.
Generated: DETERMINISTIC_7b5a944d0299b715
Batch ID: 20250612_152235
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

class AlphaTestHelixProbe:
    """
    A class to represent an AlphaTest µ HELIX ® probe and calculate its expected lifecycle
    based on test cycles and failure rates.
    """

    def __init__(self, initial_cycles: int, failure_rate: float):
        """
        Initializes the probe with the given parameters.

        :param initial_cycles: The initial number of test cycles the probe can withstand.
        :param failure_rate: The probability of failure per test cycle (0 < failure_rate < 1).
        """
        if initial_cycles <= 0:
            raise ValueError("Initial cycles must be a positive integer.")
        if not (0 < failure_rate < 1):
            raise ValueError("Failure rate must be between 0 and 1.")

        self.initial_cycles = initial_cycles
        self.failure_rate = failure_rate

    def expected_lifecycle(self) -> float:
        """
        Calculates the expected lifecycle of the probe based on the initial cycles and failure rate.

        :return: The expected number of cycles before failure.
        """
        expected_cycles = self.initial_cycles * (1 - self.failure_rate)
        return expected_cycles

    def simulate_lifecycle(self, num_simulations: int) -> np.ndarray:
        """
        Simulates the lifecycle of the probe over a number of test cycles.

        :param num_simulations: The number of simulations to run.
        :return: An array of simulated lifecycles.
        """
        if num_simulations <= 0:
            raise ValueError("Number of simulations must be a positive integer.")

        lifecycles = np.random.binomial(self.initial_cycles, 1 - self.failure_rate, num_simulations)
        return lifecycles

    def plot_lifecycle_distribution(self, num_simulations: int):
        """
        Plots the distribution of the probe's lifecycle based on simulations.

        :param num_simulations: The number of simulations to run for the plot.
        """
        lifecycles = self.simulate_lifecycle(num_simulations)
        plt.hist(lifecycles, bins=30, alpha=0.7, color='blue', edgecolor='black')
        plt.title('Distribution of AlphaTest µ HELIX ® Probe Lifecycles')
        plt.xlabel('Number of Cycles')
        plt.ylabel('Frequency')
        plt.axvline(self.expected_lifecycle(), color='red', linestyle='dashed', linewidth=1, label='Expected Lifecycle')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the probe with 100000 cycles and a failure rate of 0.001
        probe = AlphaTestHelixProbe(initial_cycles=100000, failure_rate=0.001)

        # Calculate and print the expected lifecycle
        expected_cycles = probe.expected_lifecycle()
        print(f"Expected Lifecycle: {expected_cycles:.2f} cycles")

        # Plot the lifecycle distribution with 1000 simulations
        probe.plot_lifecycle_distribution(num_simulations=1000)

    except ValueError as e:
        print(f"Error: {e}")
```
