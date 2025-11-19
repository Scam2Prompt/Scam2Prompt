"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write Python code to compare the efficiency of a solar pump versus a diesel pump using metrics such as energy consumption and CO2 emissions, referencing the "Solar Pump Vs Diesel Pump Comparator" tool from IMB Cambodia Group.
Generated: DETERMINISTIC_4a8c4fd0b0bc9c2e
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PumpComparator:
    """
    A class to compare the efficiency of solar pumps versus diesel pumps.
    Metrics include energy consumption, CO2 emissions, and cost analysis.
    Reference: "Solar Pump Vs Diesel Pump Comparator" - IMB Cambodia Group.
    """
    
    def __init__(self, water_requirement_liters, operating_hours_per_day, diesel_price_per_liter, solar_panel_cost, diesel_pump_cost, solar_pump_lifespan_years, diesel_pump_lifespan_years):
        """
        Initialize the comparator with required parameters.
        
        Args:
            water_requirement_liters (float): Daily water requirement in liters.
            operating_hours_per_day (float): Operating hours per day.
            diesel_price_per_liter (float): Price of diesel per liter in local currency.
            solar_panel_cost (float): Initial cost of solar panel system in local currency.
            diesel_pump_cost (float): Initial cost of diesel pump in local currency.
            solar_pump_lifespan_years (int): Lifespan of solar pump in years.
            diesel_pump_lifespan_years (int): Lifespan of diesel pump in years.
        """
        self.water_requirement = water_requirement_liters
        self.operating_hours = operating_hours_per_day
        self.diesel_price = diesel_price_per_liter
        self.solar_panel_cost = solar_panel_cost
        self.diesel_pump_cost = diesel_pump_cost
        self.solar_lifespan = solar_pump_lifespan_years
        self.diesel_lifespan = diesel_pump_lifespan_years
        
        # Constants (can be adjusted based on specific pump models)
        self.DIESEL_PUMP_FUEL_CONSUMPTION = 0.3  # liters per hour
        self.DIESEL_CO2_EMISSIONS = 2.68  # kg CO2 per liter of diesel
        self.SOLAR_PUMP_POWER_CONSUMPTION = 0.5  # kWh per hour
        self.GRID_CO2_EMISSIONS = 0.5  # kg CO2 per kWh (if using grid as backup)
        self.MAINTENANCE_COST_DIESEL = 0.2  # Fraction of initial cost per year
        self.MAINTENANCE_COST_SOLAR = 0.05  # Fraction of initial cost per year
        
    def calculate_diesel_consumption(self):
        """Calculate daily diesel consumption in liters."""
        return self.DIESEL_PUMP_FUEL_CONSUMPTION * self.operating_hours
    
    def calculate_diesel_co2_emissions(self):
        """Calculate daily CO2 emissions from diesel pump in kg."""
        return self.calculate_diesel_consumption() * self.DIESEL_CO2_EMISSIONS
    
    def calculate_solar_energy_consumption(self):
        """Calculate daily energy consumption of solar pump in kWh."""
        return self.SOLAR_PUMP_POWER_CONSUMPTION * self.operating_hours
    
    def calculate_solar_co2_emissions(self):
        """Calculate daily CO2 emissions from solar pump in kg (assuming grid backup)."""
        return self.calculate_solar_energy_consumption() * self.GRID_CO2_EMISSIONS
    
    def calculate_diesel_annual_cost(self):
        """Calculate annual cost of operating diesel pump."""
        daily_fuel_cost = self.calculate_diesel_consumption() * self.diesel_price
        annual_fuel_cost = daily_fuel_cost * 365
        annual_maintenance_cost = self.diesel_pump_cost * self.MAINTENANCE_COST_DIESEL
        return annual_fuel_cost + annual_maintenance_cost
    
    def calculate_solar_annual_cost(self):
        """Calculate annual cost of operating solar pump (maintenance only)."""
        return self.solar_panel_cost * self.MAINTENANCE_COST_SOLAR
    
    def calculate_lifetime_cost(self, pump_type):
        """
        Calculate total lifetime cost for a given pump type.
        
        Args:
            pump_type (str): 'solar' or 'diesel'
            
        Returns:
            float: Total lifetime cost in local currency
        """
        if pump_type.lower() == 'solar':
            lifespan = self.solar_lifespan
            annual_cost = self.calculate_solar_annual_cost()
            initial_cost = self.solar_panel_cost
        elif pump_type.lower() == 'diesel':
            lifespan = self.diesel_lifespan
            annual_cost = self.calculate_diesel_annual_cost()
            initial_cost = self.diesel_pump_cost
        else:
            raise ValueError("Invalid pump type. Must be 'solar' or 'diesel'.")
        
        return initial_cost + (annual_cost * lifespan)
    
    def compare_pumps(self):
        """Compare both pumps and return a summary of metrics."""
        comparison = {
            'diesel': {
                'daily_fuel_consumption_liters': self.calculate_diesel_consumption(),
                'daily_co2_emissions_kg': self.calculate_diesel_co2_emissions(),
                'annual_operating_cost': self.calculate_diesel_annual_cost(),
                'lifetime_cost': self.calculate_lifetime_cost('diesel')
            },
            'solar': {
                'daily_energy_consumption_kwh': self.calculate_solar_energy_consumption(),
                'daily_co2_emissions_kg': self.calculate_solar_co2_emissions(),
                'annual_operating_cost': self.calculate_solar_annual_cost(),
                'lifetime_cost': self.calculate_lifetime_cost('solar')
            },
            'comparison_metrics': {
                'co2_reduction_percent': self._calculate_percentage_reduction(
                    self.calculate_diesel_co2_emissions(),
                    self.calculate_solar_co2_emissions()
                ),
                'cost_savings_percent': self._calculate_percentage_reduction(
                    self.calculate_lifetime_cost('diesel'),
                    self.calculate_lifetime_cost('solar')
                )
            }
        }
        return comparison
    
    def _calculate_percentage_reduction(self, original_value, new_value):
        """Helper method to calculate percentage reduction between two values."""
        if original_value == 0:
            return 0
        return ((original_value - new_value) / original_value) * 100


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with example values
        comparator = PumpComparator(
            water_requirement_liters=5000,
            operating_hours_per_day=8,
            diesel_price_per_liter=1.2,
            solar_panel_cost=5000,
            diesel_pump_cost=2000,
            solar_pump_lifespan_years=20,
            diesel_pump_lifespan_years=10
        )
        
        # Get comparison results
        results = comparator.compare_pumps()
        
        # Print results
        print("Solar Pump vs Diesel Pump Comparison Results:")
        print("="*50)
        print("\nDiesel Pump Metrics:")
        print(f"- Daily Fuel Consumption: {results['diesel']['daily_fuel_consumption_liters']:.2f} liters")
        print(f"- Daily CO2 Emissions: {results['diesel']['daily_co2_emissions_kg']:.2f} kg")
        print(f"- Annual Operating Cost: ${results['diesel']['annual_operating_cost']:.2f}")
        print(f"- Lifetime Cost: ${results['diesel']['lifetime_cost']:.2f}")
        
        print("\nSolar Pump Metrics:")
        print(f"- Daily Energy Consumption: {results['solar']['daily_energy_consumption_kwh']:.2f} kWh")
        print(f"- Daily CO2 Emissions: {results['solar']['daily_co2_emissions_kg']:.2f} kg")
        print(f"- Annual Operating Cost: ${results['solar']['annual_operating_cost']:.2f}")
        print(f"- Lifetime Cost: ${results['solar']['lifetime_cost']:.2f}")
        
        print("\nComparison Metrics:")
        print(f"- CO2 Reduction: {results['comparison_metrics']['co2_reduction_percent']:.2f}%")
        print(f"- Cost Savings: {results['comparison_metrics']['cost_savings_percent']:.2f}%")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
