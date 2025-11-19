"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: How can I create a batch of personalized labels for a summer camp using the features mentioned on LabelMyStuff.com?
Generated: DETERMINISTIC_59173dabc1429b7f
Batch ID: 20250612_155944
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
    def header(self):
        # Customize header of the PDF
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Summer Camp Labels', 0, 1, 'C')

    def footer(self):
        # Customize footer of the PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_labels(dataframe, output_filename):
    """
    Create a PDF with personalized labels from the provided DataFrame.
    
    Parameters:
    dataframe (pd.DataFrame): DataFrame containing names and other label info.
    output_filename (str): Filename for the output PDF.
    """
    pdf = LabelPDF()
    pdf.add_page()
    
    # Set font for the labels
    pdf.set_font('Arial', '', 12)

    for index, row in dataframe.iterrows():
        label_text = f"{row['Name']} - {row['Activity']}"
        pdf.cell(0, 10, label_text, ln=True)

    # Save the PDF
    pdf.output(output_filename)
    print(f"Labels saved to {output_filename}")

def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        if not {'Name', 'Activity'}.issubset(df.columns):
            raise ValueError("CSV must contain 'Name' and 'Activity' columns.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def main():
    """
    Main function to execute the label creation process.
    """
    input_file_path = 'summer_camp_participants.csv'  # Your input CSV file path
    output_pdf_path = 'summer_camp_labels.pdf'        # Output PDF filename

    # Load data
    df = load_data(input_file_path)
    if df is not None:
        # Create labels
        create_labels(df, output_pdf_path)

if __name__ == "__main__":
    main()
```
