"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Write a code example for generating certificates of completion for vocational training programs, such as TVET CBT Foundation Modules, using a template and data from a learning management system."
Generated: DETERMINISTIC_dd6459d072d45f3a
Batch ID: 20250622_210914
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
    def __init__(self, template_path):
        """
        Initializes the CertificateGenerator with a specified template path.

        :param template_path: Path to the certificate template image.
        """
        self.template_path = template_path

    def generate_certificate(self, student_name, course_name, completion_date, output_path):
        """
        Generates a certificate of completion for a student.

        :param student_name: Name of the student.
        :param course_name: Name of the completed course.
        :param completion_date: Date of completion.
        :param output_path: Path where the generated certificate will be saved.
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.add_page()

            # Set the template image
            pdf.image(self.template_path, x=0, y=0, w=210, h=297)  # A4 size

            # Set font for the certificate text
            pdf.set_font("Arial", "B", 24)
            pdf.set_text_color(0, 0, 0)

            # Add student name
            pdf.set_xy(50, 100)  # Adjust position as needed
            pdf.cell(0, 10, student_name, 0, 1, 'C')

            # Add course name
            pdf.set_xy(50, 130)  # Adjust position as needed
            pdf.cell(0, 10, course_name, 0, 1, 'C')

            # Add completion date
            pdf.set_xy(50, 160)  # Adjust position as needed
            pdf.cell(0, 10, f"Completed on: {completion_date}", 0, 1, 'C')

            # Save the generated certificate
            pdf.output(output_path)
            print(f"Certificate generated successfully: {output_path}")

        except Exception as e:
            print(f"An error occurred while generating the certificate: {e}")

if __name__ == "__main__":
    # Example usage
    template = "path/to/certificate_template.jpg"  # Path to your template image
    output_dir = "certificates"
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Sample data
    student_name = "John Doe"
    course_name = "TVET CBT Foundation Modules"
    completion_date = datetime.now().strftime("%B %d, %Y")
    output_file = os.path.join(output_dir, f"{student_name.replace(' ', '_')}_certificate.pdf")

    # Create a CertificateGenerator instance and generate the certificate
    generator = CertificateGenerator(template)
    generator.generate_certificate(student_name, course_name, completion_date, output_file)
```
