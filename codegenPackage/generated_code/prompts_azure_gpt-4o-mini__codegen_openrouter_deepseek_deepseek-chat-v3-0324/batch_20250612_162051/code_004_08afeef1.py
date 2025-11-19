"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write a code example that showcases how to manage a digital platform for music rehearsal sessions at the Ferme Bermond, as described by the association.
Generated: DETERMINISTIC_08afeef1bfd4dbcd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Platform for Music Rehearsal Sessions at Ferme Bermond

This module provides functionality to manage music rehearsal sessions,
including scheduling, participant management, and resource allocation.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
import os
from enum import Enum, auto

# Error classes
class SessionError(Exception):
    """Base class for session-related errors."""
    pass

class SessionConflictError(SessionError):
    """Raised when there's a scheduling conflict."""
    pass

class ResourceUnavailableError(SessionError):
    """Raised when requested resources are unavailable."""
    pass

class ParticipantLimitError(SessionError):
    """Raised when participant limit is exceeded."""
    pass

class SessionStatus(Enum):
    """Enum representing session statuses."""
    SCHEDULED = auto()
    ONGOING = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class RehearsalSession:
    """Class representing a music rehearsal session."""
    
    def __init__(self, session_id: str, title: str, start_time: datetime, 
                 duration: timedelta, max_participants: int):
        """
        Initialize a rehearsal session.
        
        Args:
            session_id: Unique identifier for the session
            title: Title/name of the session
            start_time: When the session starts
            duration: How long the session lasts
            max_participants: Maximum number of participants allowed
        """
        self.session_id = session_id
        self.title = title
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration
        self.max_participants = max_participants
        self.participants: List[str] = []
        self.resources: List[str] = []
        self.status = SessionStatus.SCHEDULED
        self.notes: str = ""
    
    def add_participant(self, participant_name: str) -> None:
        """Add a participant to the session."""
        if len(self.participants) >= self.max_participants:
            raise ParticipantLimitError("Session has reached maximum participants")
        if participant_name not in self.participants:
            self.participants.append(participant_name)
    
    def remove_participant(self, participant_name: str) -> None:
        """Remove a participant from the session."""
        if participant_name in self.participants:
            self.participants.remove(participant_name)
    
    def add_resource(self, resource: str) -> None:
        """Add a resource to the session."""
        if resource not in self.resources:
            self.resources.append(resource)
    
    def remove_resource(self, resource: str) -> None:
        """Remove a resource from the session."""
        if resource in self.resources:
            self.resources.remove(resource)
    
    def update_status(self, new_status: SessionStatus) -> None:
        """Update the session status."""
        self.status = new_status
    
    def add_note(self, note: str) -> None:
        """Add notes to the session."""
        self.notes += f"\n{datetime.now().isoformat()}: {note}"
    
    def to_dict(self) -> Dict:
        """Convert session to dictionary for serialization."""
        return {
            "session_id": self.session_id,
            "title": self.title,
            "start_time": self.start_time.isoformat(),
            "duration": self.duration.total_seconds(),
            "end_time": self.end_time.isoformat(),
            "max_participants": self.max_participants,
            "participants": self.participants,
            "resources": self.resources,
            "status": self.status.name,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'RehearsalSession':
        """Create session from dictionary."""
        session = cls(
            session_id=data["session_id"],
            title=data["title"],
            start_time=datetime.fromisoformat(data["start_time"]),
            duration=timedelta(seconds=data["duration"]),
            max_participants=data["max_participants"]
        )
        session.participants = data.get("participants", [])
        session.resources = data.get("resources", [])
        session.status = SessionStatus[data["status"]]
        session.notes = data.get("notes", "")
        return session

class SessionManager:
    """Class to manage all rehearsal sessions."""
    
    def __init__(self, data_file: str = "sessions.json"):
        """
        Initialize the session manager.
        
        Args:
            data_file: Path to JSON file for persistent storage
        """
        self.data_file = data_file
        self.sessions: Dict[str, RehearsalSession] = {}
        self.resources: List[str] = [
            "Main Hall", "Practice Room 1", "Practice Room 2",
            "Drum Kit", "Piano", "PA System", "Microphones"
        ]
        self.load_sessions()
    
    def add_session(self, session: RehearsalSession) -> None:
        """Add a new session after checking for conflicts."""
        self._check_scheduling_conflict(session)
        self._check_resource_availability(session)
        self.sessions[session.session_id] = session
        self.save_sessions()
    
    def _check_scheduling_conflict(self, new_session: RehearsalSession) -> None:
        """Check if new session conflicts with existing ones."""
        for session in self.sessions.values():
            if (new_session.start_time < session.end_time and 
                new_session.end_time > session.start_time):
                raise SessionConflictError(
                    f"Conflict with session {session.session_id} ({session.title})"
                )
    
    def _check_resource_availability(self, session: RehearsalSession) -> None:
        """Check if requested resources are available."""
        for resource in session.resources:
            if resource not in self.resources:
                raise ResourceUnavailableError(f"Resource {resource} does not exist")
            
            for existing_session in self.sessions.values():
                if (resource in existing_session.resources and 
                    session.start_time < existing_session.end_time and 
                    session.end_time > existing_session.start_time):
                    raise ResourceUnavailableError(
                        f"Resource {resource} is already booked"
                    )
    
    def get_session(self, session_id: str) -> Optional[RehearsalSession]:
        """Retrieve a session by ID."""
        return self.sessions.get(session_id)
    
    def cancel_session(self, session_id: str) -> None:
        """Cancel a session."""
        session = self.sessions.get(session_id)
        if session:
            session.update_status(SessionStatus.CANCELLED)
            self.save_sessions()
    
    def get_upcoming_sessions(self) -> List[RehearsalSession]:
        """Get all upcoming sessions."""
        now = datetime.now()
        return [
            session for session in self.sessions.values()
            if session.status == SessionStatus.SCHEDULED and session.start_time > now
        ]
    
    def get_ongoing_sessions(self) -> List[RehearsalSession]:
        """Get all ongoing sessions."""
        now = datetime.now()
        return [
            session for session in self.sessions.values()
            if session.status == SessionStatus.ONGOING or 
               (session.status == SessionStatus.SCHEDULED and 
                session.start_time <= now <= session.end_time)
        ]
    
    def load_sessions(self) -> None:
        """Load sessions from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.sessions = {
                        session_id: RehearsalSession.from_dict(session_data)
                        for session_id, session_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise SessionError(f"Error loading sessions: {str(e)}")
    
    def save_sessions(self) -> None:
        """Save sessions to the data file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(
                    {session_id: session.to_dict() 
                     for session_id, session in self.sessions.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise SessionError(f"Error saving sessions: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize session manager
    manager = SessionManager()
    
    # Create a new session
    session1 = RehearsalSession(
        session_id="sess001",
        title="Jazz Ensemble Rehearsal",
        start_time=datetime.now() + timedelta(days=1),
        duration=timedelta(hours=2),
        max_participants=8
    )
    
    # Add resources and participants
    session1.add_resource("Main Hall")
    session1.add_resource("Piano")
    session1.add_participant("Alice")
    session1.add_participant("Bob")
    
    # Add the session to the manager
    try
