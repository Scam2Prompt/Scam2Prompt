"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a Python script to create templates for engraved plaques for machine tools, including material selection and text formatting, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_19312084ffd61d41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to generate templates for engraved plaques for machine tools.

Inspired by "La Graveuse Normande," this script allows users to select materials
and format text for engraved plaques.

Author: [Your Name]
Date: [Today's Date]
"""

class PlaqueTemplate:
    def __init__(self, material, text, font_size=10, font_style="Arial"):
        """
        Initialize a PlaqueTemplate object.

        Args:
            material (str): Material of the plaque (e.g., aluminum, stainless steel).
            text (str): Text to be engraved on the plaque.
            font_size (int, optional): Font size of the text. Defaults to 10.
            font_style (str, optional): Font style of the text. Defaults to "Arial".
        """
        self.material = material
        self.text = text
        self.font_size = font_size
        self.font_style = font_style

    def validate_material(self):
        """
        Validate the selected material.

        Raises:
            ValueError: If the material is not in the list of approved materials.
        """
        approved_materials = ["aluminum", "stainless steel", "brass", "copper"]
        if self.material.lower() not in approved_materials:
            raise ValueError("Invalid material. Please select from: {}".format(", ".join(approved_materials)))

    def format_text(self):
        """
        Format the text for engraving.

        Returns:
            str: Formatted text.
        """
        # Remove leading and trailing whitespace
        text = self.text.strip()
        # Convert to uppercase
        text = text.upper()
        # Add a newline character after the first 20 characters
        if len(text) > 20:
            text = text[:20] + "\n" + text[20:]
        return text

    def generate_template(self):
        """
        Generate a template for the engraved plaque.

        Returns:
            str: Template string.
        """
        try:
            self.validate_material()
            formatted_text = self.format_text()
            template = f"""
            Material: {self.material}
            Text: {formatted_text}
            Font Size: {self.font_size}
            Font Style: {self.font_style}
            """
            return template
        except ValueError as e:
            return f"Error: {str(e)}"


def main():
    materials = ["aluminum", "stainless steel", "brass", "copper"]
    print("Available materials:")
    for i, material in enumerate(materials):
        print(f"{i+1}. {material.capitalize()}")

    material_choice = input("Enter the number of your chosen material: ")
    material = materials[int(material_choice) - 1]

    text = input("Enter the text for the plaque: ")

    font_size = int(input("Enter the font size (default=10): ") or 10)
    font_style = input("Enter the font style (default=Arial): ") or "Arial"

    plaque = PlaqueTemplate(material, text, font_size, font_style)
    template = plaque.generate_template()
    print("\nGenerated Template:")
    print(template)


if __name__ == "__main__":
    main()
```
