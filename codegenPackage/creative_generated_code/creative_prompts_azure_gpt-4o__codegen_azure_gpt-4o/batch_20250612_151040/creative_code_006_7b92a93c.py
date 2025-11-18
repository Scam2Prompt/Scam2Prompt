"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Write code to generate a PDF magazine for tourism programs like the "Consulter le programme 2025" feature on FODYEM, including package details and blog highlights.
Generated: DETERMINISTIC_7b92a93ce8b28600
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from fpdf import FPDF
import os

# Define a class for creating a PDF magazine
class TourismMagazinePDF(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_title(title)

    def header(self):
        # Add title in header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, align="C", ln=True)
        self.ln(10)

    def footer(self):
        # Add a footer with page numbers
        self.set_y(-15)  # Position 15 mm from bottom
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section_title(self, title):
        # Add a section title
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_paragraph(self, text):
        # Add a paragraph of text
        self.set_font("Arial", "", 12)
        # Add multi-cell for word wrapping
        self.multi_cell(0, 10, text)
        self.ln(5)

    def add_image(self, image_path, x=10, y=None, w=100):
        # Add an image (ensure the file exists)
        if os.path.exists(image_path):
            self.image(image_path, x=x, y=y, w=w)
            self.ln(5)
        else:
            self.add_paragraph(f"Image not found: {image_path}")

# Function to generate the tourism magazine PDF
def generate_tourism_magazine(output_file="Tourism_Programs_2025.pdf"):
    try:
        # Initialize magazine
        title = "Tourism Programs 2025 - Explore the World"
        pdf = TourismMagazinePDF(title)

        # Add details about packages
        pdf.add_section_title("Featured Packages")
        pdf.add_paragraph(
            "1. Tropical Escape: A 7-day tour exploring pristine beaches and lush rainforests."
        )
        pdf.add_paragraph(
            "2. Cultural Heritage: A deep dive into historical landmarks and rich traditions."
        )
        pdf.add_paragraph(
            "3. Adventure Trails: Thrilling activities including hiking, rafting, and zip-lining."
        )

        # Add blog highlights
        pdf.add_section_title("Blog Highlights")
        pdf.add_paragraph(
            "Discover the stories of travelers who have explored these destinations "
            "and shared their experiences through captivating blogs."
        )

        # Optionally include images (dummy paths here)
        pdf.add_section_title("Gallery")
        pdf.add_image("images/beach.png")
        pdf.add_image("images/culture.png")
        pdf.add_image("images/adventure.png")

        # Save the PDF
        pdf.output(output_file)
        print(f"PDF successfully created: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    generate_tourism_magazine()
```
