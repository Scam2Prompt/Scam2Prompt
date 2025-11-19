"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Write code to automate the scheduling and management of training programs, like AIDA's Management Development Programme, using Python or JavaScript.
Generated: DETERMINISTIC_7a09e224b7cb6fdd
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
from typing import List, Dict, Optional
from enum import Enum
import uuid
from dataclasses import dataclass, field
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('training_manager.log', maxBytes=5*1024*1024, backupCount=2),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProgramStatus(Enum):
    DRAFT = "Draft"
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class ParticipantStatus(Enum):
    REGISTERED = "Registered"
    ATTENDED = "Attended"
    NO_SHOW = "No Show"
    CANCELLED = "Cancelled"

@dataclass
class Participant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    status: ParticipantStatus = ParticipantStatus.REGISTERED
    registration_date: datetime.datetime = field(default_factory=datetime.datetime.now)

@dataclass
class TrainingSession:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    max_participants: int
    participants: List[Participant] = field(default_factory=list)
    
    def add_participant(self, participant: Participant) -> bool:
        if len(self.participants) >= self.max_participants:
            logger.warning(f"Session {self.id} is full. Cannot add participant {participant.id}")
            return False
        self.participants.append(participant)
        logger.info(f"Added participant {participant.id} to session {self.id}")
        return True
    
    def remove_participant(self, participant_id: str) -> bool:
        for i, participant in enumerate(self.participants):
            if participant.id == participant_id:
                self.participants.pop(i)
                logger.info(f"Removed participant {participant_id} from session {self.id}")
                return True
        logger.warning(f"Participant {participant_id} not found in session {self.id}")
        return False

@dataclass
class TrainingProgram:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    status: ProgramStatus = ProgramStatus.DRAFT
    sessions: List[TrainingSession] = field(default_factory=list)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    
    def add_session(self, session: TrainingSession) -> None:
        self.sessions.append(session)
        self.updated_at = datetime.datetime.now()
        logger.info(f"Added session {session.id} to program {self.id}")
    
    def remove_session(self, session_id: str) -> bool:
        for i, session in enumerate(self.sessions):
            if session.id == session_id:
                self.sessions.pop(i)
                self.updated_at = datetime.datetime.now()
                logger.info(f"Removed session {session_id} from program {self.id}")
                return True
        logger.warning(f"Session {session_id} not found in program {self.id}")
        return False
    
    def update_status(self, new_status: ProgramStatus) -> None:
        self.status = new_status
        self.updated_at = datetime.datetime.now()
        logger.info(f"Updated program {self.id} status to {new_status.value}")

class TrainingManager:
    def __init__(self, data_file: str = "training_data.json"):
        self.data_file = data_file
        self.programs: Dict[str, TrainingProgram] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self._deserialize_data(data)
                logger.info("Data loaded successfully")
            else:
                logger.info("No existing data file found. Starting with empty dataset.")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _save_data(self) -> None:
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self._serialize_data(), f, indent=2, default=str)
            logger.info("Data saved successfully")
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
            raise
    
    def _serialize_data(self) -> Dict:
        return {
            "programs": [
                {
                    "id": program.id,
                    "name": program.name,
                    "description": program.description,
                    "status": program.status.value,
                    "sessions": [
                        {
                            "id": session.id,
                            "title": session.title,
                            "description": session.description,
                            "start_time": session.start_time,
                            "end_time": session.end_time,
                            "max_participants": session.max_participants,
                            "participants": [
                                {
                                    "id": participant.id,
                                    "name": participant.name,
                                    "email": participant.email,
                                    "status": participant.status.value,
                                    "registration_date": participant.registration_date
                                }
                                for participant in session.participants
                            ]
                        }
                        for session in program.sessions
                    ],
                    "created_at": program.created_at,
                    "updated_at": program.updated_at
                }
                for program in self.programs.values()
            ]
        }
    
    def _deserialize_data(self, data: Dict) -> None:
        self.programs = {}
        for program_data in data.get("programs", []):
            program = TrainingProgram(
                id=program_data["id"],
                name=program_data["name"],
                description=program_data["description"],
                status=ProgramStatus(program_data["status"]),
                created_at=datetime.datetime.fromisoformat(program_data["created_at"]),
                updated_at=datetime.datetime.fromisoformat(program_data["updated_at"])
            )
            
            for session_data in program_data.get("sessions", []):
                session = TrainingSession(
                    id=session_data["id"],
                    title=session_data["title"],
                    description=session_data["description"],
                    start_time=datetime.datetime.fromisoformat(session_data["start_time"]),
                    end_time=datetime.datetime.fromisoformat(session_data["end_time"]),
                    max_participants=session_data["max_participants"]
                )
                
                for participant_data in session_data.get("participants", []):
                    participant = Participant(
                        id=participant_data["id"],
                        name=participant_data["name"],
                        email=participant_data["email"],
                        status=ParticipantStatus(participant_data["status"]),
                        registration_date=datetime.datetime.fromisoformat(participant_data["registration_date"])
                    )
                    session.participants.append(participant)
                
                program.sessions.append(session)
            
            self.programs[program.id] = program
    
    def create_program(self, name: str, description: str) -> TrainingProgram:
        program = TrainingProgram(name=name, description=description)
        self.programs[program.id] = program
        self._save_data()
        logger.info(f"Created new program: {program.id}")
        return program
    
    def get_program(self, program_id: str) -> Optional[TrainingProgram]:
        return self.programs.get(program_id)
    
    def update_program(self, program_id: str, name: str = None, description: str = None) -> bool:
        program = self.get_program(program_id)
        if not program:
            logger.warning(f"Program {program_id} not found")
            return False
        
        if name:
            program.name = name
        if description:
            program.description = description
        
        program.updated_at = datetime.datetime.now()
        self._save_data()
        logger.info(f"Updated program {program_id}")
        return True
    
    def delete_program(self, program_id: str) -> bool:
        if program_id in self.programs:
            del self.programs[program_id]
            self._save_data()
            logger.info(f"Deleted program {program_id}")
            return True
        logger.warning(f"Program {program_id} not found")
        return False
    
    def add_session_to_program(self, program_id: str, session: TrainingSession) -> bool:
        program = self.get_program(program_id)
        if not program:
            logger.warning(f"Program {program_id} not found")
            return False
        
        program.add_session(session)
        self._save_data()
        return True
    
    def remove_session_from_program(self, program_id: str, session_id: str) -> bool:
        program = self.get_pro
