"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Generate a script to simulate the cold-state precision rolling process for stainless steel pipes, ensuring high inner surface smoothness and dimensional accuracy, using specifications like OD6.0mm-60.0mm and WT0.45mm-5.0mm.
Generated: DETERMINISTIC_80dd2643beaa68d5
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
from scipy.interpolate import interp1d
from enum import Enum

class MaterialGrade(Enum):
    """Enum for stainless steel grades"""
    AISI_304 = 1
    AISI_316 = 2
    AISI_321 = 3

class PipeSpecification:
    """Class to hold pipe specifications"""
    def __init__(self, outer_diameter, wall_thickness, length, material_grade):
        """
        Initialize pipe specifications
        
        Args:
            outer_diameter (float): Outer diameter in mm (6.0-60.0mm)
            wall_thickness (float): Wall thickness in mm (0.45-5.0mm)
            length (float): Pipe length in mm
            material_grade (MaterialGrade): Stainless steel grade
        """
        self.outer_diameter = outer_diameter
        self.wall_thickness = wall_thickness
        self.length = length
        self.material_grade = material_grade
        
        self._validate_specs()
    
    def _validate_specs(self):
        """Validate pipe specifications"""
        if not (6.0 <= self.outer_diameter <= 60.0):
            raise ValueError(f"Outer diameter {self.outer_diameter}mm is outside valid range (6.0-60.0mm)")
        if not (0.45 <= self.wall_thickness <= 5.0):
            raise ValueError(f"Wall thickness {self.wall_thickness}mm is outside valid range (0.45-5.0mm)")
        if self.wall_thickness >= self.outer_diameter / 2:
            raise ValueError("Wall thickness cannot be greater than or equal to half of outer diameter")

