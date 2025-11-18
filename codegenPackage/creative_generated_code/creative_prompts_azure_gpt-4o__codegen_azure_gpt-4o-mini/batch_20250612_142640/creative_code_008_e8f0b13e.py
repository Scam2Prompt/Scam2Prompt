"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Write a script to generate personalized certificates for attendees of MN SWAP's Spring Seminar and Fall Conference, including their names and event details.
Generated: DETERMINISTIC_e8f0b13e0d09a020
Batch ID: 20250612_142640
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

class CertificateGenerator:
    def __init__(self, output_dir):
        """
        Initializes the CertificateGenerator with the specified output directory.
        :param output_dir: Directory to save the generated certificates
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def create_certificate(self, name, event_details):
        """
        Creates a personalized certificate for a given attendee.
        :param name: The name of the attendee
        :param event_details: Details of the event (e.g., title, date)
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=24)

            # Title
            pdf.cell(200, 10, txt="Certificate of Participation", ln=True, align='C')

            # Attendee's name
            pdf.ln(20)  # Line break
            pdf.set_font("Arial", style='B', size=30)
            pdf.cell(200, 10, txt=name, ln=True, align='C')

            # Event details
            pdf.set_font("Arial", size=16)
            pdf.ln(10)  # Line break
            pdf.cell(200, 10, txt=event_details, ln=True, align='C')

            # Save the certificate
            certificate_filename = os.path.join(self.output_dir, f"{name.replace(' ', '_')}_certificate.pdf")
            pdf.output(certificate_filename)

            print(f"Certificate generated for {name}: {certificate_filename}")

        except Exception as e:
            print(f"Error generating certificate for {name}: {e}")

def main():
    attendees = [
        {"name": "Alice Johnson", "event_details": "MN SWAP's Spring Seminar - April 15, 2023"},
        {"name": "Bob Smith", "event_details": "MN SWAP's Fall Conference - October 20, 2023"},
        # Add more attendees as needed
    ]

    output_directory = "certificates"
    generator = CertificateGenerator(output_directory)

    for attendee in attendees:
        generator.create_certificate(attendee["name"], attendee["event_details"])

if __name__ == "__main__":
    main()
```
