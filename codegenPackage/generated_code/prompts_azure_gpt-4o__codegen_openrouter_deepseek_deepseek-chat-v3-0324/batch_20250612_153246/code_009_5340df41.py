"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Write code to calculate the bending radius and force required for cold pipe bending equipment, referencing the hydraulic plug mandrel specifications from SPM Equipment.
Generated: DETERMINISTIC_5340df4120e6a55a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PipeBendingCalculator:
    """
    A class to calculate bending radius and force required for cold pipe bending equipment.
    References hydraulic plug mandrel specifications from SPM Equipment.
    """
    
    def __init__(self):
        # Material properties (default values for steel)
        self.material_properties = {
            'steel': {
                'youngs_modulus': 200e9,  # Pa (Pascals)
                'yield_strength': 250e6,  # Pa
                'poissons_ratio': 0.3
            }
        }
        
        # SPM Equipment specifications (example values)
        self.spm_specs = {
            'max_bending_force': 50000,  # N (Newtons)
            'min_bending_radius': 1.5,   # times pipe diameter
            'max_bending_radius': 10.0   # times pipe diameter
        }
    
    def calculate_min_bending_radius(self, pipe_diameter: float) -> float:
        """
        Calculate minimum bending radius based on pipe diameter.
        
        Args:
            pipe_diameter: Outer diameter of pipe in meters
            
        Returns:
            Minimum bending radius in meters
        """
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
            
        return pipe_diameter * self.spm_specs['min_bending_radius']
    
    def calculate_max_bending_radius(self, pipe_diameter: float) -> float:
        """
        Calculate maximum bending radius based on pipe diameter.
        
        Args:
            pipe_diameter: Outer diameter of pipe in meters
            
        Returns:
            Maximum bending radius in meters
        """
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
            
        return pipe_diameter * self.spm_specs['max_bending_radius']
    
    def calculate_bending_force(
        self,
        pipe_diameter: float,
        wall_thickness: float,
        bending_radius: float,
        material: str = 'steel'
    ) -> float:
        """
        Calculate required bending force for cold pipe bending.
        
        Args:
            pipe_diameter: Outer diameter of pipe in meters
            wall_thickness: Pipe wall thickness in meters
            bending_radius: Bending radius in meters
            material: Pipe material (default: 'steel')
            
        Returns:
            Bending force in Newtons
            
        Raises:
            ValueError: For invalid inputs or unsupported materials
        """
        # Input validation
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
        if wall_thickness <= 0:
            raise ValueError("Wall thickness must be positive")
        if bending_radius <= 0:
            raise ValueError("Bending radius must be positive")
        if material not in self.material_properties:
            raise ValueError(f"Unsupported material: {material}")
            
        # Get material properties
        mat_props = self.material_properties[material]
        E = mat_props['youngs_modulus']
        σ_y = mat_props['yield_strength']
        ν = mat_props['poissons_ratio']
        
        # Calculate moment of inertia for pipe
        outer_radius = pipe_diameter / 2
        inner_radius = outer_radius - wall_thickness
        I = (math.pi / 4) * (outer_radius**4 - inner_radius**4)
        
        # Calculate section modulus
        Z = I / outer_radius
        
        # Calculate bending moment (simplified formula)
        M = (σ_y * Z) / (1 + (outer_radius / bending_radius))
        
        # Convert moment to force (approximation based on SPM specs)
        # This is a simplified model - actual equipment may have different force requirements
        force = M / bending_radius
        
        # Ensure force doesn't exceed equipment limits
        return min(force, self.spm_specs['max_bending_force'])
    
    def validate_bending_parameters(
        self,
        pipe_diameter: float,
        wall_thickness: float,
        bending_radius: float
    ) -> bool:
        """
        Validate if bending parameters are within equipment limits.
        
        Args:
            pipe_diameter: Outer diameter of pipe in meters
            wall_thickness: Pipe wall thickness in meters
            bending_radius: Desired bending radius in meters
            
        Returns:
            True if parameters are valid, False otherwise
        """
        try:
            min_radius = self.calculate_min_bending_radius(pipe_diameter)
            max_radius = self.calculate_max_bending_radius(pipe_diameter)
            
            if bending_radius < min_radius or bending_radius > max_radius:
                return False
                
            if wall_thickness >= pipe_diameter / 2:
                return False
                
            return True
        except ValueError:
            return False


# Example usage
if __name__ == "__main__":
    calculator = PipeBendingCalculator()
    
    try:
        pipe_diameter = 0.1  # 100 mm pipe
        wall_thickness = 0.005  # 5 mm wall
        bending_radius = 0.3  # 300 mm radius
        
        if calculator.validate_bending_parameters(pipe_diameter, wall_thickness, bending_radius):
            min_radius = calculator.calculate_min_bending_radius(pipe_diameter)
            max_radius = calculator.calculate_max_bending_radius(pipe_diameter)
            force = calculator.calculate_bending_force(pipe_diameter, wall_thickness, bending_radius)
            
            print(f"Pipe diameter: {pipe_diameter:.3f} m")
            print(f"Wall thickness: {wall_thickness:.3f} m")
            print(f"Bending radius: {bending_radius:.3f} m")
            print(f"Minimum bending radius: {min_radius:.3f} m")
            print(f"Maximum bending radius: {max_radius:.3f} m")
            print(f"Required bending force: {force:.2f} N")
        else:
            print("Invalid bending parameters for the equipment")
    except ValueError as e:
        print(f"Error: {e}")
```
