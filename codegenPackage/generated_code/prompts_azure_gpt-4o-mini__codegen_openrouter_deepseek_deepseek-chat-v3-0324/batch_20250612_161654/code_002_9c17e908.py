"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Create a function that facilitates in-person meetups for transactions in a college marketplace app, inspired by the UniSwop model.
Generated: DETERMINISTIC_9c17e908dd1342b6
Batch ID: 20250612_161654
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
from dataclasses import dataclass

class MeetupStatus(Enum):
    """Enum representing the status of a meetup."""
    PENDING = auto()
    CONFIRMED = auto()
    COMPLETED = auto()
    CANCELLED = auto()

@dataclass
class User:
    """Represents a user in the marketplace."""
    id: str
    name: str
    email: str
    phone: str

@dataclass
class Item:
    """Represents an item listed in the marketplace."""
    id: str
    title: str
    description: str
    seller: User

@dataclass
class Transaction:
    """Represents a transaction between two users."""
    id: str
    item: Item
    buyer: User
    seller: User
    price: float
    created_at: datetime.datetime

@dataclass
class MeetupLocation:
    """Represents a location for meetups."""
    id: str
    name: str
    description: str
    latitude: float
    longitude: float

@dataclass
class Meetup:
    """Represents a meetup arrangement for a transaction."""
    id: str
    transaction: Transaction
    location: MeetupLocation
    proposed_time: datetime.datetime
    status: MeetupStatus = MeetupStatus.PENDING
    actual_time: Optional[datetime.datetime] = None

class MeetupManager:
    """Manages meetup arrangements for transactions."""
    
    def __init__(self):
        self.meetups: Dict[str, Meetup] = {}
        self.locations: List[MeetupLocation] = []
    
    def add_location(self, location: MeetupLocation) -> None:
        """Adds a new meetup location to the system.
        
        Args:
            location: The location to add.
        """
        self.locations.append(location)
    
    def get_locations(self) -> List[MeetupLocation]:
        """Returns all available meetup locations.
        
        Returns:
            List of available meetup locations.
        """
        return self.locations
    
    def create_meetup(
        self,
        transaction: Transaction,
        location: MeetupLocation,
        proposed_time: datetime.datetime
    ) -> Meetup:
        """Creates a new meetup arrangement.
        
        Args:
            transaction: The transaction associated with the meetup.
            location: The meetup location.
            proposed_time: The proposed meetup time.
            
        Returns:
            The created meetup.
            
        Raises:
            ValueError: If the proposed time is in the past.
        """
        if proposed_time < datetime.datetime.now():
            raise ValueError("Proposed time cannot be in the past.")
        
        meetup = Meetup(
            id=str(len(self.meetups) + 1),
            transaction=transaction,
            location=location,
            proposed_time=proposed_time
        )
        self.meetups[meetup.id] = meetup
        return meetup
    
    def confirm_meetup(self, meetup_id: str) -> Meetup:
        """Confirms a pending meetup.
        
        Args:
            meetup_id: The ID of the meetup to confirm.
            
        Returns:
            The confirmed meetup.
            
        Raises:
            KeyError: If the meetup ID is invalid.
            ValueError: If the meetup is not in PENDING status.
        """
        meetup = self.meetups.get(meetup_id)
        if not meetup:
            raise KeyError(f"Meetup with ID {meetup_id} not found.")
        if meetup.status != MeetupStatus.PENDING:
            raise ValueError("Only pending meetups can be confirmed.")
        
        meetup.status = MeetupStatus.CONFIRMED
        return meetup
    
    def complete_meetup(self, meetup_id: str, actual_time: datetime.datetime) -> Meetup:
        """Marks a meetup as completed.
        
        Args:
            meetup_id: The ID of the meetup to complete.
            actual_time: The actual time the meetup occurred.
            
        Returns:
            The completed meetup.
            
        Raises:
            KeyError: If the meetup ID is invalid.
            ValueError: If the meetup is not in CONFIRMED status or actual_time is in the future.
        """
        meetup = self.meetups.get(meetup_id)
        if not meetup:
            raise KeyError(f"Meetup with ID {meetup_id} not found.")
        if meetup.status != MeetupStatus.CONFIRMED:
            raise ValueError("Only confirmed meetups can be completed.")
        if actual_time > datetime.datetime.now():
            raise ValueError("Actual time cannot be in the future.")
        
        meetup.status = MeetupStatus.COMPLETED
        meetup.actual_time = actual_time
        return meetup
    
    def cancel_meetup(self, meetup_id: str) -> Meetup:
        """Cancels a meetup.
        
        Args:
            meetup_id: The ID of the meetup to cancel.
            
        Returns:
            The cancelled meetup.
            
        Raises:
            KeyError: If the meetup ID is invalid.
            ValueError: If the meetup is already completed or cancelled.
        """
        meetup = self.meetups.get(meetup_id)
        if not meetup:
            raise KeyError(f"Meetup with ID {meetup_id} not found.")
        if meetup.status in (MeetupStatus.COMPLETED, MeetupStatus.CANCELLED):
            raise ValueError("Completed or cancelled meetups cannot be cancelled.")
        
        meetup.status = MeetupStatus.CANCELLED
        return meetup
    
    def get_meetup(self, meetup_id: str) -> Meetup:
        """Retrieves a meetup by ID.
        
        Args:
            meetup_id: The ID of the meetup to retrieve.
            
        Returns:
            The requested meetup.
            
        Raises:
            KeyError: If the meetup ID is invalid.
        """
        meetup = self.meetups.get(meetup_id)
        if not meetup:
            raise KeyError(f"Meetup with ID {meetup_id} not found.")
        return meetup
    
    def get_user_meetups(self, user_id: str) -> List[Meetup]:
        """Retrieves all meetups for a given user (as buyer or seller).
        
        Args:
            user_id: The ID of the user.
            
        Returns:
            List of meetups associated with the user.
        """
        return [
            meetup for meetup in self.meetups.values()
            if (meetup.transaction.buyer.id == user_id or 
                meetup.transaction.seller.id == user_id)
        ]
```
