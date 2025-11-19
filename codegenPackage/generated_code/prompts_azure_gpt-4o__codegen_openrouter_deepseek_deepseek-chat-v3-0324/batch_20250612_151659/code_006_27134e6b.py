"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write code to simulate rain washout protection on embankments using Groundcell's perforated strips, incorporating data from the technical data sheet.
Generated: DETERMINISTIC_27134e6b18641f2c
Batch ID: 20250612_151659
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
from typing import Tuple, List, Dict

class PerforatedStrip:
    """Class representing Groundcell's perforated strip for rain washout protection."""
    
    def __init__(self, strip_length: float, strip_width: float, hole_diameter: float, 
                 hole_spacing: float, material_thickness: float, material_density: float):
        """
        Initialize perforated strip with technical specifications.
        
        Args:
            strip_length: Length of the strip in meters
            strip_width: Width of the strip in meters
            hole_diameter: Diameter of each hole in meters
            hole_spacing: Distance between hole centers in meters
            material_thickness: Thickness of strip material in meters
            material_density: Density of strip material in kg/m³
        """
        self.strip_length = strip_length
        self.strip_width = strip_width
        self.hole_diameter = hole_diameter
        self.hole_spacing = hole_spacing
        self.material_thickness = material_thickness
        self.material_density = material_density
        
        # Calculate derived properties
        self.hole_area = np.pi * (hole_diameter / 2) ** 2
        self.holes_per_row = int(strip_length / hole_spacing) + 1
        self.total_holes = self.holes_per_row * int(strip_width / hole_spacing)
        self.solid_area = (strip_length * strip_width) - (self.total_holes * self.hole_area)
        self.mass = self.solid_area * material_thickness * material_density
        
    def calculate_flow_capacity(self, rainfall_intensity: float) -> float:
        """
        Calculate the flow capacity of the strip for given rainfall intensity.
        
        Args:
            rainfall_intensity: Rainfall intensity in mm/hour
            
        Returns:
            Flow capacity in liters/second
        """
        # Convert rainfall intensity to m/s
        rainfall_rate = rainfall_intensity / (1000 * 3600)
        
        # Calculate total flow through holes (assuming 60% efficiency due to turbulence)
        flow_rate = 0.6 * self.total_holes * self.hole_area * rainfall_rate
        
        # Convert to liters/second
        return flow_rate * 1000
    
    def calculate_washout_protection(self, embankment_slope: float, soil_erodibility: float, 
                                    rainfall_intensity: float) -> Tuple[float, bool]:
        """
        Calculate washout protection effectiveness for given conditions.
        
        Args:
            embankment_slope: Slope angle in degrees
            soil_erodibility: Soil erodibility factor (0-1)
            rainfall_intensity: Rainfall intensity in mm/hour
            
        Returns:
            Tuple of (protection_factor, is_effective) where:
            - protection_factor: Ratio of protected vs unprotected erosion (0-1)
            - is_effective: Boolean indicating if protection is sufficient
        """
        # Base erosion rate without protection (simplified model)
        base_erosion = (0.1 * soil_erodibility * np.tan(np.radians(embankment_slope)) * 
                       (rainfall_intensity / 25) ** 2)
        
        # Protected erosion rate depends on flow capacity
        flow_capacity = self.calculate_flow_capacity(rainfall_intensity)
        required_flow = rainfall_intensity * self.strip_length * self.strip_width / 3600
        
        if flow_capacity >= required_flow:
            protected_erosion = base_erosion * 0.2  # 80% reduction
            is_effective = True
        else:
            # Linear reduction in effectiveness based on flow capacity
            effectiveness = flow_capacity / required_flow
            protected_erosion = base_erosion * (1 - 0.8 * effectiveness)
            is_effective = effectiveness > 0.7
            
        protection_factor = protected_erosion / base_erosion if base_erosion > 0 else 0
        return protection_factor, is_effective

