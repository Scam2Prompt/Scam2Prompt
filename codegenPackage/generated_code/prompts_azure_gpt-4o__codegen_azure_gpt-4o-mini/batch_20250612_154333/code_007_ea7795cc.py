"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write a script to create labels for small businesses, including options for branding and product identification, as described on Etiquettetout.com.
Generated: DETERMINISTIC_ea7795cca2e6d5f3
Batch ID: 20250612_154333
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

class LabelGenerator:
    def __init__(self, business_name, branding_color, product_name, label_size=(100, 50)):
        """
        Initializes the LabelGenerator with business details.

        :param business_name: Name of the business
        :param branding_color: Branding color in RGB tuple (R, G, B)
        :param product_name: Name of the product for identification
        :param label_size: Size of the label in mm (width, height)
        """
        self.business_name = business_name
        self.branding_color = branding_color
        self.product_name = product_name
        self.label_size = label_size
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def create_label(self):
        """
        Creates a label PDF with the business and product information.
        """
        try:
            self.pdf.add_page()
            self.pdf.set_font("Arial", 'B', 16)
            self.pdf.set_fill_color(*self.branding_color)
            self.pdf.rect(10, 10, self.label_size[0], self.label_size[1], 'F')

            # Business Name
            self.pdf.set_text_color(255, 255, 255)  # White text
            self.pdf.cell(0, 10, self.business_name, ln=True, align='C')

            # Product Name
            self.pdf.set_font("Arial", 'I', 12)
            self.pdf.cell(0, 10, self.product_name, ln=True, align='C')

            # Save the PDF
            output_file = f"{self.business_name.replace(' ', '_')}_label.pdf"
            self.pdf.output(output_file)
            print(f"Label created successfully: {output_file}")

        except Exception as e:
            print(f"An error occurred while creating the label: {e}")

def main():
    """
    Main function to run the label generator.
    """
    # Example input for the label
    business_name = "Sample Business"
    branding_color = (0, 102, 204)  # Blue color
    product_name = "Sample Product"

    # Create a LabelGenerator instance
    label_generator = LabelGenerator(business_name, branding_color, product_name)

    # Generate the label
    label_generator.create_label()

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
