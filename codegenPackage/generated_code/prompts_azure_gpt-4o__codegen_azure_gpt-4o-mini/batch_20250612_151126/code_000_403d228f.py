"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Write Python code to simulate the energy savings of installing microturbines, referencing Chico Electric's use of microturbines for distributed power applications.
Generated: DETERMINISTIC_403d228f35d4d72b
Batch ID: 20250612_151126
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

class Microturbine:
    """
    A class to represent a microturbine and its energy savings.
    """

    def __init__(self, capacity_kw, efficiency, operational_hours_per_day):
        """
        Initializes the microturbine with its capacity, efficiency, and operational hours.

        :param capacity_kw: The capacity of the microturbine in kilowatts (kW).
        :param efficiency: The efficiency of the microturbine as a decimal (e.g., 0.85 for 85%).
        :param operational_hours_per_day: The number of hours the microturbine operates per day.
        """
        self.capacity_kw = capacity_kw
        self.efficiency = efficiency
        self.operational_hours_per_day = operational_hours_per_day

    def calculate_daily_energy_output(self):
        """
        Calculates the daily energy output of the microturbine in kilowatt-hours (kWh).

        :return: Daily energy output in kWh.
        """
        return self.capacity_kw * self.efficiency * self.operational_hours_per_day

    def calculate_annual_energy_output(self):
        """
        Calculates the annual energy output of the microturbine in kilowatt-hours (kWh).

        :return: Annual energy output in kWh.
        """
        return self.calculate_daily_energy_output() * 365

def simulate_energy_savings(microturbine, grid_energy_cost_per_kwh):
    """
    Simulates the energy savings from using a microturbine compared to grid energy.

    :param microturbine: An instance of the Microturbine class.
    :param grid_energy_cost_per_kwh: The cost of grid energy per kWh.
    :return: Annual savings in currency.
    """
    try:
        annual_output = microturbine.calculate_annual_energy_output()
        annual_savings = annual_output * grid_energy_cost_per_kwh
        return annual_savings
    except Exception as e:
        print(f"Error during savings calculation: {e}")
        return None

def plot_energy_output(microturbine):
    """
    Plots the daily energy output of the microturbine over a year.

    :param microturbine: An instance of the Microturbine class.
    """
    try:
        days = np.arange(1, 366)
        daily_output = np.full(days.shape, microturbine.calculate_daily_energy_output())
        
        plt.figure(figsize=(10, 5))
        plt.plot(days, daily_output, label='Daily Energy Output (kWh)', color='blue')
        plt.title('Daily Energy Output of Microturbine Over a Year')
        plt.xlabel('Day of the Year')
        plt.ylabel('Energy Output (kWh)')
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

if __name__ == "__main__":
    # Example parameters for the microturbine
    capacity_kw = 30  # Capacity in kW
    efficiency = 0.85  # Efficiency as a decimal
    operational_hours_per_day = 24  # Operational hours per day

    # Create a microturbine instance
    microturbine = Microturbine(capacity_kw, efficiency, operational_hours_per_day)

    # Cost of grid energy per kWh
    grid_energy_cost_per_kwh = 0.12  # Example cost in currency

    # Calculate annual savings
    annual_savings = simulate_energy_savings(microturbine, grid_energy_cost_per_kwh)
    if annual_savings is not None:
        print(f"Annual savings from microturbine: ${annual_savings:.2f}")

    # Plot the energy output
    plot_energy_output(microturbine)
```
