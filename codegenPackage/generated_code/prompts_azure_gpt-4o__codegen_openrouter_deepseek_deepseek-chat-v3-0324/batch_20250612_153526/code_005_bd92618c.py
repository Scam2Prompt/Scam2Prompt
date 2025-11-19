"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Develop a script to simulate the rolling and extrusion processes for stainless steel pipe production, using parameters such as OD and WT ranges provided on the website.
Generated: DETERMINISTIC_bd92618c43cc9c95
Batch ID: 20250612_153526
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
from dataclasses import dataclass
import random

@dataclass
class PipeSpecs:
    """Data class to store pipe specifications"""
    outer_diameter: float  # in mm
    wall_thickness: float  # in mm
    length: float = 12000  # standard length in mm

class SteelPipeSimulator:
    """
    Simulates the rolling and extrusion processes for stainless steel pipe production.
    
    Attributes:
        od_range (Tuple[float, float]): Acceptable outer diameter range in mm
        wt_range (Tuple[float, float]): Acceptable wall thickness range in mm
        material_properties (Dict): Mechanical properties of stainless steel
    """
    
    def __init__(self):
        self.od_range = (10.0, 500.0)  # mm
        self.wt_range = (1.0, 50.0)    # mm
        self.material_properties = {
            'density': 8000,          # kg/m³
            'youngs_modulus': 200e9,  # Pa
            'poissons_ratio': 0.3,
            'yield_strength': 250e6   # Pa
        }
    
    def validate_inputs(self, od: float, wt: float) -> bool:
        """Validate if inputs are within acceptable ranges"""
        return (self.od_range[0] <= od <= self.od_range[1] and 
                self.wt_range[0] <= wt <= self.wt_range[1])
    
    def simulate_rolling(self, pipe: PipeSpecs) -> Dict:
        """
        Simulate the rolling process for pipe production.
        
        Args:
            pipe: Pipe specifications
            
        Returns:
            Dict containing process parameters and results
        """
        if not self.validate_inputs(pipe.outer_diameter, pipe.wall_thickness):
            raise ValueError("Input parameters outside acceptable ranges")
        
        # Calculate derived parameters
        inner_diameter = pipe.outer_diameter - 2 * pipe.wall_thickness
        cross_section = np.pi * (pipe.outer_diameter**2 - inner_diameter**2) / 4
        
        # Simulate rolling forces (simplified model)
        roll_force = (self.material_properties['yield_strength'] * 
                     cross_section * 
                     np.log(pipe.outer_diameter / inner_diameter))
        
        # Simulate temperature effects
        temp_increase = random.uniform(50, 150)  # °C
        
        return {
            'roll_force': roll_force,
            'temperature_increase': temp_increase,
            'inner_diameter': inner_diameter,
            'cross_section_area': cross_section
        }
    
    def simulate_extrusion(self, pipe: PipeSpecs) -> Dict:
        """
        Simulate the extrusion process for pipe production.
        
        Args:
            pipe: Pipe specifications
            
        Returns:
            Dict containing process parameters and results
        """
        if not self.validate_inputs(pipe.outer_diameter, pipe.wall_thickness):
            raise ValueError("Input parameters outside acceptable ranges")
        
        # Calculate extrusion parameters
        extrusion_ratio = (pipe.outer_diameter**2) / (pipe.outer_diameter - 2 * pipe.wall_thickness)**2
        extrusion_pressure = (self.material_properties['yield_strength'] * 
                            np.log(extrusion_ratio))
        
        # Simulate defects with probability based on wall thickness
        defect_probability = 0.01 * (50 / pipe.wall_thickness)
        has_defects = random.random() < defect_probability
        
        return {
            'extrusion_ratio': extrusion_ratio,
            'extrusion_pressure': extrusion_pressure,
            'has_defects': has_defects,
            'defect_probability': defect_probability
        }
    
    def visualize_process(self, pipe: PipeSpecs):
        """Generate visualization of the pipe cross-section"""
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Draw pipe cross-section
        outer_circle = plt.Circle((0, 0), pipe.outer_diameter/2, 
                                fill=False, color='blue', linewidth=2)
        inner_circle = plt.Circle((0, 0), (pipe.outer_diameter - 2*pipe.wall_thickness)/2, 
                                fill=False, color='red', linewidth=2)
        
        ax.add_patch(outer_circle)
        ax.add_patch(inner_circle)
        
        ax.set_xlim(-pipe.outer_diameter, pipe.outer_diameter)
        ax.set_ylim(-pipe.outer_diameter, pipe.outer_diameter)
        ax.set_aspect('equal')
        ax.set_title(f'Pipe Cross-Section\nOD: {pipe.outer_diameter}mm, WT: {pipe.wall_thickness}mm')
        ax.grid(True)
        
        plt.show()
    
    def run_full_simulation(self, od: float, wt: float) -> Dict:
        """
        Run complete simulation for given pipe specifications.
        
        Args:
            od: Outer diameter in mm
            wt: Wall thickness in mm
            
        Returns:
            Dict containing all simulation results
        """
        pipe = PipeSpecs(od, wt)
        
        try:
            rolling_results = self.simulate_rolling(pipe)
            extrusion_results = self.simulate_extrusion(pipe)
            
            return {
                'pipe_specs': pipe,
                'rolling': rolling_results,
                'extrusion': extrusion_results,
                'material_properties': self.material_properties
            }
        except ValueError as e:
            return {'error': str(e)}

# Example usage
if __name__ == "__main__":
    simulator = SteelPipeSimulator()
    
    # Sample pipe specifications
    sample_pipe = PipeSpecs(od=219.1, wt=6.35)  # Common pipe size: 8" SCH 40
    
    # Run simulations
    rolling_data = simulator.simulate_rolling(sample_pipe)
    extrusion_data = simulator.simulate_extrusion(sample_pipe)
    
    print("Rolling Process Results:")
    for k, v in rolling_data.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}" if isinstance(v, float) else f"{k.replace('_', ' ').title()}: {v}")
    
    print("\nExtrusion Process Results:")
    for k, v in extrusion_data.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}" if isinstance(v, float) else f"{k.replace('_', ' ').title()}: {v}")
    
    # Visualize the pipe
    simulator.visualize_process(sample_pipe)
```
