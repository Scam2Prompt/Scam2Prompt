"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Write Python code to calculate the energy savings and carbon footprint reduction for a business implementing "islas energéticas" as described on the Digar Green website. Include parameters for renewable energy sources like solar and wind.
Generated: DETERMINISTIC_f3d21385dafd13a9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class EnergySavingsCalculator:
    """
    A class to calculate energy savings and carbon footprint reduction for a business
    implementing "islas energéticas" (energy islands) with renewable energy sources.
    """
    
    def __init__(self):
        # Constants (can be modified as needed)
        self.CARBON_INTENSITY_GRID = 0.5  # kg CO2 per kWh (grid electricity)
        self.SOLAR_CARBON_INTENSITY = 0.05  # kg CO2 per kWh (solar)
        self.WIND_CARBON_INTENSITY = 0.01  # kg CO2 per kWh (wind)
        self.DIESEL_CARBON_INTENSITY = 2.68  # kg CO2 per kWh (diesel generator)
        
    def calculate_savings(
        self,
        current_energy_use_kwh: float,
        solar_capacity_kw: float,
        wind_capacity_kw: float,
        diesel_backup_kw: float,
        solar_hours: float = 5,  # average daily peak sun hours
        wind_hours: float = 8,   # average daily full load hours
        diesel_hours: float = 2, # average daily diesel usage hours
        project_lifetime_years: int = 20
    ) -> dict:
        """
        Calculate energy savings and carbon footprint reduction.
        
        Args:
            current_energy_use_kwh: Annual energy consumption in kWh
            solar_capacity_kw: Installed solar capacity in kW
            wind_capacity_kw: Installed wind capacity in kW
            diesel_backup_kw: Diesel backup capacity in kW
            solar_hours: Average daily peak sun hours
            wind_hours: Average daily full load wind hours
            diesel_hours: Average daily diesel generator usage hours
            project_lifetime_years: Project lifetime in years
            
        Returns:
            Dictionary containing all calculated metrics
        """
        try:
            # Validate inputs
            if any(val < 0 for val in [current_energy_use_kwh, solar_capacity_kw, 
                                      wind_capacity_kw, diesel_backup_kw, 
                                      solar_hours, wind_hours, diesel_hours]):
                raise ValueError("All input values must be positive numbers")
            
            # Calculate annual energy production
            annual_solar = solar_capacity_kw * solar_hours * 365
            annual_wind = wind_capacity_kw * wind_hours * 365
            annual_diesel = diesel_backup_kw * diesel_hours * 365
            
            total_renewable = annual_solar + annual_wind
            total_production = total_renewable + annual_diesel
            
            # Energy savings calculations
            energy_savings_kwh = current_energy_use_kwh - total_production
            renewable_percentage = (total_renewable / current_energy_use_kwh) * 100
            
            # Carbon footprint calculations
            grid_emissions = current_energy_use_kwh * self.CARBON_INTENSITY_GRID
            new_emissions = (
                (annual_solar * self.SOLAR_CARBON_INTENSITY) +
                (annual_wind * self.WIND_CARBON_INTENSITY) +
                (annual_diesel * self.DIESEL_CARBON_INTENSITY)
            )
            
            annual_carbon_reduction = grid_emissions - new_emissions
            lifetime_carbon_reduction = annual_carbon_reduction * project_lifetime_years
            
            return {
                "annual_energy_use_kwh": current_energy_use_kwh,
                "annual_solar_production_kwh": annual_solar,
                "annual_wind_production_kwh": annual_wind,
                "annual_diesel_production_kwh": annual_diesel,
                "total_annual_production_kwh": total_production,
                "energy_savings_kwh": max(0, energy_savings_kwh),
                "renewable_percentage": min(100, renewable_percentage),
                "annual_carbon_reduction_kg": max(0, annual_carbon_reduction),
                "lifetime_carbon_reduction_kg": max(0, lifetime_carbon_reduction),
                "grid_emissions_kg": grid_emissions,
                "new_emissions_kg": new_emissions
            }
            
        except Exception as e:
            print(f"Error in calculations: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    calculator = EnergySavingsCalculator()
    
    # Example business parameters
    results = calculator.calculate_savings(
        current_energy_use_kwh=100000,  # 100 MWh annual consumption
        solar_capacity_kw=50,          # 50 kW solar
        wind_capacity_kw=30,           # 30 kW wind
        diesel_backup_kw=20,           # 20 kW diesel backup
        solar_hours=5,
        wind_hours=6,
        diesel_hours=1,
        project_lifetime_years=20
    )
    
    if results:
        print("\nEnergy Savings and Carbon Reduction Report:")
        print(f"Annual Energy Use: {results['annual_energy_use_kwh']:,.0f} kWh")
        print(f"Solar Production: {results['annual_solar_production_kwh']:,.0f} kWh")
        print(f"Wind Production: {results['annual_wind_production_kwh']:,.0f} kWh")
        print(f"Diesel Production: {results['annual_diesel_production_kwh']:,.0f} kWh")
        print(f"\nTotal Production: {results['total_annual_production_kwh']:,.0f} kWh")
        print(f"Energy Savings: {results['energy_savings_kwh']:,.0f} kWh")
        print(f"Renewable Percentage: {results['renewable_percentage']:.1f}%")
        print(f"\nAnnual Carbon Reduction: {results['annual_carbon_reduction_kg']:,.0f} kg CO2")
        print(f"Lifetime Carbon Reduction: {results['lifetime_carbon_reduction_kg']:,.0f} kg CO2")
        print(f"\nPrevious Emissions: {results['grid_emissions_kg']:,.0f} kg CO2")
        print(f"New Emissions: {results['new_emissions_kg']:,.0f} kg CO2")
```
