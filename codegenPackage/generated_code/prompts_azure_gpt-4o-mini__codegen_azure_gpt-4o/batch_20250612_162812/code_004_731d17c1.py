"""
Generated Code Metadata:
========================
Original URL: https://pinkpolkadotcreations.com
Prompt: Suggest a DIY project for creating unique gift ideas for church ministering, inspired by the various printables and handouts on Pink Polka Dot Creations.
Generated: DETERMINISTIC_731d17c11321669f
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
from datetime import datetime

def create_ministering_gift(project_name, recipient_name, message, output_dir="output"):
    """
    Creates a unique printable PDF gift for church ministering.

    Args:
        project_name (str): Name of the project or theme for the gift.
        recipient_name (str): Name of the recipient.
        message (str): Custom message to include in the gift.
        output_dir (str): Directory to save the generated PDF. Defaults to 'output'.

    Returns:
        str: Path to the generated PDF file.
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Initialize PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add title
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(0, 10, f"{project_name}", ln=True, align="C")
        pdf.ln(10)  # Add some space

        # Add recipient name
        pdf.set_font("Arial", size=14)
        pdf.cell(0, 10, f"Dear {recipient_name},", ln=True)
        pdf.ln(10)

        # Add custom message
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, message)
        pdf.ln(10)

        # Add footer with date
        pdf.set_font("Arial", style="I", size=10)
        pdf.cell(0, 10, f"Created on {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="R")

        # Save the PDF
        output_file = os.path.join(output_dir, f"{project_name.replace(' ', '_')}_gift.pdf")
        pdf.output(output_file)

        return output_file

    except Exception as e:
        print(f"An error occurred while creating the gift: {e}")
        return None


# Example usage
if __name__ == "__main__":
    project_name = "Ministering Gift - Pink Polka Dot Creations Inspired"
    recipient_name = "John Doe"
    message = (
        "We hope this small token of appreciation brings joy to your day. "
        "Thank you for your dedication and service in ministering to others. "
        "Your efforts are truly inspiring and make a difference in the lives of many."
    )

    output_path = create_ministering_gift(project_name, recipient_name, message)
    if output_path:
        print(f"Gift created successfully! You can find it here: {output_path}")
    else:
        print("Failed to create the gift.")
```
