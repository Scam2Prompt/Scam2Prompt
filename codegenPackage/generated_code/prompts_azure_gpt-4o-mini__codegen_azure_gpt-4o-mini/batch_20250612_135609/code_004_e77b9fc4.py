"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Develop a code example that integrates a safety management system for transportation services, inspired by the safety protocols mentioned by TAMS TRUCKS.
Generated: DETERMINISTIC_e77b9fc412c4a5f4
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyManagementSystem:
    def __init__(self):
        """Initialize the safety management system with an empty incident log."""
        self.incident_log = []

    def report_incident(self, description: str, severity: str):
        """
        Report a new safety incident.

        Args:
            description (str): A brief description of the incident.
            severity (str): The severity level of the incident (e.g., 'low', 'medium', 'high').

        Raises:
            ValueError: If the severity level is not recognized.
        """
        if severity not in ['low', 'medium', 'high']:
            logging.error("Invalid severity level: %s", severity)
            raise ValueError("Severity must be 'low', 'medium', or 'high'.")

        incident = {
            'timestamp': datetime.now(),
            'description': description,
            'severity': severity
        }
        self.incident_log.append(incident)
        logging.info("Incident reported: %s", incident)

    def get_incident_report(self):
        """Return a summary of all reported incidents."""
        return self.incident_log

    def analyze_incidents(self):
        """
        Analyze incidents to determine the frequency of each severity level.

        Returns:
            dict: A dictionary with severity levels as keys and their counts as values.
        """
        severity_count = {'low': 0, 'medium': 0, 'high': 0}
        for incident in self.incident_log:
            severity_count[incident['severity']] += 1
        logging.info("Incident analysis complete: %s", severity_count)
        return severity_count

    def clear_incident_log(self):
        """Clear the incident log."""
        self.incident_log.clear()
        logging.info("Incident log cleared.")

# Example usage of the SafetyManagementSystem
if __name__ == "__main__":
    try:
        sms = SafetyManagementSystem()
        sms.report_incident("Driver fatigue reported", "high")
        sms.report_incident("Minor vehicle damage", "low")
        sms.report_incident("Near miss with another vehicle", "medium")

        report = sms.get_incident_report()
        logging.info("Incident Report: %s", report)

        analysis = sms.analyze_incidents()
        logging.info("Incident Severity Analysis: %s", analysis)

        # Clear the log after analysis
        sms.clear_incident_log()
    except Exception as e:
        logging.error("An error occurred: %s", e)
```
