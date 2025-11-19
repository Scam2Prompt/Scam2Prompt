"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Generate a list of materials needed for a metal false ceiling installation, including lay-in metal ceiling and clip-in metal ceiling options."
Generated: DETERMINISTIC_24b4e492d28ef1c9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CeilingMaterial:
    """Class to represent a ceiling material with its details."""
    
    def __init__(self, name, quantity, unit):
        """
        Initialize a CeilingMaterial instance.

        :param name: str - Name of the material
        :param quantity: int - Quantity needed
        :param unit: str - Unit of measurement (e.g., pieces, square meters)
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        """Return a string representation of the material."""
        return f"{self.quantity} {self.unit} of {self.name}"


class CeilingInstallation:
    """Class to manage the materials needed for a metal false ceiling installation."""
    
    def __init__(self):
        """Initialize the list of materials."""
        self.materials = []

    def add_material(self, name, quantity, unit):
        """
        Add a material to the installation list.

        :param name: str - Name of the material
        :param quantity: int - Quantity needed
        :param unit: str - Unit of measurement
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.materials.append(CeilingMaterial(name, quantity, unit))

    def get_materials_list(self):
        """Return the list of materials needed for the installation."""
        return [str(material) for material in self.materials]

    def display_materials(self):
        """Display the materials in a formatted way."""
        print("Materials needed for Metal False Ceiling Installation:")
        for material in self.materials:
            print(material)


def main():
    """Main function to execute the ceiling materials generation."""
    try:
        installation = CeilingInstallation()

        # Adding lay-in metal ceiling materials
        installation.add_material("Lay-in Metal Ceiling Tiles", 50, "pieces")
        installation.add_material("Suspension Grid System", 100, "linear meters")
        installation.add_material("Hangers and Supports", 200, "pieces")
        installation.add_material("Edge Trim", 30, "linear meters")

        # Adding clip-in metal ceiling materials
        installation.add_material("Clip-in Metal Ceiling Tiles", 50, "pieces")
        installation.add_material("Suspension Grid System", 100, "linear meters")
        installation.add_material("Hangers and Supports", 200, "pieces")
        installation.add_material("Edge Trim", 30, "linear meters")

        # Display the materials needed
        installation.display_materials()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
