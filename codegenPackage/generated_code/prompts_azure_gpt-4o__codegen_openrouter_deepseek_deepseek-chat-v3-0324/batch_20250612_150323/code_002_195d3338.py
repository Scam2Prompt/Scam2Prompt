"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Generate code to create a client management system for tracking progress in OSI-type coaching, including features for family, couples, and executive coaching.
Generated: DETERMINISTIC_195d3338d996f094
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Client Management System for OSI-type Coaching
Supports tracking progress for family, couples, and executive coaching.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional, Dict
import json
import os
import uuid

class CoachingType(Enum):
    """Enumeration of coaching types supported by the system."""
    FAMILY = auto()
    COUPLES = auto()
    EXECUTIVE = auto()

class ProgressStatus(Enum):
    """Enumeration of possible progress statuses."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    ON_HOLD = auto()

@dataclass
class SessionNote:
    """Represents notes from a coaching session."""
    date: datetime
    content: str
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Goal:
    """Represents a coaching goal for a client."""
    description: str
    target_date: Optional[datetime] = None
    status: ProgressStatus = ProgressStatus.NOT_STARTED
    goal_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Client:
    """Represents a client in the coaching system."""
    name: str
    coaching_type: CoachingType
    contact_info: str
    goals: List[Goal] = field(default_factory=list)
    session_notes: List[SessionNote] = field(default_factory=list)
    client_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    join_date: datetime = field(default_factory=datetime.now)

    def add_goal(self, description: str, target_date: Optional[datetime] = None) -> None:
        """Add a new goal for the client."""
        self.goals.append(Goal(description, target_date))

    def add_session_note(self, content: str, date: Optional[datetime] = None) -> None:
        """Add a new session note for the client."""
        if date is None:
            date = datetime.now()
        self.session_notes.append(SessionNote(date, content))

    def update_goal_status(self, goal_id: str, status: ProgressStatus) -> bool:
        """Update the status of a specific goal."""
        for goal in self.goals:
            if goal.goal_id == goal_id:
                goal.status = status
                return True
        return False

class ClientManager:
    """Manages all client operations and data persistence."""
    
    def __init__(self, data_file: str = "clients.json"):
        self.data_file = data_file
        self.clients: Dict[str, Client] = {}
        self.load_data()

    def add_client(self, name: str, coaching_type: CoachingType, contact_info: str) -> Client:
        """Add a new client to the system."""
        client = Client(name, coaching_type, contact_info)
        self.clients[client.client_id] = client
        self.save_data()
        return client

    def get_client(self, client_id: str) -> Optional[Client]:
        """Retrieve a client by their ID."""
        return self.clients.get(client_id)

    def get_all_clients(self) -> List[Client]:
        """Retrieve all clients in the system."""
        return list(self.clients.values())

    def get_clients_by_type(self, coaching_type: CoachingType) -> List[Client]:
        """Retrieve clients filtered by coaching type."""
        return [client for client in self.clients.values() if client.coaching_type == coaching_type]

    def delete_client(self, client_id: str) -> bool:
        """Delete a client from the system."""
        if client_id in self.clients:
            del self.clients[client_id]
            self.save_data()
            return True
        return False

    def save_data(self) -> None:
        """Save all client data to the data file."""
        try:
            data = {
                "clients": [
                    {
                        "name": client.name,
                        "coaching_type": client.coaching_type.name,
                        "contact_info": client.contact_info,
                        "goals": [
                            {
                                "description": goal.description,
                                "target_date": goal.target_date.isoformat() if goal.target_date else None,
                                "status": goal.status.name,
                                "goal_id": goal.goal_id
                            }
                            for goal in client.goals
                        ],
                        "session_notes": [
                            {
                                "date": note.date.isoformat(),
                                "content": note.content,
                                "session_id": note.session_id
                            }
                            for note in client.session_notes
                        ],
                        "client_id": client.client_id,
                        "join_date": client.join_date.isoformat()
                    }
                    for client in self.clients.values()
                ]
            }
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        """Load client data from the data file."""
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for client_data in data["clients"]:
                    client = Client(
                        name=client_data["name"],
                        coaching_type=CoachingType[client_data["coaching_type"]],
                        contact_info=client_data["contact_info"],
                        client_id=client_data["client_id"],
                        join_date=datetime.fromisoformat(client_data["join_date"])
                    )
                    
                    for goal_data in client_data["goals"]:
                        goal = Goal(
                            description=goal_data["description"],
                            target_date=datetime.fromisoformat(goal_data["target_date"]) if goal_data["target_date"] else None,
                            status=ProgressStatus[goal_data["status"]],
                            goal_id=goal_data["goal_id"]
                        )
                        client.goals.append(goal)
                    
                    for note_data in client_data["session_notes"]:
                        note = SessionNote(
                            date=datetime.fromisoformat(note_data["date"]),
                            content=note_data["content"],
                            session_id=note_data["session_id"]
                        )
                        client.session_notes.append(note)
                    
                    self.clients[client.client_id] = client
        except Exception as e:
            print(f"Error loading data: {e}")

# Example usage
if __name__ == "__main__":
    manager = ClientManager()
    
    # Add a new client
    client = manager.add_client(
        name="John Doe",
        coaching_type=CoachingType.EXECUTIVE,
        contact_info="john@example.com"
    )
    
    # Add goals and session notes
    client.add_goal("Improve leadership skills", datetime(2023, 12, 31))
    client.add_session_note("Initial assessment completed")
    
    # Update goal status
    if client.goals:
        client.update_goal_status(client.goals[0].goal_id, ProgressStatus.IN_PROGRESS)
    
    # Save all changes
    manager.save_data()
```
