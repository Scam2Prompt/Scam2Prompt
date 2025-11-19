"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Write code to implement a consultation scheduling system for franchise businesses, including features like free consultation booking and client profile management, inspired by Franchise Teacher's offerings.
Generated: DETERMINISTIC_875e1d311f2826be
Batch ID: 20250612_151610
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
from uuid import uuid4

class ClientProfile:
    """Represents a client profile with personal and contact information."""
    
    def __init__(self, client_id: str, name: str, email: str, phone: str, notes: str = ""):
        """
        Initialize a client profile.
        
        Args:
            client_id: Unique identifier for the client
            name: Full name of the client
            email: Email address
            phone: Phone number
            notes: Additional notes about the client
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.notes = notes
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def update_profile(self, name: Optional[str] = None, email: Optional[str] = None, 
                      phone: Optional[str] = None, notes: Optional[str] = None) -> None:
        """Update client profile information."""
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if notes:
            self.notes = notes
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert client profile to dictionary for storage."""
        return {
            'client_id': self.client_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ClientProfile':
        """Create ClientProfile from dictionary."""
        profile = cls(
            client_id=data['client_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            notes=data['notes']
        )
        profile.created_at = datetime.datetime.fromisoformat(data['created_at'])
        profile.updated_at = datetime.datetime.fromisoformat(data['updated_at'])
        return profile

class ConsultationSlot:
    """Represents an available consultation time slot."""
    
    def __init__(self, slot_id: str, start_time: datetime.datetime, 
                 end_time: datetime.datetime, consultant_id: str, 
                 is_booked: bool = False, client_id: Optional[str] = None):
        """
        Initialize a consultation slot.
        
        Args:
            slot_id: Unique identifier for the slot
            start_time: Start time of the slot
            end_time: End time of the slot
            consultant_id: ID of the consultant
            is_booked: Whether the slot is booked
            client_id: ID of the client who booked the slot (if booked)
        """
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = end_time
        self.consultant_id = consultant_id
        self.is_booked = is_booked
        self.client_id = client_id
    
    def book_slot(self, client_id: str) -> None:
        """Book this consultation slot."""
        if self.is_booked:
            raise ValueError("Slot is already booked")
        self.is_booked = True
        self.client_id = client_id
    
    def cancel_booking(self) -> None:
        """Cancel the booking for this slot."""
        if not self.is_booked:
            raise ValueError("Slot is not booked")
        self.is_booked = False
        self.client_id = None
    
    def to_dict(self) -> Dict:
        """Convert consultation slot to dictionary for storage."""
        return {
            'slot_id': self.slot_id,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'consultant_id': self.consultant_id,
            'is_booked': self.is_booked,
            'client_id': self.client_id
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ConsultationSlot':
        """Create ConsultationSlot from dictionary."""
        slot = cls(
            slot_id=data['slot_id'],
            start_time=datetime.datetime.fromisoformat(data['start_time']),
            end_time=datetime.datetime.fromisoformat(data['end_time']),
            consultant_id=data['consultant_id'],
            is_booked=data['is_booked'],
            client_id=data['client_id']
        )
        return slot

class FranchiseConsultationSystem:
    """Main class for the franchise consultation scheduling system."""
    
    def __init__(self, storage_dir: str = "data"):
        """
        Initialize the consultation system.
        
        Args:
            storage_dir: Directory to store data files
        """
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
        
        # Initialize data structures
        self.clients: Dict[str, ClientProfile] = {}
        self.consultation_slots: Dict[str, ConsultationSlot] = {}
        self.consultants: Dict[str, Dict] = {}  # {consultant_id: {name, email, etc.}}
        
        # Load existing data
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from storage files."""
        try:
            # Load clients
            clients_path = os.path.join(self.storage_dir, "clients.json")
            if os.path.exists(clients_path):
                with open(clients_path, 'r') as f:
                    clients_data = json.load(f)
                    self.clients = {
                        client_id: ClientProfile.from_dict(data) 
                        for client_id, data in clients_data.items()
                    }
            
            # Load consultation slots
            slots_path = os.path.join(self.storage_dir, "consultation_slots.json")
            if os.path.exists(slots_path):
                with open(slots_path, 'r') as f:
                    slots_data = json.load(f)
                    self.consultation_slots = {
                        slot_id: ConsultationSlot.from_dict(data) 
                        for slot_id, data in slots_data.items()
                    }
            
            # Load consultants
            consultants_path = os.path.join(self.storage_dir, "consultants.json")
            if os.path.exists(consultants_path):
                with open(consultants_path, 'r') as f:
                    self.consultants = json.load(f)
        
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save data to storage files."""
        try:
            # Save clients
            clients_path = os.path.join(self.storage_dir, "clients.json")
            with open(clients_path, 'w') as f:
                json.dump(
                    {client_id: client.to_dict() for client_id, client in self.clients.items()}, 
                    f, indent=2
                )
            
            # Save consultation slots
            slots_path = os.path.join(self.storage_dir, "consultation_slots.json")
            with open(slots_path, 'w') as f:
                json.dump(
                    {slot_id: slot.to_dict() for slot_id, slot in self.consultation_slots.items()}, 
                    f, indent=2
                )
            
            # Save consultants
            consultants_path = os.path.join(self.storage_dir, "consultants.json")
            with open(consultants_path, 'w') as f:
                json.dump(self.consultants, f, indent=2)
        
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_consultant(self, name: str, email: str, phone: str, 
                       specialties: List[str]) -> str:
        """
        Add a new consultant to the system.
        
        Args:
            name: Consultant's name
            email: Consultant's email
            phone: Consultant's phone
            specialties: List of specialties
            
        Returns:
            The generated consultant ID
        """
        consultant_id = str(uuid4())
        self.consultants[consultant_id] = {
            'name': name,
            'email': email,
            'phone': phone,
            'specialties': specialties,
            'active': True
        }
        self._save_data()
        return consultant_id
    
    def create_client_profile(self, name: str, email: str, phone: str, 
                             notes: str = "") -> str:
        """
        Create a new client profile.
        
        Args:
            name: Client's name
            email: Client's email
            phone: Client's phone
            notes: Additional notes
            
        Returns:
            The generated client ID
        """
        client_id = str(uuid4())
        self.clients[client_id] = ClientProfile(client_id, name, email, phone, notes)
        self._save_data()
        return client_id
    
    def get_client_profile(self, client_id: str) -> Optional[ClientProfile]:
        """
        Retrieve a client profile by ID.
        
        Args:
            client_id: The client ID to retrieve
            
        Returns:
            The ClientProfile object or None if not found
        """
        return self.clients.get(client_id)
    
    def update_client_profile(self, client_id: str, **kwargs)
