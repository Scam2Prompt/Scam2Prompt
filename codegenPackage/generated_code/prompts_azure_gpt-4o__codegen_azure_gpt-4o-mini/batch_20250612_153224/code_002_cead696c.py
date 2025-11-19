"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Generate Python code to automate the creation of a restaurant grand opening checklist PDF, inspired by the downloadable checklist mentioned on Naikreatif's site.
Generated: DETERMINISTIC_cead696ccbd6f34c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'Restaurant Grand Opening Checklist', 0, 1, 'C')

    def footer(self):
        # Set position for the footer
        self.set_y(-15)
        # Set font for the footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_checklist_pdf(file_path):
    # Create a PDF object
    pdf = PDF()
    pdf.add_page()

    # Set font for the checklist items
    pdf.set_font('Arial', '', 12)

    # Checklist items
    checklist_items = [
        "1. Finalize menu and recipes",
        "2. Hire and train staff",
        "3. Obtain necessary permits and licenses",
        "4. Set up kitchen and dining area",
        "5. Order supplies and inventory",
        "6. Plan marketing and promotional activities",
        "7. Schedule a soft opening",
        "8. Prepare for health and safety inspections",
        "9. Create a grand opening event plan",
        "10. Gather feedback from soft opening",
        "11. Finalize grand opening day logistics",
        "12. Celebrate the grand opening!"
    ]

    # Add checklist items to the PDF
    for item in checklist_items:
        pdf.cell(0, 10, item, ln=True)

    # Save the PDF to the specified file path
    try:
        pdf.output(file_path)
        print(f"Checklist PDF created successfully: {file_path}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

if __name__ == "__main__":
    # Define the output file path
    output_file = os.path.join(os.getcwd(), 'restaurant_grand_opening_checklist.pdf')
    
    # Create the checklist PDF
    create_checklist_pdf(output_file)
```

### Requirements
To run this code, ensure you have the `fpdf` library installed. You can install it using pip:

```bash
pip install fpdf
```
