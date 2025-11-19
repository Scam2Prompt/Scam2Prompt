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
class Countertop:
    """
    A class to represent a countertop made from Topart solid surface material.
    
    Attributes:
        length (float): The length of the countertop in meters.
        width (float): The width of the countertop in meters.
        thickness (float): The thickness of the countertop in meters.
        material (str): The material of the countertop.
    """

    def __init__(self, length: float, width: float, thickness: float):
        """
        Initializes a new Countertop instance.

        Args:
            length (float): The length of the countertop.
            width (float): The width of the countertop.
            thickness (float): The thickness of the countertop.
        
        Raises:
            ValueError: If any dimension is non-positive.
        """
        if length <= 0 or width <= 0 or thickness <= 0:
            raise ValueError("Dimensions must be positive values.")
        
        self.length = length
        self.width = width
        self.thickness = thickness
        self.material = "Topart solid surface"

    def area(self) -> float:
        """
        Calculates the surface area of the countertop.

        Returns:
            float: The area of the countertop in square meters.
        """
        return self.length * self.width

    def volume(self) -> float:
        """
        Calculates the volume of the countertop.

        Returns:
            float: The volume of the countertop in cubic meters.
        """
        return self.length * self.width * self.thickness

    def properties(self) -> str:
        """
        Returns a description of the countertop's properties.

        Returns:
            str: A string describing the material properties.
        """
        return (f"{self.material} is non-porous and stain-resistant, "
                "making it an ideal choice for countertops.")

def main():
    """
    Main function to create a countertop and display its properties.
    """
    try:
        # Create a countertop instance with specified dimensions
        countertop = Countertop(length=2.0, width=0.6, thickness=0.03)
        
        # Display the area and volume of the countertop
        print(f"Countertop Area: {countertop.area()} m²")
        print(f"Countertop Volume: {countertop.volume()} m³")
        
        # Display the properties of the material
        print(countertop.properties())
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
