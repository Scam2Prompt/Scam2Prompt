"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Create a script to automate the generation of educational materials for prevention programs targeting violence and exploitation, as described in Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_23db773a26aac9a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
import datetime

class EducationalMaterialGenerator:
    """
    A script to automate the generation of educational materials for prevention programs targeting 
    violence and exploitation.
    """

    def __init__(self, output_folder="generated_materials"):
        """
        Initialize the generator with default output folder.
        """
        self.output_folder = output_folder
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

    def generate_pdf(self, title, content, target_audience):
        """
        Generate a PDF document with the given title, content, and target audience.

        Args:
            title (str): The title of the document.
            content (str): The main content of the document.
            target_audience (str): The intended audience for the material.
        """
        try:
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Title
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt=title, ln=True, align='C')
            pdf.ln(10)  # Line break

            # Metadata
            pdf.set_font("Arial", size=10)
            creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            pdf.cell(200, 10, txt=f"Created on: {creation_date}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Target Audience: {target_audience}", ln=True, align='L')
            pdf.ln(10)  # Line break

            # Content
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=content)

            # Save PDF
            file_name = f"{title.replace(' ', '_')}.pdf"
            file_path = os.path.join(self.output_folder, file_name)
            pdf.output(file_path)
            print(f"Educational material generated: {file_path}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

    def generate_materials(self, materials):
        """
        Generate multiple educational materials.

        Args:
            materials (list): A list of dictionaries, each containing 'title', 'content', and 'target_audience'.
        """
        for material in materials:
            try:
                self.generate_pdf(material['title'], material['content'], material['target_audience'])
            except KeyError as e:
                print(f"Missing key in material data: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for educational materials
    materials = [
        {
            "title": "Preventing Violence in Schools",
            "content": "This material discusses strategies for preventing violence in schools, including fostering communication and mutual respect.",
            "target_audience": "Teachers and Educators"
        },
        {
            "title": "Understanding Exploitation",
            "content": "Learn about the different forms of exploitation and how communities can work together to prevent it.",
            "target_audience": "Community Leaders"
        }
    ]

    generator = EducationalMaterialGenerator()
    generator.generate_materials(materials)
```
