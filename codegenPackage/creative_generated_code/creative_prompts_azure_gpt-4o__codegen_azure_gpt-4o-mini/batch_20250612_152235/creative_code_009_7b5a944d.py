"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Write a script to calculate the expected lifecycle of AlphaTest µ HELIX ® probes in aerospace component testing, considering their ability to last hundreds of thousands of test cycles.
Generated: DETERMINISTIC_7b5a944d0299b715
Batch ID: 20250612_152235
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

class ProbeLifecycleCalculator:
    """
    Class to calculate and visualize the expected lifecycle of AlphaTest µ HELIX ® probes
    in aerospace component testing.
    """

    def __init__(self, initial_cycles: int, failure_rate: float, max_cycles: int):
        """
        Initializes the calculator with the specified parameters.

        :param initial_cycles: The initial number of test cycles (e.g., 0)
        :param failure_rate: The probability of failure per cycle (between 0 and 1)
        :param max_cycles: The maximum test cycles to consider for lifecycle analysis
        """
        if not (0 <= failure_rate <= 1):
            raise ValueError("Failure rate must be between 0 and 1.")
        if initial_cycles < 0 or max_cycles < 0:
            raise ValueError("Cycle counts must be non-negative.")

        self.initial_cycles = initial_cycles
        self.failure_rate = failure_rate
        self.max_cycles = max_cycles

    def expected_lifetime(self) -> float:
        """
        Calculate the expected lifetime of the probe based on the failure rate.

        :return: The expected number of test cycles the probe can endure before failure.
        """
        if self.failure_rate == 0:
            return float('inf')  # Infinite lifetime if failure rate is zero

        expected_lifetime = 1 / self.failure_rate
        return min(expected_lifetime, self.max_cycles)

    def simulate_lifecycle(self, num_simulations: int = 1000) -> np.ndarray:
        """
        Simulate the lifecycle of the probes over a number of cycles.

        :param num_simulations: Number of simulations to run
        :return: An array of the number of cycles at which each probe fails
        """
        failures = np.random.geometric(self.failure_rate, num_simulations)
        return np.clip(failures + self.initial_cycles, self.initial_cycles, self.max_cycles)

    def plot_lifecycle_distribution(self, num_simulations: int = 1000):
        """
        Plot the distribution of probe failures over the simulated lifecycle.

        :param num_simulations: Number of simulations to run for plotting
        """
        failures = self.simulate_lifecycle(num_simulations)
        plt.hist(failures, bins=50, color='blue', alpha=0.7, edgecolor='black')
        plt.title('Probe Lifecycle Distribution')
        plt.xlabel('Number of Test Cycles')
        plt.ylabel('Number of Failures')
        plt.xlim(self.initial_cycles, self.max_cycles)
        plt.grid(axis='y', linestyle='--')
        plt.show()

if __name__ == "__main__":
    try:
        # Sample usage
        initial_cycles = 0
        failure_rate = 0.0001  # Example failure rate
        max_cycles = 1000000    # Max test cycles to consider

        probe_calculator = ProbeLifecycleCalculator(initial_cycles, failure_rate, max_cycles)

        expected_lifetime = probe_calculator.expected_lifetime()
        print(f"Expected Lifetime of Probe: {expected_lifetime:.2f} cycles")

        probe_calculator.plot_lifecycle_distribution()
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
