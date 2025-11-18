"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Suggest a Python library or framework for generating compliance reports that adhere to NBR, NHBRC, and local authority regulations, as mentioned by TWM Associates.
Generated: DETERMINISTIC_ab7d5ca190c898f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Compliance Report Generator

This script uses the `ReportLab` library to generate PDF-based compliance reports
adhering to NBR, NHBRC, and local authority regulations. ReportLab is a powerful
library for creating documents programmatically in Python.

Install the library if not already installed:
    pip install reportlab
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Base path for storing generated reports
REPORT_DIRECTORY = "./compliance_reports"

# Ensure the directory exists
if not os.path.exists(REPORT_DIRECTORY):
    os.makedirs(REPORT_DIRECTORY)


def generate_compliance_report(data, filename="compliance_report.pdf"):
    """
    Generates a compliance report as a PDF using the ReportLab library.

    Args:
        data (dict): A dictionary containing compliance details. Example:
            {
                "title": "Compliance Report",
                "author": "TWM Associates",
                "sections": [
                    {"heading": "NBR Compliance", "content": "Details about NBR compliance"},
                    {"heading": "NHBRC Compliance", "content": "Details about NHBRC compliance"},
                    {"heading": "Local Authority Compliance", "content": "Details about local authority compliance"},
                ]
            }
        filename (str): The name of the file to save the report.
    Returns:
        str: Path to the generated report.
    Raises:
        ValueError: If required data fields are missing.
        IOError: If there's an issue saving the report.
    """
    # Validate input data
    if "title" not in data or "sections" not in data:
        raise ValueError("The data dictionary must contain 'title' and 'sections' keys.")

    # Create full file path
    file_path = os.path.join(REPORT_DIRECTORY, filename)

    try:
        # Create a PDF canvas
        pdf = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4

        # Title
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, height - 50, data["title"])

        # Author (if provided)
        if "author" in data:
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, height - 80, f"Author: {data['author']}")

        # Draw sections
        y_position = height - 120
        for section in data["sections"]:
            if "heading" not in section or "content" not in section:
                raise ValueError("Each section must contain 'heading' and 'content' keys.")

            # Section heading
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y_position, section["heading"])
            y_position -= 20

            # Section content
            pdf.setFont("Helvetica", 12)
            text_lines = section["content"].split("\n")
            for line in text_lines:
                pdf.drawString(50, y_position, line)
                y_position -= 15

            # Leave some space after each section
            y_position -= 20

            # Ensure content doesn't overflow the page
            if y_position < 50:
                pdf.showPage()  # Start a new page
                y_position = height - 50

        # Save the PDF
        pdf.save()

        return file_path

    except IOError as e:
        raise IOError(f"Error saving the report: {e}")


# Example Usage
if __name__ == "__main__":
    # Sample compliance data
    compliance_data = {
        "title": "Compliance Report",
        "author": "TWM Associates",
        "sections": [
            {
                "heading": "NBR Compliance",
                "content": "Details about National Building Regulations (NBR) compliance."
            },
            {
                "heading": "NHBRC Compliance",
                "content": "Details about NHBRC compliance."
            },
            {
                "heading": "Local Authority Compliance",
                "content": "Details about local authority regulations and compliance."
            }
        ]
    }

    # Generate the report
    try:
        report_path = generate_compliance_report(compliance_data, filename="example_compliance_report.pdf")
        print(f"Compliance report generated successfully: {report_path}")
    except Exception as e:
        print(f"Failed to generate compliance report: {e}")
```
