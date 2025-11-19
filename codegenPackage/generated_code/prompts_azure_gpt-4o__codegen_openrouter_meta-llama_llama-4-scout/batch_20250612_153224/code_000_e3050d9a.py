"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write Python code to calculate energy savings for a residential photovoltaic solar system based on the specifications provided by Nexe Energetic's autoconsumo solutions.
Generated: DETERMINISTIC_e3050d9ae3747459
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Residential Photovoltaic Solar System Energy Savings Calculator

This script calculates the energy savings for a residential photovoltaic solar system
based on the specifications provided by Nexe Energetic's autoconsumo solutions.
"""

import math

class SolarSystem:
    def __init__(self, 
                 system_capacity_kw, 
                 system_efficiency, 
                 location_solar_irradiance_kwh_m2_year, 
                 annual_energy_consumption_kwh, 
                 load_factor):
        """
        Initialize a SolarSystem object.

        Args:
        - system_capacity_kw (float): The capacity of the solar system in kW.
        - system_efficiency (float): The efficiency of the solar system.
        - location_solar_irradiance_kwh_m2_year (float): The solar irradiance in kWh/m²/year.
        - annual_energy_consumption_kwh (float): The annual energy consumption in kWh.
        - load_factor (float): The load factor of the system.
        """
        self.system_capacity_kw = system_capacity_kw
        self.system_efficiency = system_efficiency
        self.location_solar_irradiance_kwh_m2_year = location_solar_irradiance_kwh_m2_year
        self.annual_energy_consumption_kwh = annual_energy_consumption_kwh
        self.load_factor = load_factor

    def calculate_annual_energy_production_kwh(self):
        """
        Calculate the annual energy production of the solar system in kWh.

        Returns:
        - float: The annual energy production in kWh.
        """
        # Assume a standard solar panel area of 1.6 m²/kW
        solar_panel_area_m2_kw = 1.6

        # Calculate the total solar panel area
        total_solar_panel_area_m2 = self.system_capacity_kw * solar_panel_area_m2_kw

        # Calculate the annual energy production
        annual_energy_production_kwh = total_solar_panel_area_m2 * self.location_solar_irradiance_kwh_m2_year * self.system_efficiency

        return annual_energy_production_kwh

    def calculate_energy_savings(self):
        """
        Calculate the energy savings of the solar system.

        Returns:
        - float: The energy savings in kWh and percentage.
        """
        annual_energy_production_kwh = self.calculate_annual_energy_production_kwh()

        # Calculate the energy savings in kWh
        energy_savings_kwh = min(annual_energy_production_kwh, self.annual_energy_consumption_kwh)

        # Calculate the energy savings in percentage
        energy_savings_percentage = (energy_savings_kwh / self.annual_energy_consumption_kwh) * 100 if self.annual_energy_consumption_kwh > 0 else 0

        return energy_savings_kwh, energy_savings_percentage

    def calculate_peak_sun_hours(self):
        """
        Calculate the peak sun hours.

        Returns:
        - float: The peak sun hours.
        """
        # Assume a standard solar irradiance of 1000 W/m²
        standard_solar_irradiance_w_m2 = 1000

        # Calculate the peak sun hours
        peak_sun_hours = self.location_solar_irradiance_kwh_m2_year / standard_solar_irradiance_w_m2 * 1000

        return peak_sun_hours


def main():
    try:
        # Example usage:
        system_capacity_kw = 5  # kW
        system_efficiency = 0.20  # 20%
        location_solar_irradiance_kwh_m2_year = 1800  # kWh/m²/year
        annual_energy_consumption_kwh = 6000  # kWh
        load_factor = 0.5  # 50%

        solar_system = SolarSystem(system_capacity_kw, 
                                   system_efficiency, 
                                   location_solar_irradiance_kwh_m2_year, 
                                   annual_energy_consumption_kwh, 
                                   load_factor)

        annual_energy_production_kwh = solar_system.calculate_annual_energy_production_kwh()
        energy_savings_kwh, energy_savings_percentage = solar_system.calculate_energy_savings()
        peak_sun_hours = solar_system.calculate_peak_sun_hours()

        print(f"Annual Energy Production: {annual_energy_production_kwh:.2f} kWh")
        print(f"Energy Savings: {energy_savings_kwh:.2f} kWh ({energy_savings_percentage:.2f}%)")
        print(f"Peak Sun Hours: {peak_sun_hours:.2f} hours")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
