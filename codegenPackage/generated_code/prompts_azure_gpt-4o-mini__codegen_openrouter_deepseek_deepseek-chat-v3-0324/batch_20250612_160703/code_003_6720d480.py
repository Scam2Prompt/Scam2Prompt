"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Develop a code snippet that organizes training sessions for young leaders, utilizing the concepts introduced in the UngLeder Norway program.
Generated: DETERMINISTIC_6720d48003178f99
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
Training Session Organizer for Young Leaders - Inspired by UngLeder Norway Program
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
import random

class TrainingSession:
    """Represents a single training session for young leaders."""
    
    def __init__(self, title: str, description: str, duration_hours: float, 
                 max_participants: int, required_skills: List[str] = None):
        """
        Initialize a training session.
        
        Args:
            title: Title of the session
            description: Description of session content
            duration_hours: Length of session in hours
            max_participants: Maximum number of participants
            required_skills: List of required skills (optional)
        """
        self.title = title
        self.description = description
        self.duration = timedelta(hours=duration_hours)
        self.max_participants = max_participants
        self.required_skills = required_skills or []
        self.participants = []
        self.scheduled_time = None
    
    def schedule(self, start_time: datetime) -> bool:
        """Schedule the session at a specific time."""
        if start_time < datetime.now():
            return False
        self.scheduled_time = start_time
        return True
    
    def add_participant(self, participant: 'Participant') -> bool:
        """Add a participant to the session if requirements are met and space available."""
        if (len(self.participants) >= self.max_participants or
            not all(skill in participant.skills for skill in self.required_skills)):
            return False
        self.participants.append(participant)
        return True
    
    def to_dict(self) -> Dict:
        """Convert session data to dictionary for serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'duration_hours': self.duration.total_seconds() / 3600,
            'max_participants': self.max_participants,
            'required_skills': self.required_skills,
            'participants': [p.to_dict() for p in self.participants],
            'scheduled_time': self.scheduled_time.isoformat() if self.scheduled_time else None
        }

class Participant:
    """Represents a participant in the leadership program."""
    
    def __init__(self, name: str, age: int, skills: List[str], experience_level: str):
        """
        Initialize a participant.
        
        Args:
            name: Participant's name
            age: Participant's age
            skills: List of skills the participant has
            experience_level: Experience level (beginner, intermediate, advanced)
        """
        self.name = name
        self.age = age
        self.skills = skills
        self.experience_level = experience_level
    
    def to_dict(self) -> Dict:
        """Convert participant data to dictionary for serialization."""
        return {
            'name': self.name,
            'age': self.age,
            'skills': self.skills,
            'experience_level': self.experience_level
        }

class TrainingProgram:
    """Manages a collection of training sessions and participants."""
    
    def __init__(self):
        self.sessions = []
        self.participants = []
    
    def add_session(self, session: TrainingSession) -> None:
        """Add a training session to the program."""
        self.sessions.append(session)
    
    def register_participant(self, participant: Participant) -> None:
        """Register a participant in the program."""
        self.participants.append(participant)
    
    def find_compatible_sessions(self, participant: Participant) -> List[TrainingSession]:
        """Find sessions that match a participant's skills and have available spots."""
        return [
            session for session in self.sessions
            if (all(skill in participant.skills for skill in session.required_skills) and
                len(session.participants) < session.max_participants)
        ]
    
    def schedule_random_session(self, session: TrainingSession) -> bool:
        """Schedule a session at a random future time within the next 30 days."""
        if session.scheduled_time:
            return False
        
        now = datetime.now()
        random_days = random.randint(1, 30)
        random_hours = random.randint(9, 17)  # Business hours
        start_time = now + timedelta(days=random_days)
        start_time = start_time.replace(hour=random_hours, minute=0, second=0, microsecond=0)
        
        return session.schedule(start_time)
    
    def save_to_file(self, filename: str) -> bool:
        """Save the entire program data to a JSON file."""
        try:
            data = {
                'sessions': [s.to_dict() for s in self.sessions],
                'participants': [p.to_dict() for p in self.participants]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load program data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.sessions = []
            self.participants = []
            
            for session_data in data['sessions']:
                session = TrainingSession(
                    title=session_data['title'],
                    description=session_data['description'],
                    duration_hours=session_data['duration_hours'],
                    max_participants=session_data['max_participants'],
                    required_skills=session_data['required_skills']
                )
                if session_data['scheduled_time']:
                    session.schedule(datetime.fromisoformat(session_data['scheduled_time']))
                self.sessions.append(session)
            
            for participant_data in data['participants']:
                participant = Participant(
                    name=participant_data['name'],
                    age=participant_data['age'],
                    skills=participant_data['skills'],
                    experience_level=participant_data['experience_level']
                )
                self.participants.append(participant)
            
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    program = TrainingProgram()
    
    # Create some sessions
    session1 = TrainingSession(
        title="Effective Communication",
        description="Learn how to communicate clearly and persuasively",
        duration_hours=2.5,
        max_participants=15,
        required_skills=["basic communication"]
    )
    
    session2 = TrainingSession(
        title="Team Leadership",
        description="Develop skills to lead and motivate teams",
        duration_hours=3,
        max_participants=10,
        required_skills=["basic leadership", "communication"]
    )
    
    program.add_session(session1)
    program.add_session(session2)
    
    # Register participants
    participant1 = Participant(
        name="Alice",
        age=18,
        skills=["basic communication", "teamwork"],
        experience_level="beginner"
    )
    
    participant2 = Participant(
        name="Bob",
        age=20,
        skills=["basic communication", "basic leadership", "problem solving"],
        experience_level="intermediate"
    )
    
    program.register_participant(participant1)
    program.register_participant(participant2)
    
    # Schedule sessions
    program.schedule_random_session(session1)
    program.schedule_random_session(session2)
    
    # Enroll participants
    for participant in program.participants:
        compatible_sessions = program.find_compatible_sessions(participant)
        for session in compatible_sessions:
            session.add_participant(participant)
    
    # Save program data
    program.save_to_file("leadership_program.json")
```
