"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Design a custom box packaging for a company's Christmas event using materials like mika, rotan, or paperbag.
Generated: DETERMINISTIC_ac45302afdd196d8
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

class BoxDesign:
    """
    A class to design custom packaging boxes for a company's Christmas event.
    Supports materials like mika, rotan, and paperbag.
    """
    
    def __init__(self, length, width, height, material="paperbag"):
        """
        Initialize box dimensions and material.
        
        Args:
            length (float): Length of the box in cm
            width (float): Width of the box in cm
            height (float): Height of the box in cm
            material (str): Material type ('mika', 'rotan', 'paperbag')
        """
        self.length = length
        self.width = width
        self.height = height
        self.material = material.lower()
        self.validate_dimensions()
        self.validate_material()
        
    def validate_dimensions(self):
        """Ensure all dimensions are positive numbers."""
        if any(dim <= 0 for dim in [self.length, self.width, self.height]):
            raise ValueError("All dimensions must be positive numbers")
            
    def validate_material(self):
        """Ensure material is one of the supported types."""
        valid_materials = ['mika', 'rotan', 'paperbag']
        if self.material not in valid_materials:
            raise ValueError(f"Material must be one of: {', '.join(valid_materials)}")
    
    def calculate_surface_area(self):
        """Calculate total surface area of the box."""
        return 2 * (self.length * self.width + 
                    self.length * self.height + 
                    self.width * self.height)
    
    def calculate_volume(self):
        """Calculate internal volume of the box."""
        return self.length * self.width * self.height
    
    def calculate_material_cost(self, cost_per_sqcm):
        """
        Calculate material cost based on surface area.
        
        Args:
            cost_per_sqcm (float): Cost per square cm of material
            
        Returns:
            float: Total material cost
        """
        if cost_per_sqcm <= 0:
            raise ValueError("Cost per square cm must be positive")
        return self.calculate_surface_area() * cost_per_sqcm
    
    def generate_design_template(self):
        """Generate a design template based on material."""
        designs = {
            'mika': self._generate_mika_design(),
            'rotan': self._generate_rotan_design(),
            'paperbag': self._generate_paperbag_design()
        }
        return designs[self.material]
    
    def _generate_mika_design(self):
        """Generate design template for mika material."""
        return {
            'material': 'Mika',
            'design': 'Glossy finish with embossed Christmas patterns',
            'recommendations': [
                'Use gold or silver accents',
                'Add ribbon for premium look'
            ]
        }
    
    def _generate_rotan_design(self):
        """Generate design template for rotan material."""
        return {
            'material': 'Rotan',
            'design': 'Natural woven look with festive accents',
            'recommendations': [
                'Use red and green ribbons',
                'Add small Christmas ornaments'
            ]
        }
    
    def _generate_paperbag_design(self):
        """Generate design template for paperbag material."""
        return {
            'material': 'Paperbag',
            'design': 'Eco-friendly kraft paper with printed designs',
            'recommendations': [
                'Use biodegradable inks',
                'Add a sprig of pine for fragrance'
            ]
        }
    
    def print_design_specs(self):
        """Print complete design specifications."""
        design = self.generate_design_template()
        print("\nCustom Christmas Packaging Box Specifications:")
        print(f"Material: {design['material']}")
        print(f"Dimensions: {self.length}cm × {self.width}cm × {self.height}cm")
        print(f"Volume: {self.calculate_volume():.2f} cm³")
        print(f"Surface Area: {self.calculate_surface_area():.2f} cm²")
        print("\nDesign Features:")
        print(f"- {design['design']}")
        print("\nDesign Recommendations:")
        for rec in design['recommendations']:
            print(f"- {rec}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a Christmas gift box
        christmas_box = BoxDesign(
            length=30, 
            width=20, 
            height=15, 
            material="mika"
        )
        
        # Print design specifications
        christmas_box.print_design_specs()
        
        # Calculate material cost (example cost)
        cost = christmas_box.calculate_material_cost(0.02)
        print(f"\nEstimated Material Cost: ${cost:.2f}")
        
    except ValueError as e:
        print(f"Error creating box design: {e}")
```
