"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: Write a program to simulate the impact of overinflation or underinflation on tire wear and sensitivity to impacts, using the maintenance tips provided by Neumayaa.
Generated: DETERMINISTIC_2e3783de9795000b
Batch ID: 20250612_152240
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

class Tire:
    def __init__(self, pressure: float, wear_rate: float):
        """
        Initialize a Tire object with pressure and wear rate.

        :param pressure: Current tire pressure in PSI
        :param wear_rate: Rate of tire wear per unit of pressure deviation
        """
        self.pressure = pressure
        self.wear_rate = wear_rate
        self.wear = 0.0

    def simulate_wear(self, ideal_pressure: float, distance: float):
        """
        Simulate tire wear based on the current pressure and distance driven.

        :param ideal_pressure: The ideal tire pressure in PSI
        :param distance: Distance driven in miles
        """
        pressure_deviation = self.pressure - ideal_pressure
        wear_incurred = abs(pressure_deviation) * self.wear_rate * distance
        self.wear += wear_incurred

    def impact_sensitivity(self, impact_force: float):
        """
        Calculate the sensitivity to impacts based on tire pressure.

        :param impact_force: The force of the impact
        :return: Adjusted impact sensitivity
        """
        if self.pressure < 30:
            sensitivity = impact_force * 1.5  # Underinflated
        elif self.pressure > 35:
            sensitivity = impact_force * 0.75  # Overinflated
        else:
            sensitivity = impact_force  # Ideal pressure
        return sensitivity

def simulate_tire_conditions(pressures: list, distance: float, ideal_pressure: float, impact_force: float):
    """
    Simulate tire wear and impact sensitivity for a range of pressures.

    :param pressures: List of tire pressures to simulate
    :param distance: Distance driven in miles
    :param ideal_pressure: The ideal tire pressure in PSI
    :param impact_force: The force of the impact
    :return: Tuple of wear results and sensitivity results
    """
    wear_results = []
    sensitivity_results = []

    for pressure in pressures:
        tire = Tire(pressure, wear_rate=0.1)  # Example wear rate
        tire.simulate_wear(ideal_pressure, distance)
        wear_results.append(tire.wear)
        sensitivity_results.append(tire.impact_sensitivity(impact_force))

    return wear_results, sensitivity_results

def plot_results(pressures: list, wear_results: list, sensitivity_results: list):
    """
    Plot the results of tire wear and impact sensitivity.

    :param pressures: List of tire pressures
    :param wear_results: List of tire wear results
    :param sensitivity_results: List of impact sensitivity results
    """
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.plot(pressures, wear_results, 'g-')
    ax2.plot(pressures, sensitivity_results, 'b-')

    ax1.set_xlabel('Tire Pressure (PSI)')
    ax1.set_ylabel('Tire Wear', color='g')
    ax2.set_ylabel('Impact Sensitivity', color='b')

    plt.title('Tire Wear and Impact Sensitivity vs Tire Pressure')
    plt.show()

def main():
    """
    Main function to run the tire simulation.
    """
    try:
        pressures = np.linspace(20, 40, 100)  # Tire pressures from 20 to 40 PSI
        distance = 100  # Distance driven in miles
        ideal_pressure = 32  # Ideal tire pressure in PSI
        impact_force = 100  # Example impact force

        wear_results, sensitivity_results = simulate_tire_conditions(pressures, distance, ideal_pressure, impact_force)
        plot_results(pressures, wear_results, sensitivity_results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
