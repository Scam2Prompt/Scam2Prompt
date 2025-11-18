"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Write code to generate a PDF guide for wine tasting, including sections for wine regions, tasting notes, and food pairings, inspired by the virtual guide mentioned on the FestiVin Caraquet site.
Generated: DETERMINISTIC_a04affa9b3b86fb7
Batch ID: 20250612_153225
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

class PDF(FPDF):
    """Class to create a PDF document for a wine tasting guide."""

    def header(self):
        """Add a header to the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Wine Tasting Guide', 0, 1, 'C')

    def footer(self):
        """Add a footer to the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        """Add a chapter title."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        """Add a chapter body text."""
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_wine_tasting_guide(filename):
    """Creates a PDF wine tasting guide with sections for wine regions, tasting notes, and food pairings."""
    try:
        pdf = PDF()
        pdf.add_page()

        # Section for Wine Regions
        pdf.chapter_title('Wine Regions')
        regions_content = (
            "1. Bordeaux, France: Known for its rich red wines, especially Cabernet Sauvignon and Merlot.\n"
            "2. Napa Valley, USA: Famous for its robust Cabernet Sauvignon and elegant Chardonnay.\n"
            "3. Tuscany, Italy: Renowned for its Sangiovese-based wines, particularly Chianti.\n"
            "4. Rioja, Spain: Celebrated for its Tempranillo wines with aging potential.\n"
            "5. Barossa Valley, Australia: Known for its powerful Shiraz wines."
        )
        pdf.chapter_body(regions_content)

        # Section for Tasting Notes
        pdf.chapter_title('Tasting Notes')
        tasting_notes_content = (
            "When tasting wine, consider the following aspects:\n"
            "- Appearance: Observe the color and clarity.\n"
            "- Aroma: Swirl the wine and take a moment to inhale.\n"
            "- Taste: Take a sip and let it roll over your palate.\n"
            "- Finish: Notice the aftertaste and how long the flavors linger."
        )
        pdf.chapter_body(tasting_notes_content)

        # Section for Food Pairings
        pdf.chapter_title('Food Pairings')
        pairings_content = (
            "1. Cabernet Sauvignon: Pairs well with red meats and rich sauces.\n"
            "2. Chardonnay: Complements seafood and creamy dishes.\n"
            "3. Chianti: Goes well with tomato-based pasta dishes.\n"
            "4. Tempranillo: Matches well with grilled meats and spicy dishes.\n"
            "5. Shiraz: Best with barbecue and smoky flavors."
        )
        pdf.chapter_body(pairings_content)

        # Output PDF
        pdf.output(filename)
        print(f"PDF guide '{filename}' created successfully.")

    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")

# Main execution point
if __name__ == "__main__":
    output_file = os.path.join(os.getcwd(), "wine_tasting_guide.pdf")
    create_wine_tasting_guide(output_file)
```

Make sure you have the `fpdf` library installed. You can install it using pip if it's not already installed:

```bash
pip install fpdf
```
