"""
Generated Code Metadata:
========================
Original URL: https://anotherbrilliantidea.com
Prompt: Write code to automate the scheduling of personalized mentorship sessions for businesses, ensuring clear direction and measurable results, as described in the Marketing Mentor Program.
Generated: DETERMINISTIC_3f2917817b41ef06
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
from enum import Enum
import uuid
from dataclasses import dataclass, asdict


class SessionStatus(Enum):
    """Enum representing the status of a mentorship session."""
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    RESCHEDULED = "rescheduled"


@dataclass
class Mentor:
    """Data class representing a mentor."""
    id: str
    name: str
    expertise: List[str]
    availability: Dict[str, List[str]]  # day: [time_slots]
    max_sessions_per_week: int


@dataclass
class Mentee:
    """Data class representing a mentee."""
    id: str
    name: str
    goals: List[str]
    preferred_availability: Dict[str, List[str]]  # day: [time_slots]


@dataclass
class Session:
    """Data class representing a mentorship session."""
    id: str
    mentor_id: str
    mentee_id: str
    date: str  # YYYY-MM-DD
    time: str  # HH:MM
    duration: int  # in minutes
    status: SessionStatus
    goals: List[str]
    notes: Optional[str] = None


class MentorshipScheduler:
    """Class to handle the scheduling of mentorship sessions."""
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the scheduler with data directory."""
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.mentors: Dict[str, Mentor] = self._load_data("mentors.json", Mentor)
        self.mentees: Dict[str, Mentee] = self._load_data("mentees.json", Mentee)
        self.sessions: Dict[str, Session] = self._load_data("sessions.json", Session)
    
    def _load_data(self, filename: str, data_class) -> Dict[str, any]:
        """Load data from JSON file and convert to specified data class."""
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            return {}
        
        with open(filepath, "r") as f:
            data = json.load(f)
        
        result = {}
        for item_id, item_data in data.items():
            if data_class == Session and "status" in item_data:
                item_data["status"] = SessionStatus(item_data["status"])
            result[item_id] = data_class(**item_data)
        
        return result
    
    def _save_data(self, filename: str, data: Dict[str, any]):
        """Save data to JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        serializable_data = {k: asdict(v) if hasattr(v, "__dataclass_fields__") else v 
                            for k, v in data.items()}
        
        with open(filepath, "w") as f:
            json.dump(serializable_data, f, indent=2)
    
    def add_mentor(self, name: str, expertise: List[str], 
                   availability: Dict[str, List[str]], max_sessions_per_week: int) -> str:
        """Add a new mentor to the system."""
        mentor_id = str(uuid.uuid4())
        self.mentors[mentor_id] = Mentor(
            id=mentor_id,
            name=name,
            expertise=expertise,
            availability=availability,
            max_sessions_per_week=max_sessions_per_week
        )
        self._save_data("mentors.json", self.mentors)
        return mentor_id
    
    def add_mentee(self, name: str, goals: List[str], 
                   preferred_availability: Dict[str, List[str]]) -> str:
        """Add a new mentee to the system."""
        mentee_id = str(uuid.uuid4())
        self.mentees[mentee_id] = Mentee(
            id=mentee_id,
            name=name,
            goals=goals,
            preferred_availability=preferred_availability
        )
        self._save_data("mentees.json", self.mentees)
        return mentee_id
    
    def find_compatible_mentors(self, mentee_id: str) -> List[Mentor]:
        """Find mentors compatible with a mentee based on goals and availability."""
        if mentee_id not in self.mentees:
            raise ValueError("Mentee not found")
        
        mentee = self.mentees[mentee_id]
        compatible_mentors = []
        
        for mentor in self.mentors.values():
            # Check if mentor has expertise in mentee's goals
            common_goals = set(mentee.goals) & set(mentor.expertise)
            if not common_goals:
                continue
            
            # Check availability overlap
            common_availability = {}
            for day, mentee_times in mentee.preferred_availability.items():
                if day in mentor.availability:
                    common_times = set(mentee_times) & set(mentor.availability[day])
                    if common_times:
                        common_availability[day] = list(common_times)
            
            if common_availability:
                compatible_mentors.append(mentor)
        
        return compatible_mentors
    
    def schedule_session(self, mentor_id: str, mentee_id: str, date: str, 
                         time: str, duration: int = 60) -> str:
        """Schedule a new mentorship session."""
        if mentor_id not in self.mentors:
            raise ValueError("Mentor not found")
        if mentee_id not in self.mentees:
            raise ValueError("Mentee not found")
        
        # Validate date and time
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            datetime.datetime.strptime(time, "%H:%M")
        except ValueError as e:
            raise ValueError("Invalid date or time format") from e
        
        # Check mentor availability
        mentor = self.mentors[mentor_id]
        day = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A").lower()
        
        if day not in mentor.availability or time not in mentor.availability[day]:
            raise ValueError("Mentor not available at the requested time")
        
        # Check mentor's weekly session limit
        week_start = (datetime.datetime.strptime(date, "%Y-%m-%d") - 
                      datetime.timedelta(days=datetime.datetime.strptime(date, "%Y-%m-%d").weekday()))
        week_start_str = week_start.strftime("%Y-%m-%d")
        
        mentor_sessions_this_week = sum(
            1 for s in self.sessions.values() 
            if s.mentor_id == mentor_id and 
            datetime.datetime.strptime(s.date, "%Y-%m-%d") >= week_start and
            s.status != SessionStatus.CANCELLED
        )
        
        if mentor_sessions_this_week >= mentor.max_sessions_per_week:
            raise ValueError("Mentor has reached weekly session limit")
        
        # Create and save session
        session_id = str(uuid.uuid4())
        mentee = self.mentees[mentee_id]
        
        self.sessions[session_id] = Session(
            id=session_id,
            mentor_id=mentor_id,
            mentee_id=mentee_id,
            date=date,
            time=time,
            duration=duration,
            status=SessionStatus.SCHEDULED,
            goals=mentee.goals
        )
        
        self._save_data("sessions.json", self.sessions)
        return session_id
    
    def update_session_status(self, session_id: str, status: SessionStatus, notes: str = None):
        """Update the status of a session."""
        if session_id not in self.sessions:
            raise ValueError("Session not found")
        
        session = self.sessions[session_id]
        session.status = status
        session.notes = notes
        self._save_data("sessions.json", self.sessions)
    
    def reschedule_session(self, session_id: str, new_date: str, new_time: str):
        """Reschedule an existing session."""
        if session_id not in self.sessions:
            raise ValueError("Session not found")
        
        session = self.sessions[session_id]
        self.update_session_status(session_id, SessionStatus.CANCELLED, "Rescheduled")
        
        # Schedule new session
        new_session_id = self.schedule_session(
            mentor_id=session.mentor_id,
            mentee_id=session.mentee_id,
            date=new_date,
            time=new_time,
            duration=session.duration
        )
        
        # Update goals from original session
        self.sessions[new_session_id].goals = session.goals
        self._save_data("sessions.json", self.sessions)
        
        return new_session_id
    
    def get_upcoming_sessions(self, user_id: str, is_mentor: bool = False) -> List[Session]:
        """Get upcoming sessions for a
