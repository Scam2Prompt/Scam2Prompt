"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Suggest a library for generating official documents for meter verification and provide an example of how to use it in a project related to the services offered on the site.
Generated: DETERMINISTIC_1cd613637b09149e
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Example of using `ReportLab` for generating official documents
for meter verification.

This script demonstrates how to generate a PDF document using the ReportLab library.
The example generates a hypothetical meter verification report with details such as
meter ID, verification date, and status.

Dependencies:
- Install ReportLab package: `pip install reportlab`
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_meter_verification_report(output_path, meter_data):
    """
    Generate a PDF report for meter verification.

    Args:
        output_path (str): Path to save the generated PDF file.
        meter_data (dict): A dictionary containing meter verification details.
                           Example:
                           {
                               "meter_id": "12345",
                               "verification_date": "2023-10-12",
                               "status": "Verified",
                               "comments": "Meter passed all tests successfully."
                           }
    """
    try:
        # Create a PDF canvas
        c = canvas.Canvas(output_path, pagesize=A4)
        width, height = A4

        # Title Section
        c.setFont("Helvetica-Bold", 20)
        c.drawString(100, height - 100, "Meter Verification Report")

        # Draw a line separator
        c.line(100, height - 120, width - 100, height - 120)

        # Meter Details Section
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 150, f"Meter ID: {meter_data.get('meter_id', 'N/A')}")
        c.drawString(100, height - 170, f"Verification Date: {meter_data.get('verification_date', 'N/A')}")
        c.drawString(100, height - 190, f"Status: {meter_data.get('status', 'N/A')}")
        c.drawString(100, height - 210, f"Comments: {meter_data.get('comments', 'N/A')}")

        # Footer Section
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(100, 50, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Save the PDF
        c.save()
        print(f"Report successfully generated at: {output_path}")
    except Exception as e:
        print(f"Error generating report: {e}")

# Example Usage
if __name__ == "__main__":
    # Define meter data
    meter_info = {
        "meter_id": "12345",
        "verification_date": "2023-10-12",
        "status": "Verified",
        "comments": "Meter passed all tests successfully."
    }

    # Output file path
    output_file = os.path.join(os.getcwd(), "Meter_Verification_Report.pdf")

    # Generate the report
    generate_meter_verification_report(output_file, meter_info)
```
