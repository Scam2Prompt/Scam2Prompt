"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Write a program to manage athlete training schedules for a football mentorship program like DGA.
Generated: DETERMINISTIC_c5daaa3203227f46
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class Athlete:
    """Represents an athlete in the training program."""
    
    def __init__(self, name: str, age: int, position: str, contact: str):
        """
        Initialize an Athlete instance.
        
        Args:
            name: Full name of the athlete
            age: Age of the athlete
            position: Football position (e.g., 'Forward', 'Midfielder')
            contact: Contact information (email or phone)
        """
        self.name = name
        self.age = age
        self.position = position
        self.contact = contact
        self.training_sessions = []
    
    def add_training_session(self, session: 'TrainingSession') -> None:
        """Add a training session to the athlete's schedule."""
        self.training_sessions.append(session)
    
    def remove_training_session(self, session_id: str) -> bool:
        """Remove a training session by ID."""
        for i, session in enumerate(self.training_sessions):
            if session.session_id == session_id:
                del self.training_sessions[i]
                return True
        return False
    
    def get_upcoming_sessions(self) -> List['TrainingSession']:
        """Return all upcoming training sessions."""
        now = datetime.now()
        return [s for s in self.training_sessions if s.start_time > now]
    
    def to_dict(self) -> Dict:
        """Convert athlete data to dictionary for serialization."""
        return {
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'contact': self.contact,
            'training_sessions': [s.to_dict() for s in self.training_sessions]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Athlete':
        """Create Athlete instance from dictionary."""
        athlete = cls(
            name=data['name'],
            age=data['age'],
            position=data['position'],
            contact=data['contact']
        )
        athlete.training_sessions = [
            TrainingSession.from_dict(s) for s in data.get('training_sessions', [])
        ]
        return athlete

class TrainingSession:
    """Represents a training session for athletes."""
    
    def __init__(self, session_id: str, name: str, start_time: datetime, 
                 duration: int, location: str, coach: str):
        """
        Initialize a TrainingSession instance.
        
        Args:
            session_id: Unique identifier for the session
            name: Name/description of the session
            start_time: Datetime when session starts
            duration: Duration in minutes
            location: Training location
            coach: Coach leading the session
        """
        self.session_id = session_id
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.location = location
        self.coach = coach
    
    @property
    def end_time(self) -> datetime:
        """Calculate and return the session end time."""
        return self.start_time + timedelta(minutes=self.duration)
    
    def to_dict(self) -> Dict:
        """Convert session data to dictionary for serialization."""
        return {
            'session_id': self.session_id,
            'name': self.name,
            'start_time': self.start_time.isoformat(),
            'duration': self.duration,
            'location': self.location,
            'coach': self.coach
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TrainingSession':
        """Create TrainingSession instance from dictionary."""
        return cls(
            session_id=data['session_id'],
            name=data['name'],
            start_time=datetime.fromisoformat(data['start_time']),
            duration=data['duration'],
            location=data['location'],
            coach=data['coach']
        )

class TrainingProgram:
    """Manages athletes and their training schedules."""
    
    def __init__(self):
        """Initialize the training program with empty athletes list."""
        self.athletes = []
    
    def add_athlete(self, athlete: Athlete) -> None:
        """Add an athlete to the program."""
        self.athletes.append(athlete)
    
    def remove_athlete(self, name: str) -> bool:
        """Remove an athlete by name."""
        for i, athlete in enumerate(self.athletes):
            if athlete.name == name:
                del self.athletes[i]
                return True
        return False
    
    def get_athlete(self, name: str) -> Optional[Athlete]:
        """Get an athlete by name."""
        for athlete in self.athletes:
            if athlete.name == name:
                return athlete
        return None
    
    def schedule_session(self, athlete_name: str, session: TrainingSession) -> bool:
        """Schedule a training session for an athlete."""
        athlete = self.get_athlete(athlete_name)
        if athlete:
            athlete.add_training_session(session)
            return True
        return False
    
    def cancel_session(self, athlete_name: str, session_id: str) -> bool:
        """Cancel a training session for an athlete."""
        athlete = self.get_athlete(athlete_name)
        if athlete:
            return athlete.remove_training_session(session_id)
        return False
    
    def get_upcoming_sessions(self) -> Dict[str, List[TrainingSession]]:
        """Get all upcoming sessions for all athletes."""
        return {
            athlete.name: athlete.get_upcoming_sessions() 
            for athlete in self.athletes
        }
    
    def save_to_file(self, filename: str) -> bool:
        """Save program data to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {'athletes': [a.to_dict() for a in self.athletes]},
                    f,
                    indent=2
                )
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load program data from JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.athletes = [
                    Athlete.from_dict(a) for a in data.get('athletes', [])
                ]
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create program instance
    program = TrainingProgram()
    
    # Add athletes
    athlete1 = Athlete("John Doe", 18, "Forward", "john@example.com")
    athlete2 = Athlete("Jane Smith", 17, "Midfielder", "jane@example.com")
    program.add_athlete(athlete1)
    program.add_athlete(athlete2)
    
    # Schedule training sessions
    session1 = TrainingSession(
        "s001",
        "Speed Training",
        datetime.now() + timedelta(days=1),
        90,
        "Field A",
        "Coach Johnson"
    )
    program.schedule_session("John Doe", session1)
    
    session2 = TrainingSession(
        "s002",
        "Tactical Session",
        datetime.now() + timedelta(days=2),
        120,
        "Field B",
        "Coach Williams"
    )
    program.schedule_session("Jane Smith", session2)
    
    # Save to file
    program.save_to_file("training_program.json")
    
    # Load from file
    new_program = TrainingProgram()
    new_program.load_from_file("training_program.json")
    
    # Print upcoming sessions
    print("Upcoming sessions:")
    for name, sessions in new_program.get_upcoming_sessions().items():
        print(f"\nAthlete: {name}")
        for session in sessions:
            print(f"  - {session.name} at {session.start_time} with {session.coach}")
```
