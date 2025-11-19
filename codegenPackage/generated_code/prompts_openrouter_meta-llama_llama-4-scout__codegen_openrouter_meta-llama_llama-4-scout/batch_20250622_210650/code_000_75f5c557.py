"""
Generated Code Metadata:
========================
Original URL: https://universalsolar1.com
Prompt: Write a Python code snippet to calculate the potential profitability of a large-scale solar project using data from Universal Solar's services.
Generated: DETERMINISTIC_75f5c557577f6157
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_project_profitability_calculator.py

import pandas as pd

class SolarProjectProfitabilityCalculator:
    """
    Calculates the potential profitability of a large-scale solar project.

    Attributes:
        project_capacity (float): The capacity of the solar project in MW.
        solar_irradiance (float): The solar irradiance in kW/m².
        panel_efficiency (float): The efficiency of the solar panels.
        installation_cost (float): The installation cost per watt.
        maintenance_cost (float): The annual maintenance cost per watt.
        electricity_price (float): The price of electricity per kWh.
    """

    def __init__(self, project_capacity, solar_irradiance, panel_efficiency, 
                 installation_cost, maintenance_cost, electricity_price):
        """
        Initializes the calculator with the given parameters.

        Args:
            project_capacity (float): The capacity of the solar project in MW.
            solar_irradiance (float): The solar irradiance in kW/m².
            panel_efficiency (float): The efficiency of the solar panels.
            installation_cost (float): The installation cost per watt.
            maintenance_cost (float): The annual maintenance cost per watt.
            electricity_price (float): The price of electricity per kWh.
        """
        self.project_capacity = project_capacity  # in MW
        self.solar_irradiance = solar_irradiance  # in kW/m²
        self.panel_efficiency = panel_efficiency  # in percentage
        self.installation_cost = installation_cost  # in $/W
        self.maintenance_cost = maintenance_cost  # in $/W/year
        self.electricity_price = electricity_price  # in $/kWh

    def calculate_annual_energy_production(self):
        """
        Calculates the annual energy production of the solar project.

        Returns:
            float: The annual energy production in kWh.
        """
        # Assume 8760 hours per year
        annual_hours = 8760
        # Calculate the total capacity in watts
        total_capacity = self.project_capacity * 1e6  # Convert MW to W
        # Calculate the annual energy production
        annual_energy_production = total_capacity * self.panel_efficiency / 100 * self.solar_irradiance * annual_hours / 1000  # in kWh
        return annual_energy_production

    def calculate_installation_cost_total(self):
        """
        Calculates the total installation cost of the solar project.

        Returns:
            float: The total installation cost in $.
        """
        # Calculate the total capacity in watts
        total_capacity = self.project_capacity * 1e6  # Convert MW to W
        # Calculate the total installation cost
        installation_cost_total = total_capacity * self.installation_cost
        return installation_cost_total

    def calculate_maintenance_cost_total(self, years):
        """
        Calculates the total maintenance cost of the solar project over the given years.

        Args:
            years (int): The number of years.

        Returns:
            float: The total maintenance cost in $.
        """
        # Calculate the total capacity in watts
        total_capacity = self.project_capacity * 1e6  # Convert MW to W
        # Calculate the total maintenance cost
        maintenance_cost_total = total_capacity * self.maintenance_cost * years
        return maintenance_cost_total

    def calculate_revenue(self, years):
        """
        Calculates the total revenue of the solar project over the given years.

        Args:
            years (int): The number of years.

        Returns:
            float: The total revenue in $.
        """
        # Calculate the annual energy production
        annual_energy_production = self.calculate_annual_energy_production()
        # Calculate the total revenue
        total_revenue = annual_energy_production * self.electricity_price * years
        return total_revenue

    def calculate_profitability(self, years):
        """
        Calculates the profitability of the solar project over the given years.

        Args:
            years (int): The number of years.

        Returns:
            dict: A dictionary containing the profitability metrics.
        """
        # Calculate the total installation cost
        installation_cost_total = self.calculate_installation_cost_total()
        # Calculate the total maintenance cost
        maintenance_cost_total = self.calculate_maintenance_cost_total(years)
        # Calculate the total revenue
        total_revenue = self.calculate_revenue(years)
        # Calculate the net present value (NPV)
        npv = total_revenue - installation_cost_total - maintenance_cost_total
        # Calculate the return on investment (ROI)
        roi = (total_revenue - installation_cost_total - maintenance_cost_total) / installation_cost_total * 100
        # Return the profitability metrics
        return {
            'installation_cost': installation_cost_total,
            'maintenance_cost': maintenance_cost_total,
            'revenue': total_revenue,
            'npv': npv,
            'roi': roi
        }


def main():
    try:
        # Example usage
        calculator = SolarProjectProfitabilityCalculator(
            project_capacity=10,  # in MW
            solar_irradiance=1.8,  # in kW/m²
            panel_efficiency=20,  # in percentage
            installation_cost=1.2,  # in $/W
            maintenance_cost=0.01,  # in $/W/year
            electricity_price=0.15  # in $/kWh
        )
        years = 25
        profitability = calculator.calculate_profitability(years)
        print("Profitability Metrics:")
        for metric, value in profitability.items():
            print(f"{metric.capitalize()}: ${value:,.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
