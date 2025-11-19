"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Write code to generate a PDF guide for wine tasting, including sections for wine regions, tasting notes, and food pairings, inspired by the virtual guide mentioned on the FestiVin Caraquet site.
Generated: DETERMINISTIC_a04affa9b3b86fb7
Batch ID: 20250612_153225
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

class PDF(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'Wine Tasting Guide', 0, 1, 'C')

    def footer(self):
        # Set position for the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        # Set font for chapter title
        self.set_font('Arial', 'B', 12)
        # Add chapter title
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        # Set font for chapter body
        self.set_font('Arial', '', 12)
        # Add chapter body
        self.multi_cell(0, 10, body)
        self.ln()

def create_wine_tasting_guide(filename):
    # Create a PDF object
    pdf = PDF()
    pdf.add_page()

    # Wine regions section
    pdf.chapter_title('Wine Regions')
    wine_regions = (
        "1. Bordeaux, France: Known for its rich red wines, particularly Merlot and Cabernet Sauvignon.\n"
        "2. Napa Valley, USA: Famous for its bold Cabernet Sauvignon and Chardonnay.\n"
        "3. Tuscany, Italy: Renowned for Chianti and Sangiovese wines.\n"
        "4. Rioja, Spain: Known for its Tempranillo wines, often aged in oak.\n"
        "5. Barossa Valley, Australia: Famous for Shiraz and Grenache."
    )
    pdf.chapter_body(wine_regions)

    # Tasting notes section
    pdf.chapter_title('Tasting Notes')
    tasting_notes = (
        "1. Bordeaux: Deep ruby color, aromas of blackcurrant, cedar, and tobacco.\n"
        "2. Napa Valley: Full-bodied with notes of dark fruit, vanilla, and spice.\n"
        "3. Tuscany: Bright acidity with flavors of cherry, plum, and earthy undertones.\n"
        "4. Rioja: Medium-bodied with red fruit, leather, and a hint of vanilla.\n"
        "5. Barossa Valley: Rich and bold with flavors of blackberry, chocolate, and pepper."
    )
    pdf.chapter_body(tasting_notes)

    # Food pairings section
    pdf.chapter_title('Food Pairings')
    food_pairings = (
        "1. Bordeaux: Pairs well with grilled meats, lamb, and hard cheeses.\n"
        "2. Napa Valley: Excellent with steak, roasted chicken, and creamy pasta.\n"
        "3. Tuscany: Great with pasta dishes, grilled vegetables, and pizza.\n"
        "4. Rioja: Complements tapas, grilled fish, and cured meats.\n"
        "5. Barossa Valley: Ideal with barbecue, rich stews, and dark chocolate."
    )
    pdf.chapter_body(food_pairings)

    # Save the PDF to a file
    try:
        pdf.output(filename)
        print(f"PDF guide '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")

if __name__ == "__main__":
    # Define the output filename
    output_filename = "wine_tasting_guide.pdf"
    # Create the wine tasting guide
    create_wine_tasting_guide(output_filename)
```
