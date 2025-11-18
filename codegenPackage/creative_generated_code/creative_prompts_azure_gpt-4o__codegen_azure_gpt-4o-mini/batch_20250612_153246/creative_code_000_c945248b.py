"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-investment.gr
Prompt: Write Python code to simulate the METIS Closed Loop System for integrated biomass management and energy recovery, as described on the Metis Investment website.
Generated: DETERMINISTIC_c945248bdad6c309
Batch ID: 20250612_153246
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

class BiomassManagementSystem:
    """
    A class to represent a closed-loop system for integrated biomass management
    and energy recovery.
    """

    def __init__(self, initial_biomass, degradation_rate, energy_conversion_efficiency):
        """
        Initializes the BiomassManagementSystem with the given parameters.

        Parameters:
        initial_biomass (float): The initial amount of biomass (in tons).
        degradation_rate (float): The rate at which biomass degrades (as a fraction per time unit).
        energy_conversion_efficiency (float): The efficiency of converting biomass to energy (as a fraction).
        """
        self.biomass = initial_biomass
        self.degradation_rate = degradation_rate
        self.energy_conversion_efficiency = energy_conversion_efficiency
        self.energy_generated = 0

    def degrade_biomass(self, time_units):
        """
        Simulates the degradation of biomass over a specified number of time units.

        Parameters:
        time_units (int): The number of time units to simulate.
        """
        for _ in range(time_units):
            if self.biomass > 0:
                self.biomass -= self.biomass * self.degradation_rate
            else:
                self.biomass = 0
                break

    def convert_to_energy(self):
        """
        Converts the remaining biomass into energy, updating the energy generated.
        """
        energy = self.biomass * self.energy_conversion_efficiency
        self.energy_generated += energy
        self.biomass = 0  # Biomass is fully converted

    def simulate(self, time_units):
        """
        Runs the simulation for a specified number of time units.

        Parameters:
        time_units (int): The total number of time units for the simulation.
        """
        biomass_history = []
        energy_history = []

        for t in range(time_units):
            self.degrade_biomass(1)
            biomass_history.append(self.biomass)
            self.convert_to_energy()
            energy_history.append(self.energy_generated)

        return biomass_history, energy_history

    def plot_results(self, biomass_history, energy_history):
        """
        Plots the results of the simulation showing biomass over time and energy generated.

        Parameters:
        biomass_history (list): The history of biomass amounts over time.
        energy_history (list): The history of energy generated over time.
        """
        time = np.arange(len(biomass_history))

        plt.figure(figsize=(14, 6))

        plt.subplot(1, 2, 1)
        plt.plot(time, biomass_history, label='Biomass (tons)', color='green')
        plt.title('Biomass Degradation Over Time')
        plt.xlabel('Time Units')
        plt.ylabel('Biomass (tons)')
        plt.grid()
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(time, energy_history, label='Energy Generated (MJ)', color='orange')
        plt.title('Energy Generation Over Time')
        plt.xlabel('Time Units')
        plt.ylabel('Energy Generated (MJ)')
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    try:
        # Initialize the Biomass Management System with example parameters
        initial_biomass = 100.0  # Initial biomass in tons
        degradation_rate = 0.05    # 5% degradation per time unit
        energy_conversion_efficiency = 0.8  # 80% conversion efficiency

        # Create the system instance
        bms = BiomassManagementSystem(initial_biomass, degradation_rate, energy_conversion_efficiency)

        # Run the simulation for a specified number of time units
        simulation_time_units = 20
        biomass_history, energy_history = bms.simulate(simulation_time_units)

        # Plot the results
        bms.plot_results(biomass_history, energy_history)

    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
