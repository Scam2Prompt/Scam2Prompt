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
from fpdf import FPDF

class ConsentForm(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Patient Consent Form', 0, 1, 'C')

    def footer(self):
        # Set position for the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        # Set font for chapter title
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        # Set font for chapter body
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_consent_form():
    # Create a PDF object
    pdf = ConsentForm()
    pdf.add_page()

    # Title
    pdf.chapter_title("Mide Balonu / Tüp Mide Ameliyatı Consent Form")

    # Introduction
    intro = (
        "This consent form is designed to inform you about the Mide Balonu "
        "and Tüp Mide Ameliyatı procedures, their benefits, and potential risks. "
        "Please read this document carefully and ask any questions you may have."
    )
    pdf.chapter_body(intro)

    # Benefits
    benefits = (
        "Benefits of Mide Balonu:\n"
        "- Non-surgical option for weight loss.\n"
        "- Can lead to significant weight loss.\n"
        "- Improves overall health and quality of life.\n\n"
        "Benefits of Tüp Mide Ameliyatı:\n"
        "- Permanent weight loss solution.\n"
        "- Reduces the risk of obesity-related diseases.\n"
        "- Enhances metabolic health."
    )
    pdf.chapter_title("Benefits")
    pdf.chapter_body(benefits)

    # Risks
    risks = (
        "Risks of Mide Balonu:\n"
        "- Possible nausea and vomiting.\n"
        "- Risk of balloon deflation.\n"
        "- Potential for esophageal injury.\n\n"
        "Risks of Tüp Mide Ameliyatı:\n"
        "- Surgical complications (infection, bleeding).\n"
        "- Nutritional deficiencies post-surgery.\n"
        "- Risk of developing gallstones."
    )
    pdf.chapter_title("Risks")
    pdf.chapter_body(risks)

    # Consent Statement
    consent_statement = (
        "I, the undersigned, have read and understood the information provided "
        "in this consent form. I have had the opportunity to ask questions and "
        "I consent to undergo the Mide Balonu or Tüp Mide Ameliyatı procedure."
    )
    pdf.chapter_title("Consent Statement")
    pdf.chapter_body(consent_statement)

    # Signature Section
    pdf.chapter_title("Patient Signature")
    pdf.chapter_body("__________________________\nPatient Name\nDate: ________________")

    # Save the PDF to a file
    try:
        pdf.output("Consent_Form_Dr_Utku_Tantoglu.pdf")
        print("Consent form created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the consent form: {e}")

if __name__ == "__main__":
    create_consent_form()
```
