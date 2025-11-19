"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Create a program that calculates the dimensions and material requirements for a porch built with Fortic's rustic-style concrete beams.
Generated: DETERMINISTIC_d3a7f45505877e30
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PorchCalculator:
    """
    A class to calculate the dimensions and material requirements for a porch built with Fortic's rustic-style concrete beams.
    """
    
    def __init__(self, length, width, beam_length=2.0, beam_width=0.15, beam_height=0.2, beam_spacing=0.4):
        """
        Initialize the PorchCalculator with porch dimensions and beam specifications.
        
        Args:
            length (float): Length of the porch in meters.
            width (float): Width of the porch in meters.
            beam_length (float, optional): Length of each beam in meters. Defaults to 2.0.
            beam_width (float, optional): Width of each beam in meters. Defaults to 0.15.
            beam_height (float, optional): Height of each beam in meters. Defaults to 0.2.
            beam_spacing (float, optional): Spacing between beams in meters. Defaults to 0.4.
        """
        self.length = length
        self.width = width
        self.beam_length = beam_length
        self.beam_width = beam_width
        self.beam_height = beam_height
        self.beam_spacing = beam_spacing
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate that all inputs are positive numbers."""
        if any(val <= 0 for val in [self.length, self.width, self.beam_length, 
                                   self.beam_width, self.beam_height, self.beam_spacing]):
            raise ValueError("All dimensions must be positive numbers.")
        
        if self.beam_spacing < self.beam_width:
            raise ValueError("Beam spacing must be greater than beam width.")
    
    def calculate_number_of_beams(self):
        """
        Calculate the number of beams required along the width of the porch.
        
        Returns:
            int: Number of beams required.
        """
        effective_width = self.width - self.beam_width
        if effective_width <= 0:
            return 1
        
        number_of_spaces = math.ceil(effective_width / self.beam_spacing)
        return number_of_spaces + 1
    
    def calculate_total_beam_length(self):
        """
        Calculate the total length of all beams required.
        
        Returns:
            float: Total beam length in meters.
        """
        number_of_beams = self.calculate_number_of_beams()
        return number_of_beams * self.beam_length
    
    def calculate_concrete_volume(self):
        """
        Calculate the total volume of concrete required for all beams.
        
        Returns:
            float: Total concrete volume in cubic meters.
        """
        beam_volume = self.beam_length * self.beam_width * self.beam_height
        return beam_volume * self.calculate_number_of_beams()
    
    def generate_materials_report(self):
        """
        Generate a report of material requirements for the porch.
        
        Returns:
            dict: Dictionary containing material requirements.
        """
        return {
            "porch_dimensions": {
                "length": self.length,
                "width": self.width
            },
            "beam_specifications": {
                "length": self.beam_length,
                "width": self.beam_width,
                "height": self.beam_height,
                "spacing": self.beam_spacing
            },
            "material_requirements": {
                "number_of_beams": self.calculate_number_of_beams(),
                "total_beam_length": round(self.calculate_total_beam_length(), 2),
                "total_concrete_volume": round(self.calculate_concrete_volume(), 3)
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a porch calculator instance
        porch = PorchCalculator(length=5.0, width=3.0)
        
        # Generate and print the materials report
        report = porch.generate_materials_report()
        print("Porch Materials Report:")
        print(f"Porch Dimensions: {report['porch_dimensions']['length']}m x {report['porch_dimensions']['width']}m")
        print(f"Beam Specifications: Length={report['beam_specifications']['length']}m, "
              f"Width={report['beam_specifications']['width']}m, "
              f"Height={report['beam_specifications']['height']}m, "
              f"Spacing={report['beam_specifications']['spacing']}m")
        print(f"Number of Beams Required: {report['material_requirements']['number_of_beams']}")
        print(f"Total Beam Length: {report['material_requirements']['total_beam_length']}m")
        print(f"Total Concrete Volume: {report['material_requirements']['total_concrete_volume']}m³")
    
    except ValueError as e:
        print(f"Error: {e}")
```
