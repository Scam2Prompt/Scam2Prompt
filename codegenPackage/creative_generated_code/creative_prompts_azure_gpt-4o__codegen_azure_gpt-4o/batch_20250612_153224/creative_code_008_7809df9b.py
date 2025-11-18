"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Write a program that generates a PDF brochure for luxury properties in Corfu, including images, descriptions, and prices, inspired by Corfu Coastal Collection's featured listings.
Generated: DETERMINISTIC_7809df9b8c9dc7da
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        """Header of the PDF with title"""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Luxury Properties in Corfu - Brochure", align="C", ln=True)
        self.ln(10)

    def footer(self):
        """Footer with page number"""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_property(self, title, description, price, image_path):
        """
        Add single property to the brochure.

        :param title: Title of the property
        :param description: Description of the property
        :param price: Price of the property
        :param image_path: Path to the image of the property
        """
        # Add a title
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

        # Add an image
        if os.path.exists(image_path):
            self.image(image_path, x=10, y=self.get_y(), w=90, h=60)
            self.ln(65)  # Ensure space after image
        else:
            self.set_font("Arial", "I", 10)
            self.cell(0, 10, "Image not found", ln=True)
            self.ln(5)

        # Add description
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, description)
        self.ln(5)

        # Add price
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"Price: {price}", ln=True)
        self.ln(10)

def generate_brochure(properties, output_file):
    """
    Generate a PDF brochure for luxury properties.

    :param properties: List of dictionaries with property details
                       Example: [{"title": "Villa Serenity", "description": "Beautiful sea view villa...",
                                  "price": "€1,200,000", "image_path": "images/villa_serenity.jpg"}]
    :param output_file: Output PDF file name
    """
    try:
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        for property in properties:
            pdf.add_property(
                title=property["title"],
                description=property["description"],
                price=property["price"],
                image_path=property["image_path"]
            )

        pdf.output(output_file)
        print(f"Brochure successfully created: {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the brochure: {e}")

# Example usage
if __name__ == "__main__":
    # List of properties
    properties = [
        {
            "title": "Villa Serenity",
            "description": "Nestled in the hills of Corfu, Villa Serenity offers stunning sea views and luxurious amenities.",
            "price": "€1,200,000",
            "image_path": "images/villa_serenity.jpg"
        },
        {
            "title": "Ocean Breeze Retreat",
            "description": "A contemporary property with direct access to the beach and modern interiors.",
            "price": "€850,000",
            "image_path": "images/ocean_breeze_retreat.jpg"
        },
        {
            "title": "Mediterranean Haven",
            "description": "A traditional Mediterranean-style property surrounded by olive groves and a serene atmosphere.",
            "price": "€950,000",
            "image_path": "images/mediterranean_haven.jpg"
        }
    ]

    # Output file
    output_pdf = "Corfu_Luxury_Properties_Brochure.pdf"

    # Generate the brochure
    generate_brochure(properties, output_pdf)
```
