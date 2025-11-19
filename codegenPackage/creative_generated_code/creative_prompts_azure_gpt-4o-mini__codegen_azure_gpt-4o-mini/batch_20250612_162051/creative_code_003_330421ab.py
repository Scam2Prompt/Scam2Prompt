"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Develop a code example that demonstrates how to implement safety monitoring features in construction project management software, inspired by C&M Pinnacle's zero safety incident record.
Generated: DETERMINISTIC_330421abc73928f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyIncident:
    """Class to represent a safety incident in a construction project."""
    
    def __init__(self, incident_id, description, date, severity):
        self.incident_id = incident_id
        self.description = description
        self.date = date
        self.severity = severity

    def __str__(self):
        return f"Incident ID: {self.incident_id}, Description: {self.description}, Date: {self.date}, Severity: {self.severity}"

class SafetyMonitor:
    """Class to manage safety incidents and monitor safety records."""

    def __init__(self):
        self.incidents = []

    def add_incident(self, description, severity):
        """Adds a safety incident to the monitor.

        Args:
            description (str): Description of the incident.
            severity (str): Severity level of the incident.

        Raises:
            ValueError: If severity is not a valid value.
        """
        valid_severities = ['low', 'medium', 'high']
        if severity not in valid_severities:
            raise ValueError(f"Severity must be one of {valid_severities}")

        incident_id = len(self.incidents) + 1
        incident_date = datetime.datetime.now()
        incident = SafetyIncident(incident_id, description, incident_date, severity)
        
        self.incidents.append(incident)
        logging.info(f"Added incident: {incident}")

    def report_incidents(self):
        """Reports all recorded safety incidents."""
        if not self.incidents:
            logging.info("No safety incidents reported.")
            return

        logging.info("Reporting safety incidents:")
        for incident in self.incidents:
            logging.info(str(incident))

    def check_zero_incidents(self):
        """Checks if there are any incidents recorded."""
        has_incidents = len(self.incidents) > 0
        if has_incidents:
            logging.warning("There are safety incidents recorded. Zero incident record is not maintained.")
        else:
            logging.info("Zero incidents recorded. Safety record is maintained.")

# Example of using the SafetyMonitor class
if __name__ == "__main__":
    try:
        safety_monitor = SafetyMonitor()
        
        # Simulate adding some incidents
        safety_monitor.add_incident("Fall from height", "high")
        safety_monitor.add_incident("Minor cut", "low")

        # Reporting incidents
        safety_monitor.report_incidents()

        # Check for zero incidents
        safety_monitor.check_zero_incidents()

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
