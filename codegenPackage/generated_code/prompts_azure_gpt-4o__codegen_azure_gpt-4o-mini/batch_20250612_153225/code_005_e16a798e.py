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
from typing import List, Dict, Optional

class Member:
    """Class to represent a club member."""
    
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.equipment_used: List[str] = []

    def __repr__(self):
        return f"Member({self.member_id}, {self.name}, {self.email})"

class Equipment:
    """Class to represent equipment available for club members."""
    
    def __init__(self, equipment_id: int, name: str):
        self.equipment_id = equipment_id
        self.name = name
        self.is_available: bool = True

    def __repr__(self):
        return f"Equipment({self.equipment_id}, {self.name}, Available: {self.is_available})"

class DroneClub:
    """Class to manage drone club memberships and equipment usage."""
    
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.equipments: Dict[int, Equipment] = {}

    def add_member(self, member_id: int, name: str, email: str) -> None:
        """Add a new member to the club."""
        if member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member_id] = Member(member_id, name, email)

    def add_equipment(self, equipment_id: int, name: str) -> None:
        """Add new equipment to the club."""
        if equipment_id in self.equipments:
            raise ValueError("Equipment ID already exists.")
        self.equipments[equipment_id] = Equipment(equipment_id, name)

    def borrow_equipment(self, member_id: int, equipment_id: int) -> None:
        """Allow a member to borrow equipment if available."""
        member = self.members.get(member_id)
        equipment = self.equipments.get(equipment_id)

        if not member:
            raise ValueError("Member not found.")
        if not equipment:
            raise ValueError("Equipment not found.")
        if not equipment.is_available:
            raise ValueError("Equipment is currently unavailable.")

        equipment.is_available = False
        member.equipment_used.append(equipment.name)

    def return_equipment(self, member_id: int, equipment_id: int) -> None:
        """Allow a member to return borrowed equipment."""
        member = self.members.get(member_id)
        equipment = self.equipments.get(equipment_id)

        if not member:
            raise ValueError("Member not found.")
        if not equipment:
            raise ValueError("Equipment not found.")
        if equipment.name not in member.equipment_used:
            raise ValueError("This equipment was not borrowed by the member.")

        equipment.is_available = True
        member.equipment_used.remove(equipment.name)

    def get_member_info(self, member_id: int) -> Optional[Dict]:
        """Retrieve member information including borrowed equipment."""
        member = self.members.get(member_id)
        if member:
            return {
                "member_id": member.member_id,
                "name": member.name,
                "email": member.email,
                "equipment_used": member.equipment_used
            }
        return None

    def get_equipment_info(self, equipment_id: int) -> Optional[Dict]:
        """Retrieve equipment information."""
        equipment = self.equipments.get(equipment_id)
        if equipment:
            return {
                "equipment_id": equipment.equipment_id,
                "name": equipment.name,
                "is_available": equipment.is_available
            }
        return None

    def save_data(self, filename: str) -> None:
        """Save members and equipment data to a JSON file."""
        data = {
            "members": {member_id: member.__dict__ for member_id, member in self.members.items()},
            "equipments": {equipment_id: equipment.__dict__ for equipment_id, equipment in self.equipments.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str) -> None:
        """Load members and equipment data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.members = {int(member_id): Member(**member) for member_id, member in data['members'].items()}
                self.equipments = {int(equipment_id): Equipment(**equipment) for equipment_id, equipment in data['equipments'].items()}
        except FileNotFoundError:
            print("Data file not found. Starting with empty data.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Please check the file format.")

# Example usage
if __name__ == "__main__":
    club = DroneClub()
    club.add_member(1, "Alice Smith", "alice@example.com")
    club.add_equipment(101, "DJI Phantom 4")
    
    try:
        club.borrow_equipment(1, 101)
        print(club.get_member_info(1))
        club.return_equipment(1, 101)
        print(club.get_equipment_info(101))
    except ValueError as e:
        print(f"Error: {e}")

    # Save and load data
    club.save_data("club_data.json")
    club.load_data("club_data.json")
```
