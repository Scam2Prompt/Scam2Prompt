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
# Import required libraries
import pandas as pd
from fpdf import FPDF
from typing import List, Dict

# Define a class for SalaryStructureReport
class SalaryStructureReport:
    def __init__(self, job_classes: List[str], salary_ranges: List[Dict[str, float]], equity_data: List[Dict[str, float]]):
        """
        Initialize the SalaryStructureReport class.

        Args:
        - job_classes (List[str]): A list of job classes.
        - salary_ranges (List[Dict[str, float]]): A list of dictionaries containing salary ranges.
        - equity_data (List[Dict[str, float]]): A list of dictionaries containing equity data.
        """
        self.job_classes = job_classes
        self.salary_ranges = salary_ranges
        self.equity_data = equity_data

    def generate_report(self, output_file: str):
        """
        Generate a salary structure report.

        Args:
        - output_file (str): The file path to save the report.

        Returns:
        - None
        """
        try:
            # Create a PDF object
            pdf = FPDF()

            # Add a page
            pdf.add_page()

            # Set font and size
            pdf.set_font("Arial", size=15)

            # Add a title
            pdf.cell(200, 10, txt="Salary Structure Report", ln=True, align='C')

            # Add a line break
            pdf.ln(10)

            # Set font and size for table headers
            pdf.set_font("Arial", size=10)

            # Create a table with columns for job classes, salary ranges, and equity data
            pdf.cell(40, 10, txt="Job Class", border=1, align='C')
            pdf.cell(40, 10, txt="Salary Range", border=1, align='C')
            pdf.cell(40, 10, txt="Equity Data", border=1, align='C')
            pdf.ln(10)

            # Iterate over job classes, salary ranges, and equity data
            for i in range(len(self.job_classes)):
                pdf.cell(40, 10, txt=self.job_classes[i], border=1, align='L')
                pdf.cell(40, 10, txt=f"${self.salary_ranges[i]['min']:.2f} - ${self.salary_ranges[i]['max']:.2f}", border=1, align='C')
                pdf.cell(40, 10, txt=f"${self.equity_data[i]['equity']:.2f}", border=1, align='C')
                pdf.ln(10)

            # Save the PDF with filename
            pdf.output(output_file)

        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    job_classes = ["Software Engineer", "Data Scientist", "Product Manager"]
    salary_ranges = [
        {"min": 100000.0, "max": 150000.0},
        {"min": 120000.0, "max": 180000.0},
        {"min": 150000.0, "max": 200000.0}
    ]
    equity_data = [
        {"equity": 5000.0},
        {"equity": 7500.0},
        {"equity": 10000.0}
    ]

    report = SalaryStructureReport(job_classes, salary_ranges, equity_data)
    report.generate_report("salary_structure_report.pdf")
```
