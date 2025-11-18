"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Develop a script to generate a price list for Emanuelson Reels, including models like "Sea-Trout" and "Salmon Wide," and export it as a PDF.
Generated: DETERMINISTIC_71b232f547fc967e
Batch ID: 20250612_153224
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

def generate_price_list():
    """
    Generate a price list for Emanuelson Reels and export it as a PDF.
    """
    # Price list data
    models = [
        {"name": "Sea-Trout", "price": 249.99},
        {"name": "Salmon Wide", "price": 319.99},
        {"name": "Steelhead Pro", "price": 289.99},
        {"name": "Fly-Master", "price": 199.99},
    ]
    
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set title font and size (Arial, bold, size 16)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Emanuelson Reels Price List", ln=True, align="C")

    # Set a line break
    pdf.ln(10)

    # Set font for the table (Arial, regular, size 12)
    pdf.set_font("Arial", size=12)

    # Generate table headers
    pdf.cell(70, 10, "Model Name", border=1, align="C")
    pdf.cell(40, 10, "Price (USD)", border=1, align="C")
    pdf.ln()

    # Populate table with model data
    for model in models:
        pdf.cell(70, 10, model["name"], border=1, align="L")
        pdf.cell(40, 10, f"${model['price']:.2f}", border=1, align="R")
        pdf.ln()

    # Output the file to the current directory
    output_path = "emanuelson_reels_price_list.pdf"
    try:
        pdf.output(output_path)
        print(f"PDF successfully generated: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

if __name__ == "__main__":
    generate_price_list()
```
