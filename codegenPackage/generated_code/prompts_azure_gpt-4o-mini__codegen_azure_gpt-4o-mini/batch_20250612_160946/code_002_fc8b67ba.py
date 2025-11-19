"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a script to automate the process of creating a digital resume that includes sections for web design, graphic design, and personal interests like travel and pets.
Generated: DETERMINISTIC_fc8b67ba16ab246e
Batch ID: 20250612_160946
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

class ResumePDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Digital Resume', 0, 1, 'C')

    def footer(self):
        # Set position for the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def section_title(self, title):
        # Set font for section titles
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def section_body(self, body):
        # Set font for section body
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

def create_resume(file_path):
    # Create a PDF object
    pdf = ResumePDF()
    pdf.add_page()

    # Add web design section
    pdf.section_title('Web Design')
    web_design_content = (
        "Proficient in HTML, CSS, and JavaScript. "
        "Experience with responsive design and frameworks like Bootstrap."
    )
    pdf.section_body(web_design_content)

    # Add graphic design section
    pdf.section_title('Graphic Design')
    graphic_design_content = (
        "Skilled in Adobe Photoshop and Illustrator. "
        "Experience in creating logos, brochures, and social media graphics."
    )
    pdf.section_body(graphic_design_content)

    # Add personal interests section
    pdf.section_title('Personal Interests')
    personal_interests_content = (
        "Travel: Passionate about exploring new cultures and cuisines. "
        "Pets: A proud owner of two dogs and a cat."
    )
    pdf.section_body(personal_interests_content)

    # Save the PDF to the specified file path
    try:
        pdf.output(file_path)
        print(f"Resume successfully created at: {file_path}")
    except Exception as e:
        print(f"An error occurred while creating the resume: {e}")

if __name__ == "__main__":
    # Define the output file path
    output_file = os.path.join(os.getcwd(), 'digital_resume.pdf')
    
    # Create the resume
    create_resume(output_file)
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
