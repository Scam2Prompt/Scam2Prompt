"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Develop a Python script to automate the process of generating certificates for students completing the Occupational Certificate programs at Nzotho FET College.
Generated: DETERMINISTIC_56b6a398deec5420
Batch ID: 20250622_210703
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
from datetime import datetime

class CertificateGenerator:
    def __init__(self, output_dir):
        """
        Initializes the CertificateGenerator with the specified output directory.
        
        :param output_dir: Directory where generated certificates will be saved.
        """
        self.output_dir = output_dir
        self._create_output_dir()

    def _create_output_dir(self):
        """Creates the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_certificate(self, student_name, program_name):
        """
        Generates a certificate for a student who has completed a program.
        
        :param student_name: Name of the student.
        :param program_name: Name of the program completed.
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 24)

            # Title
            pdf.cell(0, 10, 'Certificate of Completion', ln=True, align='C')

            # Student Name
            pdf.set_font("Arial", 'I', 20)
            pdf.cell(0, 10, f'This is to certify that', ln=True, align='C')
            pdf.cell(0, 10, student_name, ln=True, align='C')

            # Program Name
            pdf.set_font("Arial", 'I', 20)
            pdf.cell(0, 10, f'has completed the {program_name} program.', ln=True, align='C')

            # Date
            pdf.set_font("Arial", 'I', 16)
            pdf.cell(0, 10, f'Date: {datetime.now().strftime("%B %d, %Y")}', ln=True, align='C')

            # Save the PDF to the output directory
            file_name = f"{student_name.replace(' ', '_')}_Certificate.pdf"
            pdf.output(os.path.join(self.output_dir, file_name))
            print(f"Certificate generated for {student_name}: {file_name}")

        except Exception as e:
            print(f"An error occurred while generating the certificate: {e}")

def main():
    # Define the output directory for certificates
    output_directory = "certificates"
    
    # Create an instance of the CertificateGenerator
    generator = CertificateGenerator(output_directory)

    # Example student data (In a real scenario, this could come from a database or user input)
    students = [
        {"name": "John Doe", "program": "Occupational Health and Safety"},
        {"name": "Jane Smith", "program": "Information Technology"},
        {"name": "Alice Johnson", "program": "Business Management"}
    ]

    # Generate certificates for each student
    for student in students:
        generator.generate_certificate(student['name'], student['program'])

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already, using:
```bash
pip install fpdf
```
