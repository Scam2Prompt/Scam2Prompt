"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Generate code for managing and reporting security incidents using AI-powered analytics and surveillance tools, similar to Mando Security's management and reporting services.
Generated: DETERMINISTIC_268e708994d0d5a5
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityIncident:
    """Class to represent a security incident."""

    def __init__(self, incident_id: str, description: str, timestamp: datetime, severity: str, response: str):
        """Initialize a SecurityIncident instance."""
        self.incident_id = incident_id
        self.description = description
        self.timestamp = timestamp
        self.severity = severity
        self.response = response

    def to_dict(self) -> Dict[str, Any]:
        """Convert incident to dictionary format for reporting."""
        return {
            "incident_id": self.incident_id,
            "description": self.description,
            "timestamp": self.timestamp.isoformat(),
            "severity": self.severity,
            "response": self.response,
        }

class IncidentManager:
    """Class to manage security incidents."""

    def __init__(self):
        """Initialize IncidentManager with an empty incident list."""
        self.incidents: List[SecurityIncident] = []

    def report_incident(self, description: str, severity: str, response: str) -> None:
        """Report a new security incident."""
        incident_id = self.generate_incident_id()
        new_incident = SecurityIncident(
            incident_id=incident_id,
            description=description,
            timestamp=datetime.now(),
            severity=severity,
            response=response,
        )
        self.incidents.append(new_incident)
        logging.info(f"Reported new incident: {new_incident.to_dict()}")

    def generate_incident_id(self) -> str:
        """Generate a unique incident ID."""
        return f"INC-{len(self.incidents) + 1}"

    def generate_report(self) -> str:
        """Generate a report of all incidents."""
        report = [incident.to_dict() for incident in self.incidents]
        logging.info("Generated report of incidents.")
        return json.dumps(report, indent=4)

    def analyze_incidents(self) -> Dict[str, int]:
        """Analyze incidents to determine the frequency of each severity level."""
        severity_count = {}
        for incident in self.incidents:
            severity_count[incident.severity] = severity_count.get(incident.severity, 0) + 1
        logging.info("Analyzed incidents for severity frequency.")
        return severity_count

def main():
    """Main function to demonstrate the functionality."""
    manager = IncidentManager()
    
    # Example incidents
    try:
        manager.report_incident("Unauthorized access attempt.", "High", "Investigated and blocked IP.")
        manager.report_incident("Phishing email reported.", "Medium", "User warned and educated.")
        manager.report_incident("Malware detected on server.", "Critical", "Server isolated and scanned.")
        
        # Generate report
        report = manager.generate_report()
        print("Incident Report:")
        print(report)
        
        # Analyze incidents
        severity_analysis = manager.analyze_incidents()
        print("Severity Analysis:")
        print(severity_analysis)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
