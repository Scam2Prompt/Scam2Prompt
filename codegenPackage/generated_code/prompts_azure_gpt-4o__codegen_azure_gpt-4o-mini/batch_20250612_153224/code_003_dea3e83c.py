"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Write code in Python to simulate the impact of repeated ankle sprains on long-term mobility, using a biomechanics library or API.
Generated: DETERMINISTIC_dea3e83c1545eb0b
Batch ID: 20250612_153224
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

class AnkleSprainSimulator:
    """
    A class to simulate the impact of repeated ankle sprains on long-term mobility.
    """

    def __init__(self, initial_mobility: float, sprain_effect: float, recovery_rate: float):
        """
        Initializes the simulator with initial mobility, sprain effect, and recovery rate.

        :param initial_mobility: Initial mobility score (0 to 100)
        :param sprain_effect: Mobility reduction per sprain (0 to 100)
        :param recovery_rate: Rate of recovery after each sprain (0 to 1)
        """
        self.initial_mobility = initial_mobility
        self.sprain_effect = sprain_effect
        self.recovery_rate = recovery_rate
        self.mobility_history = []

    def simulate_sprains(self, num_sprains: int):
        """
        Simulates the impact of repeated ankle sprains on mobility.

        :param num_sprains: Number of sprains to simulate
        """
        current_mobility = self.initial_mobility

        for i in range(num_sprains):
            # Apply the effect of the sprain
            current_mobility -= self.sprain_effect
            current_mobility = max(current_mobility, 0)  # Mobility cannot go below 0

            # Record the current mobility
            self.mobility_history.append(current_mobility)

            # Apply recovery after the sprain
            current_mobility += (self.initial_mobility - current_mobility) * self.recovery_rate

    def plot_mobility(self):
        """
        Plots the mobility history over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.mobility_history, marker='o')
        plt.title('Mobility Over Time with Repeated Ankle Sprains')
        plt.xlabel('Number of Sprains')
        plt.ylabel('Mobility Score')
        plt.ylim(0, self.initial_mobility)
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the ankle sprain simulation.
    """
    try:
        # Parameters for the simulation
        initial_mobility = 100.0  # Starting mobility score
        sprain_effect = 15.0       # Mobility reduction per sprain
        recovery_rate = 0.2        # Recovery rate after each sprain

        # Create an instance of the simulator
        simulator = AnkleSprainSimulator(initial_mobility, sprain_effect, recovery_rate)

        # Simulate a specified number of sprains
        num_sprains = 10
        simulator.simulate_sprains(num_sprains)

        # Plot the results
        simulator.plot_mobility()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
