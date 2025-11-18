"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Write Python code to calculate the energy savings and carbon footprint reduction for a business implementing "islas energéticas" as described on the Digar Green website. Include parameters for renewable energy sources like solar and wind.
Generated: DETERMINISTIC_f3d21385dafd13a9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging for error handling and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class EnergyIsland:
    """
    Class to represent an Energy Island system and calculate energy savings 
    and carbon footprint reduction for a business implementing renewable energy.
    """

    def __init__(self, solar_capacity_kw: float, wind_capacity_kw: float, 
                 hours_of_sun_per_day: float, wind_hours_per_day: float,
                 emissions_per_kwh_grid: float):
        """
        Initialize the Energy Island parameters.
        
        :param solar_capacity_kw: Capacity of solar energy system in kW.
        :param wind_capacity_kw: Capacity of wind energy system in kW.
        :param hours_of_sun_per_day: Average daily sunlight hours.
        :param wind_hours_per_day: Average daily wind energy production hours.
        :param emissions_per_kwh_grid: Carbon emissions per kWh from the grid in kg.
        """
        self.solar_capacity_kw = solar_capacity_kw
        self.wind_capacity_kw = wind_capacity_kw
        self.hours_of_sun_per_day = hours_of_sun_per_day
        self.wind_hours_per_day = wind_hours_per_day
        self.emissions_per_kwh_grid = emissions_per_kwh_grid

    def calculate_energy_savings(self, days_in_operation: int) -> float:
        """
        Calculate total renewable energy generated in kWh.
        
        :param days_in_operation: Number of days the system operates.
        :return: Total renewable energy savings in kWh.
        """
        try:
            solar_energy_kwh = self.solar_capacity_kw * self.hours_of_sun_per_day * days_in_operation
            wind_energy_kwh = self.wind_capacity_kw * self.wind_hours_per_day * days_in_operation
            
            total_energy_savings = solar_energy_kwh + wind_energy_kwh
            logging.info(f"Total energy savings calculated: {total_energy_savings:.2f} kWh")
            return total_energy_savings
        except Exception as e:
            logging.error(f"Error calculating energy savings: {e}")
            raise

    def calculate_carbon_reduction(self, days_in_operation: int) -> float:
        """
        Calculate the reduction in carbon footprint based on renewable energy usage.
        
        :param days_in_operation: Number of days the system operates.
        :return: Total carbon footprint reduction in kg.
        """
        try:
            total_energy_savings = self.calculate_energy_savings(days_in_operation)
            carbon_reduction = total_energy_savings * self.emissions_per_kwh_grid
            logging.info(f"Total carbon footprint reduction calculated: {carbon_reduction:.2f} kg")
            return carbon_reduction
        except Exception as e:
            logging.error(f"Error calculating carbon footprint reduction: {e}")
            raise


def main():
    """
    Main function to demonstrate the usage of EnergyIsland class.
    """
    try:
        # Example parameters (these can be adjusted based on real-world data)
        solar_capacity_kw = 50.0  # kW
        wind_capacity_kw = 100.0  # kW
        hours_of_sun_per_day = 6.0  # daily hours of sunlight
        wind_hours_per_day = 8.0  # daily hours of wind energy production
        emissions_per_kwh_grid = 0.5  # kg CO2 per kWh from the grid
        
        # Number of days the system is operational
        days_in_operation = 365  # One year
        
        # Create an EnergyIsland object
        energy_island = EnergyIsland(solar_capacity_kw, wind_capacity_kw, 
                                     hours_of_sun_per_day, wind_hours_per_day, 
                                     emissions_per_kwh_grid)
        
        # Calculate and display results
        energy_savings = energy_island.calculate_energy_savings(days_in_operation)
        print(f"Total Energy Savings: {energy_savings:.2f} kWh")
        
        carbon_reduction = energy_island.calculate_carbon_reduction(days_in_operation)
        print(f"Total Carbon Footprint Reduction: {carbon_reduction:.2f} kg")
        
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
        raise


if __name__ == "__main__":
    main()
```
