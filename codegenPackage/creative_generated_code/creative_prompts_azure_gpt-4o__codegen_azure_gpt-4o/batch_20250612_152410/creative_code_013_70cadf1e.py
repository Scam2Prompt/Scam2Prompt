"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Develop a Python script to generate a PDF catalog for "Karma Çalışma Tezgahları," including images, dimensions, and technical specifications.
Generated: DETERMINISTIC_70cadf1e59680e37
Batch ID: 20250612_152410
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
from PIL import Image

class PDFCatalog(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
    
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, align='C', ln=True)
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')
    
    def add_product(self, name, image_path, dimensions, specifications):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, name, ln=True)
        self.ln(5)
        
        # Add image if exists
        if os.path.exists(image_path):
            try:
                self.image(image_path, x=10, y=self.get_y(), w=100)
                self.ln(60)  # Adjust spacing below the image
            except Exception as e:
                self.set_font('Arial', 'I', 12)
                self.cell(0, 10, f"[Image not available: {str(e)}]", ln=True)
        else:
            self.set_font('Arial', 'I', 12)
            self.cell(0, 10, "[Image not found]", ln=True)
        
        # Add dimensions
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Dimensions:", ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, dimensions, ln=True)
        self.ln(5)
        
        # Add technical specifications
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Technical Specifications:", ln=True)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, specifications)
        self.ln(10)

def generate_pdf_catalog(title, products, output_path):
    """
    Generate a PDF catalog.

    :param title: Title of the catalog
    :param products: List of products, each being a dictionary with keys: name, image_path, dimensions, specifications
    :param output_path: File path to save the generated PDF
    """
    pdf = PDFCatalog(title)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    for product in products:
        pdf.add_product(
            name=product.get("name", "Unknown Product"),
            image_path=product.get("image_path", ""),
            dimensions=product.get("dimensions", "No dimensions available"),
            specifications=product.get("specifications", "No specifications available")
        )
    
    try:
        pdf.output(output_path)
        print(f"PDF successfully generated: {output_path}")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")

# Example usage:

# Define product details
products = [
    {
        "name": "Karma Çalışma Tezgahı - Model A",
        "image_path": "images/model_a.jpg",
        "dimensions": "Height: 120cm, Width: 60cm, Depth: 40cm",
        "specifications": "Material: Stainless steel\nWeight: 25kg\nLoad Capacity: 100kg"
    },
    {
        "name": "Karma Çalışma Tezgahı - Model B",
        "image_path": "images/model_b.jpg",
        "dimensions": "Height: 150cm, Width: 80cm, Depth: 50cm",
        "specifications": "Material: Aluminum\nWeight: 20kg\nLoad Capacity: 120kg"
    }
]

# Generate PDF catalog
output_file = "karma_tezgah_catalog.pdf"
generate_pdf_catalog("Karma Çalışma Tezgahları Catalog", products, output_file)
```
