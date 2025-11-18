"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Write Python code to automate the generation of annual reports for a community development organization like AIDA, including sections for project summaries, financial data, and impact metrics.
Generated: DETERMINISTIC_3bc4711e682e0c94
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
import json
from datetime import datetime
from fpdf import FPDF

# Constants
REPORT_OUTPUT_DIR = "reports"
PROJECT_SUMMARIES_FILE = "data/project_summaries.json"
FINANCIAL_DATA_FILE = "data/financial_data.json"
IMPACT_METRICS_FILE = "data/impact_metrics.json"

class AnnualReport:
    def __init__(self, year):
        self.year = year
        self.project_summaries = []
        self.financial_data = {}
        self.impact_metrics = {}

    def load_data(self):
        """
        Load data from JSON files. Includes project summaries, financial data, and impact metrics.
        """
        try:
            # Load project summaries
            with open(PROJECT_SUMMARIES_FILE, 'r') as file:
                self.project_summaries = json.load(file).get(str(self.year), [])
            
            # Load financial data
            with open(FINANCIAL_DATA_FILE, 'r') as file:
                self.financial_data = json.load(file).get(str(self.year), {})
            
            # Load impact metrics
            with open(IMPACT_METRICS_FILE, 'r') as file:
                self.impact_metrics = json.load(file).get(str(self.year), {})
        
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Required data file not found: {e.filename}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")

    def generate_pdf(self):
        """
        Generate a PDF report for the annual report content.
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Title
        pdf.set_font("Arial", size=16, style='B')
        pdf.cell(0, 10, f"Annual Report - {self.year}", ln=True, align='C')
        pdf.ln(10)

        # Section: Project Summaries
        pdf.set_font("Arial", size=14, style='B')
        pdf.cell(0, 10, "Project Summaries", ln=True)
        pdf.set_font("Arial", size=12)
        if self.project_summaries:
            for project in self.project_summaries:
                pdf.multi_cell(0, 10, f"- {project}")
                pdf.ln(5)
        else:
            pdf.cell(0, 10, "No project summaries available.", ln=True)
        pdf.ln(10)

        # Section: Financial Data
        pdf.set_font("Arial", size=14, style='B')
        pdf.cell(0, 10, "Financial Data", ln=True)
        pdf.set_font("Arial", size=12)
        if self.financial_data:
            for key, value in self.financial_data.items():
                pdf.cell(0, 10, f"{key}: ${value:,}", ln=True)
        else:
            pdf.cell(0, 10, "No financial data available.", ln=True)
        pdf.ln(10)

        # Section: Impact Metrics
        pdf.set_font("Arial", size=14, style='B')
        pdf.cell(0, 10, "Impact Metrics", ln=True)
        pdf.set_font("Arial", size=12)
        if self.impact_metrics:
            for metric, value in self.impact_metrics.items():
                pdf.cell(0, 10, f"{metric}: {value}", ln=True)
        else:
            pdf.cell(0, 10, "No impact metrics available.", ln=True)

        # Ensure the output directory exists
        os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)

        # Save the PDF
        output_path = os.path.join(REPORT_OUTPUT_DIR, f"Annual_Report_{self.year}.pdf")
        pdf.output(output_path)
        return output_path

def main():
    """
    Main function to generate the annual report.
    """
    try:
        # Prompt user for the year
        year = int(input("Enter the year for the annual report: "))
        report = AnnualReport(year)
        
        # Load data
        print("Loading data...")
        report.load_data()

        # Generate PDF
        print("Generating report...")
        output_path = report.generate_pdf()

        print(f"Annual report successfully generated: {output_path}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
