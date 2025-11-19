"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Generate a code snippet that simulates the gradual decrease of staking power over a 52-week lock period for the Polyhedra Network token.
Generated: DETERMINISTIC_c459034843264c39
Batch ID: 20250612_155446
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

class StakingSimulation:
    def __init__(self, initial_stake, weeks=52):
        """
        Initialize the staking simulation with an initial stake and duration.
        
        :param initial_stake: Initial staking power.
        :param weeks: Number of weeks for the staking period.
        """
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        
        if weeks <= 0:
            raise ValueError("Number of weeks must be greater than zero.")

        self.initial_stake = initial_stake
        self.weeks = weeks

    def simulate_decrease(self):
        """
        Simulates the gradual decrease of staking power over the specified number of weeks.
        
        :return: A list of staking power values for each week.
        """
        # Calculate the weekly decay rate
        decay_rate = 1 / self.weeks
        staking_power = [self.initial_stake * (1 - decay_rate * week) for week in range(self.weeks + 1)]
        return staking_power

    def plot_staking_power(self, staking_power):
        """
        Plots the staking power over the weeks.
        
        :param staking_power: List of staking power values for each week.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(range(self.weeks + 1), staking_power, marker='o')
        plt.title('Staking Power Decrease Over 52 Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Staking Power')
        plt.xticks(np.arange(0, self.weeks + 1, step=4))
        plt.grid()
        plt.show()

def main():
    try:
        initial_stake = float(input("Enter the initial staking power: "))
        simulation = StakingSimulation(initial_stake)
        staking_power = simulation.simulate_decrease()
        simulation.plot_staking_power(staking_power)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
