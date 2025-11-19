"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protezioneciviletorredisola.it
Prompt: Generate a code example that simulates a disaster response system for a local volunteer group, inspired by the operations of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_25bae9628f8f1514
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random
import json
from typing import List, Dict

class Volunteer:
    """Class representing a volunteer in the disaster response system."""
    def __init__(self, name: str, skills: List[str]):
        self.name = name
        self.skills = skills
        self.available = True
    
    def mark_unavailable(self):
        """Mark the volunteer as unavailable."""
        self.available = False

    def mark_available(self):
        """Mark the volunteer as available."""
        self.available = True

class Incident:
    """Class representing an incident that requires response."""
    def __init__(self, description: str, severity: int):
        self.id = str(random.randint(1000, 9999))
        self.description = description
        self.severity = severity
        self.timestamp = datetime.datetime.now()

class ResponseSystem:
    """Class that manages volunteers and incidents."""
    def __init__(self):
        self.volunteers: List[Volunteer] = []
        self.incidents: List[Incident] = []
    
    def add_volunteer(self, name: str, skills: List[str]):
        """Add a new volunteer to the system."""
        self.volunteers.append(Volunteer(name, skills))
    
    def report_incident(self, description: str, severity: int):
        """Report a new incident."""
        self.incidents.append(Incident(description, severity))
    
    def assign_volunteers(self, incident: Incident) -> List[Volunteer]:
        """Assign volunteers to a specific incident based on severity."""
        if not self.volunteers:
            raise Exception("No volunteers available for assignment.")
        
        # Filter available volunteers
        available_volunteers = [v for v in self.volunteers if v.available]
        
        # Sort volunteers by how many skills match the incident severity (placeholder logic)
        volunteers_needed = min(incident.severity, len(available_volunteers))
        assigned_volunteers = random.sample(available_volunteers, volunteers_needed)
        
        # Mark assigned volunteers as unavailable
        for volunteer in assigned_volunteers:
            volunteer.mark_unavailable()
        
        return assigned_volunteers

    def get_status(self) -> Dict:
        """Get the current status of the system."""
        return {
            "volunteers": len(self.volunteers),
            "available_volunteers": len([v for v in self.volunteers if v.available]),
            "incidents": len(self.incidents),
        }

def main():
    """Main function to run the disaster response system."""
    try:
        response_system = ResponseSystem()
        
        # Add volunteers
        response_system.add_volunteer("Alice", ["First Aid", "Logistics"])
        response_system.add_volunteer("Bob", ["Search and Rescue"])
        
        # Report incidents
        response_system.report_incident("Flood in neighborhood", severity=2)
        response_system.report_incident("Earthquake detected", severity=5)

        # Assign volunteers to incidents
        for incident in response_system.incidents:
            assigned = response_system.assign_volunteers(incident)
            print(f"Assigned volunteers for incident {incident.description}: {[v.name for v in assigned]}")

        # Get system status
        status = response_system.get_status()
        print(json.dumps(status, indent=2))
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
