"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Create a script in Python to generate a PDF catalog of metallic sticker products offered by jttlogos.com, including customization options and electroforming signs.
Generated: DETERMINISTIC_90bff90117a164ee
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

def create_pdf_catalog(output_path, product_data):
    """
    Generate a PDF catalog for metallic stickers and electroforming signs.

    Parameters:
    - output_path (str): The path where the PDF should be saved.
    - product_data (list): A list of dictionaries containing product details.
    """

    # Initialize the PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)

    # Title Page
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Metallic Stickers & Electroforming Signs Catalog", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Custom products offered by JTT Logos", ln=True, align='C')
    pdf.ln(20)

    # Add content for each product
    for product in product_data:
        # Add a new page for each product
        pdf.add_page()

        # Product Title
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, product.get("name", "Unnamed Product"), ln=True, align='L')
        pdf.ln(8)

        # Product Description
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, product.get("description", "No description available."))

        # Customization Options
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Customization Options:", ln=True)
        pdf.set_font("Arial", size=12)
        options = product.get("customization_options", [])
        for option in options:
            pdf.cell(0, 10, f"- {option}", ln=True)

        # Electroforming Details (if available)
        pdf.ln(5)
        if product.get("electroforming"):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "Electroforming Details:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, product.get("electroforming_details", "Details not provided."))

        # Add a horizontal line
        pdf.ln(5)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.3)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

    # Save the generated PDF
    try:
        pdf.output(output_path)
        print(f"PDF catalog successfully created: {output_path}")
    except Exception as e:
        print(f"Failed to create PDF catalog: {e}")

# Example product data
product_list = [
    {
        "name": "Metallic Logo Sticker - Gold",
        "description": "Premium metallic gold stickers for branding and promotional purposes.",
        "customization_options": ["Text", "Logo", "Colors", "Shape"],
        "electroforming": True,
        "electroforming_details": "Electroforming ensures precise and durable designs with a metallic finish.",
    },
    {
        "name": "Electroformed Name Plate",
        "description": "Durable name plates made with advanced electroforming technology.",
        "customization_options": ["Font Style", "Plate Size", "Material"],
        "electroforming": True,
        "electroforming_details": "Provides a sleek metallic appearance with enhanced durability.",
    },
    {
        "name": "Custom Metallic Label",
        "description": "High-quality metallic labels for product packaging and branding.",
        "customization_options": ["Dimensions", "Material Type", "Finish"],
        "electroforming": False
    },
]

# Generate the PDF catalog
output_file = "Metallic_Sticker_Catalog.pdf"
create_pdf_catalog(output_file, product_list)
```
