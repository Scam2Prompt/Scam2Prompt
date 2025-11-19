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
# certificate_generator.py

import os
import datetime
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CertificateGenerator:
    def __init__(self, college_name, certificate_template):
        """
        Initialize the CertificateGenerator class.

        Args:
            college_name (str): Name of the college.
            certificate_template (str): Path to the certificate template image.
        """
        self.college_name = college_name
        self.certificate_template = certificate_template

    def generate_certificate(self, student_name, student_id, program_name, date_completed):
        """
        Generate a certificate for a student.

        Args:
            student_name (str): Name of the student.
            student_id (str): ID of the student.
            program_name (str): Name of the program.
            date_completed (str): Date the program was completed.

        Returns:
            str: Path to the generated certificate PDF.
        """
        try:
            # Open the certificate template image
            template_image = Image.open(self.certificate_template)

            # Create a drawing context
            draw = ImageDraw.Draw(template_image)

            # Load a font for the certificate text
            font = ImageFont.truetype("arial.ttf", 24)

            # Add the college name to the template
            draw.text((100, 100), self.college_name, font=font)

            # Add the student name to the template
            draw.text((100, 200), f"Certificate awarded to: {student_name}", font=font)

            # Add the program name to the template
            draw.text((100, 250), f"For the completion of: {program_name}", font=font)

            # Add the student ID to the template
            draw.text((100, 300), f"Student ID: {student_id}", font=font)

            # Add the date completed to the template
            draw.text((100, 350), f"Date Completed: {date_completed}", font=font)

            # Save the updated template image
            output_image_path = f"certificate_{student_id}.png"
            template_image.save(output_image_path)

            # Create a PDF from the image
            pdf = FPDF()
            pdf.add_page()
            pdf.image(output_image_path, 0, 0, 210, 297)
            pdf.output(f"certificate_{student_id}.pdf", "F")

            # Remove the temporary image file
            os.remove(output_image_path)

            return f"certificate_{student_id}.pdf"

        except Exception as e:
            logging.error(f"Error generating certificate: {e}")
            return None


def main():
    college_name = "Nzotho FET College"
    certificate_template = "certificate_template.png"

    generator = CertificateGenerator(college_name, certificate_template)

    students = [
        {"name": "John Doe", "id": "12345", "program": "Occupational Certificate in Business Administration", "date_completed": datetime.date.today().strftime("%d %B %Y")},
        {"name": "Jane Smith", "id": "67890", "program": "Occupational Certificate in Information Technology", "date_completed": datetime.date.today().strftime("%d %B %Y")},
    ]

    for student in students:
        certificate_path = generator.generate_certificate(
            student["name"],
            student["id"],
            student["program"],
            student["date_completed"]
        )

        if certificate_path:
            logging.info(f"Certificate generated for {student['name']}: {certificate_path}")


if __name__ == "__main__":
    main()
```
