"""
Generated Code Metadata:
========================
Original URL: https://www.beardlegalgroup.com
Prompt: Generate a code snippet for a legal case management system that tracks client interactions and case developments, inspired by the client-focused approach of Beard Legal Group.
Generated: DETERMINISTIC_153a11f16c2fb37c
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import json
import uuid

class CaseStatus(Enum):
    """Enum representing the possible statuses of a legal case."""
    OPEN = auto()
    CLOSED = auto()
    PENDING = auto()
    APPEAL = auto()

class InteractionType(Enum):
    """Enum representing types of client interactions."""
    PHONE_CALL = auto()
    EMAIL = auto()
    MEETING = auto()
    COURT_APPEARANCE = auto()
    DOCUMENT_REVIEW = auto()

class Client:
    """Represents a client in the legal case management system."""
    
    def __init__(self, client_id: str, name: str, email: str, phone: str):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
    
    def to_dict(self) -> Dict:
        """Serialize Client object to dictionary."""
        return {
            'client_id': self.client_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

class Case:
    """Represents a legal case with associated client and interactions."""
    
    def __init__(self, case_id: str, title: str, description: str, client: Client, 
                 status: CaseStatus = CaseStatus.OPEN):
        self.case_id = case_id
        self.title = title
        self.description = description
        self.client = client
        self.status = status
        self.interactions: List[Dict] = []
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def add_interaction(self, interaction_type: InteractionType, notes: str) -> None:
        """Add an interaction to the case with timestamp."""
        interaction = {
            'interaction_id': str(uuid.uuid4()),
            'type': interaction_type.name,
            'notes': notes,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.interactions.append(interaction)
        self.updated_at = datetime.datetime.now()
    
    def update_status(self, new_status: CaseStatus) -> None:
        """Update the status of the case."""
        self.status = new_status
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Serialize Case object to dictionary."""
        return {
            'case_id': self.case_id,
            'title': self.title,
            'description': self.description,
            'client': self.client.to_dict(),
            'status': self.status.name,
            'interactions': self.interactions,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class CaseManager:
    """Manages all cases and provides search functionality."""
    
    def __init__(self):
        self.cases: Dict[str, Case] = {}
    
    def create_case(self, title: str, description: str, client: Client) -> Case:
        """Create a new case and add it to the manager."""
        case_id = str(uuid.uuid4())
        new_case = Case(case_id, title, description, client)
        self.cases[case_id] = new_case
        return new_case
    
    def get_case(self, case_id: str) -> Optional[Case]:
        """Retrieve a case by its ID."""
        return self.cases.get(case_id)
    
    def search_cases_by_client(self, client_name: str) -> List[Case]:
        """Search for cases by client name (case-insensitive)."""
        return [case for case in self.cases.values() 
                if client_name.lower() in case.client.name.lower()]
    
    def save_to_file(self, filename: str) -> None:
        """Save all cases to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {'cases': [case.to_dict() for case in self.cases.values()]},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load cases from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for case_data in data['cases']:
                    client_data = case_data['client']
                    client = Client(
                        client_data['client_id'],
                        client_data['name'],
                        client_data['email'],
                        client_data['phone']
                    )
                    case = Case(
                        case_data['case_id'],
                        case_data['title'],
                        case_data['description'],
                        client,
                        CaseStatus[case_data['status']]
                    )
                    case.interactions = case_data['interactions']
                    case.created_at = datetime.datetime.fromisoformat(case_data['created_at'])
                    case.updated_at = datetime.datetime.fromisoformat(case_data['updated_at'])
                    self.cases[case.case_id] = case
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize case manager
    manager = CaseManager()
    
    # Create a client
    client = Client(
        client_id=str(uuid.uuid4()),
        name="John Doe",
        email="john.doe@example.com",
        phone="555-123-4567"
    )
    
    # Create a case
    case = manager.create_case(
        title="Personal Injury Claim",
        description="Client injured in a car accident",
        client=client
    )
    
    # Add interactions
    case.add_interaction(InteractionType.PHONE_CALL, "Initial consultation with client")
    case.add_interaction(InteractionType.MEETING, "Reviewed medical records")
    
    # Update case status
    case.update_status(CaseStatus.PENDING)
    
    # Save to file
    manager.save_to_file("cases.json")
```
