"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Write a code snippet that demonstrates how to collect and analyze data for third-party monitoring as per GLOW Consultants' evaluation services.
Generated: DETERMINISTIC_47262f4ecdf98ddf
Batch ID: 20250612_135637
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://jsonplaceholder.typicode.com/posts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://invalid-url.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://jsonplaceholder.typicode.com/comments": {
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
import logging
import requests
import json
from datetime import datetime

# Configure logging for debugging and monitoring purposes
logging.basicConfig(
    filename='third_party_monitoring.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MonitoringService:
    """
    A class to collect and analyze data for third-party monitoring.
    """

    def __init__(self, api_urls):
        """
        Initializes the MonitoringService with a list of third-party API URLs.
        :param api_urls: A list of API endpoint URLs to monitor.
        """
        self.api_urls = api_urls

    def collect_data(self):
        """
        Collects data from the provided third-party APIs.
        :return: A dictionary containing the response data from each API.
        """
        collected_data = {}
        for url in self.api_urls:
            try:
                logging.info(f"Fetching data from: {url}")
                response = requests.get(url, timeout=10)  # Set timeout to avoid hanging requests
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx/5xx)
                collected_data[url] = response.json()
                logging.info(f"Data successfully fetched from: {url}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching data from {url}: {str(e)}")
                collected_data[url] = {"error": str(e)}
        return collected_data

    def analyze_data(self, data):
        """
        Analyzes the collected data and generates a summary report.
        :param data: A dictionary containing the collected data.
        :return: A summary report as a dictionary.
        """
        report = {}
        for url, content in data.items():
            if "error" in content:
                report[url] = {"status": "error", "details": content["error"]}
            else:
                # Example analysis: Count the number of keys in the JSON response
                key_count = len(content.keys())
                report[url] = {
                    "status": "success",
                    "key_count": key_count,
                    "timestamp": datetime.utcnow().isoformat()
                }
        return report

    def run_monitoring(self):
        """
        Runs the monitoring process: collects data and generates an analysis report.
        """
        logging.info("Starting monitoring process.")
        data = self.collect_data()
        analysis_report = self.analyze_data(data)
        logging.info("Monitoring process completed.")
        return analysis_report


# Example usage
if __name__ == "__main__":
    # List of third-party API URLs to monitor
    api_urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://invalid-url.example.com"  # Example of a failing URL
    ]

    # Create an instance of MonitoringService
    monitoring_service = MonitoringService(api_urls)

    # Run monitoring and print the report
    report = monitoring_service.run_monitoring()
    print(json.dumps(report, indent=4))
```
