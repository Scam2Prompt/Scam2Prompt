"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Develop a simple algorithm to determine the optimal size and number of solar panels required for a residential building in Brazil, considering factors like roof size, energy consumption, and local solar irradiance.
Generated: DETERMINISTIC_eb1e1a42dc510258
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class SolarPanelCalculator:
    """
    A class to calculate the optimal number and size of solar panels for a residential building in Brazil.
    Takes into account roof size, energy consumption, and local solar irradiance.
    """
    
    def __init__(self, panel_efficiency=0.18, panel_width=1.0, panel_height=1.6, 
                 performance_ratio=0.75, safety_factor=1.2):
        """
        Initialize the calculator with default panel specifications and system parameters.
        
        Args:
            panel_efficiency (float): Efficiency of the solar panel (default 18%).
            panel_width (float): Width of a single panel in meters (default 1.0m).
            panel_height (float): Height of a single panel in meters (default 1.6m).
            performance_ratio (float): System performance ratio accounting for losses (default 0.75).
            safety_factor (float): Safety factor to account for inefficiencies (default 1.2).
        """
        self.panel_efficiency = panel_efficiency
        self.panel_area = panel_width * panel_height
        self.performance_ratio = performance_ratio
        self.safety_factor = safety_factor
    
    def calculate_panels(self, annual_consumption_kwh, roof_area, irradiance_kwh_m2_day):
        """
        Calculate the optimal number of solar panels required.
        
        Args:
            annual_consumption_kwh (float): Annual energy consumption in kWh.
            roof_area (float): Available roof area in square meters.
            irradiance_kwh_m2_day (float): Average daily solar irradiance in kWh/m²/day.
            
        Returns:
            dict: A dictionary containing the number of panels, required area, and system capacity.
        """
        try:
            if any(val <= 0 for val in [annual_consumption_kwh, roof_area, irradiance_kwh_m2_day]):
                raise ValueError("All input values must be positive")
            
            # Calculate daily energy requirement
            daily_consumption_kwh = annual_consumption_kwh / 365
            
            # Calculate required panel area
            daily_energy_per_m2 = irradiance_kwh_m2_day * self.panel_efficiency * self.performance_ratio
            required_area = (daily_consumption_kwh / daily_energy_per_m2) * self.safety_factor
            
            # Calculate number of panels
            num_panels = math.ceil(required_area / self.panel_area)
            
            # Check if roof area is sufficient
            required_total_area = num_panels * self.panel_area
            if required_total_area > roof_area:
                # Recalculate with maximum possible panels
                num_panels = math.floor(roof_area / self.panel_area)
                required_total_area = num_panels * self.panel_area
                daily_energy_production = num_panels * self.panel_area * daily_energy_per_m2
                annual_energy_production = daily_energy_production * 365
            else:
                daily_energy_production = daily_consumption_kwh * self.safety_factor
                annual_energy_production = daily_energy_production * 365
            
            system_capacity_kw = (num_panels * self.panel_area * irradiance_kwh_m2_day * 
                                 self.panel_efficiency * self.performance_ratio) / 1000
            
            return {
                'num_panels': num_panels,
                'required_area_m2': round(required_total_area, 2),
                'system_capacity_kw': round(system_capacity_kw, 2),
                'annual_energy_production_kwh': round(annual_energy_production, 2),
                'roof_area_utilization_percent': round((required_total_area / roof_area) * 100, 2)
            }
            
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    calculator = SolarPanelCalculator()
    
    # Example values for Brazil (average)
    result = calculator.calculate_panels(
        annual_consumption_kwh=3600,  # Average Brazilian household consumption
        roof_area=30,                 # Available roof area in m²
        irradiance_kwh_m2_day=5.5     # Average solar irradiance in Brazil
    )
    
    if result:
        print("Solar Panel System Calculation Results:")
        print(f"Number of panels required: {result['num_panels']}")
        print(f"Required area: {result['required_area_m2']} m²")
        print(f"System capacity: {result['system_capacity_kw']} kW")
        print(f"Annual energy production: {result['annual_energy_production_kwh']} kWh")
        print(f"Roof area utilization: {result['roof_area_utilization_percent']}%")
```