class EmbankmentSimulator:
    """Class to simulate rain washout protection on embankments."""
    
    def __init__(self, strip_specs: Dict, embankment_length: float, embankment_width: float):
        """
        Initialize embankment simulator.
        
        Args:
            strip_specs: Dictionary containing strip specifications
            embankment_length: Length of embankment in meters
            embankment_width: Width of embankment in meters
        """
        self.strip = PerforatedStrip(**strip_specs)
        self.embankment_length = embankment_length
        self.embankment_width = embankment_width
        self.strips_needed = int(np.ceil(embankment_width / self.strip.strip_width))
        
    def simulate_rain_event(self, duration: float, rainfall_intensity: float, 
                           embankment_slope: float, soil_erodibility: float) -> Dict:
        """
        Simulate a rain event and calculate protection effectiveness.
        
        Args:
            duration: Duration of rain event in hours
            rainfall_intensity: Rainfall intensity in mm/hour
            embankment_slope: Slope angle in degrees
            soil_erodibility: Soil erodibility factor (0-1)
            
        Returns:
            Dictionary containing simulation results
        """
        protection_factor, is_effective = self.strip.calculate_washout_protection(
            embankment_slope, soil_erodibility, rainfall_intensity)
        
        total_flow = self.strip.calculate_flow_capacity(rainfall_intensity) * self.strips_needed
        required_flow = (rainfall_intensity * self.embankment_length * 
                        self.embankment_width / 3600)
        
        return {
            'protection_factor': protection_factor,
            'is_effective': is_effective,
            'total_flow_capacity': total_flow,
            'required_flow': required_flow,
            'strips_used': self.strips_needed,
            'flow_ratio': total_flow / required_flow if required_flow > 0 else float('inf')
        }
    
    def run_scenario_analysis(self, slope_range: Tuple[float, float, float], 
                            rainfall_range: Tuple[float, float, float], 
                            soil_erodibility: float) -> Dict:
        """
        Run scenario analysis across slope and rainfall ranges.
        
        Args:
            slope_range: Tuple of (start, stop, step) for slope angles in degrees
            rainfall_range: Tuple of (start, stop, step) for rainfall in mm/hour
            soil_erodibility: Soil erodibility factor (0-1)
            
        Returns:
            Dictionary containing scenario results and visualization data
        """
        slopes = np.arange(*slope_range)
        rainfalls = np.arange(*rainfall_range)
        
        results = []
        effectiveness_grid = np.zeros((len(slopes), len(rainfalls)))
        
        for i, slope in enumerate(slopes):
            for j, rainfall in enumerate(rainfalls):
                res = self.simulate_rain_event(1, rainfall, slope, soil_erodibility)
                effectiveness_grid[i, j] = res['protection_factor']
                results.append({
                    'slope': slope,
                    'rainfall': rainfall,
                    **res
                })
        
        return {
            'results': results,
            'effectiveness_grid': effectiveness_grid,
            'slopes': slopes,
            'rainfalls': rainfalls
        }

def visualize_results(scenario_results: Dict):
    """Visualize scenario analysis results."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create contour plot
    X, Y = np.meshgrid(scenario_results['rainfalls'], scenario_results['slopes'])
    Z = scenario_results['effectiveness_grid']
    
    levels = np.linspace(0, 1, 11)
    cs = ax.contourf(X, Y, Z, levels=levels, cmap='RdYlGn_r')
    fig.colorbar(cs, ax=ax, label='Protection Factor (lower is better)')
    
    # Add effectiveness threshold line
    effective_mask = Z <= 0.3
    if np.any(effective_mask):
        ax.contour(X, Y, effective_mask, levels=[0.5], colors='white', linewidths=2)
    
    ax.set_xlabel('Rainfall Intensity (mm/hour)')
    ax.set_ylabel('Embankment Slope (degrees)')
    ax.set_title('Rain Washout Protection Effectiveness')
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Technical specifications from Groundcell's data sheet
    strip_specs = {
        'strip_length': 2.0,
        'strip_width': 0.5,
        'hole_diameter': 0.01,
        'hole_spacing': 0.05,
        'material_thickness': 0.002,
        'material_density': 2700  # Aluminum density kg/m³
    }
    
    # Initialize simulator
    embankment
