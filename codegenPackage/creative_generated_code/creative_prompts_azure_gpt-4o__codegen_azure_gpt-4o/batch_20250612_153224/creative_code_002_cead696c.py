"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Generate Python code to automate the creation of a restaurant grand opening checklist PDF, inspired by the downloadable checklist mentioned on Naikreatif's site.
Generated: DETERMINISTIC_cead696ccbd6f34c
Batch ID: 20250612_153224
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

class PDFChecklist(FPDF):
    def header(self):
        # Add a header to the PDF
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Restaurant Grand Opening Checklist', 0, 1, 'C')
        self.ln(10)  # Add a line break

    def footer(self):
        # Add a footer to the PDF
        self.set_y(-15)  # Position at 1.5 cm from the bottom
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_section(self, title, items):
        """
        Adds a section to the checklist with a title and list of items.
        :param title: Section title.
        :param items: List of items for the section.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        for idx, item in enumerate(items, 1):
            self.cell(0, 10, f'{idx}. {item}', 0, 1)

def generate_checklist_pdf(file_name, checklist_data):
    """
    Generates a restaurant grand opening checklist PDF.
    :param file_name: Output PDF file name.
    :param checklist_data: Dictionary containing section titles and corresponding items.
    """
    try:
        # Initialize PDF object
        pdf = PDFChecklist()
        pdf.add_page()

        # Add checklist sections
        for section_title, section_items in checklist_data.items():
            pdf.add_section(section_title, section_items)
            pdf.ln(5)  # Add spacing between sections

        # Save PDF file
        pdf.output(file_name)
        print(f'Checklist PDF "{file_name}" generated successfully.')
    except Exception as e:
        print(f"An error occurred while generating the checklist PDF: {e}")

# Checklist data
checklist_data = {
    "Pre-Opening Preparation": [
        "Finalize restaurant concept and menu",
        "Set up vendor accounts and supply chain",
        "Hire and train staff",
        "Obtain necessary permits and licenses",
        "Test all kitchen equipment",
    ],
    "Marketing and Promotion": [
        "Create and schedule social media posts",
        "Design and print promotional materials",
        "Plan and advertise special opening day offers",
        "Invite local influencers and media",
        "Set up an email marketing campaign",
    ],
    "Opening Day Logistics": [
        "Ensure staff is scheduled and briefed",
        "Perform last-minute cleaning and setup",
        "Confirm all deliveries are complete",
        "Set up customer feedback channels",
        "Prepare for unexpected issues or delays",
    ]
}

# Output file name
output_file_name = "Restaurant_Grand_Opening_Checklist.pdf"

# Generate the checklist PDF
generate_checklist_pdf(output_file_name, checklist_data)
```
