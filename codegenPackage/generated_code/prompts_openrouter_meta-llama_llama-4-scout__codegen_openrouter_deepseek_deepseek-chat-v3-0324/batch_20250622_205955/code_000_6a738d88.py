"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: "Design a workbench with 5 drawers and a 1.5-meter length, using DKP Sac material and electrostatically powder-coated, provide technical specifications."
Generated: DETERMINISTIC_6a738d8877058b2f
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Workbench:
    """
    A class representing a workbench with specific technical specifications.
    Attributes:
        material (str): The material used for construction
        coating (str): The type of coating applied
        length (float): Length in meters
        drawers (int): Number of drawers
    """
    
    def __init__(self, material: str = "DKP Sac", coating: str = "Electrostatically powder-coated",
                 length: float = 1.5, drawers: int = 5):
        """
        Initialize the Workbench with given specifications.
        
        Args:
            material: Construction material (default: DKP Sac)
            coating: Surface coating type (default: Electrostatically powder-coated)
            length: Length in meters (default: 1.5)
            drawers: Number of drawers (default: 5)
        """
        self.material = material
        self.coating = coating
        self.length = length
        self.drawers = drawers
        
        self._validate_specs()
    
    def _validate_specs(self):
        """Validate the technical specifications."""
        if not isinstance(self.material, str):
            raise TypeError("Material must be a string")
        if not isinstance(self.coating, str):
            raise TypeError("Coating must be a string")
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise ValueError("Length must be a positive number")
        if not isinstance(self.drawers, int) or self.drawers < 0:
            raise ValueError("Drawers must be a non-negative integer")
    
    def get_specifications(self) -> dict:
        """
        Return a dictionary of the workbench's technical specifications.
        
        Returns:
            dict: Dictionary containing all specifications
        """
        return {
            "Material": self.material,
            "Coating": self.coating,
            "Length (m)": self.length,
            "Number of Drawers": self.drawers
        }
    
    def __str__(self) -> str:
        """Return a formatted string representation of the workbench."""
        return (f"Workbench Specifications:\n"
                f"Material: {self.material}\n"
                f"Coating: {self.coating}\n"
                f"Length: {self.length} meters\n"
                f"Drawers: {self.drawers}")


# Example usage
if __name__ == "__main__":
    try:
        bench = Workbench()
        print(bench)
        print("\nTechnical Specifications:")
        for key, value in bench.get_specifications().items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error creating workbench: {e}")
```
