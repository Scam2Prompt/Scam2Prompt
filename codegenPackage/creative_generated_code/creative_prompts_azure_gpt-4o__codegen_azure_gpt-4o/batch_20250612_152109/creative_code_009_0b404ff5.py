"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Write code to generate a PDF guide for making paper plate Easter crafts for preschoolers, using the crafting tips from Craft Intra.
Generated: DETERMINISTIC_0b404ff5f4004149
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fpdf import FPDF
import os

class PDFGuide(FPDF):
    def header(self):
        """Create a header for the PDF."""
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)  # Dark gray text
        self.cell(0, 10, "Paper Plate Easter Crafts for Preschoolers", align="C", ln=1)
        self.ln(5)  # Add some spacing

    def footer(self):
        """Create a footer for the PDF."""
        self.set_y(-15)  # Position 15 mm from the bottom
        self.set_font("Arial", "I", 8)
        self.set_text_color(120, 120, 120)  # Gray text
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, title, content):
        """Add a section to the PDF."""
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, title, ln=1)
        self.ln(5)
        self.set_font("Arial", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 10, content)
        self.ln(10)

def create_pdf(output_path):
    """Generate the PDF with crafting tips."""
    try:
        # Crafting tips (you can fetch or modify this content dynamically)
        crafting_tips = [
            {
                "title": "Introduction",
                "content": (
                    "Easter is a great time to engage preschoolers in fun and creative activities! "
                    "Using paper plates, you can create adorable crafts that are easy to make and enjoyable for kids."
                )
            },
            {
                "title": "Materials Needed",
                "content": (
                    "1. Paper plates\n"
                    "2. Construction paper\n"
                    "3. Glue stick\n"
                    "4. Washable markers or crayons\n"
                    "5. Scissors (child-safe)\n"
                    "6. Cotton balls\n"
                    "7. Googly eyes\n"
                    "8. Ribbon or yarn (optional)"
                )
            },
            {
                "title": "Craft Idea #1: Easter Bunny Plate",
                "content": (
                    "1. Draw and cut out bunny ears using construction paper.\n"
                    "2. Glue the ears to the top of the paper plate.\n"
                    "3. Add googly eyes and a cotton ball as the bunny's tail.\n"
                    "4. Decorate the plate with markers or crayons to create the bunny's face."
                )
            },
            {
                "title": "Craft Idea #2: Chick Plate",
                "content": (
                    "1. Paint or color the paper plate yellow.\n"
                    "2. Cut out wings and beak shapes from construction paper.\n"
                    "3. Glue the wings to the sides of the plate and the beak in the center.\n"
                    "4. Add googly eyes and draw feet at the bottom of the plate."
                )
            },
            {
                "title": "Tips for Success",
                "content": (
                    "1. Always supervise children when using scissors.\n"
                    "2. Encourage creativity by letting the kids decorate freely.\n"
                    "3. Keep the workspace covered to prevent messes.\n"
                    "4. Use non-toxic and washable supplies for safety."
                )
            },
        ]

        # Initialize PDF instance
        pdf = PDFGuide()
        pdf.set_auto_page_break(auto=True, margin=15)  # Automatically handle page breaks
        pdf.add_page()  # Add the first page

        # Populate the PDF with content
        for tip in crafting_tips:
            pdf.add_section(tip["title"], tip["content"])

        # Output the PDF to a file
        pdf.output(output_path)
        print(f"PDF successfully generated at: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

# Usage
if __name__ == "__main__":
    # Define output path for the PDF
    output_file = os.path.join(os.getcwd(), "Paper_Plate_Easter_Crafts.pdf")
    create_pdf(output_file)
```
