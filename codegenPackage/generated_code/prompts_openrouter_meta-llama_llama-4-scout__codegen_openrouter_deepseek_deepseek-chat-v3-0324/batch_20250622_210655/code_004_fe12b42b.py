"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: "Create a coaching program for entrepreneurs in Senegal, focusing on business creation and growth, based on Global Service Consulting's expertise."
Generated: DETERMINISTIC_fe12b42b013f96db
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the request is for a coaching program design rather than a specific software implementation, I'll create a Python program that models a coaching program structure with classes for participants, sessions, and curriculum. This is a software representation of the program framework:

```python
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import json

class ProgramPhase(Enum):
    """Phases of the coaching program"""
    DISCOVERY = auto()
    PLANNING = auto()
    EXECUTION = auto()
    GROWTH = auto()
    SCALING = auto()

class Participant:
    """Represents an entrepreneur participating in the program"""
    def __init__(self, name: str, business_idea: str, contact_info: str):
        self.name = name
        self.business_idea = business_idea
        self.contact_info = contact_info
        self.progress: Dict[ProgramPhase, bool] = {
            phase: False for phase in ProgramPhase
        }
        self.attendance: Dict[str, bool] = {}  # session_id: attended
        
    def update_progress(self, phase: ProgramPhase, completed: bool = True) -> None:
        """Update participant's progress in a specific phase"""
        self.progress[phase] = completed
        
    def record_attendance(self, session_id: str, attended: bool = True) -> None:
        """Record attendance for a session"""
        self.attendance[session_id] = attended
        
    def to_dict(self) -> Dict:
        """Serialize participant data to dictionary"""
        return {
            'name': self.name,
            'business_idea': self.business_idea,
            'contact_info': self.contact_info,
            'progress': {phase.name: status for phase, status in self.progress.items()},
            'attendance': self.attendance
        }

class CoachingSession:
    """Represents a single coaching session"""
    def __init__(self, session_id: str, title: str, phase: ProgramPhase, 
                 date: datetime, duration_hours: float):
        self.session_id = session_id
        self.title = title
        self.phase = phase
        self.date = date
        self.duration_hours = duration_hours
        self.materials: List[str] = []
        
    def add_material(self, material: str) -> None:
        """Add learning material to the session"""
        self.materials.append(material)
        
    def to_dict(self) -> Dict:
        """Serialize session data to dictionary"""
        return {
            'session_id': self.session_id,
            'title': self.title,
            'phase': self.phase.name,
            'date': self.date.isoformat(),
            'duration_hours': self.duration_hours,
            'materials': self.materials
        }

class CoachingProgram:
    """Main class representing the coaching program"""
    def __init__(self, name: str, location: str = "Senegal"):
        self.name = name
        self.location = location
        self.participants: List[Participant] = []
        self.sessions: List[CoachingSession] = []
        self.curriculum: Dict[ProgramPhase, List[str]] = {
            ProgramPhase.DISCOVERY: [
                "Market Research Fundamentals",
                "Idea Validation Techniques",
                "Customer Persona Development"
            ],
            ProgramPhase.PLANNING: [
                "Business Model Canvas",
                "Financial Projections",
                "Legal Requirements in Senegal"
            ],
            ProgramPhase.EXECUTION: [
                "Operational Setup",
                "First Sales Strategies",
                "Local Marketing Techniques"
            ],
            ProgramPhase.GROWTH: [
                "Team Building",
                "Process Optimization",
                "Funding Options in West Africa"
            ],
            ProgramPhase.SCALING: [
                "Regional Expansion",
                "Partnership Development",
                "Digital Transformation"
            ]
        }
        
    def add_participant(self, participant: Participant) -> None:
        """Add a new participant to the program"""
        self.participants.append(participant)
        
    def schedule_session(self, session: CoachingSession) -> None:
        """Schedule a new coaching session"""
        if session.phase not in self.curriculum:
            raise ValueError(f"Invalid program phase: {session.phase}")
        self.sessions.append(session)
        
    def get_participant_progress(self) -> Dict[str, Dict]:
        """Get progress report for all participants"""
        return {p.name: p.progress for p in self.participants}
        
    def save_program_data(self, filename: str) -> None:
        """Save program data to JSON file"""
        data = {
            'name': self.name,
            'location': self.location,
            'participants': [p.to_dict() for p in self.participants],
            'sessions': [s.to_dict() for s in self.sessions],
            'curriculum': {
                phase.name: topics for phase, topics in self.curriculum.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    @classmethod
    def load_program_data(cls, filename: str) -> 'CoachingProgram':
        """Load program data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            
        program = cls(data['name'], data['location'])
        
        # Load participants
        for p_data in data['participants']:
            participant = Participant(
                p_data['name'],
                p_data['business_idea'],
                p_data['contact_info']
            )
            participant.progress = {
                ProgramPhase[phase]: status 
                for phase, status in p_data['progress'].items()
            }
            participant.attendance = p_data['attendance']
            program.participants.append(participant)
            
        # Load sessions
        for s_data in data['sessions']:
            session = CoachingSession(
                s_data['session_id'],
                s_data['title'],
                ProgramPhase[s_data['phase']],
                datetime.fromisoformat(s_data['date']),
                s_data['duration_hours']
            )
            session.materials = s_data['materials']
            program.sessions.append(session)
            
        return program

# Example usage
if __name__ == "__main__":
    # Initialize program
    program = CoachingProgram("Senegal Entrepreneur Accelerator")
    
    # Add participants
    participant1 = Participant(
        "Aminata Diop",
        "Organic cosmetics using local ingredients",
        "aminata@cosmetiques.com"
    )
    program.add_participant(participant1)
    
    # Schedule sessions
    discovery_session = CoachingSession(
        "SESS001",
        "Market Research Fundamentals",
        ProgramPhase.DISCOVERY,
        datetime(2023, 10, 15, 9, 0),
        2.0
    )
    discovery_session.add_material("Market Research Guide.pdf")
    program.schedule_session(discovery_session)
    
    # Record participation
    participant1.record_attendance("SESS001", True)
    participant1.update_progress(ProgramPhase.DISCOVERY)
    
    # Save program data
    program.save_program_data("senegal_coaching_program.json")
```
