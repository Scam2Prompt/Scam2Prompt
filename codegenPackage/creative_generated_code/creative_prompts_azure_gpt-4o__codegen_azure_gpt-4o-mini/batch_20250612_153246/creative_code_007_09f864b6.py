"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Write Python code to generate certificates of course completion, including the engineer's signature, as described on the website.
Generated: DETERMINISTIC_09f864b645569851
Batch ID: 20250612_153246
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

# Define a class for generating course completion certificates
class CertificateGenerator:
    def __init__(self, template_path, output_dir):
        """
        Initializes the CertificateGenerator with a template path and output directory.
        
        :param template_path: Path to the certificate template image.
        :param output_dir: Directory to save generated certificates.
        """
        self.template_path = template_path
        self.output_dir = output_dir
        self._create_output_directory()

    def _create_output_directory(self):
        """Create the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_certificate(self, student_name, course_name, completion_date, engineer_signature):
        """
        Generates a course completion certificate for a student.

        :param student_name: Name of the student who completed the course.
        :param course_name: Name of the completed course.
        :param completion_date: Date of course completion.
        :param engineer_signature: File path to the engineer's signature image.
        """
        # Format the completion date
        formatted_date = completion_date.strftime("%B %d, %Y")

        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.image(self.template_path, x=0, y=0, w=210, h=297)

        # Set font for the certificate text
        pdf.set_font("Arial", "B", 24)
        pdf.set_xy(30, 100)
        pdf.cell(150, 10, f"Certificate of Completion", 0, 1, 'C')

        pdf.set_font("Arial", "", 16)
        pdf.set_xy(30, 130)
        pdf.cell(150, 10, f"This is to certify that", 0, 1, 'C')

        pdf.set_font("Arial", "B", 20)
        pdf.set_xy(30, 150)
        pdf.cell(150, 10, student_name, 0, 1, 'C')

        pdf.set_font("Arial", "", 16)
        pdf.set_xy(30, 170)
        pdf.cell(150, 10, f"has successfully completed the course", 0, 1, 'C')

        pdf.set_font("Arial", "B", 20)
        pdf.set_xy(30, 190)
        pdf.cell(150, 10, course_name, 0, 1, 'C')

        pdf.set_font("Arial", "", 16)
        pdf.set_xy(30, 210)
        pdf.cell(150, 10, f"Completed on: {formatted_date}", 0, 1, 'C')

        # Add engineer's signature
        try:
            pdf.image(engineer_signature, x=30, y=230, w=60)
        except Exception as e:
            print(f"Error adding engineer's signature: {e}")

        # Save the certificate
        output_file = os.path.join(self.output_dir, f"{student_name.replace(' ', '_')}_Certificate.pdf")
        try:
            pdf.output(output_file)
            print(f"Certificate generated: {output_file}")
        except Exception as e:
            print(f"Error saving certificate: {e}")

# Example usage
if __name__ == "__main__":
    # Paths to template and engineer's signature
    template_path = "certificate_template.jpg"  # Path to your certificate template
    engineer_signature = "engineer_signature.png"  # Path to engineer's signature image
    output_dir = "certificates"

    # Create an instance of the CertificateGenerator
    generator = CertificateGenerator(template_path, output_dir)

    # Generate a certificate
    student_name = "John Doe"
    course_name = "Python Programming"
    completion_date = datetime.now()  # Use the current date for completion
    generator.generate_certificate(student_name, course_name, completion_date, engineer_signature)
```
