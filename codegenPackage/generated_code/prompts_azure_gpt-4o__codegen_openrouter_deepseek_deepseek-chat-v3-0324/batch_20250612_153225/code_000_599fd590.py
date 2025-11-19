"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Write Python code to calculate the load distribution for screw piles with dimensions ranging from Ø60 mm to Ø114 mm and thicknesses between 2 mm and 6 mm, as described on the His Teknik Çelik website.
Generated: DETERMINISTIC_599fd5909c4cba3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ScrewPile:
    """
    A class to represent a screw pile and calculate its load distribution.
    
    Attributes:
        diameter (float): Diameter of the screw pile in mm.
        thickness (float): Thickness of the screw pile wall in mm.
        material_yield_strength (float): Yield strength of the material in MPa (default: 235 MPa for S235 steel).
    """
    
    def __init__(self, diameter: float, thickness: float, material_yield_strength: float = 235.0):
        """
        Initialize the ScrewPile with diameter, thickness, and material yield strength.
        
        Args:
            diameter (float): Diameter in mm (60 to 114 mm).
            thickness (float): Thickness in mm (2 to 6 mm).
            material_yield_strength (float): Yield strength in MPa (default: 235 MPa).
            
        Raises:
            ValueError: If diameter or thickness is out of specified range.
        """
        if not (60 <= diameter <= 114):
            raise ValueError("Diameter must be between 60 mm and 114 mm.")
        if not (2 <= thickness <= 6):
            raise ValueError("Thickness must be between 2 mm and 6 mm.")
        if material_yield_strength <= 0:
            raise ValueError("Material yield strength must be positive.")
            
        self.diameter = diameter
        self.thickness = thickness
        self.material_yield_strength = material_yield_strength
    
    def calculate_cross_sectional_area(self) -> float:
        """
        Calculate the cross-sectional area of the screw pile.
        
        Returns:
            float: Cross-sectional area in mm².
        """
        outer_radius = self.diameter / 2
        inner_radius = outer_radius - self.thickness
        return math.pi * (outer_radius**2 - inner_radius**2)
    
    def calculate_axial_load_capacity(self) -> float:
        """
        Calculate the axial load capacity of the screw pile.
        
        Returns:
            float: Axial load capacity in kN.
        """
        area = self.calculate_cross_sectional_area()
        return (area * self.material_yield_strength) / 1000  # Convert N to kN
    
    def calculate_lateral_load_capacity(self, unsupported_length: float, fixity_factor: float = 2.0) -> float:
        """
        Calculate the lateral load capacity of the screw pile.
        
        Args:
            unsupported_length (float): Unsupported length of the pile in meters.
            fixity_factor (float): Fixity factor (1.0 for pinned, 2.0 for fixed, default: 2.0).
            
        Returns:
            float: Lateral load capacity in kN.
            
        Raises:
            ValueError: If unsupported_length or fixity_factor is not positive.
        """
        if unsupported_length <= 0:
            raise ValueError("Unsupported length must be positive.")
        if fixity_factor <= 0:
            raise ValueError("Fixity factor must be positive.")
            
        # Calculate moment of inertia
        outer_radius = self.diameter / 2
        inner_radius = outer_radius - self.thickness
        moment_of_inertia = (math.pi / 4) * (outer_radius**4 - inner_radius**4)
        
        # Euler's critical load formula (converted to kN)
        euler_load = (math.pi**2 * 200000 * moment_of_inertia) / ((fixity_factor * unsupported_length * 1000)**2)
        return euler_load / 1000  # Convert N to kN

# Example usage
if __name__ == "__main__":
    try:
        # Create a screw pile instance
        pile = ScrewPile(diameter=89.0, thickness=3.2)
        
        # Calculate and print load capacities
        print(f"Cross-sectional area: {pile.calculate_cross_sectional_area():.2f} mm²")
        print(f"Axial load capacity: {pile.calculate_axial_load_capacity():.2f} kN")
        print(f"Lateral load capacity (5m unsupported): {pile.calculate_lateral_load_capacity(5.0):.2f} kN")
    except ValueError as e:
        print(f"Error: {e}")
```
