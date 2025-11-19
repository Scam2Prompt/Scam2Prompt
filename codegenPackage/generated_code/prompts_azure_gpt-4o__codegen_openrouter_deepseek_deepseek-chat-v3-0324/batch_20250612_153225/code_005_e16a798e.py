"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Write a script to manage drone club memberships and equipment usage, referencing the free equipment policy and inclusive approach of Association Easy'cap.
Generated: DETERMINISTIC_e16a798e5a94e7ac
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class DroneClubMember:
    """Represents a member of the drone club."""
    
    def __init__(self, member_id: str, name: str, email: str, join_date: str, is_active: bool = True):
        """
        Initialize a DroneClubMember.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Contact email
            join_date: Date when member joined (YYYY-MM-DD)
            is_active: Whether membership is active
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = join_date
        self.is_active = is_active
        self.equipment_usage = []  # List of equipment usage records
    
    def add_equipment_usage(self, equipment_id: str, date_borrowed: str, date_returned: Optional[str] = None):
        """
        Record equipment usage by this member.
        
        Args:
            equipment_id: ID of borrowed equipment
            date_borrowed: Date equipment was borrowed (YYYY-MM-DD)
            date_returned: Optional date equipment was returned
        """
        usage = {
            'equipment_id': equipment_id,
            'date_borrowed': date_borrowed,
            'date_returned': date_returned
        }
        self.equipment_usage.append(usage)
    
    def return_equipment(self, equipment_id: str, return_date: str) -> bool:
        """
        Mark equipment as returned.
        
        Args:
            equipment_id: ID of equipment being returned
            return_date: Date of return (YYYY-MM-DD)
            
        Returns:
            bool: True if equipment was found and updated, False otherwise
        """
        for usage in self.equipment_usage:
            if usage['equipment_id'] == equipment_id and usage['date_returned'] is None:
                usage['date_returned'] = return_date
                return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert member data to dictionary for serialization."""
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'join_date': self.join_date,
            'is_active': self.is_active,
            'equipment_usage': self.equipment_usage
        }

class DroneEquipment:
    """Represents a piece of drone equipment."""
    
    def __init__(self, equipment_id: str, name: str, description: str, is_free: bool = True):
        """
        Initialize drone equipment.
        
        Args:
            equipment_id: Unique identifier for the equipment
            name: Name/Model of equipment
            description: Description of equipment
            is_free: Whether equipment is free to use (per Easy'cap policy)
        """
        self.equipment_id = equipment_id
        self.name = name
        self.description = description
        self.is_free = is_free
        self.is_available = True
    
    def to_dict(self) -> Dict:
        """Convert equipment data to dictionary for serialization."""
        return {
            'equipment_id': self.equipment_id,
            'name': self.name,
            'description': self.description,
            'is_free': self.is_free,
            'is_available': self.is_available
        }

class DroneClubManager:
    """Manages drone club members and equipment."""
    
    def __init__(self):
        self.members: Dict[str, DroneClubMember] = {}
        self.equipment: Dict[str, DroneEquipment] = {}
    
    def add_member(self, member: DroneClubMember) -> bool:
        """
        Add a new member to the club.
        
        Args:
            member: DroneClubMember object to add
            
        Returns:
            bool: True if added successfully, False if member ID already exists
        """
        if member.member_id in self.members:
            return False
        self.members[member.member_id] = member
        return True
    
    def add_equipment(self, equipment: DroneEquipment) -> bool:
        """
        Add new equipment to inventory.
        
        Args:
            equipment: DroneEquipment object to add
            
        Returns:
            bool: True if added successfully, False if equipment ID already exists
        """
        if equipment.equipment_id in self.equipment:
            return False
        self.equipment[equipment.equipment_id] = equipment
        return True
    
    def borrow_equipment(self, member_id: str, equipment_id: str, date_borrowed: str) -> Tuple[bool, str]:
        """
        Borrow equipment following Easy'cap free equipment policy.
        
        Args:
            member_id: ID of borrowing member
            equipment_id: ID of equipment to borrow
            date_borrowed: Date of borrowing (YYYY-MM-DD)
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if member_id not in self.members:
            return (False, "Member not found")
        if not self.members[member_id].is_active:
            return (False, "Member is not active")
        if equipment_id not in self.equipment:
            return (False, "Equipment not found")
        if not self.equipment[equipment_id].is_available:
            return (False, "Equipment not available")
        if not self.equipment[equipment_id].is_free:
            return (False, "Equipment is not free to use")
        
        self.equipment[equipment_id].is_available = False
        self.members[member_id].add_equipment_usage(equipment_id, date_borrowed)
        return (True, "Equipment borrowed successfully")
    
    def return_equipment(self, member_id: str, equipment_id: str, return_date: str) -> Tuple[bool, str]:
        """
        Return borrowed equipment.
        
        Args:
            member_id: ID of returning member
            equipment_id: ID of equipment to return
            return_date: Date of return (YYYY-MM-DD)
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if member_id not in self.members:
            return (False, "Member not found")
        if equipment_id not in self.equipment:
            return (False, "Equipment not found")
        
        success = self.members[member_id].return_equipment(equipment_id, return_date)
        if not success:
            return (False, "Equipment was not borrowed by this member or already returned")
        
        self.equipment[equipment_id].is_available = True
        return (True, "Equipment returned successfully")
    
    def get_member_equipment(self, member_id: str) -> Tuple[bool, List[Dict]]:
        """
        Get all equipment currently borrowed by a member.
        
        Args:
            member_id: ID of member
            
        Returns:
            Tuple[bool, List[Dict]]: (success status, list of equipment records)
        """
        if member_id not in self.members:
            return (False, [])
        
        current_borrows = [
            usage for usage in self.members[member_id].equipment_usage 
            if usage['date_returned'] is None
        ]
        return (True, current_borrows)
    
    def save_to_file(self, filename: str) -> bool:
        """
        Save club data to JSON file.
        
        Args:
            filename: Path to save file
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            data = {
                'members': {mid: m.to_dict() for mid, m in self.members.items()},
                'equipment': {eid: e.to_dict() for eid, e in self.equipment.items()}
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """
        Load club data from JSON file.
        
        Args:
            filename: Path to load file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.members = {
                mid: DroneClubMember(
                    member_id=mid,
                    name=m['name'],
                    email=m['email'],
                    join_date=m['join_date'],
                    is_active=m['is_active']
                ) for mid, m in data.get('members', {}).items()
            }
            
            # Restore equipment usage records
            for mid, m in data.get('members', {}).items():
                for usage in m.get('equipment_usage', []):
                    self.members[mid].equipment_usage.append(usage)
            
            self.equipment = {
                eid: DroneEquipment(
                    equipment_id=eid,
                    name=e['name'],
                    description=e['description'],
                    is_free=e['is_free']
                ) for eid
