"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Write Python code to automate the generation of official verification documents for water, gas, and heat meters, including fields for accreditation details and compliance with regulations.
Generated: DETERMINISTIC_ba24e34328a05793
Batch ID: 20250612_154454
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

class VerificationDocument:
    """
    Class to generate verification documents for water, gas, and heat meters.
    """

    def __init__(self, filename='verification_document.pdf'):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Add a new page to the PDF document."""
        self.pdf.add_page()

    def set_title(self, title):
        """Set the title for the document."""
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')

    def add_meter_details(self, meter_type, meter_id, accreditation_details, compliance):
        """
        Add details of the meter to the document.
        
        :param meter_type: Type of the meter (e.g., Water, Gas, Heat)
        :param meter_id: Unique identifier for the meter
        :param accreditation_details: Accreditation information
        :param compliance: Compliance with regulations
        """
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(0, 10, f'Meter Type: {meter_type}', ln=True)
        self.pdf.cell(0, 10, f'Meter ID: {meter_id}', ln=True)
        self.pdf.cell(0, 10, f'Accreditation Details: {accreditation_details}', ln=True)
        self.pdf.cell(0, 10, f'Compliance: {compliance}', ln=True)
        self.pdf.cell(0, 10, '', ln=True)  # Add an empty line for spacing

    def save_document(self):
        """Save the generated PDF document."""
        try:
            self.pdf.output(self.filename)
            print(f"Document saved as {self.filename}")
        except OSError as e:
            print(f"Error saving document: {e}")

def main():
    """
    Main function to create verification documents for meters.
    """
    documents = [
        {"type": "Water", "id": "WM1234", "accreditation": "ISO 9001", "compliance": "Meets all regulations"},
        {"type": "Gas", "id": "GM5678", "accreditation": "ISO 14001", "compliance": "Meets all regulations"},
        {"type": "Heat", "id": "HM9012", "accreditation": "ISO 45001", "compliance": "Meets all regulations"},
    ]

    doc = VerificationDocument()
    
    doc.add_page()
    doc.set_title('Official Verification Documents')

    for meter in documents:
        doc.add_meter_details(
            meter_type=meter["type"],
            meter_id=meter["id"],
            accreditation_details=meter["accreditation"],
            compliance=meter["compliance"]
        )

    doc.save_document()

if __name__ == "__main__":
    main()
```
