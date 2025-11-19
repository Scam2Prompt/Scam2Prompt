"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write Python code to automate filling out the guardianship forms for an adult disabled child as described on the Utah Courts website, including generating the checklist, coversheet, and petition.
Generated: DETERMINISTIC_6e77743f89cccf32
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
from fpdf import FPDF

class GuardianshipFormGenerator:
    def __init__(self, child_name, guardian_name, court_name, case_number):
        """
        Initialize the form generator with necessary details.

        :param child_name: Name of the disabled child
        :param guardian_name: Name of the guardian
        :param court_name: Name of the court
        :param case_number: Case number for the guardianship
        """
        self.child_name = child_name
        self.guardian_name = guardian_name
        self.court_name = court_name
        self.case_number = case_number

    def generate_checklist(self):
        """
        Generate a checklist for the guardianship forms.
        """
        checklist_items = [
            "Completed Petition for Appointment of Guardian",
            "Notice of Hearing",
            "Proposed Order",
            "Affidavit of Service",
            "Financial Disclosure",
            "Background Check Authorization"
        ]
        
        with open("guardianship_checklist.txt", "w") as file:
            file.write("Guardianship Forms Checklist\n")
            file.write("=" * 30 + "\n")
            for item in checklist_items:
                file.write(f"- {item}\n")
        
        print("Checklist generated: guardianship_checklist.txt")

    def generate_coversheet(self):
        """
        Generate a coversheet for the guardianship petition.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        pdf.cell(0, 10, f"Coversheet for Guardianship Petition", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Child's Name: {self.child_name}", ln=True)
        pdf.cell(0, 10, f"Guardian's Name: {self.guardian_name}", ln=True)
        pdf.cell(0, 10, f"Court Name: {self.court_name}", ln=True)
        pdf.cell(0, 10, f"Case Number: {self.case_number}", ln=True)
        
        pdf_file_name = "guardianship_coversheet.pdf"
        pdf.output(pdf_file_name)
        print(f"Coversheet generated: {pdf_file_name}")

    def generate_petition(self):
        """
        Generate the guardianship petition form.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        pdf.cell(0, 10, f"Petition for Appointment of Guardian", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Petitioner: {self.guardian_name}", ln=True)
        pdf.cell(0, 10, f"Child's Name: {self.child_name}", ln=True)
        pdf.cell(0, 10, f"Court: {self.court_name}", ln=True)
        pdf.cell(0, 10, f"Case Number: {self.case_number}", ln=True)
        pdf.cell(0, 10, "I hereby petition the court for the appointment of a guardian.", ln=True)
        
        pdf_file_name = "guardianship_petition.pdf"
        pdf.output(pdf_file_name)
        print(f"Petition generated: {pdf_file_name}")

    def run(self):
        """
        Execute the form generation process.
        """
        try:
            self.generate_checklist()
            self.generate_coversheet()
            self.generate_petition()
            print("All forms generated successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    child_name = "John Doe"
    guardian_name = "Jane Smith"
    court_name = "Utah County Court"
    case_number = "123456789"

    form_generator = GuardianshipFormGenerator(child_name, guardian_name, court_name, case_number)
    form_generator.run()
```

Make sure to install the `fpdf` library if you haven't already, using:
```bash
pip install fpdf
```
