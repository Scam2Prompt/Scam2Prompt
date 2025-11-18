"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Write a script to generate a PDF catalog of glass products, including laminated, reflective, and decorative options, with descriptions and images.
Generated: DETERMINISTIC_5dfcfb483aaa191c
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf_catalog(output_file, products):
    """
    Generates a PDF catalog for glass products.

    Args:
        output_file (str): The filename for the generated PDF.
        products (list of dict): List of product information. Each dict should contain:
            - name (str): Product name
            - description (str): Product description
            - image_path (str): Path to the product image
    """
    # Create the PDF document
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Add a title
    title_style = styles['Title']
    elements.append(Paragraph("Glass Products Catalog", title_style))
    elements.append(Spacer(1, 0.5 * inch))
    
    for product in products:
        try:
            # Add product name
            name_style = styles['Heading2']
            elements.append(Paragraph(product['name'], name_style))
            
            # Add product description
            description_style = styles['BodyText']
            elements.append(Paragraph(product['description'], description_style))
            
            # Add product image
            if os.path.exists(product['image_path']):
                img = Image(product['image_path'])
                img.drawWidth = 3 * inch  # Resize image width
                img.drawHeight = 3 * inch  # Resize image height
                elements.append(img)
            else:
                elements.append(Paragraph("Image not found.", description_style))
            
            elements.append(Spacer(1, 0.5 * inch))  # Add space between products
        except KeyError as e:
            # Handle missing keys in the product dictionary
            print(f"Error: Missing key {e} in product data.")
    
    # Build the PDF
    doc.build(elements)

# Example usage
if __name__ == "__main__":
    # Define products list with name, description, and image path
    products = [
        {
            "name": "Laminated Glass",
            "description": "Durable laminated glass suitable for various applications.",
            "image_path": "images/laminated_glass.jpg"
        },
        {
            "name": "Reflective Glass",
            "description": "Energy-efficient reflective glass designed to reduce heat.",
            "image_path": "images/reflective_glass.jpg"
        },
        {
            "name": "Decorative Glass",
            "description": "Stylish decorative glass for aesthetic purposes.",
            "image_path": "images/decorative_glass.jpg"
        },
    ]
    
    # Generate the PDF catalog
    generate_pdf_catalog("glass_products_catalog.pdf", products)
```

Make sure you have the `reportlab` library installed and the image files exist in the specified paths for the script to work correctly. You can install the library using `pip install reportlab`.
