"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Create a step-by-step Python program to generate a Notice of Hearing and Proof of Service forms for guardianship cases, as described on Serve Utah.
Generated: DETERMINISTIC_29c53f7e6415cdd9
Batch ID: 20250612_154741
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

class NoticeOfHearing:
    def __init__(self, case_number, hearing_date, hearing_time, location, petitioner_name):
        self.case_number = case_number
        self.hearing_date = hearing_date
        self.hearing_time = hearing_time
        self.location = location
        self.petitioner_name = petitioner_name

    def generate_pdf(self, output_path):
        """Generates a PDF for the Notice of Hearing."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add content to the PDF
        pdf.cell(200, 10, txt="Notice of Hearing", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Case Number: {self.case_number}", ln=True)
        pdf.cell(200, 10, txt=f"Hearing Date: {self.hearing_date.strftime('%B %d, %Y')}", ln=True)
        pdf.cell(200, 10, txt=f"Hearing Time: {self.hearing_time}", ln=True)
        pdf.cell(200, 10, txt=f"Location: {self.location}", ln=True)
        pdf.cell(200, 10, txt=f"Petitioner: {self.petitioner_name}", ln=True)

        # Save the PDF
        try:
            pdf.output(output_path)
            print(f"Notice of Hearing saved to {output_path}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

class ProofOfService:
    def __init__(self, case_number, served_person, service_date, server_name):
        self.case_number = case_number
        self.served_person = served_person
        self.service_date = service_date
        self.server_name = server_name

    def generate_pdf(self, output_path):
        """Generates a PDF for the Proof of Service."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add content to the PDF
        pdf.cell(200, 10, txt="Proof of Service", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Case Number: {self.case_number}", ln=True)
        pdf.cell(200, 10, txt=f"Served Person: {self.served_person}", ln=True)
        pdf.cell(200, 10, txt=f"Service Date: {self.service_date.strftime('%B %d, %Y')}", ln=True)
        pdf.cell(200, 10, txt=f"Server Name: {self.server_name}", ln=True)

        # Save the PDF
        try:
            pdf.output(output_path)
            print(f"Proof of Service saved to {output_path}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

def main():
    # Example data for the forms
    case_number = "123456"
    hearing_date = datetime(2023, 10, 15)
    hearing_time = "10:00 AM"
    location = "123 Main St, Salt Lake City, UT"
    petitioner_name = "John Doe"
    
    served_person = "Jane Smith"
    service_date = datetime(2023, 10, 10)
    server_name = "John Doe"

    # Create Notice of Hearing
    notice = NoticeOfHearing(case_number, hearing_date, hearing_time, location, petitioner_name)
    notice_output_path = os.path.join(os.getcwd(), "Notice_of_Hearing.pdf")
    notice.generate_pdf(notice_output_path)

    # Create Proof of Service
    proof = ProofOfService(case_number, served_person, service_date, server_name)
    proof_output_path = os.path.join(os.getcwd(), "Proof_of_Service.pdf")
    proof.generate_pdf(proof_output_path)

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
