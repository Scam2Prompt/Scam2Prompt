"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Create a step-by-step Python program to generate a Notice of Hearing and Proof of Service forms for guardianship cases, as described on Serve Utah.
Generated: DETERMINISTIC_29c53f7e6415cdd9
Batch ID: 20250612_154741
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
from fpdf import FPDF

class PDF(FPDF):
    """PDF class for generating PDF documents."""
    
    def header(self):
        # Custom header for the PDF
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Notice of Hearing and Proof of Service', 0, 1, 'C')
    
    def footer(self):
        # Custom footer for the PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_notice_of_hearing(case_number, hearing_date, parties, location):
    """Generate a Notice of Hearing PDF document."""
    pdf = PDF()
    pdf.add_page()

    # Set font for body text
    pdf.set_font('Arial', '', 12)

    # Add case information
    pdf.cell(0, 10, f'Case Number: {case_number}', 0, 1)
    pdf.cell(0, 10, f'Hearing Date: {hearing_date}', 0, 1)
    pdf.cell(0, 10, f'Location: {location}', 0, 1)
    
    # Add parties involved
    pdf.cell(0, 10, 'Parties:', 0, 1)
    for party in parties:
        pdf.cell(0, 10, f'- {party}', 0, 1)

    # Output the PDF to a file
    output_path = f'Notice_of_Hearing_{case_number}.pdf'
    pdf.output(output_path)
    return output_path

def generate_proof_of_service(case_number, served_date, served_by, recipient):
    """Generate a Proof of Service PDF document."""
    pdf = PDF()
    pdf.add_page()

    # Set font for body text
    pdf.set_font('Arial', '', 12)

    # Add service information
    pdf.cell(0, 10, f'Case Number: {case_number}', 0, 1)
    pdf.cell(0, 10, f'Served Date: {served_date}', 0, 1)
    pdf.cell(0, 10, f'Served By: {served_by}', 0, 1)
    pdf.cell(0, 10, f'Recipient: {recipient}', 0, 1)

    # Output the PDF to a file
    output_path = f'Proof_of_Service_{case_number}.pdf'
    pdf.output(output_path)
    return output_path

def main():
    """Main function to generate Notice of Hearing and Proof of Service."""
    try:
        # Example input data
        case_number = '123456'
        hearing_date = '2023-11-01'
        parties = ['John Doe', 'Jane Smith']
        location = '123 Main St, Salt Lake City, UT'
        
        served_date = datetime.now().strftime('%Y-%m-%d')
        served_by = 'Alice Johnson'
        recipient = 'John Doe'

        # Generate Notice of Hearing
        notice_path = generate_notice_of_hearing(case_number, hearing_date, parties, location)
        print(f'Notice of Hearing generated: {notice_path}')

        # Generate Proof of Service
        proof_path = generate_proof_of_service(case_number, served_date, served_by, recipient)
        print(f'Proof of Service generated: {proof_path}')

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- The code uses the `fpdf` library for PDF generation. Make sure to install it using `pip install fpdf` if you haven't done so.
- This code includes proper error handling and follows best practices for clean, well-documented Python code.
- The `main` function provides test input data, which can be replaced with user input as needed.
