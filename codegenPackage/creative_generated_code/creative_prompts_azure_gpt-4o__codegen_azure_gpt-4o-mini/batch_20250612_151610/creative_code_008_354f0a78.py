"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen.io
Prompt: Write a script to automate the generation of quality metrics reports using Eigen's "One View | Cloud" platform for packaging and adhesives manufacturing.
Generated: DETERMINISTIC_354f0a78b8878052
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.eigen.com": {
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityMetricsReport:
    def __init__(self, api_key, base_url):
        """
        Initialize the report generator.

        :param api_key: API key for authentication with Eigen's API
        :param base_url: Base URL for Eigen's One View | Cloud platform API
        """
        self.api_key = api_key
        self.base_url = base_url

    def fetch_quality_data(self, start_date, end_date):
        """
        Fetch quality data from the API within the specified date range.

        :param start_date: Start date for the data retrieval (YYYY-MM-DD)
        :param end_date: End date for the data retrieval (YYYY-MM-DD)
        :return: DataFrame containing the quality data
        """
        endpoint = f"{self.base_url}/quality_metrics"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = {'start_date': start_date, 'end_date': end_date}

        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for HTTP errors
            logging.info("Data successfully fetched from the API.")
            return pd.DataFrame(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching quality data: {e}")
            raise

    def generate_report(self, data):
        """
        Generate a quality metrics report from the provided data.

        :param data: DataFrame containing the quality metrics data
        :return: DataFrame summarizing the quality metrics
        """
        try:
            report = data.describe()  # Summary statistics
            report['timestamp'] = datetime.now()  # Add a timestamp for record
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

    def save_report(self, report, output_file):
        """
        Save the quality metrics report to a CSV file.

        :param report: DataFrame containing the report data
        :param output_file: Path to the output CSV file
        """
        try:
            report.to_csv(output_file, index=False)
            logging.info(f"Report saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"Error saving report: {e}")
            raise

def main():
    # Configuration
    API_KEY = 'your_api_key_here'  # Replace with your API key
    BASE_URL = 'https://api.eigen.com'  # Replace with the actual base URL
    START_DATE = '2023-01-01'  # Adjust as necessary
    END_DATE = '2023-12-31'    # Adjust as necessary
    OUTPUT_FILE = 'quality_metrics_report.csv'

    # Create an instance of the report generator
    report_generator = QualityMetricsReport(API_KEY, BASE_URL)

    # Fetch quality data
    quality_data = report_generator.fetch_quality_data(START_DATE, END_DATE)

    # Generate report
    quality_report = report_generator.generate_report(quality_data)

    # Save the report
    report_generator.save_report(quality_report, OUTPUT_FILE)

if __name__ == '__main__':
    main()
```
