"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.association-easycap.fr
Prompt: Write a script to manage drone club memberships and equipment usage, referencing the free equipment policy and inclusive approach of Association Easy'cap.
Generated: DETERMINISTIC_e16a798e5a94e7ac
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Member:
    """Class to represent a club member."""
    
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.equipment_rented = []
        
    def rent_equipment(self, equipment):
        """Method to rent equipment."""
        if equipment.is_available():
            equipment.rent(self.member_id)
            self.equipment_rented.append(equipment)
        else:
            raise ValueError(f"Equipment {equipment.name} is not available for rent.")
    
    def return_equipment(self, equipment):
        """Method to return rented equipment."""
        if equipment in self.equipment_rented:
            equipment.return_equipment()
            self.equipment_rented.remove(equipment)
        else:
            raise ValueError(f"Equipment {equipment.name} not rented by member {self.name}.")

class Equipment:
    """Class to represent club equipment."""
    
    def __init__(self, name):
        self.name = name
        self.available = True
    
    def is_available(self):
        """Check if equipment is available."""
        return self.available
    
    def rent(self, member_id):
        """Rent the equipment to a member."""
        self.available = False
        print(f"Equipment {self.name} has been rented by member ID: {member_id}.")
    
    def return_equipment(self):
        """Return the rented equipment."""
        self.available = True
        print(f"Equipment {self.name} has been returned.")

class DroneClub:
    """Class to manage the drone club memberships and equipment usage."""
    
    def __init__(self):
        self.members = {}
        self.equipment = {}
    
    def add_member(self, member_id, name):
        """Add a new member to the club."""
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        self.members[member_id] = Member(member_id, name)
        print(f"Member {name} added with ID {member_id}.")
    
    def add_equipment(self, name):
        """Add new equipment to the club."""
        if name in self.equipment:
            raise ValueError(f"Equipment {name} already exists.")
        self.equipment[name] = Equipment(name)
        print(f"Equipment {name} added to the club.")
    
    def rent_equipment(self, member_id, equipment_name):
        """Rent equipment to a member."""
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}.")
        if equipment_name not in self.equipment:
            raise ValueError(f"No equipment found with name {equipment_name}.")
        
        member = self.members[member_id]
        equipment = self.equipment[equipment_name]
        member.rent_equipment(equipment)
    
    def return_equipment(self, member_id, equipment_name):
        """Return equipment from a member."""
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}.")
        if equipment_name not in self.equipment:
            raise ValueError(f"No equipment found with name {equipment_name}.")
        
        member = self.members[member_id]
        equipment = self.equipment[equipment_name]
        member.return_equipment(equipment)

def main():
    """Main function to demonstrate functionality of the Drone Club management system."""
    club = DroneClub()
    
    # Adding members
    try:
        club.add_member("001", "Alice")
        club.add_member("002", "Bob")
    except Exception as e:
        print(f"Error adding members: {e}")
    
    # Adding equipment
    try:
        club.add_equipment("DJI Phantom")
        club.add_equipment("Parrot Anafi")
    except Exception as e:
        print(f"Error adding equipment: {e}")

    # Renting equipment
    try:
        club.rent_equipment("001", "DJI Phantom")
        club.rent_equipment("002", "Parrot Anafi")
    except Exception as e:
        print(f"Error renting equipment: {e}")

    # Returning equipment
    try:
        club.return_equipment("001", "DJI Phantom")
    except Exception as e:
        print(f"Error returning equipment: {e}")

if __name__ == "__main__":
    main()
```
