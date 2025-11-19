"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Design a raised access flooring system for a data centre using calcium sulphate materials."
Generated: DETERMINISTIC_24236b5b3842a9e8
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Raised Access Flooring System Design

class FlooringMaterial:
    """Base class for flooring materials."""
    
    def __init__(self, name, compressive_strength, thickness):
        """
        Initialize a flooring material.

        Args:
            name (str): Name of the material.
            compressive_strength (float): Compressive strength of the material in MPa.
            thickness (float): Thickness of the material in mm.
        """
        self.name = name
        self.compressive_strength = compressive_strength
        self.thickness = thickness


class CalciumSulphateMaterial(FlooringMaterial):
    """Calcium sulphate material for raised access flooring."""

    def __init__(self, compressive_strength=20, thickness=20):
        """
        Initialize a calcium sulphate material.

        Args:
            compressive_strength (float, optional): Compressive strength in MPa. Defaults to 20.
            thickness (float, optional): Thickness in mm. Defaults to 20.
        """
        super().__init__("Calcium Sulphate", compressive_strength, thickness)


class RaisedAccessFloor:
    """Raised access floor design."""

    def __init__(self, length, width, material, pedestal_height, tile_thickness):
        """
        Initialize a raised access floor.

        Args:
            length (float): Length of the floor in meters.
            width (float): Width of the floor in meters.
            material (FlooringMaterial): Flooring material.
            pedestal_height (float): Height of the pedestal in mm.
            tile_thickness (float): Thickness of the floor tile in mm.
        """
        self.length = length
        self.width = width
        self.material = material
        self.pedestal_height = pedestal_height
        self.tile_thickness = tile_thickness

    def calculate_total_thickness(self):
        """
        Calculate the total thickness of the raised access floor.

        Returns:
            float: Total thickness in mm.
        """
        return self.pedestal_height + self.tile_thickness

    def check_compressive_strength(self, load):
        """
        Check if the material can withstand a given load.

        Args:
            load (float): Load in kg/m².

        Returns:
            bool: True if the material can withstand the load, False otherwise.
        """
        # Assume a safety factor of 2
        safety_factor = 2
        max_load = self.material.compressive_strength * 1000 / safety_factor
        return load <= max_load


def design_raised_access_flooring(length, width, compressive_strength, thickness, pedestal_height, tile_thickness, load):
    """
    Design a raised access flooring system.

    Args:
        length (float): Length of the floor in meters.
        width (float): Width of the floor in meters.
        compressive_strength (float): Compressive strength of the material in MPa.
        thickness (float): Thickness of the material in mm.
        pedestal_height (float): Height of the pedestal in mm.
        tile_thickness (float): Thickness of the floor tile in mm.
        load (float): Load in kg/m².

    Returns:
        RaisedAccessFloor: Raised access floor design.
    """
    material = CalciumSulphateMaterial(compressive_strength, thickness)
    floor = RaisedAccessFloor(length, width, material, pedestal_height, tile_thickness)

    if not floor.check_compressive_strength(load):
        raise ValueError("The material cannot withstand the given load.")

    return floor


# Example usage
if __name__ == "__main__":
    try:
        length = 10  # meters
        width = 5   # meters
        compressive_strength = 25  # MPa
        thickness = 20  # mm
        pedestal_height = 100  # mm
        tile_thickness = 20  # mm
        load = 500  # kg/m²

        floor = design_raised_access_flooring(length, width, compressive_strength, thickness, pedestal_height, tile_thickness, load)
        print(f"Raised Access Floor Design:")
        print(f"Material: {floor.material.name}")
        print(f"Total Thickness: {floor.calculate_total_thickness()} mm")
        print(f"Pedestal Height: {floor.pedestal_height} mm")
        print(f"Tile Thickness: {floor.tile_thickness} mm")

    except Exception as e:
        print(f"Error: {str(e)}")
```
