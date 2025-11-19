"""
Generated Code Metadata:
========================
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Generate a code snippet that simulates the gradual decrease of staking power over a 52-week lock period for the Polyhedra Network token.
Generated: DETERMINISTIC_c459034843264c39
Batch ID: 20250612_155446
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

class StakingPowerSimulator:
    def __init__(self, initial_power: float, lock_period_weeks: int = 52):
        """
        Initializes the StakingPowerSimulator with the initial staking power and lock period.

        :param initial_power: The initial staking power (in tokens).
        :param lock_period_weeks: The duration of the lock period in weeks (default is 52).
        """
        if initial_power <= 0:
            raise ValueError("Initial staking power must be greater than zero.")
        if lock_period_weeks <= 0:
            raise ValueError("Lock period must be a positive integer.")

        self.initial_power = initial_power
        self.lock_period_weeks = lock_period_weeks
        self.staking_power_over_time = []

    def simulate_decrease(self):
        """
        Simulates the gradual decrease of staking power over the lock period.
        The staking power decreases linearly to zero over the specified number of weeks.
        """
        for week in range(self.lock_period_weeks + 1):
            # Calculate the current staking power
            current_power = self.initial_power * (1 - week / self.lock_period_weeks)
            self.staking_power_over_time.append(current_power)

    def plot_staking_power(self):
        """
        Plots the staking power over the lock period.
        """
        weeks = np.arange(0, self.lock_period_weeks + 1)
        plt.figure(figsize=(10, 5))
        plt.plot(weeks, self.staking_power_over_time, marker='o')
        plt.title('Staking Power Decrease Over 52 Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Staking Power (Tokens)')
        plt.xticks(weeks)
        plt.grid()
        plt.axhline(0, color='red', linestyle='--', linewidth=0.8)
        plt.show()

if __name__ == "__main__":
    try:
        # Initialize the simulator with an initial staking power of 100 tokens
        simulator = StakingPowerSimulator(initial_power=100)
        # Simulate the decrease in staking power
        simulator.simulate_decrease()
        # Plot the results
        simulator.plot_staking_power()
    except ValueError as e:
        print(f"Error: {e}")
```
