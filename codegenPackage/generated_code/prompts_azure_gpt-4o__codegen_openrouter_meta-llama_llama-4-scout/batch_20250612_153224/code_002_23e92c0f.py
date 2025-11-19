"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Create a code snippet using a CAD API to design a "bed loft" for a small bedroom, inspired by Nyiku Design's blog tips on maximizing space in small rooms.
Generated: DETERMINISTIC_23e92c0f58dd6d42
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math
from typing import Dict

class BedLoft:
    """
    A class representing a bed loft design.

    Attributes:
    -----------
    length : float
        The length of the bed loft.
    width : float
        The width of the bed loft.
    height : float
        The height of the bed loft.
    material : str
        The material used for the bed loft.

    Methods:
    --------
    calculate_volume() -> float:
        Calculates the volume of the bed loft.
    calculate_surface_area() -> float:
        Calculates the surface area of the bed loft.
    """

    def __init__(self, length: float, width: float, height: float, material: str):
        """
        Initializes a BedLoft object.

        Args:
        -----
        length (float): The length of the bed loft.
        width (float): The width of the bed loft.
        height (float): The height of the bed loft.
        material (str): The material used for the bed loft.

        Raises:
        ------
        ValueError: If any dimension is non-positive.
        """
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")

        self.length = length
        self.width = width
        self.height = height
        self.material = material

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the bed loft.

        Returns:
        -------
        float: The volume of the bed loft.
        """
        return self.length * self.width * self.height

    def calculate_surface_area(self) -> float:
        """
        Calculates the surface area of the bed loft.

        Returns:
        -------
        float: The surface area of the bed loft.
        """
        # Calculate surface area of all sides
        surface_area = 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
        return surface_area


class CAD_API:
    """
    A class representing a CAD API.

    Attributes:
    -----------
    designs : Dict[str, BedLoft]
        A dictionary of bed loft designs.

    Methods:
    --------
    create_design(name: str, length: float, width: float, height: float, material: str) -> None:
        Creates a new bed loft design.
    get_design(name: str) -> BedLoft:
        Retrieves a bed loft design by name.
    """

    def __init__(self):
        """
        Initializes a CAD_API object.
        """
        self.designs = {}

    def create_design(self, name: str, length: float, width: float, height: float, material: str) -> None:
        """
        Creates a new bed loft design.

        Args:
        -----
        name (str): The name of the design.
        length (float): The length of the bed loft.
        width (float): The width of the bed loft.
        height (float): The height of the bed loft.
        material (str): The material used for the bed loft.

        Raises:
        ------
        ValueError: If a design with the same name already exists.
        """
        if name in self.designs:
            raise ValueError("Design with the same name already exists.")

        self.designs[name] = BedLoft(length, width, height, material)

    def get_design(self, name: str) -> BedLoft:
        """
        Retrieves a bed loft design by name.

        Args:
        -----
        name (str): The name of the design.

        Returns:
        -------
        BedLoft: The bed loft design.

        Raises:
        ------
        ValueError: If the design does not exist.
        """
        if name not in self.designs:
            raise ValueError("Design does not exist.")

        return self.designs[name]


def main():
    # Create a CAD API object
    cad_api = CAD_API()

    # Create a new bed loft design inspired by Nyiku Design's blog tips
    # Assuming a small bedroom with limited space, let's design a bed loft with the following dimensions:
    # Length: 80 inches (203.2 cm), Width: 60 inches (152.4 cm), Height: 40 inches (101.6 cm)
    # Material: Wood
    cad_api.create_design("Small Bedroom Bed Loft", 80, 60, 40, "Wood")

    # Retrieve the design
    design = cad_api.get_design("Small Bedroom Bed Loft")

    # Calculate and print the volume and surface area of the bed loft
    print(f"Design Name: Small Bedroom Bed Loft")
    print(f"Volume: {design.calculate_volume()} cubic inches")
    print(f"Surface Area: {design.calculate_surface_area()} square inches")


if __name__ == "__main__":
    main()
```
