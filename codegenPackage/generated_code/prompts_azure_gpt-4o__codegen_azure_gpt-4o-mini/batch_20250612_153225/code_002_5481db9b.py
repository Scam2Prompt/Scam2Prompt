"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Create a script to automate the generation of admission forms for MBBS and MD/MS courses at MIMSR Medical College, including fields for merit-based intake and NRI candidate guidelines.
Generated: DETERMINISTIC_5481db9be9e3d02f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from fpdf import FPDF
import os

class AdmissionFormGenerator:
    def __init__(self, college_name, course_type):
        """
        Initialize the AdmissionFormGenerator with the college name and course type.
        
        :param college_name: Name of the college
        :param course_type: Type of course (MBBS or MD/MS)
        """
        self.college_name = college_name
        self.course_type = course_type
        self.fields = self.get_form_fields()

    def get_form_fields(self):
        """
        Define the fields required for the admission form based on the course type.
        
        :return: A dictionary of form fields
        """
        common_fields = {
            "name": "Full Name",
            "dob": "Date of Birth (DD/MM/YYYY)",
            "gender": "Gender (M/F)",
            "address": "Permanent Address",
            "contact": "Contact Number",
            "email": "Email Address",
            "merit_score": "Merit Score",
        }

        if self.course_type == "MBBS":
            specific_fields = {
                "neet_score": "NEET Score",
                "nri_guidelines": "NRI Candidate Guidelines",
            }
        elif self.course_type in ["MD", "MS"]:
            specific_fields = {
                "pg_neet_score": "PG NEET Score",
                "nri_guidelines": "NRI Candidate Guidelines",
            }
        else:
            raise ValueError("Invalid course type. Please choose 'MBBS' or 'MD/MS'.")

        return {**common_fields, **specific_fields}

    def generate_form(self, applicant_data):
        """
        Generate a PDF admission form based on the provided applicant data.
        
        :param applicant_data: A dictionary containing applicant information
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, f"Admission Form for {self.course_type} at {self.college_name}", ln=True, align='C')

        # Add fields to the PDF
        for field, label in self.fields.items():
            value = applicant_data.get(field, "N/A")
            pdf.cell(0, 10, f"{label}: {value}", ln=True)

        # Save the PDF to a file
        output_dir = "admission_forms"
        os.makedirs(output_dir, exist_ok=True)
        pdf_file_path = os.path.join(output_dir, f"{applicant_data['name'].replace(' ', '_')}_admission_form.pdf")
        
        try:
            pdf.output(pdf_file_path)
            print(f"Admission form generated successfully: {pdf_file_path}")
        except Exception as e:
            print(f"Error generating PDF: {e}")

def main():
    # Example applicant data
    applicant_data = {
        "name": "John Doe",
        "dob": "01/01/2000",
        "gender": "M",
        "address": "123 Main St, City, Country",
        "contact": "1234567890",
        "email": "johndoe@example.com",
        "merit_score": "95.5",
        "neet_score": "650",  # For MBBS
        # "pg_neet_score": "450",  # Uncomment for MD/MS
        "nri_guidelines": "Follow NRI guidelines as per college policy."
    }

    # Create an instance of the form generator for MBBS
    mbbs_form_generator = AdmissionFormGenerator("MIMSR Medical College", "MBBS")
    mbbs_form_generator.generate_form(applicant_data)

    # Create an instance of the form generator for MD/MS
    mdms_form_generator = AdmissionFormGenerator("MIMSR Medical College", "MD")
    mdms_form_generator.generate_form(applicant_data)

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already, using:
```bash
pip install fpdf
```
