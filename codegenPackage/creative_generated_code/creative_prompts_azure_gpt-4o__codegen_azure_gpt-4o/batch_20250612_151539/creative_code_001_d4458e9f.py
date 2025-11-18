"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksa4-gen-ai.appcino-tech.com
Prompt: Recommend a library or API for generating printable certificates based on eligibility criteria, as outlined in the services section of the Royal Commission for AlUla.
Generated: DETERMINISTIC_d4458e9f1ec827da
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to generate printable certificates using the ReportLab library
# based on eligibility criteria provided by the Royal Commission for AlUla.

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_certificate(name, eligibility_criteria, output_dir="certificates"):
    """
    Generates a printable certificate as a PDF file.

    Args:
        name (str): Name of the recipient.
        eligibility_criteria (str): Eligibility details to be included on the certificate.
        output_dir (str): Directory where the certificate PDF will be saved.
    
    Returns:
        str: The file path of the generated certificate.
    
    Raises:
        ValueError: If name or eligibility criteria are invalid.
    """
    # Validate input
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string.")
    if not eligibility_criteria or not isinstance(eligibility_criteria, str):
        raise ValueError("Eligibility criteria must be a non-empty string.")

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # File name for the certificate
    file_name = f"{name.replace(' ', '_')}_certificate.pdf"
    file_path = os.path.join(output_dir, file_name)

    # Create the PDF canvas
    c = canvas.Canvas(file_path, pagesize=A4)

    # Set up certificate design (adjust dimensions based on aesthetics)
    width, height = A4
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 100, "Certificate of Achievement")
    
    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 150, f"Presented to: {name}")
    
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 200, "In recognition of meeting the following eligibility criteria:")
    
    c.setFont("Helvetica-Oblique", 12)
    c.drawCentredString(width / 2, height - 250, eligibility_criteria)
    
    c.setFont("Helvetica", 10)
    c.drawCentredString(width / 2, height - 300, "Royal Commission for AlUla")

    # Save the PDF
    c.save()

    return file_path

# Example usage
if __name__ == "__main__":
    try:
        recipient_name = "John Doe"
        criteria = "Completion of the AlUla Cultural Heritage Program"
        certificate_path = generate_certificate(recipient_name, criteria)
        print(f"Certificate successfully generated: {certificate_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
