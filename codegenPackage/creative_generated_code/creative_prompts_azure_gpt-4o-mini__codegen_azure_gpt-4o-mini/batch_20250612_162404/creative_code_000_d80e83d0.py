"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Generate a comparison code for a Solar Pump vs Diesel Pump using the specifications from IMB Cambodia Group.
Generated: DETERMINISTIC_d80e83d041ee923c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Pump:
    """Base class for a Pump specification."""

    def __init__(self, name, power_consumption, efficiency, operational_cost, maintenance_cost):
        """
        Initialize a new Pump instance.

        Args:
            name (str): The name of the pump.
            power_consumption (float): Power consumption in kW.
            efficiency (float): Efficiency percentage.
            operational_cost (float): Operational cost per hour.
            maintenance_cost (float): Maintenance cost per year.
        """
        self.name = name
        self.power_consumption = power_consumption
        self.efficiency = efficiency
        self.operational_cost = operational_cost
        self.maintenance_cost = maintenance_cost

    def calculate_yearly_cost(self, hours_per_day, days_per_year):
        """
        Calculate the total yearly cost of running the pump.

        Args:
            hours_per_day (float): Number of hours the pump runs per day.
            days_per_year (int): Number of operational days in a year.

        Returns:
            float: Total yearly cost.
        """
        try:
            operational_hours = hours_per_day * days_per_year
            total_operational_cost = operational_hours * self.operational_cost
            total_maintenance_cost = self.maintenance_cost
            total_cost = total_operational_cost + total_maintenance_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating yearly cost for {self.name}: {e}")
            return None


class SolarPump(Pump):
    """Class representing a Solar Pump."""

    def __init__(self, name, power_consumption, efficiency, operational_cost, maintenance_cost, solar_panel_area):
        """
        Initialize a new SolarPump instance.

        Args:
            name (str): The name of the solar pump.
            power_consumption (float): Power consumption in kW.
            efficiency (float): Efficiency percentage.
            operational_cost (float): Operational cost per hour.
            maintenance_cost (float): Maintenance cost per year.
            solar_panel_area (float): Area of solar panels in square meters.
        """
        super().__init__(name, power_consumption, efficiency, operational_cost, maintenance_cost)
        self.solar_panel_area = solar_panel_area


class DieselPump(Pump):
    """Class representing a Diesel Pump."""

    def __init__(self, name, power_consumption, efficiency, operational_cost, maintenance_cost, fuel_type):
        """
        Initialize a new DieselPump instance.

        Args:
            name (str): The name of the diesel pump.
            power_consumption (float): Power consumption in kW.
            efficiency (float): Efficiency percentage.
            operational_cost (float): Operational cost per hour.
            maintenance_cost (float): Maintenance cost per year.
            fuel_type (str): Type of diesel fuel used.
        """
        super().__init__(name, power_consumption, efficiency, operational_cost, maintenance_cost)
        self.fuel_type = fuel_type


def compare_pumps(solar_pump, diesel_pump, hours_per_day, days_per_year):
    """
    Compare two pumps based on yearly operational costs.

    Args:
        solar_pump (SolarPump): The solar pump instance.
        diesel_pump (DieselPump): The diesel pump instance.
        hours_per_day (float): Number of hours pumps run per day.
        days_per_year (int): Number of operational days in a year.

    Returns:
        dict: Comparison results containing yearly costs.
    """
    try:
        solar_cost = solar_pump.calculate_yearly_cost(hours_per_day, days_per_year)
        diesel_cost = diesel_pump.calculate_yearly_cost(hours_per_day, days_per_year)
        
        return {
            "Solar Pump": {
                "Name": solar_pump.name,
                "Yearly Cost": solar_cost
            },
            "Diesel Pump": {
                "Name": diesel_pump.name,
                "Yearly Cost": diesel_cost
            }
        }
    except Exception as e:
        print(f"Error comparing pumps: {e}")
        return None


# Example pump specifications based on IMB Cambodia Group
solar_pump = SolarPump(name="Solar Pump A", power_consumption=5.0, efficiency=85, operational_cost=0.5, maintenance_cost=300, solar_panel_area=30)
diesel_pump = DieselPump(name="Diesel Pump B", power_consumption=7.5, efficiency=80, operational_cost=1.0, maintenance_cost=500, fuel_type="Diesel")

# Compare pumps with operational parameters
comparison_results = compare_pumps(solar_pump, diesel_pump, hours_per_day=8, days_per_year=300)

# Display comparison results
if comparison_results:
    for pump_type, details in comparison_results.items():
        print(f"{pump_type}: {details}")
```
