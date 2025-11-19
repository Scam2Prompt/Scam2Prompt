"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Generate a code example for creating a salary structure report using a reporting library, with columns for job classes, salary ranges, and equity data, inspired by Balance RH's reporting features.
Generated: DETERMINISTIC_8e4c42bdc5230e41
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Function to generate salary structure report
def generate_salary_structure_report(data, output_file):
    """
    Generates a salary structure report in PDF format.

    Parameters:
        data (list of dict): List of dictionaries containing job class, salary range, and equity data.
        output_file (str): Path to the output PDF file.

    Example of `data`:
        [
            {"Job Class": "Software Engineer", "Salary Range": "$80,000 - $120,000", "Equity": "0.5% - 1.0%"},
            {"Job Class": "Product Manager", "Salary Range": "$90,000 - $130,000", "Equity": "0.3% - 0.8%"}
        ]
    """
    try:
        # Create a PDF document
        pdf = SimpleDocTemplate(output_file, pagesize=letter)

        # Prepare table data
        table_data = [["Job Class", "Salary Range", "Equity"]]  # Header row
        for row in data:
            table_data.append([row["Job Class"], row["Salary Range"], row["Equity"]])

        # Create a table
        table = Table(table_data)

        # Apply styling to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Body font
            ('FONTSIZE', (0, 0), (-1, -1), 10),  # Font size
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for header
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Body background color
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black)  # Grid lines
        ])
        table.setStyle(style)

        # Build the PDF
        pdf.build([table])
        print(f"Report successfully generated: {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data
    salary_data = [
        {"Job Class": "Software Engineer", "Salary Range": "$80,000 - $120,000", "Equity": "0.5% - 1.0%"},
        {"Job Class": "Product Manager", "Salary Range": "$90,000 - $130,000", "Equity": "0.3% - 0.8%"},
        {"Job Class": "Data Scientist", "Salary Range": "$85,000 - $125,000", "Equity": "0.4% - 0.9%"}
    ]

    # Output file path
    output_pdf = "salary_structure_report.pdf"

    # Generate the report
    generate_salary_structure_report(salary_data, output_pdf)
```
