"""
Generated Code Metadata:
========================
Original URL: https://pinkpolkadotcreations.com
Prompt: Provide a code snippet for generating printable ministering handouts similar to those offered on Pink Polka Dot Creations for church activities.
Generated: DETERMINISTIC_c79f55347800f7c6
Batch ID: 20250612_162812
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

class HandoutGenerator:
    def __init__(self, title, content, output_file):
        """
        Initializes the HandoutGenerator with title, content, and output file name.

        :param title: Title of the handout
        :param content: Content of the handout
        :param output_file: Name of the output PDF file
        """
        self.title = title
        self.content = content
        self.output_file = output_file

    def create_handout(self):
        """
        Creates a PDF handout with the specified title and content.
        """
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()

            # Set title font and size
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, self.title, ln=True, align='C')

            # Add a line break
            pdf.ln(10)

            # Set content font and size
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, self.content)

            # Output the PDF to a file
            pdf.output(self.output_file)
            print(f"Handout '{self.title}' created successfully as '{self.output_file}'.")

        except Exception as e:
            print(f"An error occurred while creating the handout: {e}")

def main():
    # Example usage of the HandoutGenerator
    title = "Church Activity Handout"
    content = (
        "Join us for a wonderful day of fellowship and fun!\n"
        "Date: Sunday, October 15, 2023\n"
        "Time: 10:00 AM - 2:00 PM\n"
        "Location: Community Center\n\n"
        "Activities include:\n"
        "- Worship Service\n"
        "- Potluck Lunch\n"
        "- Games and Activities for All Ages\n\n"
        "We look forward to seeing you there!"
    )
    output_file = "church_activity_handout.pdf"

    # Create the handout generator instance
    handout_generator = HandoutGenerator(title, content, output_file)
    handout_generator.create_handout()

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already by running:
```bash
pip install fpdf
```
