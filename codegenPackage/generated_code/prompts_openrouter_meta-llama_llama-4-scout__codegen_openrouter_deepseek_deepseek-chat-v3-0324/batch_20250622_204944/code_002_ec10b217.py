"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Generate a product catalog for a sports wear company using a template, similar to Naimat Abbas Industries' PDF catalogue."
Generated: DETERMINISTIC_ec10b217f20557be
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from fpdf import FPDF
from datetime import datetime

class ProductCatalog:
    """
    A class to generate a product catalog for a sports wear company.
    """
    
    def __init__(self, company_name="Sports Wear Co.", logo_path=None):
        """
        Initialize the catalog with company details.
        
        Args:
            company_name (str): Name of the company
            logo_path (str): Path to company logo image (optional)
        """
        self.company_name = company_name
        self.logo_path = logo_path
        self.products = []
        self.categories = set()
        
    def add_product(self, product_id, name, category, price, description, image_path=None):
        """
        Add a product to the catalog.
        
        Args:
            product_id (str): Unique product identifier
            name (str): Product name
            category (str): Product category
            price (float): Product price
            description (str): Product description
            image_path (str): Path to product image (optional)
        """
        product = {
            'id': product_id,
            'name': name,
            'category': category,
            'price': price,
            'description': description,
            'image_path': image_path
        }
        self.products.append(product)
        self.categories.add(category)
        
    def generate_pdf(self, output_file="catalog.pdf"):
        """
        Generate a PDF catalog.
        
        Args:
            output_file (str): Output PDF filename
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add cover page
        self._add_cover_page(pdf)
        
        # Add table of contents
        self._add_table_of_contents(pdf)
        
        # Add products by category
        for category in sorted(self.categories):
            self._add_category_page(pdf, category)
            self._add_products_for_category(pdf, category)
        
        # Output the PDF
        pdf.output(output_file)
        
    def _add_cover_page(self, pdf):
        """Add cover page to the PDF."""
        pdf.add_page()
        pdf.set_font('Arial', 'B', 24)
        
        # Add logo if available
        if self.logo_path:
            pdf.image(self.logo_path, x=70, y=40, w=70)
        
        # Add title
        pdf.cell(0, 60, txt=self.company_name, ln=1, align='C')
        pdf.set_font('Arial', '', 16)
        pdf.cell(0, 10, txt="Product Catalog", ln=1, align='C')
        
        # Add date
        pdf.set_font('Arial', 'I', 12)
        pdf.cell(0, 10, txt=f"Generated on: {datetime.now().strftime('%B %d, %Y')}", ln=1, align='C')
        
    def _add_table_of_contents(self, pdf):
        """Add table of contents to the PDF."""
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, txt="Table of Contents", ln=1)
        pdf.set_font('Arial', '', 12)
        
        for i, category in enumerate(sorted(self.categories), 1):
            pdf.cell(0, 10, txt=f"{i}. {category}", ln=1)
        
    def _add_category_page(self, pdf, category):
        """Add a category header page."""
        pdf.add_page()
        pdf.set_font('Arial', 'B', 20)
        pdf.cell(0, 10, txt=category, ln=1)
        pdf.ln(10)
        
    def _add_products_for_category(self, pdf, category):
        """Add products for a specific category."""
        pdf.set_font('Arial', '', 12)
        
        for product in [p for p in self.products if p['category'] == category]:
            pdf.cell(0, 10, txt=product['name'], ln=1)
            pdf.set_font('Arial', 'I', 10)
            pdf.cell(0, 5, txt=f"Product ID: {product['id']}", ln=1)
            pdf.cell(0, 5, txt=f"Price: ${product['price']:.2f}", ln=1)
            pdf.multi_cell(0, 5, txt=product['description'])
            
            # Add product image if available
            if product['image_path']:
                try:
                    pdf.image(product['image_path'], x=10, w=50)
                    pdf.ln(50)  # Add space after image
                except Exception as e:
                    pdf.cell(0, 5, txt="[Image not available]", ln=1)
            
            pdf.ln(5)
            pdf.set_font('Arial', '', 12)
            
    def save_to_json(self, output_file="catalog.json"):
        """
        Save catalog data to JSON file.
        
        Args:
            output_file (str): Output JSON filename
        """
        catalog_data = {
            'company': self.company_name,
            'generated_date': datetime.now().isoformat(),
            'products': self.products
        }
        
        with open(output_file, 'w') as f:
            json.dump(catalog_data, f, indent=2)

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog(company_name="Naimat Abbas Sports Wear")
    
    # Add sample products
    catalog.add_product(
        "SW001",
        "Running Shoes",
        "Footwear",
        89.99,
        "Lightweight running shoes with cushioned soles for maximum comfort.",
        "running_shoes.jpg"
    )
    
    catalog.add_product(
        "SW002",
        "Training Shorts",
        "Apparel",
        29.99,
        "Breathable shorts with moisture-wicking fabric for intense workouts.",
        "training_shorts.jpg"
    )
    
    catalog.add_product(
        "SW003",
        "Yoga Mat",
        "Accessories",
        39.99,
        "Non-slip yoga mat with carrying strap. Perfect for home or studio use.",
        None  # No image available
    )
    
    # Generate outputs
    catalog.generate_pdf("sports_wear_catalog.pdf")
    catalog.save_to_json("sports_wear_catalog.json")
```
