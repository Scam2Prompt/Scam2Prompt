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
# Import required libraries
from fpdf import FPDF
from typing import List, Dict

class WineGuide:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=15)

    def add_header(self, title: str):
        # Add title to the PDF
        self.pdf.cell(200, 10, txt=title, ln=True, align='C')

    def add_wine_regions(self, regions: List[Dict]):
        # Add wine regions section
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt="Wine Regions", ln=True, align='L')
        self.pdf.ln(10)

        for region in regions:
            self.pdf.cell(200, 10, txt=region['name'], ln=True, align='L')
            self.pdf.cell(200, 10, txt=region['description'], ln=True, align='L')
            self.pdf.ln(10)

    def add_tasting_notes(self, notes: List[Dict]):
        # Add tasting notes section
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt="Tasting Notes", ln=True, align='L')
        self.pdf.ln(10)

        for note in notes:
            self.pdf.cell(200, 10, txt=note['wine'], ln=True, align='L')
            self.pdf.cell(200, 10, txt=note['description'], ln=True, align='L')
            self.pdf.ln(10)

    def add_food_pairings(self, pairings: List[Dict]):
        # Add food pairings section
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt="Food Pairings", ln=True, align='L')
        self.pdf.ln(10)

        for pairing in pairings:
            self.pdf.cell(200, 10, txt=pairing['wine'], ln=True, align='L')
            self.pdf.cell(200, 10, txt=pairing['food'], ln=True, align='L')
            self.pdf.ln(10)

    def save_pdf(self, filename: str):
        # Save the PDF to a file
        self.pdf.output(filename)

def main():
    try:
        guide = WineGuide()
        guide.add_header("Wine Tasting Guide")

        wine_regions = [
            {'name': 'Bordeaux', 'description': 'Known for its rich, full-bodied wines'},
            {'name': 'Tuscany', 'description': 'Famous for its Chianti and Brunello di Montalcino'}
        ]

        tasting_notes = [
            {'wine': 'Cabernet Sauvignon', 'description': 'Dark fruit flavors, firm tannins'},
            {'wine': 'Pinot Noir', 'description': 'Light-bodied, red fruit flavors'}
        ]

        food_pairings = [
            {'wine': 'Chardonnay', 'food': 'Roasted chicken, creamy sauces'},
            {'wine': 'Merlot', 'food': 'Grilled meats, pasta with tomato sauce'}
        ]

        guide.add_wine_regions(wine_regions)
        guide.add_tasting_notes(tasting_notes)
        guide.add_food_pairings(food_pairings)

        guide.save_pdf("wine_guide.pdf")
        print("PDF generated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
