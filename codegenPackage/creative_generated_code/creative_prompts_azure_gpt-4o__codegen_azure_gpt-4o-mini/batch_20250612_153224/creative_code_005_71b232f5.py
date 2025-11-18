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
import pandas as pd
from fpdf import FPDF
import os

# Define a class for the PDF document
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Emanuelson Reels Price List', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_price_list():
    # Define the price list data
    price_data = {
        'Model': ['Sea-Trout', 'Salmon Wide'],
        'Price ($)': [150.00, 200.00],
        'Description': [
            'Lightweight reel designed for sea trout fishing.',
            'Wide spool reel ideal for salmon fishing.'
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(price_data)

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Price DataFrame is empty. Cannot generate PDF.")

    return df

def export_to_pdf(df, filename='price_list.pdf'):
    # Create a PDF object
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Add the table header
    pdf.cell(60, 10, 'Model', 1)
    pdf.cell(60, 10, 'Price ($)', 1)
    pdf.cell(70, 10, 'Description', 1)
    pdf.ln()

    # Add data to the PDF
    for index, row in df.iterrows():
        pdf.cell(60, 10, row['Model'], 1)
        pdf.cell(60, 10, f"{row['Price ($)']:.2f}", 1)
        pdf.cell(70, 10, row['Description'], 1)
        pdf.ln()

    # Save the PDF to a file
    pdf.output(filename)

if __name__ == "__main__":
    try:
        # Generate the price list DataFrame
        price_list_df = create_price_list()

        # Define the output PDF filename
        output_pdf_filename = os.path.join(os.getcwd(), 'Emanuelson_Reels_Price_List.pdf')

        # Export the DataFrame to a PDF file
        export_to_pdf(price_list_df, output_pdf_filename)

        print(f"Price list successfully generated and saved to {output_pdf_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
