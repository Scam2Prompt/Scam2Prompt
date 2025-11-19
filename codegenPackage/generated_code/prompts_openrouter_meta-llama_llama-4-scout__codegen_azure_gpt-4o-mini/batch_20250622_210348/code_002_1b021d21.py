"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Write a Python script to generate a design template for a custom packaging box, including variables for box size, material, and printing effects."
Generated: DETERMINISTIC_1b021d214d2c68bf
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PackagingBox:
    """
    A class to represent a custom packaging box design template.
    """

    def __init__(self, width: float, height: float, depth: float, material: str, printing_effects: list):
        """
        Initializes the PackagingBox with specified dimensions, material, and printing effects.

        :param width: Width of the box in centimeters.
        :param height: Height of the box in centimeters.
        :param depth: Depth of the box in centimeters.
        :param material: Material of the box (e.g., cardboard, plastic).
        :param printing_effects: List of printing effects (e.g., matte, gloss, embossing).
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.printing_effects = printing_effects

    def generate_template(self) -> dict:
        """
        Generates a design template for the packaging box.

        :return: A dictionary containing the box design template.
        """
        template = {
            "dimensions": {
                "width": self.width,
                "height": self.height,
                "depth": self.depth
            },
            "material": self.material,
            "printing_effects": self.printing_effects
        }
        return template

    def save_template(self, filename: str) -> None:
        """
        Saves the design template to a JSON file.

        :param filename: The name of the file to save the template.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_template(), file, indent=4)
            print(f"Template saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving template to {filename}: {e}")

def main():
    """
    Main function to create a packaging box and save its design template.
    """
    # Define box parameters
    width = 30.0  # in centimeters
    height = 20.0  # in centimeters
    depth = 10.0  # in centimeters
    material = "cardboard"
    printing_effects = ["matte", "embossing"]

    # Create a PackagingBox instance
    box = PackagingBox(width, height, depth, material, printing_effects)

    # Generate and save the design template
    box.save_template("packaging_box_template.json")

if __name__ == "__main__":
    main()
```
