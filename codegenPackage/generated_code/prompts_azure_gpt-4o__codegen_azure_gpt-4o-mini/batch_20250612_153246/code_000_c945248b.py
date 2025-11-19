"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Write Python code to simulate the METIS Closed Loop System for integrated biomass management and energy recovery, as described on the Metis Investment website.
Generated: DETERMINISTIC_c945248bdad6c309
Batch ID: 20250612_153246
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

class Biomass:
    """Class to represent biomass properties and behaviors."""
    
    def __init__(self, initial_mass, degradation_rate):
        """
        Initialize the biomass with an initial mass and degradation rate.
        
        :param initial_mass: Initial mass of the biomass (in kg)
        :param degradation_rate: Rate of biomass degradation (fraction per time unit)
        """
        self.mass = initial_mass
        self.degradation_rate = degradation_rate

    def degrade(self, time):
        """
        Simulate the degradation of biomass over a given time period.
        
        :param time: Time period over which degradation occurs (in time units)
        """
        self.mass *= (1 - self.degradation_rate) ** time

class EnergyRecovery:
    """Class to simulate energy recovery from biomass."""
    
    def __init__(self, energy_per_kg):
        """
        Initialize the energy recovery system with energy conversion efficiency.
        
        :param energy_per_kg: Energy recovered per kg of biomass (in MJ)
        """
        self.energy_per_kg = energy_per_kg

    def recover_energy(self, biomass_mass):
        """
        Calculate the energy recovered from a given mass of biomass.
        
        :param biomass_mass: Mass of biomass to recover energy from (in kg)
        :return: Energy recovered (in MJ)
        """
        return biomass_mass * self.energy_per_kg

class ClosedLoopSystem:
    """Class to simulate the METIS Closed Loop System for biomass management."""
    
    def __init__(self, initial_biomass_mass, degradation_rate, energy_per_kg):
        """
        Initialize the closed loop system with biomass and energy recovery parameters.
        
        :param initial_biomass_mass: Initial mass of biomass (in kg)
        :param degradation_rate: Rate of biomass degradation (fraction per time unit)
        :param energy_per_kg: Energy recovered per kg of biomass (in MJ)
        """
        self.biomass = Biomass(initial_biomass_mass, degradation_rate)
        self.energy_recovery = EnergyRecovery(energy_per_kg)
        self.time_series = []
        self.energy_series = []

    def simulate(self, total_time, time_step):
        """
        Simulate the closed loop system over a specified total time.
        
        :param total_time: Total time to simulate (in time units)
        :param time_step: Time step for the simulation (in time units)
        """
        for t in np.arange(0, total_time, time_step):
            self.biomass.degrade(time_step)
            energy = self.energy_recovery.recover_energy(self.biomass.mass)
            self.time_series.append(t)
            self.energy_series.append(energy)

    def plot_results(self):
        """Plot the results of the simulation."""
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(self.time_series, [b.mass for b in self.biomass.mass], label='Biomass Mass (kg)')
        plt.title('Biomass Mass Over Time')
        plt.xlabel('Time (units)')
        plt.ylabel('Mass (kg)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.time_series, self.energy_series, label='Energy Recovery (MJ)', color='orange')
        plt.title('Energy Recovery Over Time')
        plt.xlabel('Time (units)')
        plt.ylabel('Energy (MJ)')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Parameters for the simulation
    initial_mass = 1000  # Initial biomass mass in kg
    degradation_rate = 0.05  # 5% degradation per time unit
    energy_per_kg = 20  # 20 MJ per kg of biomass
    total_time = 100  # Total time for simulation
    time_step = 1  # Time step for simulation

    # Create and run the closed loop system simulation
    try:
        closed_loop_system = ClosedLoopSystem(initial_mass, degradation_rate, energy_per_kg)
        closed_loop_system.simulate(total_time, time_step)
        closed_loop_system.plot_results()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
