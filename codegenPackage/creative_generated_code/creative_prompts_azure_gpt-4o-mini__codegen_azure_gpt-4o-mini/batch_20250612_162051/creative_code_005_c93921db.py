"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Suggest a library or framework for developing report generation features in a custom software solution, in line with MetaCode's focus on reportability and analysis.
Generated: DETERMINISTIC_c93921db99d37f79
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import os

class ReportGenerator:
    """
    A class to generate PDF reports using ReportLab library.
    """

    def __init__(self, file_name: str):
        """
        Initialize the ReportGenerator with a specified file name.
        
        :param file_name: The name of the report file to be created (with .pdf extension).
        """
        self.file_name = file_name
        self.data = []

    def load_data(self, data_source: str):
        """
        Load data from a CSV file into the report generator.
        
        :param data_source: The path to the CSV file containing report data.
        :raises FileNotFoundError: If the specified file does not exist.
        :raises ValueError: If the file cannot be parsed as a DataFrame.
        """
        if not os.path.exists(data_source):
            raise FileNotFoundError(f"The data source file {data_source} does not exist.")
        
        try:
            self.data = pd.read_csv(data_source)
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def generate_report(self):
        """
        Generate a PDF report from the loaded data.
        :raises ValueError: If no data has been loaded.
        """
        if not self.data:
            raise ValueError("No data loaded. Please load data before generating a report.")
        
        # Create a PDF document
        doc = SimpleDocTemplate(self.file_name, pagesize=letter)
        elements = []

        # Create a table from the DataFrame
        data_table = [self.data.columns.tolist()] + self.data.values.tolist()
        table = Table(data_table)

        # Set table style
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        table.setStyle(style)

        elements.append(table)

        # Build the PDF
        try:
            doc.build(elements)
            print(f"Report generated: {self.file_name}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while generating the report: {e}")


# Example usage:
if __name__ == "__main__":
    generator = ReportGenerator("report.pdf")
    
    try:
        generator.load_data("data.csv")  # Load data from a CSV file
        generator.generate_report()        # Generate the report
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
