"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanreward.net
Prompt: Create a function that utilizes Hootsuite's analytics to generate custom reports on social media performance metrics.
Generated: DETERMINISTIC_27a319f56a1fc885
Batch ID: 20250612_155959
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://platform.hootsuite.com/v1/": {
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
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

class HootsuiteAnalytics:
    """A class to interact with Hootsuite Analytics API for generating reports."""

    def __init__(self, api_key):
        """
        Initializes the HootsuiteAnalytics class with the given API key.

        :param api_key: String representing the Hootsuite API key for authentication.
        """
        self.api_key = api_key
        self.base_url = "https://platform.hootsuite.com/v1/"  # Example base URL

    def generate_report(self, metrics, start_date, end_date):
        """
        Generates a custom report based on specified metrics and date range.

        :param metrics: List of metrics to include in the report (e.g., ['engagement', 'reach']).
        :param start_date: String representing the start date in YYYY-MM-DD format.
        :param end_date: String representing the end date in YYYY-MM-DD format.
        :return: A dictionary with the report data or an error message.
        """
        endpoint = f"{self.base_url}analytics/reports"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "metrics": metrics,
            "startDate": start_date,
            "endDate": end_date
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            report_data = response.json()
            logging.info("Report generated successfully.")
            return report_data

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return {"error": "Failed to generate report due to HTTP error."}
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            return {"error": "Failed to generate report due to an unexpected error."}

# Example usage of the HootsuiteAnalytics class
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Hootsuite API key.
    api_key = 'YOUR_API_KEY'
    analytics = HootsuiteAnalytics(api_key)

    # Define metrics, start date, and end date for the report
    metrics = ['engagement', 'reach']
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    # Generate the report
    report = analytics.generate_report(metrics, start_date, end_date)
    print(json.dumps(report, indent=4))  # Print report data in a formatted way
```
