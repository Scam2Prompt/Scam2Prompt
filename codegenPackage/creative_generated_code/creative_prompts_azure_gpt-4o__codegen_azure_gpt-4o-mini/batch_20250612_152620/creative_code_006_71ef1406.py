"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Develop a script to generate detailed management reports for electronic invoices using Mercurio's reporting tools.
Generated: DETERMINISTIC_71ef14061e9349a8
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import mercurio_api  # Assuming a hypothetical Mercurio API package
from datetime import datetime
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvoiceReportGenerator:
    def __init__(self, api_client):
        """
        Initializes the InvoiceReportGenerator with a Mercurio API client.
        
        :param api_client: An instance of the Mercurio API client for making requests.
        """
        self.api_client = api_client

    def fetch_invoices(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetches electronic invoices from the Mercurio API within a specified date range.
        
        :param start_date: The start date for fetching invoices (YYYY-MM-DD).
        :param end_date: The end date for fetching invoices (YYYY-MM-DD).
        :return: DataFrame containing invoices data.
        """
        try:
            # Retrieve invoices from the API
            invoices = self.api_client.get_invoices(start_date, end_date)
            logging.info("Invoices fetched successfully.")
            return pd.DataFrame(invoices)
        except Exception as e:
            logging.error(f"Error fetching invoices: {e}")
            raise

    def generate_report(self, invoices: pd.DataFrame) -> pd.DataFrame:
        """
        Generates a detailed management report from the invoices DataFrame.
        
        :param invoices: DataFrame containing invoice data.
        :return: DataFrame containing the generated report.
        """
        try:
            # Process invoices to create a summary report
            report = invoices.groupby(['client_id', 'invoice_status']).agg(
                total_invoices=('invoice_id', 'count'),
                total_amount=('invoice_amount', 'sum')
            ).reset_index()
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

    def save_report(self, report: pd.DataFrame, output_file: str) -> None:
        """
        Saves the report to a specified file in CSV format.
        
        :param report: DataFrame containing the report data.
        :param output_file: The file path to save the report (including .csv extension).
        """
        try:
            report.to_csv(output_file, index=False)
            logging.info(f"Report saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"Error saving report: {e}")
            raise

def main(start_date: str, end_date: str, output_file: str):
    """
    Main function to execute the report generation process.
    
    :param start_date: The start date for fetching invoices (YYYY-MM-DD).
    :param end_date: The end date for fetching invoices (YYYY-MM-DD).
    :param output_file: The file path to save the report.
    """
    # Create an API client instance (assumed to be defined in mercurio_api)
    api_client = mercurio_api.Client()  # Hypothetical Client class in the mercurio_api module

    report_generator = InvoiceReportGenerator(api_client)

    try:
        # Fetch invoices
        invoices = report_generator.fetch_invoices(start_date, end_date)

        # Generate report
        report = report_generator.generate_report(invoices)

        # Save report to a CSV file
        report_generator.save_report(report, output_file)

    except Exception as e:
        logging.error(f"Process failed: {e}")

if __name__ == "__main__":
    # Example execution (modify as necessary)
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    output_file = f"Invoice_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    main(start_date, end_date, output_file)
```
