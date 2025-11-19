"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to automate the generation of consulting reports using libraries like ReportLab or Pandas.
Generated: DETERMINISTIC_cf050343b32efbf7
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_consulting_report(data, report_filename):
    """
    Generates a consulting report in PDF format using the provided data.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the consulting data.
    report_filename (str): The filename for the generated PDF report.
    """
    try:
        # Create a PDF document
        pdf = SimpleDocTemplate(report_filename, pagesize=letter)
        
        # Prepare the data for the table
        table_data = [data.columns.tolist()] + data.values.tolist()
        
        # Create a table with the data
        table = Table(table_data)
        
        # Apply styles to the table
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

        # Build the PDF
        pdf.build([table])
        print(f"Report generated successfully: {report_filename}")

    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

def main():
    # Sample data for the consulting report
    data = {
        'Client Name': ['Client A', 'Client B', 'Client C'],
        'Project': ['Project 1', 'Project 2', 'Project 3'],
        'Status': ['Completed', 'In Progress', 'Pending'],
        'Budget': [10000, 15000, 20000]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Generate the consulting report
    report_filename = "consulting_report.pdf"
    generate_consulting_report(df, report_filename)

if __name__ == "__main__":
    main()
```
