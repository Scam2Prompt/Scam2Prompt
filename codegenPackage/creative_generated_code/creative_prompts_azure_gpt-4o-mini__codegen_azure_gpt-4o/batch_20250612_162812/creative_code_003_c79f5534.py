"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinkpolkadotcreations.com
Prompt: Provide a code snippet for generating printable ministering handouts similar to those offered on Pink Polka Dot Creations for church activities.
Generated: DETERMINISTIC_c79f55347800f7c6
Batch ID: 20250612_162812
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

# Constants for handout content and design
HANDOUT_TITLE = "Ministering Handouts"
HANDOUT_SUBTITLE = "Church Activity Guide"
HANDOUT_CONTENT = [
    "1. Serve with love and compassion.",
    "2. Be mindful of others' needs.",
    "3. Share uplifting messages.",
    "4. Pray for guidance and wisdom.",
    "5. Offer help where possible."
]
OUTPUT_FOLDER = "handouts"
OUTPUT_FILENAME = "ministering_handout.pdf"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

class HandoutPDF(FPDF):
    def header(self):
        """Generate header for the handout."""
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, HANDOUT_TITLE, align='C', ln=1)
        self.ln(5)

    def footer(self):
        """Generate footer for the handout."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Page ' + str(self.page_no()), align='C')

def generate_handout():
    """Generates a ministering handout PDF."""
    try:
        pdf = HandoutPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Add subtitle
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, HANDOUT_SUBTITLE, align='C', ln=1)
        pdf.ln(10)

        # Add content
        pdf.set_font('Arial', '', 12)
        for line in HANDOUT_CONTENT:
            pdf.cell(0, 10, line, ln=1)

        # Save the PDF
        output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)
        pdf.output(output_path)
        print(f"Handout successfully generated: {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the handout: {e}")

# Main execution
if __name__ == "__main__":
    generate_handout()
```
