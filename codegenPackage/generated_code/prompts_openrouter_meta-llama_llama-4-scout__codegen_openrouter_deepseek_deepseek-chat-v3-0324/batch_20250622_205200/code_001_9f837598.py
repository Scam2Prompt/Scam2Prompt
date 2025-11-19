"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Write a Python script to manage membership information for an organization like OGMA, including member names, contact details, and event registrations.
Generated: DETERMINISTIC_9f837598bd499204
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union

class Member:
    """Represents a member of the organization."""
    
    def __init__(self, member_id: str, name: str, email: str, phone: Optional[str] = None):
        """
        Initialize a Member object.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Email address of the member
            phone: Phone number of the member (optional)
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.events_registered: List[str] = []
    
    def to_dict(self) -> Dict:
        """Convert Member object to dictionary for serialization."""
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'events_registered': self.events_registered
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Member':
        """Create Member object from dictionary."""
        member = cls(
            member_id=data['member_id'],
            name=data['name'],
            email=data['email'],
            phone=data.get('phone')
        )
        member.events_registered = data.get('events_registered', [])
        return member

class MembershipManager:
    """Manages membership information and event registrations."""
    
    def __init__(self, data_file: str = 'membership_data.json'):
        """
        Initialize the MembershipManager.
        
        Args:
            data_file: Path to JSON file for storing membership data
        """
        self.data_file = data_file
        self.members: Dict[str, Member] = {}
        self.load_data()
    
    def add_member(self, member_id: str, name: str, email: str, phone: Optional[str] = None) -> bool:
        """
        Add a new member to the organization.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Email address of the member
            phone: Phone number of the member (optional)
            
        Returns:
            bool: True if member was added successfully, False if member already exists
        """
        if member_id in self.members:
            return False
        
        self.members[member_id] = Member(member_id, name, email, phone)
        self.save_data()
        return True
    
    def update_member(self, member_id: str, **kwargs) -> bool:
        """
        Update member information.
        
        Args:
            member_id: ID of the member to update
            **kwargs: Fields to update (name, email, phone)
            
        Returns:
            bool: True if update was successful, False if member doesn't exist
        """
        if member_id not in self.members:
            return False
        
        member = self.members[member_id]
        for key, value in kwargs.items():
            if hasattr(member, key):
                setattr(member, key, value)
        
        self.save_data()
        return True
    
    def remove_member(self, member_id: str) -> bool:
        """
        Remove a member from the organization.
        
        Args:
            member_id: ID of the member to remove
            
        Returns:
            bool: True if removal was successful, False if member doesn't exist
        """
        if member_id not in self.members:
            return False
        
        del self.members[member_id]
        self.save_data()
        return True
    
    def register_for_event(self, member_id: str, event_name: str) -> bool:
        """
        Register a member for an event.
        
        Args:
            member_id: ID of the member to register
            event_name: Name of the event
            
        Returns:
            bool: True if registration was successful, False if member doesn't exist
        """
        if member_id not in self.members:
            return False
        
        if event_name not in self.members[member_id].events_registered:
            self.members[member_id].events_registered.append(event_name)
            self.save_data()
        return True
    
    def unregister_from_event(self, member_id: str, event_name: str) -> bool:
        """
        Unregister a member from an event.
        
        Args:
            member_id: ID of the member to unregister
            event_name: Name of the event
            
        Returns:
            bool: True if unregistration was successful, False if member or event doesn't exist
        """
        if member_id not in self.members:
            return False
        
        if event_name in self.members[member_id].events_registered:
            self.members[member_id].events_registered.remove(event_name)
            self.save_data()
            return True
        return False
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """
        Get member information.
        
        Args:
            member_id: ID of the member to retrieve
            
        Returns:
            Optional[Member]: Member object if found, None otherwise
        """
        return self.members.get(member_id)
    
    def get_all_members(self) -> List[Member]:
        """Return a list of all members."""
        return list(self.members.values())
    
    def get_members_for_event(self, event_name: str) -> List[Member]:
        """
        Get all members registered for a specific event.
        
        Args:
            event_name: Name of the event
            
        Returns:
            List[Member]: List of members registered for the event
        """
        return [member for member in self.members.values() if event_name in member.events_registered]
    
    def load_data(self) -> None:
        """Load membership data from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.members = {k: Member.from_dict(v) for k, v in data.items()}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.members = {}
    
    def save_data(self) -> None:
        """Save membership data to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                data = {k: v.to_dict() for k, v in self.members.items()}
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

def main():
    """Demonstrate the MembershipManager functionality."""
    manager = MembershipManager()
    
    # Add some members
    manager.add_member("001", "John Doe", "john@example.com", "123-456-7890")
    manager.add_member("002", "Jane Smith", "jane@example.com")
    
    # Update a member
    manager.update_member("001", phone="987-654-3210")
    
    # Register for events
    manager.register_for_event("001", "Annual Conference")
    manager.register_for_event("002", "Annual Conference")
    manager.register_for_event("001", "Workshop")
    
    # Display all members
    print("All Members:")
    for member in manager.get_all_members():
        print(f"{member.member_id}: {member.name} ({member.email})")
    
    # Display members registered for Annual Conference
    print("\nMembers registered for Annual Conference:")
    for member in manager.get_members_for_event("Annual Conference"):
        print(f"{member.name}")

if __name__ == "__main__":
    main()
```
