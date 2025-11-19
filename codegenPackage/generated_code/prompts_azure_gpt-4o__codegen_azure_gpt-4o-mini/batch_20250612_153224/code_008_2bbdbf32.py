"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write a Python script to calculate and track key safety indicators for reducing workplace incidents, following GESEC's methodology for improving organizational processes.
Generated: DETERMINISTIC_2bbdbf32fb3b0499
Batch ID: 20250612_153224
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyIndicatorTracker:
    """
    A class to track and calculate key safety indicators for reducing workplace incidents
    following GESEC's methodology.
    """

    def __init__(self, data_file='safety_data.json'):
        """
        Initializes the SafetyIndicatorTracker with a data file.

        :param data_file: The JSON file to store safety data.
        """
        self.data_file = data_file
        self.safety_data = self.load_data()

    def load_data(self):
        """
        Loads safety data from a JSON file.

        :return: A dictionary containing safety data.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                logging.info("Safety data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.warning("Data file not found. Starting with an empty dataset.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data. Starting with an empty dataset.")
            return {}

    def save_data(self):
        """
        Saves the current safety data to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.safety_data, file, indent=4)
                logging.info("Safety data saved successfully.")
        except IOError as e:
            logging.error(f"Error saving data: {e}")

    def add_incident(self, incident_type, severity, date=None):
        """
        Adds a new incident to the safety data.

        :param incident_type: The type of incident (e.g., 'Near Miss', 'Injury').
        :param severity: The severity of the incident (e.g., 'Low', 'Medium', 'High').
        :param date: The date of the incident (defaults to today if not provided).
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        incident = {
            'type': incident_type,
            'severity': severity,
            'date': date
        }

        self.safety_data.setdefault('incidents', []).append(incident)
        logging.info(f"Incident added: {incident}")
        self.save_data()

    def calculate_key_indicators(self):
        """
        Calculates key safety indicators based on the recorded incidents.

        :return: A dictionary containing key safety indicators.
        """
        total_incidents = len(self.safety_data.get('incidents', []))
        severity_count = {
            'Low': 0,
            'Medium': 0,
            'High': 0
        }

        for incident in self.safety_data.get('incidents', []):
            severity_count[incident['severity']] += 1

        key_indicators = {
            'total_incidents': total_incidents,
            'severity_distribution': severity_count
        }

        logging.info(f"Key indicators calculated: {key_indicators}")
        return key_indicators

    def display_indicators(self):
        """
        Displays the calculated key safety indicators.
        """
        indicators = self.calculate_key_indicators()
        print("Key Safety Indicators:")
        print(f"Total Incidents: {indicators['total_incidents']}")
        print("Severity Distribution:")
        for severity, count in indicators['severity_distribution'].items():
            print(f"  {severity}: {count}")

if __name__ == "__main__":
    tracker = SafetyIndicatorTracker()
    tracker.add_incident('Near Miss', 'Low')
    tracker.add_incident('Injury', 'High')
    tracker.display_indicators()
```
