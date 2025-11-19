"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: How can I implement a multi-disciplinary team model in a child neurology clinic, similar to the ICON Foundation's services for ADHD and motor delays?
Generated: DETERMINISTIC_734c0f79cc5c98b0
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module implements a multi-disciplinary team model for a child neurology clinic,
inspired by ICON Foundation's approach for ADHD and motor delays.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import datetime
import uuid

class TeamMemberRole(Enum):
    """Roles of team members in the multi-disciplinary team."""
    NEUROLOGIST = auto()
    PSYCHOLOGIST = auto()
    OCCUPATIONAL_THERAPIST = auto()
    PHYSICAL_THERAPIST = auto()
    SPEECH_THERAPIST = auto()
    SPECIAL_EDUCATOR = auto()
    SOCIAL_WORKER = auto()
    CASE_MANAGER = auto()

@dataclass
class TeamMember:
    """Represents a member of the multi-disciplinary team."""
    id: uuid.UUID
    name: str
    role: TeamMemberRole
    contact_info: str
    availability: List[datetime.time]

@dataclass
class Patient:
    """Represents a patient in the clinic."""
    id: uuid.UUID
    name: str
    age: int
    conditions: List[str]
    case_manager: Optional[uuid.UUID] = None

@dataclass
class Assessment:
    """Represents an assessment conducted by the team."""
    id: uuid.UUID
    patient_id: uuid.UUID
    date: datetime.date
    notes: str
    team_members_involved: List[uuid.UUID]
    recommendations: List[str]

class ClinicTeam:
    """Manages the multi-disciplinary team and patient care coordination."""
    
    def __init__(self):
        self.team_members: List[TeamMember] = []
        self.patients: List[Patient] = []
        self.assessments: List[Assessment] = []
    
    def add_team_member(self, name: str, role: TeamMemberRole, contact_info: str, 
                       availability: List[datetime.time]) -> TeamMember:
        """Add a new member to the team."""
        member = TeamMember(
            id=uuid.uuid4(),
            name=name,
            role=role,
            contact_info=contact_info,
            availability=availability
        )
        self.team_members.append(member)
        return member
    
    def register_patient(self, name: str, age: int, conditions: List[str]) -> Patient:
        """Register a new patient to the clinic."""
        patient = Patient(
            id=uuid.uuid4(),
            name=name,
            age=age,
            conditions=conditions
        )
        self.patients.append(patient)
        return patient
    
    def assign_case_manager(self, patient_id: uuid.UUID, team_member_id: uuid.UUID) -> None:
        """Assign a case manager to a patient."""
        for patient in self.patients:
            if patient.id == patient_id:
                patient.case_manager = team_member_id
                return
        raise ValueError("Patient not found")
    
    def conduct_assessment(self, patient_id: uuid.UUID, team_member_ids: List[uuid.UUID], 
                          notes: str, recommendations: List[str]) -> Assessment:
        """Conduct a multi-disciplinary assessment for a patient."""
        # Validate all team members exist
        for member_id in team_member_ids:
            if not any(m.id == member_id for m in self.team_members):
                raise ValueError(f"Team member with ID {member_id} not found")
        
        # Validate patient exists
        if not any(p.id == patient_id for p in self.patients):
            raise ValueError("Patient not found")
        
        assessment = Assessment(
            id=uuid.uuid4(),
            patient_id=patient_id,
            date=datetime.date.today(),
            notes=notes,
            team_members_involved=team_member_ids,
            recommendations=recommendations
        )
        self.assessments.append(assessment)
        return assessment
    
    def get_patient_assessments(self, patient_id: uuid.UUID) -> List[Assessment]:
        """Get all assessments for a specific patient."""
        return [a for a in self.assessments if a.patient_id == patient_id]
    
    def get_team_members_by_role(self, role: TeamMemberRole) -> List[TeamMember]:
        """Get all team members with a specific role."""
        return [m for m in self.team_members if m.role == role]

# Example usage
if __name__ == "__main__":
    clinic = ClinicTeam()
    
    # Add team members
    neurologist = clinic.add_team_member(
        "Dr. Smith", 
        TeamMemberRole.NEUROLOGIST, 
        "smith@clinic.com", 
        [datetime.time(9, 0), datetime.time(14, 0)]
    )
    
    therapist = clinic.add_team_member(
        "Jane Doe", 
        TeamMemberRole.OCCUPATIONAL_THERAPIST, 
        "jane@clinic.com", 
        [datetime.time(10, 0), datetime.time(15, 0)]
    )
    
    # Register patient
    patient = clinic.register_patient("John Doe", 8, ["ADHD", "Motor Delay"])
    
    # Assign case manager
    clinic.assign_case_manager(patient.id, neurologist.id)
    
    # Conduct assessment
    assessment = clinic.conduct_assessment(
        patient.id,
        [neurologist.id, therapist.id],
        "Initial assessment completed. Shows signs of ADHD and motor coordination issues.",
        [
            "Occupational therapy 2x/week",
            "Behavioral therapy 1x/week",
            "Follow-up in 3 months"
        ]
    )
```
