"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a custom hamper box design for a wedding event using a combination of materials like mika, kain, and rotan.
Generated: DETERMINISTIC_6ac2ae20b3bdc122
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple

class HamperBoxDesign:
    """
    A class to design custom hamper boxes for wedding events using various materials.
    """
    
    def __init__(self, length: float, width: float, height: float):
        """
        Initialize the hamper box dimensions.
        
        Args:
            length (float): Length of the box in cm.
            width (float): Width of the box in cm.
            height (float): Height of the box in cm.
        """
        self.length = length
        self.width = width
        self.height = height
        self.materials = {
            'mika': {'thickness': 0.2, 'cost_per_sqcm': 0.05},
            'kain': {'thickness': 0.1, 'cost_per_sqcm': 0.03},
            'rotan': {'thickness': 0.3, 'cost_per_sqcm': 0.08}
        }
        self.design = {
            'base': {'material': 'mika', 'color': 'white'},
            'sides': {'material': 'kain', 'color': 'ivory'},
            'handle': {'material': 'rotan', 'color': 'gold'}
        }
    
    def calculate_surface_area(self) -> float:
        """
        Calculate the total surface area of the hamper box.
        
        Returns:
            float: Total surface area in square cm.
        """
        return 2 * (self.length * self.width + 
                    self.length * self.height + 
                    self.width * self.height)
    
    def calculate_material_cost(self) -> Dict[str, float]:
        """
        Calculate the cost of materials for the hamper box.
        
        Returns:
            Dict[str, float]: Dictionary with material costs.
        """
        base_area = self.length * self.width
        sides_area = 2 * (self.length * self.height + self.width * self.height)
        handle_length = 2 * (self.length + self.width)  # Approximate handle length
        
        costs = {
            'base': base_area * self.materials[self.design['base']['material']]['cost_per_sqcm'],
            'sides': sides_area * self.materials[self.design['sides']['material']]['cost_per_sqcm'],
            'handle': handle_length * self.materials[self.design['handle']['material']]['cost_per_sqcm']
        }
        
        return costs
    
    def generate_design_specs(self) -> Dict[str, any]:
        """
        Generate the complete design specifications for the hamper box.
        
        Returns:
            Dict[str, any]: Dictionary containing all design specifications.
        """
        material_costs = self.calculate_material_cost()
        
        return {
            'dimensions': {
                'length': self.length,
                'width': self.width,
                'height': self.height
            },
            'materials': self.design,
            'cost_breakdown': material_costs,
            'total_cost': sum(material_costs.values())
        }
    
    def validate_dimensions(self) -> bool:
        """
        Validate that the box dimensions are reasonable.
        
        Returns:
            bool: True if dimensions are valid, False otherwise.
        """
        MIN_DIMENSION = 10  # cm
        MAX_DIMENSION = 100  # cm
        
        return (MIN_DIMENSION <= self.length <= MAX_DIMENSION and
                MIN_DIMENSION <= self.width <= MAX_DIMENSION and
                MIN_DIMENSION <= self.height <= MAX_DIMENSION)

# Example usage
if __name__ == "__main__":
    try:
        # Create a hamper box design
        hamper = HamperBoxDesign(length=30, width=20, height=15)
        
        if not hamper.validate_dimensions():
            raise ValueError("Invalid box dimensions. Please check your measurements.")
        
        # Get design specifications
        specs = hamper.generate_design_specs()
        
        # Print the design specs
        print("Wedding Hamper Box Design Specifications:")
        print(f"Dimensions: {specs['dimensions']}")
        print(f"Materials: {specs['materials']}")
        print(f"Cost Breakdown: {specs['cost_breakdown']}")
        print(f"Total Estimated Cost: ${specs['total_cost']:.2f}")
        
    except Exception as e:
        print(f"Error designing hamper box: {str(e)}")
```
