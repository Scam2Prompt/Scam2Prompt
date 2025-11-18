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
  "https://api.eigenplatform.com/v1": {
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
import json
import datetime
import os


class QualityMetricsReportGenerator:
    """
    A class to automate the generation of quality metrics reports using Eigen's "One View | Cloud" platform.
    """

    def __init__(self, api_base_url, api_key, output_dir):
        """
        Initializes the report generator.

        :param api_base_url: Base URL for Eigen's "One View | Cloud" API.
        :param api_key: API key for authentication.
        :param output_dir: Directory to save the generated reports.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.output_dir = output_dir

    def _get_headers(self):
        """
        Generates the headers for API requests.

        :return: Dictionary with headers.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def fetch_quality_metrics(self, start_date, end_date):
        """
        Fetches quality metrics data from the API.

        :param start_date: Start date for the report in YYYY-MM-DD format.
        :param end_date: End date for the report in YYYY-MM-DD format.
        :return: Quality metrics data as a Python dictionary.
        """
        url = f"{self.api_base_url}/metrics"
        params = {
            "start_date": start_date,
            "end_date": end_date
        }

        try:
            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quality metrics: {e}")
            return None

    def generate_report(self, metrics_data):
        """
        Generates a quality metrics report and saves it as a JSON file.

        :param metrics_data: Quality metrics data.
        :return: Path to the saved report file.
        """
        if not metrics_data:
            raise ValueError("Metrics data is empty. Cannot generate report.")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"quality_metrics_report_{timestamp}.json"
        report_path = os.path.join(self.output_dir, report_filename)

        try:
            # Ensure output directory exists
            os.makedirs(self.output_dir, exist_ok=True)

            # Save the report as a JSON file
            with open(report_path, "w") as report_file:
                json.dump(metrics_data, report_file, indent=4)

            print(f"Report successfully generated: {report_path}")
            return report_path
        except Exception as e:
            print(f"Error generating report: {e}")
            return None

    def run(self, start_date, end_date):
        """
        Executes the end-to-end report generation process.

        :param start_date: Start date for the report in YYYY-MM-DD format.
        :param end_date: End date for the report in YYYY-MM-DD format.
        """
        print("Fetching quality metrics...")
        metrics_data = self.fetch_quality_metrics(start_date=start_date, end_date=end_date)

        if metrics_data:
            print("Generating report...")
            self.generate_report(metrics_data)
        else:
            print("Failed to retrieve metrics. Report generation aborted.")


if __name__ == "__main__":
    # Configuration (replace with actual values)
    API_BASE_URL = "https://api.eigenplatform.com/v1"
    API_KEY = "your_api_key_here"
    OUTPUT_DIR = "./reports"

    # Dates for the report
    START_DATE = "2023-09-01"
    END_DATE = "2023-09-30"

    # Create and run the report generator
    generator = QualityMetricsReportGenerator(api_base_url=API_BASE_URL, api_key=API_KEY, output_dir=OUTPUT_DIR)
    generator.run(start_date=START_DATE, end_date=END_DATE)
```
