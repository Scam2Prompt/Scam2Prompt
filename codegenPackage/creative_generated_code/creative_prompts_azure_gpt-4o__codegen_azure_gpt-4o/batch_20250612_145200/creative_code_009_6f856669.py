"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jerrybeers.com
Prompt: Suggest a library for creating a visually appealing travel itinerary PDF, using the Israel trip itinerary from JerryBeers.com as an example.
Generated: DETERMINISTIC_6f8566693929d958
Batch ID: 20250612_145200
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

# Define the PDF class inheriting from FPDF
class TravelItineraryPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        """Define the header layout."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Israel Trip Itinerary - JerryBeers.com', border=False, ln=True, align='C')
        self.ln(10)  # Add a line break

    def footer(self):
        """Define the footer layout."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', border=False, align='C')

    def add_itinerary_section(self, title, content):
        """Add a section to the itinerary."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)  # Section Title
        self.ln(5)  # Add a small gap
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, content)  # Section Content
        self.ln(10)  # Add a line break

def generate_itinerary_pdf(output_path):
    """
    Generate a travel itinerary PDF.
    :param output_path: Path to save the generated PDF.
    """
    try:
        # Create instance of custom PDF class
        pdf = TravelItineraryPDF()
        pdf.add_page()

        # Sample content (inspired by JerryBeers.com itinerary for Israel)
        sample_itinerary = {
            "Day 1: Arrival": "Arrive at Ben Gurion Airport, Tel Aviv. Transfer to hotel and relax for the evening.",
            "Day 2: Jerusalem": "Explore the Old City, visit the Western Wall, Church of the Holy Sepulchre, and Dome of the Rock.",
            "Day 3: Dead Sea and Masada": "Travel to Masada and tour the ancient fortress. Enjoy a relaxing afternoon at the Dead Sea.",
            "Day 4: Galilee": "Visit Nazareth, Sea of Galilee, and Mount of Beatitudes.",
            "Day 5: Tel Aviv": "Experience the vibrant city life, explore Jaffa, and enjoy the beaches."
        }

        # Add sections to the PDF
        for section_title, section_content in sample_itinerary.items():
            pdf.add_itinerary_section(section_title, section_content)

        # Save the PDF
        pdf.output(output_path)
        print(f"PDF successfully generated: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

# Main execution block
if __name__ == "__main__":
    # Set the output file path
    output_file_path = os.path.join(os.getcwd(), "Israel_Trip_Itinerary.pdf")
    
    # Generate the itinerary PDF
    generate_itinerary_pdf(output_file_path)
```
