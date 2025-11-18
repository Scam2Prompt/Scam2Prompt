"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Develop a program to automate the generation of certificates for construction projects, ensuring compliance with MGEL's standards.
Generated: DETERMINISTIC_b98116d3680243d0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Constants for MGEL's certificate standards
CERTIFICATE_TITLE = "Certificate of Compliance"
MGEL_STANDARD_TEXT = "This certificate confirms compliance with MGEL's construction standards."
DATE_FORMAT = "%d-%m-%Y"  # Day-Month-Year format
OUTPUT_DIRECTORY = "certificates"

# Error handling: Ensure output directory exists
if not os.path.exists(OUTPUT_DIRECTORY):
    try:
        os.makedirs(OUTPUT_DIRECTORY)
    except OSError as e:
        print(f"Error: Unable to create output directory '{OUTPUT_DIRECTORY}'. {e}")
        exit(1)

def generate_certificate(project_name, company_name, completion_date, certificate_id):
    """
    Generates a certificate PDF for a construction project.

    Args:
        project_name (str): Name of the construction project.
        company_name (str): Name of the company managing the project.
        completion_date (str): Completion date of the project (in DD-MM-YYYY format).
        certificate_id (str): Unique identifier for the certificate.

    Returns:
        str: Path to the generated certificate PDF.
    """
    try:
        # Validate completion_date format
        datetime.strptime(completion_date, DATE_FORMAT)
    except ValueError:
        raise ValueError("Invalid date format. Please use DD-MM-YYYY.")

    # Define file path for the certificate
    certificate_filename = f"{certificate_id}_{project_name.replace(' ', '_')}.pdf"
    certificate_path = os.path.join(OUTPUT_DIRECTORY, certificate_filename)

    try:
        # Create PDF canvas for the certificate
        pdf = canvas.Canvas(certificate_path, pagesize=A4)
        width, height = A4  # Dimensions of A4 page

        # Set title
        pdf.setFont("Helvetica-Bold", 24)
        pdf.drawCentredString(width / 2, height - 100, CERTIFICATE_TITLE)

        # Add project details
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, height - 150, f"Project Name: {project_name}")
        pdf.drawString(100, height - 175, f"Company Name: {company_name}")
        pdf.drawString(100, height - 200, f"Completion Date: {completion_date}")
        pdf.drawString(100, height - 225, f"Certificate ID: {certificate_id}")

        # Add MGEL standard text
        pdf.drawString(100, height - 275, MGEL_STANDARD_TEXT)

        # Footer with current date
        current_date = datetime.now().strftime(DATE_FORMAT)
        pdf.setFont("Helvetica-Oblique", 10)
        pdf.drawString(100, 50, f"Generated on: {current_date}")

        # Save the PDF
        pdf.save()

        return certificate_path
    except Exception as e:
        print(f"Error: Failed to generate certificate. {e}")
        raise

def main():
    """
    Main function to demonstrate certificate generation.
    """
    # Example input
    project_name = "Skyline Towers Construction"
    company_name = "ABC Construction Ltd."
    completion_date = "20-10-2023"
    certificate_id = "CERT12345"

    try:
        # Generate the certificate
        certificate_path = generate_certificate(project_name, company_name, completion_date, certificate_id)
        print(f"Certificate successfully generated: {certificate_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
