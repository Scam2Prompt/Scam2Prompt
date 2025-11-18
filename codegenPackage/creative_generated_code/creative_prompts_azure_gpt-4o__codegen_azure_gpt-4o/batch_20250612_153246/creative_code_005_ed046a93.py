"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Write code to design and export templates for engraved intercom or signage plaques, ensuring compatibility with laser engraving machines, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_ed046a93ab51093c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black
import traceback


class EngravingTemplateGenerator:
    """
    A class to generate engraved intercom or signage plaques templates compatible with laser engraving machines.

    Attributes:
        output_directory (str): Directory where the generated templates will be saved.
    """

    def __init__(self, output_directory="engraving_templates"):
        """
        Initialize the EngravingTemplateGenerator with an output directory.

        Args:
            output_directory (str): Directory where the templates will be saved.
        """
        self.output_directory = output_directory
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """
        Ensure the output directory exists. Create it if it doesn't.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def create_template(self, filename, plaque_dimensions, text_lines, font="Helvetica-Bold", font_size=12):
        """
        Generate a plaque template as a PDF file.

        Args:
            filename (str): Name of the output file (without extension).
            plaque_dimensions (tuple): Dimensions of the plaque (width, height) in mm.
            text_lines (list): Lines of text to engrave on the plaque.
            font (str): Font type for the text (default is Helvetica-Bold).
            font_size (int): Font size for the text (default is 12).
        """
        try:
            # Convert dimensions from mm to points (1mm = 2.83465 points)
            width, height = plaque_dimensions[0] * 2.83465, plaque_dimensions[1] * 2.83465

            # Set up the canvas
            file_path = os.path.join(self.output_directory, f"{filename}.pdf")
            c = canvas.Canvas(file_path, pagesize=(width, height))
            c.setFillColor(black)
            c.setFont(font, font_size)

            # Calculate vertical spacing and center the text
            y_position = height - font_size * 2  # Start near the top for the first line
            for line in text_lines:
                c.drawCentredString(width / 2, y_position, line)
                y_position -= font_size * 2  # Move down for the next line

            # Finalize the template
            c.save()
            print(f"Template '{filename}.pdf' created successfully in {self.output_directory}.")
        except Exception as e:
            print(f"An error occurred while creating the template: {e}")
            traceback.print_exc()

    def export_batch_templates(self, templates):
        """
        Generate multiple plaque templates in batch.

        Args:
            templates (list): List of template details. Each entry should be a dictionary
                              containing 'filename', 'plaque_dimensions', 'text_lines', 'font', and 'font_size'.
        """
        for template in templates:
            try:
                self.create_template(
                    filename=template["filename"],
                    plaque_dimensions=template["plaque_dimensions"],
                    text_lines=template["text_lines"],
                    font=template.get("font", "Helvetica-Bold"),
                    font_size=template.get("font_size", 12),
                )
            except KeyError as ke:
                print(f"Missing key in template definition: {ke}")
                traceback.print_exc()


# Example usage
if __name__ == "__main__":
    generator = EngravingTemplateGenerator()

    # Create a single template
    generator.create_template(
        filename="example_plaque",
        plaque_dimensions=(100, 50),  # 100mm x 50mm
        text_lines=["La Graveuse Normande", "Custom Engraving Solutions"],
        font="Helvetica-Bold",
        font_size=14
    )

    # Create multiple templates as a batch
    batch_templates = [
        {
            "filename": "welcome_sign",
            "plaque_dimensions": (120, 60),
            "text_lines": ["Welcome to", "Our Office"],
            "font": "Times-Roman",
            "font_size": 16,
        },
        {
            "filename": "door_sign",
            "plaque_dimensions": (80, 40),
            "text_lines": ["Meeting Room", "Do Not Disturb"],
        },
    ]

    generator.export_batch_templates(batch_templates)
```

This code is designed to be production-ready, and it includes robust error handling, clean comments, and adherence to best practices for Python.
