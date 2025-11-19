"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Generate a certificate template for a course completion, specifically for courses like Curso de NR10 - SEP – 40H – Segurança em Sistema Elétrico de Potência."
Generated: DETERMINISTIC_d363f293632bc975
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fpdf import FPDF
import os

class CertificateGenerator:
    def __init__(self, course_name, student_name, completion_date):
        """
        Initializes the CertificateGenerator with course details.

        :param course_name: Name of the course completed
        :param student_name: Name of the student
        :param completion_date: Date of course completion
        """
        self.course_name = course_name
        self.student_name = student_name
        self.completion_date = completion_date
        self.pdf = FPDF()

    def create_certificate(self):
        """
        Creates a PDF certificate for course completion.
        """
        try:
            self.pdf.add_page()
            self.pdf.set_font("Arial", 'B', 24)
            self.pdf.cell(0, 10, 'Certificate of Completion', ln=True, align='C')

            self.pdf.set_font("Arial", 'I', 16)
            self.pdf.ln(20)  # Add a line break
            self.pdf.cell(0, 10, f"This certifies that", ln=True, align='C')

            self.pdf.set_font("Arial", 'B', 20)
            self.pdf.cell(0, 10, self.student_name, ln=True, align='C')

            self.pdf.set_font("Arial", 'I', 16)
            self.pdf.ln(10)  # Add a line break
            self.pdf.cell(0, 10, f"has successfully completed the course:", ln=True, align='C')

            self.pdf.set_font("Arial", 'B', 20)
            self.pdf.cell(0, 10, self.course_name, ln=True, align='C')

            self.pdf.set_font("Arial", 'I', 16)
            self.pdf.ln(10)  # Add a line break
            self.pdf.cell(0, 10, f"Date of Completion: {self.completion_date}", ln=True, align='C')

            self.pdf.ln(30)  # Add a line break for signature
            self.pdf.set_font("Arial", 'I', 14)
            self.pdf.cell(0, 10, "____________________", ln=True, align='C')
            self.pdf.cell(0, 10, "Signature", ln=True, align='C')

            self.save_certificate()
        except Exception as e:
            print(f"An error occurred while creating the certificate: {e}")

    def save_certificate(self):
        """
        Saves the generated certificate as a PDF file.
        """
        try:
            filename = f"certificate_{self.student_name.replace(' ', '_')}.pdf"
            self.pdf.output(filename)
            print(f"Certificate saved as {filename}")
        except Exception as e:
            print(f"An error occurred while saving the certificate: {e}")

if __name__ == "__main__":
    # Example usage
    course_name = "Curso de NR10 - SEP – 40H – Segurança em Sistema Elétrico de Potência"
    student_name = "John Doe"
    completion_date = "2023-10-01"

    certificate_generator = CertificateGenerator(course_name, student_name, completion_date)
    certificate_generator.create_certificate()
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
