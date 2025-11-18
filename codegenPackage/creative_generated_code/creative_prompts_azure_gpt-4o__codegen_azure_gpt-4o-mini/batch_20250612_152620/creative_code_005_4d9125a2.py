"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Write code to calculate the energy output of a solar system using specifications for Tier 1 solar panels and smart inverter technology, as detailed by Big Sky Energy.
Generated: DETERMINISTIC_4d9125a2e1f41a68
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarSystem:
    """
    A class to represent a solar energy system.

    Attributes:
        panel_count (int): Number of solar panels in the system.
        panel_efficiency (float): Efficiency of each solar panel (as a decimal).
        inverter_efficiency (float): Efficiency of the inverter (as a decimal).
        sunlight_hours (float): Average number of sunlight hours per day.
    """

    def __init__(self, panel_count: int, panel_efficiency: float, inverter_efficiency: float, sunlight_hours: float):
        """
        Initializes the SolarSystem with the given specifications.

        Args:
            panel_count (int): Number of solar panels.
            panel_efficiency (float): Efficiency of the solar panels.
            inverter_efficiency (float): Efficiency of the inverter.
            sunlight_hours (float): Average sunlight hours per day.

        Raises:
            ValueError: If any parameter is invalid (e.g., negative values).
        """
        if panel_count <= 0:
            raise ValueError("Panel count must be a positive integer.")
        if not (0 <= panel_efficiency <= 1):
            raise ValueError("Panel efficiency must be between 0 and 1.")
        if not (0 <= inverter_efficiency <= 1):
            raise ValueError("Inverter efficiency must be between 0 and 1.")
        if sunlight_hours <= 0:
            raise ValueError("Sunlight hours must be a positive number.")

        self.panel_count = panel_count
        self.panel_efficiency = panel_efficiency
        self.inverter_efficiency = inverter_efficiency
        self.sunlight_hours = sunlight_hours

    def calculate_energy_output(self) -> float:
        """
        Calculate the daily energy output of the solar system.

        Returns:
            float: The estimated daily energy output in kilowatt-hours (kWh).
        """
        # Assume each panel has a capacity of 300 Watts (0.3 kW)
        panel_capacity_kw = 0.3 

        # Total energy produced by panels (kWh)
        total_energy_produced = self.panel_count * panel_capacity_kw * self.sunlight_hours

        # Adjust for inverter efficiency
        energy_output = total_energy_produced * self.inverter_efficiency

        return energy_output


def main():
    """
    Main function to run the solar energy system calculation.
    """
    try:
        # Example values for a solar system
        panel_count = 20
        panel_efficiency = 0.20  # Tier 1 panels typically around 20% efficiency
        inverter_efficiency = 0.95  # Smart inverters around 95% efficiency
        sunlight_hours = 5  # Average sunlight hours per day

        # Create a SolarSystem object
        solar_system = SolarSystem(panel_count, panel_efficiency, inverter_efficiency, sunlight_hours)

        # Calculate and display the energy output
        energy_output = solar_system.calculate_energy_output()
        print(f"Estimated daily energy output: {energy_output:.2f} kWh")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
