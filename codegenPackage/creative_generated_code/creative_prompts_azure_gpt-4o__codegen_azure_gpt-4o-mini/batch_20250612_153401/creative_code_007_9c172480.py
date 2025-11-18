"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for exporting financial statements and management reports from a CMS system like Nexelit.
Generated: DETERMINISTIC_9c1724809f8e688f
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nexelit.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialReportExporter:
    """Class to handle exporting financial statements and management reports from a CMS system."""

    def __init__(self, api_url, api_key):
        """
        Initializes the exporter with the API URL and the API key.
        
        Args:
            api_url (str): The base URL of the CMS API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def fetch_reports(self, report_type, start_date, end_date):
        """
        Fetches reports from the CMS API based on report type and date range.
        
        Args:
            report_type (str): The type of report to fetch (e.g., "financial", "management").
            start_date (str): The start date for filtering reports (YYYY-MM-DD).
            end_date (str): The end date for filtering reports (YYYY-MM-DD).
        
        Returns:
            pd.DataFrame: A DataFrame containing the reports data.
        
        Raises:
            ValueError: If the report type is invalid.
            Exception: If the API request fails.
        """
        if report_type not in ['financial', 'management']:
            raise ValueError("Invalid report type. Must be 'financial' or 'management'.")

        # Construct the API endpoint
        endpoint = f"{self.api_url}/reports/{report_type}"
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'api_key': self.api_key
        }

        # Make the API request
        try:
            logging.info(f"Fetching {report_type} reports from {start_date} to {end_date}.")
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Convert the response into a DataFrame
            return pd.DataFrame(data)
        except requests.exceptions.RequestException as e:
            logging.error("API request failed: %s", e)
            raise
        except ValueError as e:
            logging.error("Error processing response data: %s", e)
            raise

    def export_to_csv(self, df, report_type):
        """
        Exports the DataFrame to a CSV file.
        
        Args:
            df (pd.DataFrame): The DataFrame containing reports data.
            report_type (str): The type of report (used for naming the file).
        """
        filename = f"{report_type}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            df.to_csv(filename, index=False)
            logging.info(f"Exported {report_type} report to {filename}.")
        except Exception as e:
            logging.error("Failed to export report to CSV: %s", e)
            raise

def main():
    # Configuration for the CMS API
    API_URL = "https://api.nexelit.com"
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Instantiate the exporter
    exporter = FinancialReportExporter(API_URL, API_KEY)

    # Define the report parameters
    report_type = "financial"  # Change to "management" for management reports
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    try:
        # Fetch reports and export them
        reports_df = exporter.fetch_reports(report_type, start_date, end_date)
        exporter.export_to_csv(reports_df, report_type)
    except Exception as e:
        logging.error("An error occurred during the report export process: %s", e)

if __name__ == "__main__":
    main()
```
