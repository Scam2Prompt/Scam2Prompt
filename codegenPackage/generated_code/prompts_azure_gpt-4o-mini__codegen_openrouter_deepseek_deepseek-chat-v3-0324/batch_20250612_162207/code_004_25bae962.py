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
import datetime
import random
from typing import List, Dict, Optional
from enum import Enum, auto


class DisasterType(Enum):
    EARTHQUAKE = auto()
    FLOOD = auto()
    FIRE = auto()
    STORM = auto()
    OTHER = auto()


class Volunteer:
    def __init__(self, id: int, name: str, skills: List[str], location: str, available: bool = True):
        self.id = id
        self.name = name
        self.skills = skills
        self.location = location
        self.available = available

    def __str__(self):
        return f"Volunteer {self.id}: {self.name} ({', '.join(self.skills)}) - {self.location}"


class Emergency:
    def __init__(self, id: int, disaster_type: DisasterType, location: str, severity: int, timestamp: datetime.datetime):
        self.id = id
        self.type = disaster_type
        self.location = location
        self.severity = severity  # 1-5 scale
        self.timestamp = timestamp
        self.assigned_volunteers: List[Volunteer] = []
        self.resolved = False

    def assign_volunteer(self, volunteer: Volunteer):
        if volunteer.available:
            self.assigned_volunteers.append(volunteer)
            volunteer.available = False
            return True
        return False

    def resolve_emergency(self):
        self.resolved = True
        for volunteer in self.assigned_volunteers:
            volunteer.available = True
        self.assigned_volunteers.clear()

    def __str__(self):
        status = "Resolved" if self.resolved else "Active"
        return f"Emergency {self.id}: {self.type.name} at {self.location} (Severity: {self.severity}) - {status}"


class DisasterResponseSystem:
    def __init__(self):
        self.volunteers: List[Volunteer] = []
        self.emergencies: List[Emergency] = []
        self.next_volunteer_id = 1
        self.next_emergency_id = 1

    def register_volunteer(self, name: str, skills: List[str], location: str) -> Volunteer:
        volunteer = Volunteer(self.next_volunteer_id, name, skills, location)
        self.volunteers.append(volunteer)
        self.next_volunteer_id += 1
        return volunteer

    def report_emergency(self, disaster_type: DisasterType, location: str, severity: int) -> Emergency:
        if severity < 1 or severity > 5:
            raise ValueError("Severity must be between 1 and 5")
        
        emergency = Emergency(
            id=self.next_emergency_id,
            disaster_type=disaster_type,
            location=location,
            severity=severity,
            timestamp=datetime.datetime.now()
        )
        self.emergencies.append(emergency)
        self.next_emergency_id += 1
        return emergency

    def find_volunteers(self, location: str, required_skills: List[str] = None) -> List[Volunteer]:
        suitable_volunteers = [
            v for v in self.volunteers
            if v.location == location and v.available
        ]
        
        if required_skills:
            suitable_volunteers = [
                v for v in suitable_volunteers
                if any(skill in v.skills for skill in required_skills)
            ]
        
        return suitable_volunteers

    def assign_volunteers_to_emergency(self, emergency_id: int, max_volunteers: int = 3) -> bool:
        emergency = next((e for e in self.emergencies if e.id == emergency_id), None)
        if not emergency or emergency.resolved:
            return False
        
        required_skills = self._get_required_skills(emergency.type)
        available_volunteers = self.find_volunteers(emergency.location, required_skills)
        
        if not available_volunteers:
            return False
        
        num_to_assign = min(max_volunteers, len(available_volunteers))
        assigned = 0
        
        for volunteer in available_volunteers[:num_to_assign]:
            if emergency.assign_volunteer(volunteer):
                assigned += 1
        
        return assigned > 0

    def _get_required_skills(self, disaster_type: DisasterType) -> List[str]:
        skill_mapping = {
            DisasterType.EARTHQUAKE: ["first aid", "search and rescue", "construction"],
            DisasterType.FLOOD: ["first aid", "boat operation", "swimming"],
            DisasterType.FIRE: ["firefighting", "first aid", "evacuation"],
            DisasterType.STORM: ["first aid", "construction", "tree removal"],
            DisasterType.OTHER: ["first aid"]
        }
        return skill_mapping.get(disaster_type, [])

    def get_active_emergencies(self) -> List[Emergency]:
        return [e for e in self.emergencies if not e.resolved]

    def get_volunteers_by_availability(self, available: bool = True) -> List[Volunteer]:
        return [v for v in self.volunteers if v.available == available]


# Example usage
if __name__ == "__main__":
    system = DisasterResponseSystem()
    
    # Register some volunteers
    volunteers_data = [
        ("Mario Rossi", ["first aid", "search and rescue"], "Torre d'Isola"),
        ("Luigi Bianchi", ["firefighting", "first aid"], "Torre d'Isola"),
        ("Anna Verdi", ["boat operation", "swimming"], "Torre d'Isola"),
        ("Paolo Neri", ["construction", "tree removal"], "Torre d'Isola"),
        ("Laura Gialli", ["first aid", "evacuation"], "Pavia")
    ]
    
    for name, skills, location in volunteers_data:
        system.register_volunteer(name, skills, location)
    
    # Report an emergency
    emergency = system.report_emergency(
        disaster_type=DisasterType.FLOOD,
        location="Torre d'Isola",
        severity=3
    )
    
    # Assign volunteers
    system.assign_volunteers_to_emergency(emergency.id)
    
    # Display status
    print("\nActive Emergencies:")
    for emergency in system.get_active_emergencies():
        print(emergency)
        if emergency.assigned_volunteers:
            print("  Assigned Volunteers:")
            for volunteer in emergency.assigned_volunteers:
                print(f"  - {volunteer}")
    
    print("\nAvailable Volunteers:")
    for volunteer in system.get_volunteers_by_availability():
        print(volunteer)
```
