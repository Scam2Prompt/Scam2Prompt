"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate code to create a flexible scheduling system for Agile training sessions, reflecting CrestAgile's emphasis on accommodating busy lifestyles.
Generated: DETERMINISTIC_558d1e3535529434
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
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator


class SessionStatus(Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class SessionType(Enum):
    WORKSHOP = "Workshop"
    ONE_ON_ONE = "One-on-One"
    GROUP = "Group"
    WEBINAR = "Webinar"


class TimeSlot(BaseModel):
    start_time: datetime.datetime
    end_time: datetime.datetime
    is_booked: bool = False

    @validator('end_time')
    def validate_time_slot(cls, end_time, values):
        if 'start_time' in values and end_time <= values['start_time']:
            raise ValueError("End time must be after start time")
        return end_time


class Trainer(BaseModel):
    id: str
    name: str
    expertise: List[str]
    availability: List[TimeSlot]


class Participant(BaseModel):
    id: str
    name: str
    email: str
    time_preferences: List[datetime.time]


class TrainingSession(BaseModel):
    id: str
    title: str
    description: str
    session_type: SessionType
    trainer: Trainer
    participants: List[Participant]
    time_slot: TimeSlot
    status: SessionStatus = SessionStatus.SCHEDULED
    max_participants: Optional[int] = None

    @validator('participants')
    def validate_participants(cls, participants, values):
        if 'max_participants' in values and values['max_participants'] is not None:
            if len(participants) > values['max_participants']:
                raise ValueError("Number of participants exceeds maximum allowed")
        return participants


class ScheduleSystem:
    def __init__(self):
        self.sessions: Dict[str, TrainingSession] = {}
        self.trainers: Dict[str, Trainer] = {}
        self.participants: Dict[str, Participant] = {}

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer.id in self.trainers:
            raise ValueError("Trainer already exists")
        self.trainers[trainer.id] = trainer

    def add_participant(self, participant: Participant) -> None:
        if participant.id in self.participants:
            raise ValueError("Participant already exists")
        self.participants[participant.id] = participant

    def create_session(self, session: TrainingSession) -> TrainingSession:
        if session.id in self.sessions:
            raise ValueError("Session ID already exists")
        
        # Check trainer availability
        trainer = self.trainers.get(session.trainer.id)
        if not trainer:
            raise ValueError("Trainer not found")
        
        if not any(
            slot.start_time == session.time_slot.start_time and 
            slot.end_time == session.time_slot.end_time and 
            not slot.is_booked
            for slot in trainer.availability
        ):
            raise ValueError("Trainer not available for this time slot")
        
        self.sessions[session.id] = session
        return session

    def cancel_session(self, session_id: str) -> None:
        session = self.sessions.get(session_id)
        if not session:
            raise ValueError("Session not found")
        
        if session.status == SessionStatus.COMPLETED:
            raise ValueError("Cannot cancel completed session")
        
        session.status = SessionStatus.CANCELLED

    def reschedule_session(
        self, 
        session_id: str, 
        new_time_slot: TimeSlot
    ) -> TrainingSession:
        session = self.sessions.get(session_id)
        if not session:
            raise ValueError("Session not found")
        
        if session.status in [SessionStatus.COMPLETED, SessionStatus.CANCELLED]:
            raise ValueError("Cannot reschedule completed or cancelled session")
        
        # Check trainer availability for new time slot
        trainer = self.trainers.get(session.trainer.id)
        if not trainer:
            raise ValueError("Trainer not found")
        
        if not any(
            slot.start_time == new_time_slot.start_time and 
            slot.end_time == new_time_slot.end_time and 
            not slot.is_booked
            for slot in trainer.availability
        ):
            raise ValueError("Trainer not available for new time slot")
        
        session.time_slot = new_time_slot
        return session

    def get_available_sessions(self) -> List[TrainingSession]:
        return [
            session for session in self.sessions.values()
            if session.status == SessionStatus.SCHEDULED
        ]

    def get_participant_sessions(self, participant_id: str) -> List[TrainingSession]:
        return [
            session for session in self.sessions.values()
            if any(p.id == participant_id for p in session.participants)
        ]

    def find_sessions_by_time_range(
        self, 
        start_time: datetime.datetime, 
        end_time: datetime.datetime
    ) -> List[TrainingSession]:
        return [
            session for session in self.sessions.values()
            if session.time_slot.start_time >= start_time and 
               session.time_slot.end_time <= end_time
        ]
```
