"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Create a script to automate the generation of admission forms for MBBS and MD/MS courses at MIMSR Medical College, including fields for merit-based intake and NRI candidate guidelines.
Generated: DETERMINISTIC_5481db9be9e3d02f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from fpdf import FPDF

class AdmissionFormPDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "MIMSR Medical College Admission Form", ln=True, align="C")
        self.ln(10)

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font for footer
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_admission_form(data):
    pdf = AdmissionFormPDF()
    pdf.add_page()
    
    # Set font for the body
    pdf.set_font("Arial", "", 12)

    # Admission form fields
    for field, value in data.items():
        pdf.cell(0, 10, f"{field}: {value}", ln=True)

    # Save the PDF to a file
    try:
        pdf.output("MIMSR_Admission_Form.pdf")
        print("Admission form generated successfully!")
    except Exception as e:
        print(f"An error occurred while saving the PDF: {e}")

def main():
    # Sample data for MBBS and MD/MS admission forms
    admission_data = {
        "Name": "John Doe",
        "Age": 22,
        "Course": "MBBS",
        "Merit-Based Intake": "Yes",
        "NRI Candidate": "No",
        "Contact": "1234567890",
        "Email": "johndoe@example.com",
        "Address": "123 Main St, City, State, ZIP",
        "Previous Qualifications": "B.Sc. in Biology",
        "Comments": "Looking forward to studying at MIMSR."
    }

    # Generate the admission form PDF
    create_admission_form(admission_data)

if __name__ == "__main__":
    main()
```

### Requirements
- Install `fpdf` library to run the code:
```bash
pip install fpdf
```
