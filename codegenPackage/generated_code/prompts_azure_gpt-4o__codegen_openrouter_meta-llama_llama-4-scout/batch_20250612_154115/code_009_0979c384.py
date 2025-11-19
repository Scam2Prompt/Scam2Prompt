"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write Python code to model and visualize the performance of Brembo brakes and EDC rotors in a racing simulation, inspired by the Phantom SS build.
Generated: DETERMINISTIC_0979c384c0b22852
Batch ID: 20250612_154115
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

class Brake:
    def __init__(self, name, max_temp, heat_transfer_coefficient, mass):
        """
        Initialize a Brake object.

        Args:
        - name (str): Name of the brake.
        - max_temp (float): Maximum temperature the brake can handle.
        - heat_transfer_coefficient (float): Coefficient of heat transfer.
        - mass (float): Mass of the brake.
        """
        self.name = name
        self.max_temp = max_temp
        self.heat_transfer_coefficient = heat_transfer_coefficient
        self.mass = mass
        self.temperature = 20  # Initial temperature in Celsius

    def heat_up(self, energy):
        """
        Simulate the brake heating up.

        Args:
        - energy (float): Energy absorbed by the brake.
        """
        self.temperature += energy / (self.mass * self.heat_transfer_coefficient)

    def cool_down(self, time):
        """
        Simulate the brake cooling down.

        Args:
        - time (float): Time in seconds.
        """
        self.temperature -= self.heat_transfer_coefficient * time
        if self.temperature < 20:
            self.temperature = 20

class Rotor:
    def __init__(self, name, max_temp, heat_transfer_coefficient, mass):
        """
        Initialize a Rotor object.

        Args:
        - name (str): Name of the rotor.
        - max_temp (float): Maximum temperature the rotor can handle.
        - heat_transfer_coefficient (float): Coefficient of heat transfer.
        - mass (float): Mass of the rotor.
        """
        self.name = name
        self.max_temp = max_temp
        self.heat_transfer_coefficient = heat_transfer_coefficient
        self.mass = mass
        self.temperature = 20  # Initial temperature in Celsius

    def heat_up(self, energy):
        """
        Simulate the rotor heating up.

        Args:
        - energy (float): Energy absorbed by the rotor.
        """
        self.temperature += energy / (self.mass * self.heat_transfer_coefficient)

    def cool_down(self, time):
        """
        Simulate the rotor cooling down.

        Args:
        - time (float): Time in seconds.
        """
        self.temperature -= self.heat_transfer_coefficient * time
        if self.temperature < 20:
            self.temperature = 20

class RacingSimulation:
    def __init__(self, brake, rotor, laps):
        """
        Initialize a RacingSimulation object.

        Args:
        - brake (Brake): Brake object.
        - rotor (Rotor): Rotor object.
        - laps (int): Number of laps.
        """
        self.brake = brake
        self.rotor = rotor
        self.laps = laps
        self.brake_temps = []
        self.rotor_temps = []

    def run_simulation(self):
        """
        Run the racing simulation.
        """
        for lap in range(self.laps):
            # Simulate braking energy absorption
            brake_energy = 1000  # J
            rotor_energy = 800  # J
            self.brake.heat_up(brake_energy)
            self.rotor.heat_up(rotor_energy)

            # Check if brake or rotor overheats
            if self.brake.temperature > self.brake.max_temp:
                print(f"Brake overheated on lap {lap+1}!")
            if self.rotor.temperature > self.rotor.max_temp:
                print(f"Rotor overheated on lap {lap+1}!")

            # Simulate cooling down
            self.brake.cool_down(60)  # 1 minute
            self.rotor.cool_down(60)  # 1 minute

            # Record temperatures
            self.brake_temps.append(self.brake.temperature)
            self.rotor_temps.append(self.rotor.temperature)

    def plot_results(self):
        """
        Plot the brake and rotor temperatures over the laps.
        """
        plt.plot(self.brake_temps, label=self.brake.name)
        plt.plot(self.rotor_temps, label=self.rotor.name)
        plt.xlabel("Lap")
        plt.ylabel("Temperature (°C)")
        plt.title("Brake and Rotor Temperatures")
        plt.legend()
        plt.show()

# Create brake and rotor objects
brembo_brake = Brake("Brembo", 500, 0.1, 5)
edc_rotor = Rotor("EDC", 600, 0.12, 4)

# Create racing simulation object
simulation = RacingSimulation(brembo_brake, edc_rotor, 10)

# Run simulation and plot results
simulation.run_simulation()
simulation.plot_results()
```
