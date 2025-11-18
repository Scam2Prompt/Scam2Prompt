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
from fpdf import FPDF
import os

# Define a class for generating the PDF guide
class WineTastingGuidePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", size=12)
        
    def header(self):
        """Create a header for each page."""
        self.set_font("Arial", style="B", size=14)
        self.cell(0, 10, "Wine Tasting Guide", align="C", ln=True)
        self.ln(10)  # Line break
    
    def footer(self):
        """Create a footer for each page."""
        self.set_y(-15)  # Position at 15 mm from the bottom
        self.set_font("Arial", style="I", size=8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
    
    def add_section(self, title, content):
        """Add a section to the PDF with a title and content."""
        self.set_font("Arial", style="B", size=12)
        self.cell(0, 10, title, ln=True)  # Add section title
        self.ln(5)  # Line break
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, content)  # Add section content
        self.ln(10)  # Add spacing after section

# Prepare data for the PDF
wine_regions = """
Wine Regions:
- Bordeaux (France): Known for its red blends made from Cabernet Sauvignon, Merlot, and Cabernet Franc.
- Napa Valley (USA): Famous for its full-bodied Cabernet Sauvignon.
- Tuscany (Italy): Renowned for Chianti and Brunello di Montalcino.
"""

tasting_notes = """
Tasting Notes:
- Appearance: Observe the wine's color, clarity, and viscosity.
- Aroma: Swirl and smell the wine to identify fruit, floral, spice, or earthy notes.
- Taste: Focus on sweetness, acidity, tannins, and the finish.
"""

food_pairings = """
Food Pairings:
- Red Wine: Pair with steak, lamb, or aged cheeses.
- White Wine: Pair with seafood, chicken, or creamy pasta.
- Rosé: Pair with salads, light appetizers, or grilled vegetables.
"""

# Generate the PDF
try:
    pdf = WineTastingGuidePDF()
    pdf.add_section("Wine Regions", wine_regions)
    pdf.add_section("Tasting Notes", tasting_notes)
    pdf.add_section("Food Pairings", food_pairings)
    
    # Save the PDF to a file
    output_file = "Wine_Tasting_Guide.pdf"
    pdf.output(output_file)
    print(f"PDF generated successfully: {output_file}")

except Exception as e:
    print(f"An error occurred while creating the PDF: {e}")
```
