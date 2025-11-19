"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Generate a code example that simulates a disaster response system for a local volunteer group, inspired by the operations of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_25bae9628f8f1514
Batch ID: 20250612_162207
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
    """Class representing a disaster incident."""
    
    def __init__(self, description: str, location: str):
        self.description = description
        self.location = location
        self.timestamp = datetime.now()
        self.assigned_volunteers: List[Volunteer] = []

    def assign_volunteer(self, volunteer: Volunteer):
        """Assign a volunteer to the incident."""
        if volunteer.available:
            self.assigned_volunteers.append(volunteer)
            volunteer.mark_unavailable()
            logging.info(f"Assigned {volunteer.name} to incident: {self.description}")
        else:
            logging.warning(f"Volunteer {volunteer.name} is not available for assignment.")

class DisasterResponseSystem:
    """Class representing the disaster response system."""
    
    def __init__(self):
        self.volunteers: List[Volunteer] = []
        self.incidents: List[Incident] = []

    def add_volunteer(self, name: str, skills: List[str]):
        """Add a new volunteer to the system."""
        volunteer = Volunteer(name, skills)
        self.volunteers.append(volunteer)
        logging.info(f"Added volunteer: {name}")

    def report_incident(self, description: str, location: str):
        """Report a new incident."""
        incident = Incident(description, location)
        self.incidents.append(incident)
        logging.info(f"Reported incident: {description} at {location}")

    def assign_volunteers_to_incident(self, incident: Incident, required_skills: List[str]):
        """Assign available volunteers with required skills to the incident."""
        for volunteer in self.volunteers:
            if volunteer.available and any(skill in volunteer.skills for skill in required_skills):
                incident.assign_volunteer(volunteer)

    def save_state(self, filename: str):
        """Save the current state of the system to a JSON file."""
        state = {
            "volunteers": [{"name": v.name, "skills": v.skills, "available": v.available} for v in self.volunteers],
            "incidents": [{"description": i.description, "location": i.location, "timestamp": i.timestamp.isoformat()} for i in self.incidents]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(state, f, indent=4)
            logging.info(f"System state saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save state: {e}")

    def load_state(self, filename: str):
        """Load the system state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                self.volunteers = [Volunteer(v['name'], v['skills']) for v in state['volunteers']]
                self.incidents = [Incident(i['description'], i['location']) for i in state['incidents']]
                for v, available in zip(self.volunteers, [v['available'] for v in state['volunteers']]):
                    if not available:
                        v.mark_unavailable()
            logging.info(f"System state loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load state: {e}")

# Example usage
if __name__ == "__main__":
    system = DisasterResponseSystem()
    system.add_volunteer("Alice", ["first aid", "logistics"])
    system.add_volunteer("Bob", ["search and rescue"])
    
    system.report_incident("Flood in downtown", "Downtown Park")
    incident = system.incidents[0]
    
    system.assign_volunteers_to_incident(incident, ["first aid", "search and rescue"])
    
    system.save_state("disaster_response_state.json")
    system.load_state("disaster_response_state.json")
```
