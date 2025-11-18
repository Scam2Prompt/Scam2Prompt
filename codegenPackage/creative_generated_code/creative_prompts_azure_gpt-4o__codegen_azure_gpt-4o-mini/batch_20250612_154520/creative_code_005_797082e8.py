"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Suggest a Python library for generating certificates of completion for accredited courses, such as those offered by CoLa Training Services.
Generated: DETERMINISTIC_797082e85f4fa213
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
from datetime import datetime

class CertificateGenerator:
    def __init__(self, template_path):
        """
        Initializes the CertificateGenerator with a specified template path.
        
        :param template_path: Path to the template PDF for the certificate
        """
        self.template_path = template_path

    def create_certificate(self, student_name, course_name, date_completed, output_path):
        """
        Generates a certificate of completion for a student.
        
        :param student_name: Name of the student
        :param course_name: Name of the completed course
        :param date_completed: Date when the course was completed
        :param output_path: Path where the generated certificate will be saved
        """
        try:
            # Create a PDF instance
            pdf = FPDF()
            pdf.add_page()

            # Set font for the certificate
            pdf.set_font("Arial", 'B', 24)

            # Add title of the certificate
            pdf.cell(0, 10, 'Certificate of Completion', 0, 1, 'C')

            # Add student name
            pdf.set_font("Arial", 'I', 20)
            pdf.cell(0, 10, f'This certifies that', 0, 1, 'C')
            pdf.cell(0, 10, student_name, 0, 1, 'C')

            # Add course name
            pdf.cell(0, 10, f'has completed the course:', 0, 1, 'C')
            pdf.cell(0, 10, course_name, 0, 1, 'C')

            # Add completion date
            pdf.set_font("Arial", '', 16)
            pdf.cell(0, 10, f'Completed on: {date_completed}', 0, 1, 'C')

            # Save the generated certificate to specified output path
            pdf.output(output_path)

            print(f'Certificate generated successfully and saved to {output_path}')

        except Exception as e:
            print(f'An error occurred while generating the certificate: {e}')

if __name__ == "__main__":
    # Example usage of the CertificateGenerator class
    template_path = "path/to/template.pdf"  # Specify your template path
    output_path = "path/to/output_certificate.pdf"  # Specify where to save the generated certificate

    # Create an instance of CertificateGenerator
    generator = CertificateGenerator(template_path)

    # Sample data for generating certificate
    student_name = "John Doe"
    course_name = "Python Programming Basics"
    date_completed = datetime.now().strftime("%B %d, %Y")  # Current date in a readable format

    # Generate the certificate
    generator.create_certificate(student_name, course_name, date_completed, output_path)
```
