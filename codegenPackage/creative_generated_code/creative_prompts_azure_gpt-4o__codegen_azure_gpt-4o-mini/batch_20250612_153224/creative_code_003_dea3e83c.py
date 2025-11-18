"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Write code in Python to simulate the impact of repeated ankle sprains on long-term mobility, using a biomechanics library or API.
Generated: DETERMINISTIC_dea3e83c1545eb0b
Batch ID: 20250612_153224
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

class AnkleSprainSimulator:
    """
    A class to simulate the impact of repeated ankle sprains on long-term mobility.
    
    Attributes:
        initial_mobility (float): Initial mobility score (0 to 100).
        sprain_effect (float): Mobility reduction per ankle sprain.
        recovery_rate (float): Mobility recovery rate per time unit.
        total_sprains (int): Total number of sprains experienced.
        simulation_time (int): Total time to simulate mobility over.
    """

    def __init__(self, initial_mobility=100, sprain_effect=10, recovery_rate=1, total_sprains=5, simulation_time=50):
        """
        Initializes the AnkleSprainSimulator with parameters.
        
        Args:
            initial_mobility (float): Initial mobility score.
            sprain_effect (float): Mobility decrease per sprain.
            recovery_rate (float): Rate of mobility recovery per time unit.
            total_sprains (int): Number of ankle sprains to simulate.
            simulation_time (int): Duration of the simulation.
        """
        self.initial_mobility = initial_mobility
        self.sprain_effect = sprain_effect
        self.recovery_rate = recovery_rate
        self.total_sprains = total_sprains
        self.simulation_time = simulation_time
        self.mobility_history = []

    def simulate(self):
        """Runs the simulation of repeated ankle sprains and tracks mobility over time."""
        current_mobility = self.initial_mobility

        for time in range(self.simulation_time):
            # Apply recovery
            current_mobility = min(current_mobility + self.recovery_rate, self.initial_mobility)

            # Apply the effect of ankle sprains at regular intervals
            if time > 0 and time % (self.simulation_time // self.total_sprains) == 0:
                current_mobility -= self.sprain_effect

            # Ensure mobility does not fall below zero
            current_mobility = max(current_mobility, 0)

            # Record mobility state
            self.mobility_history.append(current_mobility)

    def plot_mobility(self):
        """Plots the mobility changes over the simulation time."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.mobility_history, label='Mobility Score', color='blue')
        plt.title('Impact of Repeated Ankle Sprains on Mobility Over Time')
        plt.xlabel('Time (units)')
        plt.ylabel('Mobility Score (0 to 100)')
        plt.ylim(0, self.initial_mobility + 10)
        plt.axhline(y=0, color='red', linestyle='--', label='No Mobility')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    try:
        # Initialize the simulator with custom parameters
        simulator = AnkleSprainSimulator(initial_mobility=100, sprain_effect=10, recovery_rate=1, total_sprains=5, simulation_time=50)
        
        # Run the simulation
        simulator.simulate()
        
        # Plot the results
        simulator.plot_mobility()
    
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
