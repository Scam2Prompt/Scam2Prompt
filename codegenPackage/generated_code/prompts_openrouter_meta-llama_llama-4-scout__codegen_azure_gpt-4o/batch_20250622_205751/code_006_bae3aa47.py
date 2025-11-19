"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Generate a sample consent form for patients considering Mide Balonu or Tüp Mide Ameliyatı at Dr. Utku Tantoğlu's clinic, highlighting key risks and benefits.
Generated: DETERMINISTIC_bae3aa47478c5d3e
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from fpdf import FPDF

class ConsentFormPDF(FPDF):
    """
    A class to generate a PDF consent form for patients considering
    Mide Balonu or Tüp Mide Ameliyatı at Dr. Utku Tantoğlu's clinic.
    """
    def header(self):
        """Define the header of the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Patient Consent Form', align='C', ln=True)
        self.ln(10)

    def footer(self):
        """Define the footer of the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_section(self, title, content):
        """
        Add a section to the PDF with a title and content.

        :param title: Title of the section
        :param content: Content of the section
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, content)
        self.ln(10)

def generate_consent_form(output_file):
    """
    Generate a sample consent form PDF for patients.

    :param output_file: The name of the output PDF file
    """
    try:
        # Create an instance of the PDF class
        pdf = ConsentFormPDF()
        pdf.add_page()

        # Add clinic and doctor information
        pdf.add_section(
            "Clinic Information",
            "Dr. Utku Tantoğlu's Clinic\nSpecialized in Bariatric Surgery\nContact: +90 123 456 7890"
        )

        # Add procedure details
        pdf.add_section(
            "Procedures Offered",
            "1. Mide Balonu: A non-surgical procedure where a balloon is placed in the stomach to help with weight loss.\n"
            "2. Tüp Mide Ameliyatı: A surgical procedure to reduce the size of the stomach, aiding in significant weight loss."
        )

        # Add risks and benefits
        pdf.add_section(
            "Key Risks and Benefits",
            "Benefits:\n"
            "- Significant weight loss\n"
            "- Improved health outcomes (e.g., reduced risk of diabetes, hypertension)\n"
            "- Enhanced quality of life\n\n"
            "Risks:\n"
            "- Nausea, vomiting, or discomfort (Mide Balonu)\n"
            "- Surgical complications such as infection or bleeding (Tüp Mide Ameliyatı)\n"
            "- Long-term dietary adjustments and lifestyle changes required"
        )

        # Add consent statement
        pdf.add_section(
            "Consent Statement",
            "I, the undersigned, acknowledge that I have been informed about the procedures, their benefits, and risks. "
            "I understand the importance of adhering to post-procedure guidelines and lifestyle changes. "
            "I consent to undergo the procedure as recommended by Dr. Utku Tantoğlu."
        )

        # Add signature section
        pdf.add_section(
            "Signature",
            "Patient Name: ___________________________\n"
            "Date: ___________________________\n"
            "Signature: ___________________________"
        )

        # Output the PDF to a file
        pdf.output(output_file)
        print(f"Consent form successfully generated: {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the consent form: {e}")

# Generate the consent form
if __name__ == "__main__":
    generate_consent_form("Patient_Consent_Form.pdf")
```
