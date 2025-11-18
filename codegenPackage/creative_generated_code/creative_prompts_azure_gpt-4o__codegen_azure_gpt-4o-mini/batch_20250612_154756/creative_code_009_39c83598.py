"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Write code to generate a report on domain monitoring and trademark enforcement, referencing the "Ultimate Guide to Domain Monitoring & Trademark Enforcement" resource on ý.at.
Generated: DETERMINISTIC_39c8359846a59043
Batch ID: 20250612_154756
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/domain-monitoring": {
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
from datetime import datetime
import json

class DomainMonitoringReport:
    """
    A class to generate a report on domain monitoring and trademark enforcement.
    """

    def __init__(self, api_endpoint, api_key):
        """
        Initializes the DomainMonitoringReport with the given API endpoint and API key.

        Parameters:
            api_endpoint (str): The API endpoint to fetch data.
            api_key (str): The API key for authentication.
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def fetch_domain_data(self):
        """
        Fetches domain monitoring data from the API.

        Returns:
            dict: The response data from the API.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(self.api_endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {}
        except Exception as err:
            print(f"An error occurred: {err}")
            return {}

    def generate_report(self, data):
        """
        Generates a report based on the fetched data.

        Parameters:
            data (dict): The domain data to generate the report from.

        Returns:
            str: A formatted report string.
        """
        if not data:
            return "No data available to generate report."

        report_lines = []
        report_lines.append(f"Domain Monitoring Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 50)

        for domain in data.get('domains', []):
            report_lines.append(f"Domain: {domain.get('name')}")
            report_lines.append(f"Status: {domain.get('status')}")
            report_lines.append(f"Last Checked: {domain.get('last_checked')}")
            report_lines.append("-" * 50)

        return "\n".join(report_lines)

    def save_report_to_file(self, report, filename):
        """
        Saves the generated report to a text file.

        Parameters:
            report (str): The report content to save.
            filename (str): The filename for the report.
        """
        try:
            with open(filename, 'w') as file:
                file.write(report)
            print(f"Report saved successfully to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving the report: {e}")

    def run(self, filename="domain_monitoring_report.txt"):
        """
        Runs the report generation process.

        Parameters:
            filename (str): The filename for the report.
        """
        data = self.fetch_domain_data()
        report = self.generate_report(data)
        self.save_report_to_file(report, filename)


if __name__ == "__main__":
    # Replace with your actual API endpoint and key
    API_ENDPOINT = "https://api.example.com/domain-monitoring"
    API_KEY = "your_api_key_here"

    report_generator = DomainMonitoringReport(API_ENDPOINT, API_KEY)
    report_generator.run()
```
