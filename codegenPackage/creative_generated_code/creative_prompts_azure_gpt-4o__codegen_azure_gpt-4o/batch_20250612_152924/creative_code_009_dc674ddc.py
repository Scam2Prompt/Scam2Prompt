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

def generate_itinerary_pdf(package_name, duration, destinations, themes, output_file):
    """
    Generates a PDF itinerary for a selected tour package.

    Args:
        package_name (str): Name of the tour package.
        duration (str): Duration of the tour (e.g., "5 Days, 4 Nights").
        destinations (list): List of destination names.
        themes (list): List of themes (e.g., "Adventure", "Relaxation").
        output_file (str): Output file path for the PDF.
    """
    try:
        # Initialize the PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        # Title
        pdf.cell(0, 10, "Safar Genie - Tour Itinerary", ln=True, align="C")
        pdf.ln(10)  # Line break

        # Package Name
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Package: {package_name}", ln=True)
        pdf.ln(5)  # Line break

        # Duration
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Duration: {duration}", ln=True)
        pdf.ln(5)  # Line break

        # Destinations
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Destinations:", ln=True)
        pdf.set_font("Arial", "", 12)
        for destination in destinations:
            pdf.cell(0, 10, f"- {destination}", ln=True)
        pdf.ln(5)  # Line break

        # Themes
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Themes:", ln=True)
        pdf.set_font("Arial", "", 12)
        for theme in themes:
            pdf.cell(0, 10, f"- {theme}", ln=True)
        pdf.ln(10)  # Line break

        # Footer
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, "Thank you for choosing Safar Genie!", ln=True, align="C")

        # Save the PDF
        pdf.output(output_file)
        print(f"PDF itinerary successfully generated: {output_file}")
    
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

if __name__ == "__main__":
    # Example data for generating a PDF itinerary
    package_name = "Exotic Adventure"
    duration = "7 Days, 6 Nights"
    destinations = ["Paris", "Rome", "Barcelona"]
    themes = ["Adventure", "Culture", "Food"]
    output_file = os.path.join(os.getcwd(), "tour_itinerary.pdf")

    # Generate the PDF
    generate_itinerary_pdf(package_name, duration, destinations, themes, output_file)
```
