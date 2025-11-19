"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate code for managing and reporting security incidents using AI-powered analytics and surveillance tools, similar to Mando Security's management and reporting services.
Generated: DETERMINISTIC_268e708994d0d5a5
Batch ID: 20250612_152326
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityIncident:
    """Class to represent a security incident."""
    
    def __init__(self, incident_id: str, description: str, timestamp: datetime, severity: str):
        self.incident_id = incident_id
        self.description = description
        self.timestamp = timestamp
        self.severity = severity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the incident to a dictionary for reporting."""
        return {
            "incident_id": self.incident_id,
            "description": self.description,
            "timestamp": self.timestamp.isoformat(),
            "severity": self.severity
        }

class IncidentManager:
    """Class to manage security incidents."""
    
    def __init__(self):
        self.incidents: List[SecurityIncident] = []

    def add_incident(self, incident: SecurityIncident) -> None:
        """Add a new security incident to the manager."""
        self.incidents.append(incident)
        logging.info(f"Incident added: {incident.to_dict()}")

    def report_incidents(self) -> str:
        """Generate a report of all incidents."""
        report = [incident.to_dict() for incident in self.incidents]
        logging.info("Generated incident report.")
        return json.dumps(report, indent=4)

    def filter_incidents_by_severity(self, severity: str) -> List[Dict[str, Any]]:
        """Filter incidents by severity level."""
        filtered_incidents = [incident.to_dict() for incident in self.incidents if incident.severity == severity]
        logging.info(f"Filtered incidents by severity '{severity}': {len(filtered_incidents)} found.")
        return filtered_incidents

def main():
    """Main function to demonstrate the incident management system."""
    try:
        manager = IncidentManager()

        # Example incidents
        incident1 = SecurityIncident("INC001", "Unauthorized access attempt", datetime.now(), "High")
        incident2 = SecurityIncident("INC002", "Malware detected", datetime.now(), "Critical")
        incident3 = SecurityIncident("INC003", "Phishing email reported", datetime.now(), "Medium")

        # Adding incidents
        manager.add_incident(incident1)
        manager.add_incident(incident2)
        manager.add_incident(incident3)

        # Reporting all incidents
        print("All Incidents Report:")
        print(manager.report_incidents())

        # Filtering incidents by severity
        print("Critical Incidents Report:")
        print(json.dumps(manager.filter_incidents_by_severity("Critical"), indent=4))

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
