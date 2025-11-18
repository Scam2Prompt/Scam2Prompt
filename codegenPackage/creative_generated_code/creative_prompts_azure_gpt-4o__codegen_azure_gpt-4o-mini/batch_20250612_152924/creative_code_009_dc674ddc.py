"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Write a Python script to generate a PDF itinerary for a selected tour package from "Safar Genie," including details like duration, destinations, and themes.
Generated: DETERMINISTIC_dc674ddcf060c15a
Batch ID: 20250612_152924
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

class ItineraryPDF(FPDF):
    """Class to create a PDF itinerary for a selected tour package."""
    
    def header(self):
        """Define header for the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Safar Genie Tour Itinerary', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        """Define footer for the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_tour_details(self, title, duration, destinations, themes):
        """Add tour details to the PDF."""
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, f'Duration: {duration}', 0, 1, 'L')
        self.cell(0, 10, f'Destinations: {destinations}', 0, 1, 'L')
        self.cell(0, 10, f'Themes: {themes}', 0, 1, 'L')
        self.ln(10)

def generate_itinerary_pdf(file_path, tour_package):
    """Generate PDF itinerary based on the tour package details."""
    try:
        # Create a PDF document
        pdf = ItineraryPDF()
        pdf.add_page()

        # Add tour package details
        pdf.add_tour_details(
            title=tour_package['title'],
            duration=tour_package['duration'],
            destinations=', '.join(tour_package['destinations']),
            themes=', '.join(tour_package['themes'])
        )

        # Check if file path directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Output PDF to the specified file path
        pdf.output(file_path)
        print(f"Itinerary PDF generated successfully at: {file_path}")

    except Exception as e:
        print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    # Sample tour package data
    tour_package = {
        'title': 'Exploring the Wonders of India',
        'duration': '10 Days',
        'destinations': ['Delhi', 'Agra', 'Jaipur', 'Varanasi'],
        'themes': ['Cultural', 'Historical', 'Spiritual']
    }

    # Generate PDF itinerary
    generate_itinerary_pdf('itineraries/india_wonders_itinerary.pdf', tour_package)
```
