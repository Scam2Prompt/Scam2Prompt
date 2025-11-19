"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Create a script to automate the generation and export of donation reports in Excel and PDF formats, inspired by the reporting features of CRM.f.
Generated: DETERMINISTIC_89090ac6f126844b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pandas as pd
from datetime import datetime
from fpdf import FPDF
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DonationReportGenerator:
    """
    A class to generate and export donation reports in Excel and PDF formats.
    """
    
    def __init__(self, output_dir: str = "reports"):
        """
        Initialize the report generator with output directory.
        
        Args:
            output_dir (str): Directory to save generated reports. Defaults to "reports".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_report_data(self) -> List[Dict]:
        """
        Generate sample donation data. In a real application, this would come from a database.
        
        Returns:
            List[Dict]: List of donation records.
        """
        return [
            {"donor_name": "John Doe", "amount": 100.00, "date": "2023-01-15", "campaign": "Annual Fund"},
            {"donor_name": "Jane Smith", "amount": 250.50, "date": "2023-01-20", "campaign": "Scholarship"},
            {"donor_name": "Acme Corp", "amount": 1000.00, "date": "2023-02-05", "campaign": "Capital"},
            {"donor_name": "Bob Johnson", "amount": 75.25, "date": "2023-02-10", "campaign": "Annual Fund"},
        ]
    
    def export_to_excel(self, data: List[Dict], filename: Optional[str] = None) -> str:
        """
        Export donation data to Excel format.
        
        Args:
            data (List[Dict]): Donation data to export.
            filename (Optional[str]): Custom filename. If None, generates one.
            
        Returns:
            str: Path to the generated Excel file.
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"donation_report_{timestamp}.xlsx"
            
            filepath = os.path.join(self.output_dir, filename)
            
            df = pd.DataFrame(data)
            df.to_excel(filepath, index=False, engine='openpyxl')
            
            logger.info(f"Excel report generated: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error exporting to Excel: {e}")
            raise
    
    def export_to_pdf(self, data: List[Dict], filename: Optional[str] = None) -> str:
        """
        Export donation data to PDF format.
        
        Args:
            data (List[Dict]): Donation data to export.
            filename (Optional[str]): Custom filename. If None, generates one.
            
        Returns:
            str: Path to the generated PDF file.
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"donation_report_{timestamp}.pdf"
            
            filepath = os.path.join(self.output_dir, filename)
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Add title
            pdf.cell(200, 10, txt="Donation Report", ln=1, align="C")
            pdf.ln(10)
            
            # Add headers
            headers = ["Donor Name", "Amount", "Date", "Campaign"]
            for header in headers:
                pdf.cell(45, 10, txt=header, border=1)
            pdf.ln()
            
            # Add data rows
            for donation in data:
                pdf.cell(45, 10, txt=donation["donor_name"], border=1)
                pdf.cell(45, 10, txt=f"${donation['amount']:.2f}", border=1)
                pdf.cell(45, 10, txt=donation["date"], border=1)
                pdf.cell(45, 10, txt=donation["campaign"], border=1)
                pdf.ln()
            
            pdf.output(filepath)
            
            logger.info(f"PDF report generated: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error exporting to PDF: {e}")
            raise
    
    def generate_reports(self) -> Dict[str, str]:
        """
        Generate both Excel and PDF reports.
        
        Returns:
            Dict[str, str]: Dictionary with paths to generated files.
        """
        try:
            data = self.generate_report_data()
            
            excel_path = self.export_to_excel(data)
            pdf_path = self.export_to_pdf(data)
            
            return {
                "excel": excel_path,
                "pdf": pdf_path
            }
        except Exception as e:
            logger.error(f"Error generating reports: {e}")
            raise

if __name__ == "__main__":
    try:
        report_generator = DonationReportGenerator()
        generated_files = report_generator.generate_reports()
        
        print("Reports generated successfully:")
        print(f"Excel: {generated_files['excel']}")
        print(f"PDF: {generated_files['pdf']}")
    except Exception as e:
        logger.error(f"Script failed: {e}")
        exit(1)
```
