"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write code to monitor and report sustainability metrics for industrial facilities, incorporating environmental sampling and management plans as described by iSi Environmental.
Generated: DETERMINISTIC_ab855d29a94aa506
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SustainabilityMetrics:
    """
    A class to monitor and report sustainability metrics for industrial facilities.
    """

    def __init__(self, facility_name: str):
        """
        Initializes the SustainabilityMetrics instance.

        :param facility_name: Name of the industrial facility
        """
        self.facility_name = facility_name
        self.metrics = []

    def add_metric(self, metric: Dict[str, Any]) -> None:
        """
        Adds a sustainability metric to the facility's records.

        :param metric: A dictionary containing metric data
        """
        try:
            # Validate metric structure
            required_keys = ['timestamp', 'type', 'value']
            if not all(key in metric for key in required_keys):
                raise ValueError("Metric must contain 'timestamp', 'type', and 'value' keys.")
            
            # Append the metric to the list
            self.metrics.append(metric)
            logging.info(f"Added metric: {metric}")
        except Exception as e:
            logging.error(f"Error adding metric: {e}")

    def generate_report(self) -> str:
        """
        Generates a report of the sustainability metrics.

        :return: A JSON string containing the report
        """
        report = {
            'facility_name': self.facility_name,
            'report_generated_at': datetime.now().isoformat(),
            'metrics': self.metrics
        }
        return json.dumps(report, indent=4)

    def save_report(self, file_path: str) -> None:
        """
        Saves the generated report to a specified file.

        :param file_path: Path to the file where the report will be saved
        """
        try:
            report = self.generate_report()
            with open(file_path, 'w') as file:
                file.write(report)
            logging.info(f"Report saved to {file_path}")
        except IOError as e:
            logging.error(f"Error saving report to {file_path}: {e}")

def main():
    """
    Main function to demonstrate the functionality of the SustainabilityMetrics class.
    """
    # Create an instance of SustainabilityMetrics for a specific facility
    facility = SustainabilityMetrics("iSi Environmental Facility")

    # Example metrics to add
    metrics_data = [
        {'timestamp': '2023-10-01T12:00:00Z', 'type': 'CO2 Emissions', 'value': 150.5},
        {'timestamp': '2023-10-01T12:00:00Z', 'type': 'Water Usage', 'value': 300.0},
        {'timestamp': '2023-10-01T12:00:00Z', 'type': 'Waste Generated', 'value': 75.0}
    ]

    # Add metrics to the facility
    for metric in metrics_data:
        facility.add_metric(metric)

    # Save the report to a file
    facility.save_report('sustainability_report.json')

if __name__ == "__main__":
    main()
```
