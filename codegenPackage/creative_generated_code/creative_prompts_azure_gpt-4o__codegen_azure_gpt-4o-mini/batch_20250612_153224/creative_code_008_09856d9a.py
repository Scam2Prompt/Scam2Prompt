"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Write code to generate branded brochures and business cards for a Dubai-based company, using design principles mentioned by Crown Advertising.
Generated: DETERMINISTIC_09856d9a678a0762
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
        # Add company logo
        self.image('logo.png', 10, 8, 33)  # Adjust the size and position as needed
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Company Name', 0, 1, 'C')

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_brochure(content, filename):
    """Generate a PDF brochure from the provided content."""
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Add content to the brochure
    for line in content:
        pdf.multi_cell(0, 10, line)
    
    # Save the PDF to a file
    try:
        pdf.output(filename)
        print(f'Brochure saved as {filename}')
    except Exception as e:
        print(f'Error saving brochure: {e}')

def create_business_card(company_name, contact_info, filename):
    """Generate a PDF business card for the specified company."""
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    
    # Business card layout
    pdf.cell(0, 10, company_name, 0, 1, 'C')
    pdf.set_font('Arial', '', 12)

    # Add contact information
    for info in contact_info:
        pdf.cell(0, 10, info, 0, 1, 'C')
    
    # Save the PDF to a file
    try:
        pdf.output(filename)
        print(f'Business card saved as {filename}')
    except Exception as e:
        print(f'Error saving business card: {e}')

def main():
    """Main function to create brochure and business card."""
    # Content for the brochure
    brochure_content = [
        "Welcome to Our Company!",
        "We are a leading Dubai-based company specializing in innovative solutions.",
        "Our services include...",
        "Contact us for more information!"
    ]
    
    # Ensure output directory exists
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Create brochure
    brochure_file = os.path.join(output_dir, 'brochure.pdf')
    create_brochure(brochure_content, brochure_file)

    # Create a business card
    business_card_info = [
        "John Doe",
        "CEO",
        "Phone: +971 50 123 4567",
        "Email: john.doe@company.com",
        "Website: www.company.com"
    ]
    business_card_file = os.path.join(output_dir, 'business_card.pdf')
    create_business_card("Company Name", business_card_info, business_card_file)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have `fpdf` installed in your Python environment. You can install it using:
```bash
pip install fpdf
```
Also, make sure to have a logo image named `logo.png` in the same directory or adjust the path accordingly.
