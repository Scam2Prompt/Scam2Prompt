"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Write a program to simulate the impact of overinflation or underinflation on tire wear and sensitivity to impacts, using the maintenance tips provided by Neumayaa.
Generated: DETERMINISTIC_2e3783de9795000b
Batch ID: 20250612_152240
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

class Tire:
    def __init__(self, pressure: float, wear_rate: float):
        """
        Initialize a Tire object with pressure and wear rate.

        :param pressure: Current tire pressure in PSI
        :param wear_rate: Rate of tire wear per impact
        """
        self.pressure = pressure
        self.wear_rate = wear_rate
        self.wear = 0

    def apply_impact(self, impact_force: float):
        """
        Simulate the impact on the tire which affects its wear.

        :param impact_force: Force of the impact
        """
        # Calculate sensitivity based on pressure
        sensitivity = self.calculate_sensitivity()
        # Update wear based on wear rate and sensitivity
        self.wear += self.wear_rate * (impact_force / sensitivity)

    def calculate_sensitivity(self) -> float:
        """
        Calculate the tire's sensitivity based on its pressure.

        :return: Sensitivity factor
        """
        if self.pressure < 30:
            return 2.0  # Underinflated sensitivity
        elif self.pressure > 35:
            return 0.5  # Overinflated sensitivity
        return 1.0  # Properly inflated sensitivity

    def get_wear(self) -> float:
        """
        Get the current wear of the tire.

        :return: Current wear
        """
        return self.wear

def simulate_tire_performance(initial_pressure: float, impact_sequence: list):
    """
    Simulate the tire performance over a sequence of impacts.

    :param initial_pressure: Starting pressure of the tire
    :param impact_sequence: List of impact forces
    :return: List of tire wear after each impact
    """
    tire = Tire(initial_pressure, wear_rate=0.1)  # Initialize tire with a wear rate of 0.1
    wear_history = []

    for impact in impact_sequence:
        tire.apply_impact(impact)
        wear_history.append(tire.get_wear())

    return wear_history

def plot_results(impact_sequence: list, wear_history: list):
    """
    Plot the results of the tire wear simulation.

    :param impact_sequence: List of impact forces
    :param wear_history: List of tire wear measurements
    """
    plt.figure(figsize=(10, 5))
    plt.plot(impact_sequence, wear_history, marker='o')
    plt.title('Tire Wear Simulation')
    plt.xlabel('Impact Force')
    plt.ylabel('Tire Wear')
    plt.grid()
    plt.show()

def main():
    """
    Main function to execute the simulation with user-defined inputs.
    """
    try:
        initial_pressure = float(input("Enter the initial tire pressure (PSI): "))
        impact_sequence = list(map(float, input("Enter a sequence of impact forces (comma-separated): ").split(',')))

        if initial_pressure < 0 or any(force < 0 for force in impact_sequence):
            raise ValueError("Pressure and impact forces must be non-negative.")

        wear_history = simulate_tire_performance(initial_pressure, impact_sequence)
        plot_results(impact_sequence, wear_history)

    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
```
