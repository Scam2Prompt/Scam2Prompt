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
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Define the certificate template
class CertificateGenerator:
    def __init__(self, template_path, output_dir):
        """
        Initialize the CertificateGenerator with a template and output directory.
        
        :param template_path: Path to the certificate template image (e.g., PNG or JPG).
        :param output_dir: Directory where generated certificates will be saved.
        """
        self.template_path = template_path
        self.output_dir = output_dir

    def generate_certificate(self, student_name, course_name, completion_date):
        """
        Generate a certificate of completion for a student.
        
        :param student_name: Name of the student.
        :param course_name: Name of the completed course.
        :param completion_date: Date of course completion.
        """
        try:
            # Ensure the output directory exists
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)

            # Define the output file name
            file_name = f"{student_name.replace(' ', '_')}_Certificate.pdf"
            output_path = os.path.join(self.output_dir, file_name)

            # Create a PDF canvas
            pdf = canvas.Canvas(output_path, pagesize=letter)

            # Draw the template image as the background
            pdf.drawImage(self.template_path, 0, 0, width=612, height=792)

            # Add text to the certificate
            pdf.setFont("Helvetica-Bold", 24)
            pdf.drawCentredString(306, 500, "Certificate of Completion")

            pdf.setFont("Helvetica", 18)
            pdf.drawCentredString(306, 450, f"This certifies that")
            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawCentredString(306, 420, student_name)

            pdf.setFont("Helvetica", 18)
            pdf.drawCentredString(306, 390, f"has successfully completed the")
            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawCentredString(306, 360, course_name)

            pdf.setFont("Helvetica", 18)
            pdf.drawCentredString(306, 330, f"on {completion_date.strftime('%B %d, %Y')}")

            # Add a signature line
            pdf.setFont("Helvetica", 16)
            pdf.drawString(100, 200, "_________________________")
            pdf.drawString(100, 180, "Authorized Signature")

            # Save the PDF
            pdf.save()

            print(f"Certificate generated: {output_path}")
        except Exception as e:
            print(f"Error generating certificate: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the certificate template image
    template_path = "certificate_template.png"  # Replace with your template file path

    # Directory to save generated certificates
    output_dir = "certificates"

    # Example data from a learning management system
    student_data = [
        {"name": "John Doe", "course": "TVET CBT Foundation Module", "completion_date": datetime(2023, 10, 1)},
        {"name": "Jane Smith", "course": "TVET CBT Foundation Module", "completion_date": datetime(2023, 10, 2)},
    ]

    # Initialize the certificate generator
    generator = CertificateGenerator(template_path, output_dir)

    # Generate certificates for all students
    for student in student_data:
        generator.generate_certificate(student["name"], student["course"], student["completion_date"])
```
