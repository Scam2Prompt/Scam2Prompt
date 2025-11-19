"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write Python code to simulate a community-based initiative that improves literacy and numeracy skills, inspired by the NICER Foundation's mission to equip educators and students for the fourth industrial revolution.
Generated: DETERMINISTIC_110e0653eef4292e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

class Participant:
    """Represents a participant in the literacy and numeracy program."""
    
    def __init__(self, participant_id: int, name: str, age: int, skill_level: str):
        """
        Initialize a participant with basic information.
        
        Args:
            participant_id: Unique identifier for the participant
            name: Full name of the participant
            age: Age of the participant
            skill_level: Initial skill level (e.g., 'beginner', 'intermediate', 'advanced')
        """
        self.participant_id = participant_id
        self.name = name
        self.age = age
        self.skill_level = skill_level
        self.enrolled_date = datetime.now()
        self.progress = []
        self.attendance = {}
    
    def add_progress(self, date: datetime, skill: str, improvement: float) -> None:
        """
        Record progress in a specific skill.
        
        Args:
            date: Date of progress recording
            skill: Skill being measured (e.g., 'literacy', 'numeracy')
            improvement: Percentage improvement (0-100)
        """
        if not 0 <= improvement <= 100:
            raise ValueError("Improvement must be between 0 and 100")
            
        self.progress.append({
            'date': date,
            'skill': skill,
            'improvement': improvement
        })
    
    def record_attendance(self, date: datetime, attended: bool) -> None:
        """
        Record attendance for a session.
        
        Args:
            date: Date of the session
            attended: Whether the participant attended
        """
        self.attendance[date] = attended
    
    def calculate_attendance_rate(self) -> float:
        """Calculate the attendance rate as a percentage."""
        if not self.attendance:
            return 0.0
        attended = sum(1 for attended in self.attendance.values() if attended)
        return (attended / len(self.attendance)) * 100
    
    def to_dict(self) -> Dict:
        """Convert participant data to a dictionary for serialization."""
        return {
            'participant_id': self.participant_id,
            'name': self.name,
            'age': self.age,
            'skill_level': self.skill_level,
            'enrolled_date': self.enrolled_date.isoformat(),
            'progress': [{
                'date': p['date'].isoformat(),
                'skill': p['skill'],
                'improvement': p['improvement']
            } for p in self.progress],
            'attendance': {k.isoformat(): v for k, v in self.attendance.items()}
        }

class Educator:
    """Represents an educator in the program."""
    
    def __init__(self, educator_id: int, name: str, expertise: List[str]):
        """
        Initialize an educator with basic information.
        
        Args:
            educator_id: Unique identifier for the educator
            name: Full name of the educator
            expertise: List of skills the educator specializes in
        """
        self.educator_id = educator_id
        self.name = name
        self.expertise = expertise
        self.assigned_participants = []
    
    def assign_participant(self, participant_id: int) -> None:
        """Assign a participant to this educator."""
        if participant_id not in self.assigned_participants:
            self.assigned_participants.append(participant_id)
    
    def to_dict(self) -> Dict:
        """Convert educator data to a dictionary for serialization."""
        return {
            'educator_id': self.educator_id,
            'name': self.name,
            'expertise': self.expertise,
            'assigned_participants': self.assigned_participants
        }

class LearningSession:
    """Represents a learning session in the program."""
    
    def __init__(self, session_id: int, date: datetime, skill: str, educator_id: int):
        """
        Initialize a learning session.
        
        Args:
            session_id: Unique identifier for the session
            date: Date and time of the session
            skill: Skill being taught
            educator_id: ID of the educator leading the session
        """
        self.session_id = session_id
        self.date = date
        self.skill = skill
        self.educator_id = educator_id
        self.attending_participants = []
    
    def add_participant(self, participant_id: int) -> None:
        """Add a participant to the session."""
        if participant_id not in self.attending_participants:
            self.attending_participants.append(participant_id)
    
    def to_dict(self) -> Dict:
        """Convert session data to a dictionary for serialization."""
        return {
            'session_id': self.session_id,
            'date': self.date.isoformat(),
            'skill': self.skill,
            'educator_id': self.educator_id,
            'attending_participants': self.attending_participants
        }

class CommunityProgram:
    """Main class representing the community literacy and numeracy program."""
    
    def __init__(self, name: str):
        """
        Initialize the community program.
        
        Args:
            name: Name of the program
        """
        self.name = name
        self.participants = {}
        self.educators = {}
        self.sessions = {}
        self.next_participant_id = 1
        self.next_educator_id = 1
        self.next_session_id = 1
    
    def add_participant(self, name: str, age: int, skill_level: str) -> int:
        """
        Add a new participant to the program.
        
        Args:
            name: Full name of the participant
            age: Age of the participant
            skill_level: Initial skill level
            
        Returns:
            The assigned participant ID
        """
        participant_id = self.next_participant_id
        self.participants[participant_id] = Participant(
            participant_id=participant_id,
            name=name,
            age=age,
            skill_level=skill_level
        )
        self.next_participant_id += 1
        return participant_id
    
    def add_educator(self, name: str, expertise: List[str]) -> int:
        """
        Add a new educator to the program.
        
        Args:
            name: Full name of the educator
            expertise: List of skills the educator specializes in
            
        Returns:
            The assigned educator ID
        """
        educator_id = self.next_educator_id
        self.educators[educator_id] = Educator(
            educator_id=educator_id,
            name=name,
            expertise=expertise
        )
        self.next_educator_id += 1
        return educator_id
    
    def create_session(self, date: datetime, skill: str, educator_id: int) -> int:
        """
        Create a new learning session.
        
        Args:
            date: Date and time of the session
            skill: Skill being taught
            educator_id: ID of the educator leading the session
            
        Returns:
            The assigned session ID
        """
        if educator_id not in self.educators:
            raise ValueError("Educator not found")
            
        session_id = self.next_session_id
        self.sessions[session_id] = LearningSession(
            session_id=session_id,
            date=date,
            skill=skill,
            educator_id=educator_id
        )
        self.next_session_id += 1
        return session_id
    
    def enroll_participant_in_session(self, participant_id: int, session_id: int) -> None:
        """
        Enroll a participant in a session.
        
        Args:
            participant_id: ID of the participant
            session_id: ID of the session
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
        if session_id not in self.sessions:
            raise ValueError("Session not found")
            
        self.sessions[session_id].add_participant(participant_id)
        self.participants[participant_id].record_attendance(
            self.sessions[session_id].date,
            True
        )
    
    def record_progress(self, participant_id: int, skill: str, improvement: float) -> None:
        """
        Record progress for a participant.
        
        Args:
            participant_id: ID of the participant
            skill: Skill being measured
            improvement: Percentage improvement
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
            
        self.participants[participant_id].add_progress(
            date=datetime.now(),
            skill=skill,
            improvement=improvement
        )
    
    def assign_educator_to_participant(self, educator_id: int, participant_id: int) -> None:
        """
        Assign an educator to a participant for mentorship.
        
        Args:
            educator_id: ID of the educator
            participant_id: ID of the participant
        """
        if educator_id not in self.ed
