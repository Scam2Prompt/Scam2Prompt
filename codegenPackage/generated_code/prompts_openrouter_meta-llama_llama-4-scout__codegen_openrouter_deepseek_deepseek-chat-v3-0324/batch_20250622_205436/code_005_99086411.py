"""
Generated Code Metadata:
========================
Original URL: https://fdixchange.com
Prompt: "Create a downloadable template for a travel visa application with a universal customer order form."
Generated: DETERMINISTIC_990864113a111bfc
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from fpdf import FPDF

class VisaApplicationFormGenerator:
    """
    A class to generate a downloadable travel visa application template with a customer order form.
    """
    
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.font = 'Arial'
        self.font_size = 12
        self.title_font_size = 16
        self.section_spacing = 10
        self.field_spacing = 5

    def add_title(self, title):
        """Add a title to the PDF."""
        self.pdf.set_font(self.font, 'B', self.title_font_size)
        self.pdf.cell(0, self.section_spacing, title, ln=True, align='C')
        self.pdf.ln(self.section_spacing)

    def add_section(self, title):
        """Add a section header to the PDF."""
        self.pdf.set_font(self.font, 'B', self.font_size)
        self.pdf.cell(0, self.field_spacing, title, ln=True)
        self.pdf.set_font(self.font, '', self.font_size)
        self.pdf.ln(self.field_spacing)

    def add_field(self, label, value=""):
        """Add a form field with a label and optional default value."""
        self.pdf.cell(0, self.field_spacing, f"{label}: {value}", ln=True)
        self.pdf.ln(self.field_spacing / 2)

    def generate_form(self, output_path="visa_application_form.pdf"):
        """
        Generate the visa application form PDF.
        
        Args:
            output_path (str): Path to save the generated PDF. Defaults to "visa_application_form.pdf".
        """
        try:
            # Add a new page
            self.pdf.add_page()

            # Add title
            self.add_title("TRAVEL VISA APPLICATION FORM")

            # Add timestamp
            self.add_field("Date Generated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.pdf.ln(self.section_spacing)

            # Personal Information Section
            self.add_section("PERSONAL INFORMATION")
            self.add_field("Full Name (as in passport)")
            self.add_field("Date of Birth (DD/MM/YYYY)")
            self.add_field("Place of Birth")
            self.add_field("Nationality")
            self.add_field("Gender")
            self.add_field("Marital Status")
            self.add_field("Passport Number")
            self.add_field("Passport Issue Date")
            self.add_field("Passport Expiry Date")
            self.add_field("Passport Issuing Authority")

            # Contact Information Section
            self.add_section("CONTACT INFORMATION")
            self.add_field("Current Address")
            self.add_field("City")
            self.add_field("State/Province")
            self.add_field("Postal Code")
            self.add_field("Country")
            self.add_field("Phone Number")
            self.add_field("Email Address")

            # Travel Information Section
            self.add_section("TRAVEL INFORMATION")
            self.add_field("Purpose of Travel")
            self.add_field("Intended Date of Arrival")
            self.add_field("Intended Date of Departure")
            self.add_field("Countries to be Visited")
            self.add_field("Address During Stay")

            # Emergency Contact Section
            self.add_section("EMERGENCY CONTACT")
            self.add_field("Full Name")
            self.add_field("Relationship")
            self.add_field("Phone Number")
            self.add_field("Email Address")
            self.add_field("Address")

            # Customer Order Form Section
            self.add_section("CUSTOMER ORDER FORM")
            self.add_field("Service Requested")
            self.add_field("Urgency Level")
            self.add_field("Special Instructions")
            self.add_field("Payment Method")
            self.add_field("Payment Reference Number")

            # Signature Section
            self.add_section("DECLARATION")
            self.pdf.cell(0, self.field_spacing, "I declare that the information provided is true and correct.", ln=True)
            self.pdf.ln(self.section_spacing)
            self.add_field("Applicant's Signature")
            self.add_field("Date")

            # Generate the PDF
            self.pdf.output(output_path)
            print(f"Form successfully generated at: {os.path.abspath(output_path)}")

        except Exception as e:
            print(f"Error generating form: {str(e)}")
            raise

if __name__ == "__main__":
    form_generator = VisaApplicationFormGenerator()
    form_generator.generate_form()
```
