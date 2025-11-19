"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Generate a script to create and format brochures and leaflets for digital offset printing, incorporating layout design principles mentioned on Ram Digi's website.
Generated: DETERMINISTIC_77f74746a21a43d6
Batch ID: 20250612_151308
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

class BrochurePDF(FPDF):
    """Class to create a PDF brochure using FPDF library."""
    
    def header(self):
        """Add a header to the brochure."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Brochure Title', 0, 1, 'C')

    def footer(self):
        """Add a footer to the brochure."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_content(self, title, content):
        """Add a title and content to the brochure."""
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.ln(10)  # Add a line break

def create_brochure(file_name):
    """Create a brochure PDF file with formatted content."""
    try:
        # Create a PDF object
        pdf = BrochurePDF()
        pdf.add_page()

        # Add content to the brochure
        pdf.add_content("Welcome to Our Services", "We offer a variety of services to meet your needs.")
        pdf.add_content("Our Mission", "To provide high-quality products and services.")
        pdf.add_content("Contact Us", "Email: info@example.com\nPhone: (123) 456-7890")

        # Save the PDF to a file
        pdf.output(file_name)
        print(f"Brochure created successfully: {file_name}")

    except Exception as e:
        print(f"An error occurred while creating the brochure: {e}")

if __name__ == "__main__":
    # Define the output file name
    output_file = "brochure.pdf"
    
    # Check if the output file already exists
    if os.path.exists(output_file):
        print(f"Error: The file '{output_file}' already exists. Please delete it or choose a different name.")
    else:
        create_brochure(output_file)
```

### Requirements:
- Ensure you have the `fpdf` library installed. You can install it using:
  ```bash
  pip install fpdf
  ```
