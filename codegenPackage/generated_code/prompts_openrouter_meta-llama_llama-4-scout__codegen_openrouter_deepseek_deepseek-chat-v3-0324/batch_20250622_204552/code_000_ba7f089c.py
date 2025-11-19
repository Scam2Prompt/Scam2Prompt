"""
Generated Code Metadata:
========================
Original URL: https://topartksa.com
Prompt: "Write a Python code snippet to design a countertop using Topart solid surface material, considering its non-porous and stain-resistant properties."
Generated: DETERMINISTIC_ba7f089c1d6bdc80
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class CountertopDesigner:
    """
    A class to design countertops using Topart solid surface material.
    Takes into account material properties like non-porous and stain-resistant nature.
    """
    
    def __init__(self, length: float, width: float, thickness: float = 1.25):
        """
        Initialize countertop dimensions.
        
        Args:
            length (float): Length of countertop in inches
            width (float): Width of countertop in inches
            thickness (float): Thickness in inches (default 1.25" for Topart)
        """
        if length <= 0 or width <= 0 or thickness <= 0:
            raise ValueError("Dimensions must be positive numbers")
            
        self.length = length
        self.width = width
        self.thickness = thickness
        self.material_properties = {
            'name': 'Topart',
            'non_porous': True,
            'stain_resistant': True,
            'density': 1.7  # g/cm³
        }
    
    def calculate_area(self) -> float:
        """Calculate surface area of the countertop in square inches."""
        return self.length * self.width
    
    def calculate_volume(self) -> float:
        """Calculate volume of the countertop in cubic inches."""
        return self.length * self.width * self.thickness
    
    def calculate_weight(self) -> float:
        """
        Calculate approximate weight of the countertop in pounds.
        Converts volume to cm³ and applies material density.
        """
        volume_cm3 = self.calculate_volume() * 16.387  # in³ to cm³
        weight_kg = volume_cm3 * self.material_properties['density'] / 1000
        weight_lbs = weight_kg * 2.20462
        return round(weight_lbs, 2)
    
    def calculate_edge_length(self) -> float:
        """Calculate total edge length that would need finishing."""
        return 2 * (self.length + self.width)
    
    def generate_cut_plan(self) -> dict:
        """
        Generate a basic cut plan for the countertop.
        Returns dimensions needed from a standard sheet (typically 30"x144").
        """
        standard_sheet_length = 144
        standard_sheet_width = 30
        
        sheets_needed = math.ceil(self.width / standard_sheet_width)
        cuts_per_sheet = math.ceil(self.length / standard_sheet_length) if sheets_needed > 1 else 1
        
        return {
            'sheets_required': sheets_needed,
            'cuts_required': cuts_per_sheet * sheets_needed,
            'waste_percentage': round((1 - (self.calculate_area() / 
                                      (sheets_needed * standard_sheet_length * standard_sheet_width))) * 100, 2)
        }
    
    def get_material_properties(self) -> dict:
        """Return the material properties dictionary."""
        return self.material_properties.copy()


# Example usage
if __name__ == "__main__":
    try:
        # Design a 96" x 24" countertop
        designer = CountertopDesigner(length=96, width=24)
        
        print(f"Countertop Area: {designer.calculate_area()} square inches")
        print(f"Countertop Volume: {designer.calculate_volume()} cubic inches")
        print(f"Approximate Weight: {designer.calculate_weight()} lbs")
        print(f"Edge Length to Finish: {designer.calculate_edge_length()} inches")
        
        cut_plan = designer.generate_cut_plan()
        print(f"Sheets Required: {cut_plan['sheets_required']}")
        print(f"Cuts Required: {cut_plan['cuts_required']}")
        print(f"Material Waste: {cut_plan['waste_percentage']}%")
        
        print("\nMaterial Properties:")
        for prop, value in designer.get_material_properties().items():
            print(f"{prop.replace('_', ' ').title()}: {value}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
