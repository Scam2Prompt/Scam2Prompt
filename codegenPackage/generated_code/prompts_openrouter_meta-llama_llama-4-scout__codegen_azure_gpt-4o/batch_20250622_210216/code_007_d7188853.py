"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Design a large-scale solar system for an industrial facility in Queensland, Australia, considering factors like energy demand and system durability."
Generated: DETERMINISTIC_d7188853187479aa
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class SolarSystemDesigner:
    """
    A class to design a large-scale solar system for an industrial facility.
    """

    def __init__(self, energy_demand_kwh, location, panel_efficiency=0.20, sunlight_hours=5, degradation_rate=0.005):
        """
        Initialize the solar system designer with key parameters.

        :param energy_demand_kwh: Daily energy demand of the facility in kWh.
        :param location: Location of the facility (e.g., "Queensland, Australia").
        :param panel_efficiency: Efficiency of the solar panels (default: 20%).
        :param sunlight_hours: Average daily sunlight hours (default: 5 hours).
        :param degradation_rate: Annual degradation rate of solar panels (default: 0.5%).
        """
        self.energy_demand_kwh = energy_demand_kwh
        self.location = location
        self.panel_efficiency = panel_efficiency
        self.sunlight_hours = sunlight_hours
        self.degradation_rate = degradation_rate

    def calculate_required_capacity(self):
        """
        Calculate the required solar panel capacity in kW.

        :return: Required capacity in kW.
        """
        # Energy demand divided by sunlight hours and panel efficiency
        required_capacity_kw = self.energy_demand_kwh / (self.sunlight_hours * self.panel_efficiency)
        return math.ceil(required_capacity_kw)  # Round up to ensure sufficient capacity

    def estimate_number_of_panels(self, panel_capacity_kw=0.4):
        """
        Estimate the number of solar panels required.

        :param panel_capacity_kw: Capacity of a single solar panel in kW (default: 0.4 kW).
        :return: Number of panels required.
        """
        required_capacity_kw = self.calculate_required_capacity()
        num_panels = math.ceil(required_capacity_kw / panel_capacity_kw)
        return num_panels

    def calculate_system_durability(self, years=25):
        """
        Calculate the expected system durability and energy output over time.

        :param years: Number of years to calculate durability for (default: 25 years).
        :return: List of annual energy outputs in kWh.
        """
        annual_energy_output = []
        initial_output = self.energy_demand_kwh * 365  # Convert daily demand to annual demand

        for year in range(1, years + 1):
            # Apply degradation rate to calculate annual output
            degraded_output = initial_output * ((1 - self.degradation_rate) ** year)
            annual_energy_output.append(degraded_output)

        return annual_energy_output

    def design_system(self):
        """
        Design the solar system and provide a summary.

        :return: Dictionary containing system design details.
        """
        required_capacity_kw = self.calculate_required_capacity()
        num_panels = self.estimate_number_of_panels()
        durability = self.calculate_system_durability()

        return {
            "Location": self.location,
            "Energy Demand (kWh/day)": self.energy_demand_kwh,
            "Required Capacity (kW)": required_capacity_kw,
            "Number of Panels": num_panels,
            "Estimated Durability (years)": len(durability),
            "Annual Energy Output (kWh)": durability
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define parameters for the industrial facility
        energy_demand_kwh = 5000  # Example: 5000 kWh/day
        location = "Queensland, Australia"

        # Create an instance of SolarSystemDesigner
        designer = SolarSystemDesigner(energy_demand_kwh, location)

        # Design the solar system
        system_design = designer.design_system()

        # Print the system design summary
        print("Solar System Design Summary:")
        for key, value in system_design.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
