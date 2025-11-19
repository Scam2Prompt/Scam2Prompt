"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Develop a Python script to generate a PDF catalog for "Karma Çalışma Tezgahları," including images, dimensions, and technical specifications.
Generated: DETERMINISTIC_70cadf1e59680e37
Batch ID: 20250612_152410
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
from PIL import Image

class PDFCatalogGenerator:
    """
    A class to generate a PDF catalog for Karma Çalışma Tezgahları.
    """
    
    def __init__(self, output_path="catalog.pdf"):
        """
        Initialize the PDF catalog generator.
        
        Args:
            output_path (str): Path to save the generated PDF. Defaults to "catalog.pdf".
        """
        self.output_path = output_path
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.current_y = 0
        
    def add_title_page(self, title):
        """
        Add a title page to the PDF.
        
        Args:
            title (str): Title of the catalog.
        """
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 24)
        self.pdf.cell(0, 20, title, 0, 1, "C")
        self.pdf.ln(20)
        
        # Add date
        self.pdf.set_font("Arial", "", 12)
        self.pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", 0, 1, "C")
        self.pdf.ln(20)
        
    def add_section_header(self, title):
        """
        Add a section header to the PDF.
        
        Args:
            title (str): Section title.
        """
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, title, 0, 1, "L")
        self.pdf.ln(5)
        
    def add_product(self, name, description, dimensions, image_path=None):
        """
        Add a product to the PDF.
        
        Args:
            name (str): Product name.
            description (str): Product description.
            dimensions (str): Product dimensions.
            image_path (str, optional): Path to product image. Defaults to None.
        """
        # Check if we need a new page
        if self.pdf.get_y() > 250:
            self.pdf.add_page()
            self.current_y = 10
        
        # Product name
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, name, 0, 1)
        self.pdf.ln(2)
        
        # Add image if provided
        if image_path and os.path.exists(image_path):
            try:
                # Resize image to fit
                with Image.open(image_path) as img:
                    img.thumbnail((150, 150))
                    temp_path = "temp_img.jpg"
                    img.save(temp_path)
                
                self.pdf.image(temp_path, x=10, y=self.pdf.get_y(), w=50)
                os.remove(temp_path)
                self.current_y = self.pdf.get_y() + 55
                self.pdf.set_y(self.current_y)
            except Exception as e:
                print(f"Error adding image {image_path}: {e}")
        
        # Product description
        self.pdf.set_font("Arial", "", 12)
        self.pdf.multi_cell(0, 8, description)
        self.pdf.ln(5)
        
        # Dimensions
        self.pdf.set_font("Arial", "I", 12)
        self.pdf.cell(0, 8, f"Dimensions: {dimensions}", 0, 1)
        self.pdf.ln(10)
        
    def generate_catalog(self, products):
        """
        Generate the complete catalog PDF.
        
        Args:
            products (list): List of product dictionaries.
        """
        try:
            # Add title page
            self.add_title_page("Karma Çalışma Tezgahları Kataloğu")
            
            # Add table of contents
            self.add_section_header("Ürünler")
            
            # Add products
            for product in products:
                self.add_product(
                    name=product.get("name", ""),
                    description=product.get("description", ""),
                    dimensions=product.get("dimensions", ""),
                    image_path=product.get("image_path")
                )
            
            # Save the PDF
            self.pdf.output(self.output_path)
            print(f"Catalog successfully generated at {self.output_path}")
            
        except Exception as e:
            print(f"Error generating catalog: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        {
            "name": "Pro Series Çalışma Tezgahı",
            "description": "Yüksek kaliteli çalışma tezgahı, profesyonel kullanım için ideal.",
            "dimensions": "120cm x 60cm x 75cm",
            "image_path": "pro_series.jpg"  # Replace with actual image path
        },
        {
            "name": "Standart Çalışma Tezgahı",
            "description": "Günlük kullanım için ekonomik ve dayanıklı çalışma tezgahı.",
            "dimensions": "100cm x 50cm x 75cm",
            "image_path": "standard.jpg"  # Replace with actual image path
        }
    ]
    
    # Generate catalog
    generator = PDFCatalogGenerator("karma_catalog.pdf")
    generator.generate_catalog(products)
```
