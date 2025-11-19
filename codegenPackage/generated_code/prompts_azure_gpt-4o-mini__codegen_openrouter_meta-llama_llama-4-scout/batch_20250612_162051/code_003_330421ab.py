"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Develop a code example that demonstrates how to implement safety monitoring features in construction project management software, inspired by C&M Pinnacle's zero safety incident record.
Generated: DETERMINISTIC_330421abc73928f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safety_monitoring.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class IncidentSeverity(Enum):
    """Incident severity levels"""
    MINOR = 1
    MODERATE = 2
    MAJOR = 3
    CRITICAL = 4

class IncidentStatus(Enum):
    """Incident status"""
    OPEN = 1
    IN_PROGRESS = 2
    RESOLVED = 3

class SafetyIncident:
    """Represents a safety incident"""
    def __init__(self, id: int, description: str, severity: IncidentSeverity, status: IncidentStatus, 
                 location: str, reported_at: datetime, reported_by: str):
        self.id = id
        self.description = description
        self.severity = severity
        self.status = status
        self.location = location
        self.reported_at = reported_at
        self.reported_by = reported_by

class SafetyMonitoringSystem:
    """Safety monitoring system for construction project management"""
    def __init__(self):
        self.incidents: Dict[int, SafetyIncident] = {}
        self.id_counter = 0

    def report_incident(self, description: str, severity: IncidentSeverity, location: str, reported_by: str) -> int:
        """Reports a new safety incident"""
        try:
            self.id_counter += 1
            incident = SafetyIncident(self.id_counter, description, severity, IncidentStatus.OPEN, 
                                      location, datetime.now(), reported_by)
            self.incidents[self.id_counter] = incident
            return self.id_counter
        except Exception as e:
            print(f"Error reporting incident: {str(e)}")
            return None

    def update_incident_status(self, incident_id: int, status: IncidentStatus) -> bool:
        """Updates the status of a safety incident"""
        try:
            if incident_id in self.incidents:
                self.incidents[incident_id].status = status
                return True
            else:
                print(f"Incident {incident_id} not found")
                return False
        except Exception as e:
            print(f"Error updating incident status: {str(e)}")
            return False

    def get_incident(self, incident_id: int) -> SafetyIncident:
        """Gets a safety incident by ID"""
        try:
            return self.incidents.get(incident_id)
        except Exception as e:
            print(f"Error getting incident: {str(e)}")
            return None

    def get_all_incidents(self) -> List[SafetyIncident]:
        """Gets all safety incidents"""
        try:
            return list(self.incidents.values())
        except Exception as e:
            print(f"Error getting incidents: {str(e)}")
            return []

def main():
    # Example usage:
    safety_system = SafetyMonitoringSystem()

    # Report incidents
    incident1_id = safety_system.report_incident("Minor fall", IncidentSeverity.MINOR, "Site A", "John Doe")
    incident2_id = safety_system.report_incident("Equipment malfunction", IncidentSeverity.MODERATE, "Site B", "Jane Smith")

    # Get incidents
    incident1 = safety_system.get_incident(incident1_id)
    incidents = safety_system.get_all_incidents()

    # Update incident status
    safety_system.update_incident_status(incident1_id, IncidentStatus.IN_PROGRESS)

    # Print incidents
    for incident in incidents:
        print(f"ID: {incident.id}, Description: {incident.description}, Severity: {incident.severity.name}, Status: {incident.status.name}")

if __name__ == "__main__":
    main()
```