class ColdRollingSimulator:
    """Simulator for cold-state precision rolling process"""
    
    # Material properties (MPa)
    MATERIAL_PROPERTIES = {
        MaterialGrade.AISI_304: {'yield_strength': 205, 'tensile_strength': 515, 'hardening_factor': 0.25},
        MaterialGrade.AISI_316: {'yield_strength': 205, 'tensile_strength': 515, 'hardening_factor': 0.28},
        MaterialGrade.AISI_321: {'yield_strength': 205, 'tensile_strength': 515, 'hardening_factor': 0.22}
    }
    
    def __init__(self, pipe_spec):
        """
        Initialize rolling simulator
        
        Args:
            pipe_spec (PipeSpecification): Pipe specifications
        """
        self.pipe_spec = pipe_spec
        self.material_props = self.MATERIAL_PROPERTIES[pipe_spec.material_grade]
        
        # Rolling parameters
        self.roll_gap = pipe_spec.wall_thickness * 0.95  # Initial roll gap (95% of wall thickness)
        self.roll_force = 0
        self.pass_count = 0
        self.tolerance = 0.01  # mm tolerance for dimensional accuracy
        
        # Surface roughness parameters
        self.initial_roughness = 1.6  # µm Ra
        self.target_roughness = 0.4   # µm Ra
        
    def calculate_roll_force(self):
        """Calculate required rolling force"""
        # Simplified force calculation based on material properties and geometry
        reduction = (self.pipe_spec.wall_thickness - self.roll_gap) / self.pipe_spec.wall_thickness
        flow_stress = self.material_props['yield_strength'] * (1 + self.material_props['hardening_factor'] * reduction)
        
        contact_area = np.pi * (self.pipe_spec.outer_diameter - self.pipe_spec.wall_thickness) * self.pipe_spec.length
        self.roll_force = flow_stress * contact_area * reduction
        
        return self.roll_force
    
    def simulate_pass(self):
        """Simulate a single rolling pass"""
        self.pass_count += 1
        
        # Gradually reduce roll gap
        self.roll_gap *= 0.9
        
        # Calculate new dimensions
        new_wall = self.roll_gap
        new_od = self.pipe_spec.outer_diameter - (self.pipe_spec.wall_thickness - new_wall) * 2
        
        # Update pipe specs
        self.pipe_spec.wall_thickness = new_wall
        self.pipe_spec.outer_diameter = new_od
        
        # Calculate surface improvement
        current_roughness = self.initial_roughness * (0.7 ** self.pass_count)
        
        return {
            'pass_number': self.pass_count,
            'wall_thickness': new_wall,
            'outer_diameter': new_od,
            'roll_force': self.calculate_roll_force(),
            'surface_roughness': max(current_roughness, self.target_roughness)
        }
    
    def simulate_full_process(self, target_wall=None):
        """
        Simulate full rolling process until target wall thickness is reached
        
        Args:
            target_wall (float): Optional target wall thickness (defaults to 95% of initial)
        
        Returns:
            list: List of pass results
        """
        if target_wall is None:
            target_wall = self.pipe_spec.wall_thickness * 0.95
        
        results = []
        while self.pipe_spec.wall_thickness > target_wall + self.tolerance:
            try:
                pass_result = self.simulate_pass()
                results.append(pass_result)
                
                # Safety check
                if self.pass_count > 20:
                    raise RuntimeError("Exceeded maximum number of passes (20)")
                    
            except Exception as e:
                print(f"Error during pass {self.pass_count}: {str(e)}")
                break
        
        return results
    
    def plot_results(self, results):
        """Plot simulation results"""
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        
        # Wall thickness and OD
        passes = [r['pass_number'] for r in results]
        walls = [r['wall_thickness'] for r in results]
        ods = [r['outer_diameter'] for r in results]
        
        ax1.plot(passes, walls, 'b-o', label='Wall Thickness')
        ax1.plot(passes, ods, 'r--o', label='Outer Diameter')
        ax1.set_title('Dimensional Changes During Rolling')
        ax1.set_xlabel('Pass Number')
        ax1.set_ylabel('Dimension (mm)')
        ax1.legend()
        ax1.grid(True)
        
        # Roll force
        forces = [r['roll_force'] / 1000 for r in results]  # Convert to kN
        ax2.plot(passes, forces, 'g-o')
        ax2.set_title('Rolling Force')
        ax2.set_xlabel('Pass Number')
        ax2.set_ylabel('Force (kN)')
        ax2.grid(True)
        
        # Surface roughness
        roughness = [r['surface_roughness'] for r in results]
        ax3.plot(passes, roughness, 'm-o')
        ax3.set_title('Surface Roughness')
        ax3.set_xlabel('Pass Number')
        ax3.set_ylabel('Roughness (µm Ra)')
        ax3.grid(True)
        
        plt.tight_layout()
        plt.show()

def main():
    """Main function to demonstrate the rolling simulation"""
    try:
        # Create pipe specification
        pipe_spec = PipeSpecification(
            outer_diameter=30.0,
            wall_thickness=3.0,
            length=1000.0,
            material_grade=MaterialGrade.AISI_304
        )
        
        # Initialize simulator
        simulator = ColdRollingSimulator(pipe_spec)
        
        # Run simulation
        results = simulator.simulate_full_process(target_wall=2.7)
        
        # Print summary
        print("\nSimulation Summary:")
        print(f"Initial Wall: {pipe_spec.wall_thickness:.2f}mm, Final Wall: {results[-1]['wall_thickness']:.2f}mm")
        print(f"Initial OD: {pipe_spec.outer_diameter:.2f}mm, Final OD: {results[-1]['outer_diameter']:.2f}mm")
        print(f"Final Surface Roughness: {results[-1]['surface_roughness']:.2f}µm Ra")
        print(f"Total Passes: {len(results)}")
        
        # Plot results
        simulator.plot_results(results)
        
    except Exception as e:
        print(f"Error in simulation: {str(e)}")

if __name__ == "__main__":
    main()
```
