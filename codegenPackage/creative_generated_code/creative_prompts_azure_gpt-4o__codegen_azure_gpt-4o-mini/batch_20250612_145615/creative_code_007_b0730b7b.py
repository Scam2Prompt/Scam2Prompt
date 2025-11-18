"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Create a script to batch print labels for children’s school trips, incorporating features for adhesive labels and personalization, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_b0730b7b7dcaeec9
Batch ID: 20250612_145615
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

class LabelPDF(FPDF):
    """Class to create a PDF for labels."""
    
    def header(self):
        """Add a header to the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'School Trip Labels', align='C', ln=True)
        self.ln(10)

    def footer(self):
        """Add a footer to the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_label(self, name, trip_details):
        """Add a label entry to the PDF document.

        Args:
            name (str): The name of the child.
            trip_details (str): Details of the trip.
        """
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, name, ln=True)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, trip_details, ln=True)
        self.ln(10)  # Space between labels

def create_labels_from_csv(csv_file, output_pdf):
    """Create a PDF of labels from a CSV file.

    Args:
        csv_file (str): Path to the CSV file containing names and trip details.
        output_pdf (str): Path to save the generated PDF.
    """
    try:
        # Read data from the CSV file
        data = pd.read_csv(csv_file)

        if 'Name' not in data.columns or 'Trip Details' not in data.columns:
            raise ValueError("CSV must contain 'Name' and 'Trip Details' columns.")

        pdf = LabelPDF()
        pdf.add_page()

        for index, row in data.iterrows():
            name = row['Name']
            trip_details = row['Trip Details']
            pdf.add_label(name, trip_details)

        pdf.output(output_pdf)
        print(f"Labels successfully created and saved to {output_pdf}")

    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to execute the label printing process."""
    # Path to the input CSV file
    csv_file = 'school_trip_labels.csv'
    
    # Path where the output PDF will be saved
    output_pdf = 'school_trip_labels.pdf'

    # Create labels from the CSV file
    create_labels_from_csv(csv_file, output_pdf)

if __name__ == '__main__':
    main()
```

### Note:
Make sure to install the required libraries by running:
```bash
pip install pandas fpdf
``` 

Place a CSV file named `school_trip_labels.csv` in the same directory with columns `Name` and `Trip Details` for the script to function correctly.
