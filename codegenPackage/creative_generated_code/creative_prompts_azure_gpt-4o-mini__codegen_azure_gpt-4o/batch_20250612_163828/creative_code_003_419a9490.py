"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Create a script that automates the reporting process in CRM.f, exporting data to Excel or PDF.
Generated: DETERMINISTIC_419a9490e14e11e8
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Constants
EXPORT_DIR = "exports"
EXPORT_FORMATS = ["excel", "pdf"]  # Supported formats for export

# Sample CRM data - Replace with your actual CRM database connection and query logic
crm_data = [
    {"Customer ID": 1, "Name": "John Doe", "Email": "john@example.com", "Purchase Amount": 100.00},
    {"Customer ID": 2, "Name": "Jane Smith", "Email": "jane@example.com", "Purchase Amount": 150.50}
]

def fetch_crm_data():
    """
    Fetch data from CRM system.
    Replace this placeholder with actual database queries.
    """
    return crm_data

def export_to_excel(data, filename):
    """
    Export data to an Excel file.
    :param data: List of dictionaries containing CRM data
    :param filename: Target file name
    """
    try:
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Write DataFrame to Excel file
        file_path = os.path.join(EXPORT_DIR, filename)
        df.to_excel(file_path, index=False)
        print(f"Excel file generated successfully: {file_path}")
    except Exception as e:
        print(f"Error exporting to Excel: {e}")

def export_to_pdf(data, filename):
    """
    Export data to a PDF file.
    :param data: List of dictionaries containing CRM data
    :param filename: Target file name
    """
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Add title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="CRM Report", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.ln(10)  # Line break
        
        # Add each row from the data
        for row in data:
            row_text = ", ".join([f"{key}: {value}" for key, value in row.items()])
            pdf.cell(200, 10, txt=row_text, ln=True)
        
        # Save PDF file
        file_path = os.path.join(EXPORT_DIR, filename)
        pdf.output(file_path)
        print(f"PDF file generated successfully: {file_path}")
    except Exception as e:
        print(f"Error exporting to PDF: {e}")

def generate_report(export_format):
    """
    Generate a report from CRM data and export it to the specified format.
    :param export_format: The format to export the data ("excel" or "pdf")
    """
    if export_format not in EXPORT_FORMATS:
        print(f"Invalid export format: {export_format}. Supported formats: {EXPORT_FORMATS}")
        return

    try:
        # Fetch CRM data
        data = fetch_crm_data()
        
        # Ensure export directory exists
        os.makedirs(EXPORT_DIR, exist_ok=True)
        
        # Generate a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"CRM_Report_{timestamp}.{export_format}"
        
        # Export based on format
        if export_format == "excel":
            export_to_excel(data, filename)
        elif export_format == "pdf":
            export_to_pdf(data, filename)
    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    # Example usage: Generate report in both formats
    generate_report("excel")
    generate_report("pdf")
```
