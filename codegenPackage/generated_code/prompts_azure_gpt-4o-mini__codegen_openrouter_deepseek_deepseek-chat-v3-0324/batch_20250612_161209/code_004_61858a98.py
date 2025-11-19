"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Illustrate how to use a library to generate a PDF catalog of hardware products, including features for items like cylinder locks and door hinges, inspired by DEVA's offerings.
Generated: DETERMINISTIC_61858a981ba02225
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF
from datetime import datetime

class Product:
    """Represents a hardware product with its attributes."""
    def __init__(self, name, sku, description, price, features=None, image_path=None):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.features = features if features else []
        self.image_path = image_path

class PDFCatalogGenerator:
    """Generates a PDF catalog for hardware products."""
    
    def __init__(self, title, company_name, logo_path=None):
        self.pdf = FPDF()
        self.title = title
        self.company_name = company_name
        self.logo_path = logo_path
        self.products = []
        
    def add_product(self, product):
        """Add a product to the catalog."""
        self.products.append(product)
    
    def _add_header(self):
        """Add header with logo, title, and date."""
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 16)
        
        # Add logo if provided
        if self.logo_path and os.path.exists(self.logo_path):
            self.pdf.image(self.logo_path, x=10, y=8, w=30)
            self.pdf.cell(0, 10, txt=self.title, ln=1, align='C')
        else:
            self.pdf.cell(0, 10, txt=self.title, ln=1, align='C')
        
        self.pdf.set_font('Arial', '', 10)
        self.pdf.cell(0, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", ln=1, align='R')
        self.pdf.cell(0, 10, txt=f"Company: {self.company_name}", ln=1, align='L')
        self.pdf.ln(10)
    
    def _add_product_section(self, product):
        """Add a product section to the PDF."""
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(0, 10, txt=product.name, ln=1)
        
        self.pdf.set_font('Arial', '', 10)
        self.pdf.cell(0, 10, txt=f"SKU: {product.sku}", ln=1)
        self.pdf.cell(0, 10, txt=f"Price: ${product.price:.2f}", ln=1)
        
        # Add product image if available
        if product.image_path and os.path.exists(product.image_path):
            self.pdf.image(product.image_path, x=10, y=self.pdf.get_y(), w=40)
            self.pdf.set_y(self.pdf.get_y() + 40)
        
        self.pdf.multi_cell(0, 5, txt=product.description)
        self.pdf.ln(5)
        
        # Add features if available
        if product.features:
            self.pdf.set_font('Arial', 'B', 10)
            self.pdf.cell(0, 10, txt="Features:", ln=1)
            self.pdf.set_font('Arial', '', 10)
            for feature in product.features:
                self.pdf.cell(0, 5, txt=f"- {feature}", ln=1)
        
        self.pdf.ln(10)
    
    def generate(self, output_path):
        """Generate the PDF catalog and save to output path."""
        try:
            self._add_header()
            
            for product in self.products:
                self._add_product_section(product)
            
            self.pdf.output(output_path)
            return True
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create catalog generator
    catalog = PDFCatalogGenerator(
        title="Hardware Products Catalog 2023",
        company_name="DEVA Inspired Hardware",
        logo_path="logo.png"  # Optional
    )
    
    # Add products
    cylinder_lock = Product(
        name="Premium Cylinder Lock",
        sku="CL-2023",
        description="High-security cylinder lock with anti-pick and anti-drill features.",
        price=24.99,
        features=[
            "6-pin cylinder for enhanced security",
            "Stainless steel construction",
            "Weather-resistant design",
            "Available in multiple finishes"
        ],
        image_path="cylinder_lock.jpg"  # Optional
    )
    
    door_hinge = Product(
        name="Heavy Duty Door Hinge",
        sku="DH-304",
        description="Industrial-grade door hinge for heavy doors with ball bearings.",
        price=18.50,
        features=[
            "Load capacity up to 120kg",
            "Stainless steel construction",
            "Self-lubricating ball bearings",
            "Adjustable tension"
        ],
        image_path="door_hinge.jpg"  # Optional
    )
    
    catalog.add_product(cylinder_lock)
    catalog.add_product(door_hinge)
    
    # Generate PDF
    success = catalog.generate("hardware_catalog.pdf")
    if success:
        print("Catalog generated successfully!")
    else:
        print("Failed to generate catalog.")
```
