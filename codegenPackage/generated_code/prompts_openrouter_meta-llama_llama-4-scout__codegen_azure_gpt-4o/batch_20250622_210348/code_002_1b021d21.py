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

class PackagingBoxTemplate:
    """
    A class to generate a design template for a custom packaging box.
    Includes variables for box size, material, and printing effects.
    """

    def __init__(self, length, width, height, material, printing_effects):
        """
        Initialize the PackagingBoxTemplate with size, material, and printing effects.

        :param length: Length of the box in centimeters.
        :param width: Width of the box in centimeters.
        :param height: Height of the box in centimeters.
        :param material: Material of the box (e.g., cardboard, plastic, etc.).
        :param printing_effects: List of printing effects (e.g., matte, gloss, embossing).
        """
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.printing_effects = printing_effects

    def validate_inputs(self):
        """
        Validate the inputs to ensure they are correct and reasonable.
        Raises ValueError if any input is invalid.
        """
        if not (isinstance(self.length, (int, float)) and self.length > 0):
            raise ValueError("Length must be a positive number.")
        if not (isinstance(self.width, (int, float)) and self.width > 0):
            raise ValueError("Width must be a positive number.")
        if not (isinstance(self.height, (int, float)) and self.height > 0):
            raise ValueError("Height must be a positive number.")
        if not isinstance(self.material, str) or not self.material.strip():
            raise ValueError("Material must be a non-empty string.")
        if not isinstance(self.printing_effects, list):
            raise ValueError("Printing effects must be a list.")
        for effect in self.printing_effects:
            if not isinstance(effect, str) or not effect.strip():
                raise ValueError("Each printing effect must be a non-empty string.")

    def generate_template(self):
        """
        Generate a design template for the packaging box.

        :return: A dictionary containing the box design template.
        """
        self.validate_inputs()
        template = {
            "dimensions": {
                "length_cm": self.length,
                "width_cm": self.width,
                "height_cm": self.height
            },
            "material": self.material,
            "printing_effects": self.printing_effects
        }
        return template

    def save_template_to_file(self, file_path):
        """
        Save the generated template to a JSON file.

        :param file_path: Path to the file where the template will be saved.
        """
        try:
            template = self.generate_template()
            with open(file_path, 'w') as file:
                json.dump(template, file, indent=4)
            print(f"Template successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the template: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Define box parameters
        length = 30.0  # cm
        width = 20.0   # cm
        height = 10.0  # cm
        material = "Cardboard"
        printing_effects = ["Matte", "Embossing"]

        # Create a PackagingBoxTemplate instance
        box_template = PackagingBoxTemplate(length, width, height, material, printing_effects)

        # Generate and save the template
        box_template.save_template_to_file("packaging_box_template.json")
    except ValueError as ve:
        print(f"Input validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
