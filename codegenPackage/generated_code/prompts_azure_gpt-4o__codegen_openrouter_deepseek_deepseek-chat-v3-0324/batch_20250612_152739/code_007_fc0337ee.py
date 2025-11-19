"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Write Python code to analyze the energy efficiency of a furnace insulated with Aprisacv's ceramic fiber (Aprifiber) and ceramic paper (ApriPaper), using their temperature ratings and density specifications.
Generated: DETERMINISTIC_fc0337ee6c1fdf89
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict, Optional

class FurnaceEfficiencyAnalyzer:
    """
    Analyzes the energy efficiency of a furnace insulated with Aprisacv's ceramic fiber (Aprifiber) and ceramic paper (ApriPaper).
    """
    
    # Material properties (thermal conductivity in W/m·K at different temperatures)
    MATERIAL_PROPERTIES = {
        'Aprifiber': {
            'density_range': (96, 128),  # kg/m³
            'thermal_conductivity': {
                200: 0.06,
                400: 0.10,
                600: 0.15,
                800: 0.20,
                1000: 0.26
            },
            'max_temp': 1260  # °C
        },
        'ApriPaper': {
            'density_range': (200, 220),  # kg/m³
            'thermal_conductivity': {
                200: 0.08,
                400: 0.12,
                600: 0.17,
                800: 0.22,
                1000: 0.28
            },
            'max_temp': 1000  # °C
        }
    }
    
    def __init__(self, material: str, thickness: float, surface_area: float, 
                 inner_temp: float, outer_temp: float, density: Optional[float] = None):
        """
        Initialize the analyzer with furnace parameters.
        
        Args:
            material: Insulation material ('Aprifiber' or 'ApriPaper')
            thickness: Insulation thickness in meters
            surface_area: Surface area of furnace in m²
            inner_temp: Inner furnace temperature in °C
            outer_temp: Outer surface temperature in °C
            density: Optional custom density in kg/m³
        """
        if material not in self.MATERIAL_PROPERTIES:
            raise ValueError(f"Invalid material. Choose from: {list(self.MATERIAL_PROPERTIES.keys())}")
            
        self.material = material
        self.thickness = thickness
        self.surface_area = surface_area
        self.inner_temp = inner_temp
        self.outer_temp = outer_temp
        
        # Validate temperature against material limits
        max_temp = self.MATERIAL_PROPERTIES[material]['max_temp']
        if inner_temp > max_temp:
            raise ValueError(f"Temperature {inner_temp}°C exceeds {material}'s max of {max_temp}°C")
            
        # Set density (use midpoint of range if not specified)
        if density is None:
            min_d, max_d = self.MATERIAL_PROPERTIES[material]['density_range']
            self.density = (min_d + max_d) / 2
        else:
            if not (self.MATERIAL_PROPERTIES[material]['density_range'][0] <= density <= 
                   self.MATERIAL_PROPERTIES[material]['density_range'][1]):
                raise ValueError(f"Density {density} is outside acceptable range for {material}")
            self.density = density
    
    def _get_thermal_conductivity(self, temp: float) -> float:
        """
        Get thermal conductivity at given temperature using linear interpolation.
        
        Args:
            temp: Temperature in °C
            
        Returns:
            Thermal conductivity in W/m·K
        """
        temp_points = sorted(self.MATERIAL_PROPERTIES[self.material]['thermal_conductivity'].keys())
        k_points = [self.MATERIAL_PROPERTIES[self.material]['thermal_conductivity'][t] for t in temp_points]
        
        # Handle temperatures outside measured range
        if temp <= temp_points[0]:
            return k_points[0]
        if temp >= temp_points[-1]:
            return k_points[-1]
            
        # Find the interval where temp lies
        for i in range(len(temp_points) - 1):
            if temp_points[i] <= temp <= temp_points[i+1]:
                # Linear interpolation
                t0, t1 = temp_points[i], temp_points[i+1]
                k0, k1 = k_points[i], k_points[i+1]
                return k0 + (k1 - k0) * (temp - t0) / (t1 - t0)
                
        return k_points[-1]  # fallback
    
    def calculate_heat_loss(self) -> Tuple[float, float]:
        """
        Calculate heat loss through the insulation.
        
        Returns:
            Tuple of (heat_loss_rate (W), heat_loss_per_hour (kWh))
        """
        avg_temp = (self.inner_temp + self.outer_temp) / 2
        k = self._get_thermal_conductivity(avg_temp)
        
        # Heat loss rate (Q = k * A * (T_hot - T_cold) / thickness)
        heat_loss_rate = k * self.surface_area * (self.inner_temp - self.outer_temp) / self.thickness
        
        # Heat loss per hour in kWh
        heat_loss_per_hour = heat_loss_rate * 3600 / 1000
        
        return heat_loss_rate, heat_loss_per_hour
    
    def calculate_efficiency(self, input_power: float) -> float:
        """
        Calculate furnace efficiency based on heat loss.
        
        Args:
            input_power: Total power input to furnace in W
            
        Returns:
            Efficiency as a percentage (0-100)
        """
        heat_loss_rate, _ = self.calculate_heat_loss()
        useful_power = input_power - heat_loss_rate
        efficiency = (useful_power / input_power) * 100
        return max(0, min(100, efficiency))  # Clamp between 0-100
    
    def plot_conductivity_vs_temperature(self):
        """Plot thermal conductivity vs temperature for the selected material."""
        temps = np.linspace(0, self.MATERIAL_PROPERTIES[self.material]['max_temp'], 100)
        conductivities = [self._get_thermal_conductivity(t) for t in temps]
        
        plt.figure(figsize=(10, 6))
        plt.plot(temps, conductivities, label=f'{self.material} Thermal Conductivity')
        plt.title(f'Thermal Conductivity vs Temperature for {self.material}')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Thermal Conductivity (W/m·K)')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def generate_report(self, input_power: Optional[float] = None) -> Dict:
        """
        Generate a comprehensive report of the analysis.
        
        Args:
            input_power: Optional input power for efficiency calculation
            
        Returns:
            Dictionary containing all analysis results
        """
        report = {
            'material': self.material,
            'density_kg_m3': self.density,
            'thickness_m': self.thickness,
            'surface_area_m2': self.surface_area,
            'inner_temp_c': self.inner_temp,
            'outer_temp_c': self.outer_temp,
            'max_temperature_c': self.MATERIAL_PROPERTIES[self.material]['max_temp']
        }
        
        heat_loss_rate, heat_loss_per_hour = self.calculate_heat_loss()
        report.update({
            'heat_loss_rate_w': heat_loss_rate,
            'heat_loss_per_hour_kwh': heat_loss_per_hour,
            'avg_thermal_conductivity': self._get_thermal_conductivity((self.inner_temp + self.outer_temp)/2)
        })
        
        if input_power is not None:
            report['efficiency_percent'] = self.calculate_efficiency(input_power)
            
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Analyze Aprifiber insulation
        analyzer = FurnaceEfficiencyAnalyzer(
            material='Aprifiber',
            thickness=0.1,  # 10 cm
            surface_area=5.0,  # 5 m²
            inner_temp=800,
            outer_temp=50
        )
        
        # Generate and print report
        report = analyzer.generate_report(input_power=5000)  # 5 kW input
        for key, value in report.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
        # Plot conductivity
        analyzer.plot_conductivity_vs_temperature()
        
    except ValueError as e:
        print(f"Error: {e}")
```
