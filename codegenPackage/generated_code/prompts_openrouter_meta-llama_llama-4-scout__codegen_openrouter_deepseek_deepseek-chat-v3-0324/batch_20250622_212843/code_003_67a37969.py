"""
Generated Code Metadata:
========================
Original URL: https://dimensions-solar.com
Prompt: "Design a solar energy system for a residential area, incorporating solar thermal and photovoltaic energy generation, and provide a detailed technical specification."
Generated: DETERMINISTIC_67a37969d0e6e88d
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class SolarEnergySystem:
    """
    A class representing a residential solar energy system combining photovoltaic (PV)
    and solar thermal components.
    """

    def __init__(self, location: Dict[str, float], roof_area: float, 
                 household_consumption: float, hot_water_demand: float):
        """
        Initialize the solar energy system with location data and requirements.
        
        Args:
            location: Dictionary containing latitude and longitude in degrees
            roof_area: Available roof area in square meters
            household_consumption: Annual electricity consumption in kWh
            hot_water_demand: Annual hot water demand in liters
        """
        self.location = location
        self.roof_area = roof_area
        self.household_consumption = household_consumption
        self.hot_water_demand = hot_water_demand
        
        # Default system parameters
        self.pv_efficiency = 0.18  # Typical PV panel efficiency
        self.thermal_efficiency = 0.70  # Typical solar thermal collector efficiency
        self.irradiance = self._calculate_irradiance()  # kWh/m²/day
        
        # System components
        self.pv_system = None
        self.thermal_system = None
        
    def _calculate_irradiance(self) -> float:
        """
        Calculate average solar irradiance based on location.
        Simplified model - in practice would use more detailed solar data.
        
        Returns:
            Average daily solar irradiance in kWh/m²/day
        """
        lat = self.location['latitude']
        # Simplified irradiance model based on latitude
        if abs(lat) <= 30:
            return 5.5  # Tropical/subtropical regions
        elif 30 < abs(lat) <= 45:
            return 4.5  # Temperate regions
        else:
            return 3.5  # Higher latitudes
        
    def design_pv_system(self) -> Dict[str, float]:
        """
        Design the photovoltaic system based on available roof area and consumption.
        
        Returns:
            Dictionary containing PV system specifications
        """
        if self.roof_area <= 0:
            raise ValueError("Roof area must be positive")
            
        # Calculate required PV area based on consumption
        required_pv_area = (self.household_consumption / 365) / (
            self.irradiance * self.pv_efficiency
        )
        
        # Use available roof area if requirement is larger
        pv_area = min(required_pv_area, self.roof_area * 0.7)  # 70% of roof for PV
        
        # Calculate system capacity in kW
        pv_capacity = pv_area * self.pv_efficiency * 1000 / 1000  # kW
        
        # Calculate annual production
        annual_production = pv_area * self.irradiance * 365 * self.pv_efficiency
        
        self.pv_system = {
            'area': pv_area,
            'capacity': pv_capacity,
            'annual_production': annual_production,
            'panel_count': math.floor(pv_area / 1.6)  # Assuming 1.6 m² per panel
        }
        
        return self.pv_system
    
    def design_thermal_system(self) -> Dict[str, float]:
        """
        Design the solar thermal system based on hot water demand.
        
        Returns:
            Dictionary containing thermal system specifications
        """
        if self.hot_water_demand <= 0:
            raise ValueError("Hot water demand must be positive")
            
        # Energy required to heat water (from 10°C to 60°C)
        energy_required = self.hot_water_demand * 4.186 * (60 - 10) / 3600  # kWh
        
        # Calculate required collector area
        thermal_area = (energy_required / 365) / (
            self.irradiance * self.thermal_efficiency
        )
        
        # Use available roof area if requirement is larger
        thermal_area = min(thermal_area, self.roof_area * 0.3)  # 30% of roof for thermal
        
        # Calculate storage tank size (3 days demand)
        tank_size = (self.hot_water_demand / 365) * 3
        
        self.thermal_system = {
            'collector_area': thermal_area,
            'tank_size': tank_size,
            'annual_energy': thermal_area * self.irradiance * 365 * self.thermal_efficiency,
            'collector_count': math.floor(thermal_area / 2)  # Assuming 2 m² per collector
        }
        
        return self.thermal_system
    
    def system_summary(self) -> Dict[str, Dict[str, float]]:
        """
        Generate a complete system summary including both PV and thermal components.
        
        Returns:
            Dictionary containing full system specifications
        """
        if not self.pv_system:
            self.design_pv_system()
        if not self.thermal_system:
            self.design_thermal_system()
            
        return {
            'location': self.location,
            'solar_irradiance': self.irradiance,
            'photovoltaic': self.pv_system,
            'solar_thermal': self.thermal_system,
            'roof_utilization': {
                'total_used': self.pv_system['area'] + self.thermal_system['collector_area'],
                'percentage_used': (self.pv_system['area'] + self.thermal_system['collector_area']) / self.roof_area * 100
            }
        }


def example_usage():
    """Example usage of the SolarEnergySystem class."""
    try:
        # Example parameters
        location = {'latitude': 40.7, 'longitude': -74.0}  # New York coordinates
        roof_area = 50  # m²
        consumption = 5000  # kWh/year
        hot_water = 15000  # liters/year
        
        # Create and design system
        system = SolarEnergySystem(location, roof_area, consumption, hot_water)
        pv_specs = system.design_pv_system()
        thermal_specs = system.design_thermal_system()
        
        # Print full system summary
        full_specs = system.system_summary()
        print("Solar Energy System Specifications:")
        for key, value in full_specs.items():
            print(f"\n{key.replace('_', ' ').title()}:")
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    print(f"  {subkey.replace('_', ' ').title()}: {subvalue:.2f}")
            else:
                print(f"  {value}")
                
    except ValueError as e:
        print(f"Error designing system: {e}")


if __name__ == "__main__":
    example_usage()
```
