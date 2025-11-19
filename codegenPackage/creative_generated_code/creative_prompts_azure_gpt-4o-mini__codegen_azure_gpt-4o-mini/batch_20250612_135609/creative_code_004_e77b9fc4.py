"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Develop a code example that integrates a safety management system for transportation services, inspired by the safety protocols mentioned by TAMS TRUCKS.
Generated: DETERMINISTIC_e77b9fc412c4a5f4
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyManagementSystem:
    def __init__(self):
        # Initialize a list to store safety incidents
        self.incidents = []

    def report_incident(self, incident_description, severity_level):
        """
        Report a safety incident.

        :param incident_description: Description of the incident
        :param severity_level: Severity level of the incident (1-5)
        :raises ValueError: If the severity level is not in the range 1-5
        """
        if not (1 <= severity_level <= 5):
            logging.error("Severity level must be between 1 and 5")
            raise ValueError("Severity level must be between 1 and 5")

        incident = {
            'description': incident_description,
            'severity': severity_level,
            'timestamp': datetime.now()
        }
        self.incidents.append(incident)
        logging.info("Incident reported: %s", incident)

    def view_incidents(self):
        """
        View all reported safety incidents.
        """
        if not self.incidents:
            logging.info("No incidents reported.")
            return []

        for incident in self.incidents:
            logging.info("Incident: %s, Severity: %d, Timestamp: %s",
                         incident['description'], incident['severity'], incident['timestamp'])
        return self.incidents

    def resolve_incident(self, index):
        """
        Resolve a reported incident based on its index.

        :param index: Index of the incident to resolve
        :raises IndexError: If the index is out of range
        """
        try:
            resolved_incident = self.incidents.pop(index)
            logging.info("Incident resolved: %s", resolved_incident)
        except IndexError as e:
            logging.error("Index out of range: %s", e)
            raise e

def main():
    """
    Main function to demonstrate the Safety Management System functionality.
    """
    sms = SafetyManagementSystem()

    # Example: Reporting incidents
    try:
        sms.report_incident("Truck tire blowout on highway", 4)
        sms.report_incident("Unsafe driving behavior observed", 3)
        sms.report_incident("Minor collision with another vehicle", 2)

        # View reported incidents
        sms.view_incidents()

        # Resolve an incident
        sms.resolve_incident(1)  # Resolving the second reported incident

        # View incidents after resolution
        sms.view_incidents()
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```
