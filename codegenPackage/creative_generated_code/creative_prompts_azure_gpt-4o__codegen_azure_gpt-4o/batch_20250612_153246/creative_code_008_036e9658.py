"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write a program to design and format engraved professional plaques with mounting options like screws and adhesive, as detailed on "La Graveuse Normande."
Generated: DETERMINISTIC_036e9658e102a3ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PlaqueDesigner:
    """
    Class to design and format engraved professional plaques with mounting options.
    """

    def __init__(self):
        # Supported materials and colors
        self.materials = ["Metal", "Wood", "Acrylic"]
        self.colors = ["Silver", "Gold", "Black", "White", "Bronze"]

        # Supported mounting options
        self.mounting_options = ["Screws", "Adhesive"]

        # Default dimensions (in cm)
        self.default_dimensions = {"width": 15, "height": 10}

    def design_plaque(self, text: str, material: str, color: str, dimensions: dict = None):
        """
        Design a plaque with specified text, material, color, and dimensions.

        Args:
            text (str): The engraved text on the plaque.
            material (str): The material for the plaque.
            color (str): The color of the plaque.
            dimensions (dict): A dictionary containing width and height in cm.

        Returns:
            dict: Design details for the plaque.
        """
        # Validate material
        if material not in self.materials:
            raise ValueError(f"Invalid material. Supported materials are: {', '.join(self.materials)}")

        # Validate color
        if color not in self.colors:
            raise ValueError(f"Invalid color. Supported colors are: {', '.join(self.colors)}")

        # Validate dimensions
        if dimensions:
            if "width" not in dimensions or "height" not in dimensions:
                raise ValueError("Dimensions must include 'width' and 'height'.")
            if dimensions["width"] <= 0 or dimensions["height"] <= 0:
                raise ValueError("Dimensions must be positive values.")
        else:
            dimensions = self.default_dimensions

        # Create plaque design
        plaque_design = {
            "text": text,
            "material": material,
            "color": color,
            "dimensions": dimensions,
        }
        return plaque_design

    def add_mounting_option(self, plaque_design: dict, mounting_option: str):
        """
        Add a mounting option to the plaque design.

        Args:
            plaque_design (dict): The existing plaque design details.
            mounting_option (str): Mounting option to add (e.g., "Screws", "Adhesive").

        Returns:
            dict: Updated plaque design with mounting options included.
        """
        # Validate mounting option
        if mounting_option not in self.mounting_options:
            raise ValueError(f"Invalid mounting option. Supported options are: {', '.join(self.mounting_options)}")

        # Add mounting option to design
        plaque_design["mounting_option"] = mounting_option
        return plaque_design

    def save_design_to_file(self, plaque_design: dict, filename: str):
        """
        Save the plaque design to a JSON file.

        Args:
            plaque_design (dict): The plaque design details to save.
            filename (str): The name of the file to save the design.
        """
        try:
            with open(filename, "w") as file:
                json.dump(plaque_design, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while saving the file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        designer = PlaqueDesigner()

        # Design plaque
        plaque = designer.design_plaque(
            text="La Graveuse Normande - Excellence in Engraving",
            material="Metal",
            color="Gold",
            dimensions={"width": 20, "height": 15},
        )

        # Add mounting option
        plaque = designer.add_mounting_option(plaque_design=plaque, mounting_option="Screws")

        # Save plaque design to file
        designer.save_design_to_file(plaque_design=plaque, filename="plaque_design.json")

        print("Plaque design saved successfully!")
    except Exception as e:
        print(f"Error: {e}")
```
