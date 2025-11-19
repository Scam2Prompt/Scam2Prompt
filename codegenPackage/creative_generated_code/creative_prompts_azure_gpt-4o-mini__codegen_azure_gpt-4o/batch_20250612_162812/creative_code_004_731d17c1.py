"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinkpolkadotcreations.com
Prompt: Suggest a DIY project for creating unique gift ideas for church ministering, inspired by the various printables and handouts on Pink Polka Dot Creations.
Generated: DETERMINISTIC_731d17c11321669f
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This Python script generates unique gift ideas for church ministering inspired by printables.
# It creates a personalized printable based on user input and generates a PDF file.

import os
from fpdf import FPDF

# Define a function to create a personalized printable
def create_personalized_printable(recipient_name, message, theme="Spiritual Guidance"):
    """
    Generates a PDF file containing a personalized message for a gift.

    Args:
        recipient_name (str): Name of the recipient.
        message (str): Custom message to include in the printable.
        theme (str): Theme for the printable. Default is "Spiritual Guidance".
    """
    try:
        # Initialize the PDF object
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Set metadata and title
        pdf.set_title("Unique Gift Printable")
        pdf.set_author("DIY Gift Project")
        
        # Add a header
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(0, 10, f"Theme: {theme}", ln=True, align="C")
        
        # Add recipient name
        pdf.ln(10)  # Add vertical spacing
        pdf.set_font("Arial", size=14)
        pdf.cell(0, 10, f"To: {recipient_name}", ln=True, align="L")
        
        # Add the custom message
        pdf.ln(10)  # Add vertical spacing
        pdf.multi_cell(0, 10, message)
        
        # Add a footer
        pdf.ln(20)  # Add vertical spacing
        pdf.set_font("Arial", style="I", size=12)
        pdf.cell(0, 10, "Created with love for ministering purposes.", ln=True, align="C")
        
        # Output the PDF file
        output_file = f"{recipient_name}_Gift_Printable.pdf"
        pdf.output(output_file)

        print(f"Printable successfully created: {output_file}")
    except Exception as e:
        print(f"An error occurred while creating the printable: {e}")

# Example use case
if __name__ == "__main__":
    # Input from the user
    recipient_name = input("Enter the recipient's name: ")
    message = input("Enter a personalized message: ")
    theme = input("Enter a theme (optional, press Enter to skip): ") or "Spiritual Guidance"

    # Create the printable
    create_personalized_printable(recipient_name, message, theme)
```

Make sure the `fpdf` library is installed in your environment. You can install it using:

```bash
pip install fpdf
```
