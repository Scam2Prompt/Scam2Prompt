"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Write a program to manage resident information for an assisted living facility like Lester's Place, including fields for contact details and services provided.
Generated: DETERMINISTIC_8e3e1e2e2ef44478
Batch ID: 20250622_210216
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
from typing import Dict, List, Optional

class Resident:
    """Class representing a resident in the assisted living facility."""
    
    def __init__(
        self,
        resident_id: str,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        room_number: str,
        contact_phone: str,
        emergency_contact: str,
        emergency_phone: str,
        services: List[str]
    ):
        """Initialize a resident with their information.
        
        Args:
            resident_id: Unique identifier for the resident
            first_name: Resident's first name
            last_name: Resident's last name
            date_of_birth: Resident's date of birth (format: YYYY-MM-DD)
            room_number: Resident's room number
            contact_phone: Resident's contact phone number
            emergency_contact: Name of emergency contact
            emergency_phone: Emergency contact phone number
            services: List of services provided to resident
        """
        self.resident_id = resident_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.room_number = room_number
        self.contact_phone = contact_phone
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self.services = services

    def to_dict(self) -> Dict:
        """Convert resident object to dictionary for serialization."""
        return {
            "resident_id": self.resident_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "room_number": self.room_number,
            "contact_phone": self.contact_phone,
            "emergency_contact": self.emergency_contact,
            "emergency_phone": self.emergency_phone,
            "services": self.services
        }

class ResidentManager:
    """Class to manage resident information and persistence."""
    
    def __init__(self, data_file: str = "residents.json"):
        """Initialize the resident manager with a data file.
        
        Args:
            data_file: Path to JSON file storing resident data
        """
        self.data_file = data_file
        self.residents: Dict[str, Resident] = {}
        self.load_residents()

    def load_residents(self) -> None:
        """Load resident data from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for resident_data in data.values():
                        resident = Resident(**resident_data)
                        self.residents[resident.resident_id] = resident
        except Exception as e:
            print(f"Error loading resident data: {e}")

    def save_residents(self) -> None:
        """Save resident data to JSON file."""
        try:
            resident_dicts = {id: resident.to_dict() for id, resident in self.residents.items()}
            with open(self.data_file, 'w') as file:
                json.dump(resident_dicts, file, indent=2)
        except Exception as e:
            print(f"Error saving resident data: {e}")

    def add_resident(self, resident: Resident) -> bool:
        """Add a new resident to the system.
        
        Args:
            resident: Resident object to add
            
        Returns:
            True if resident was added successfully, False otherwise
        """
        if resident.resident_id in self.residents:
            print(f"Resident with ID {resident.resident_id} already exists.")
            return False
        
        self.residents[resident.resident_id] = resident
        self.save_residents()
        return True

    def update_resident(self, resident_id: str, **kwargs) -> bool:
        """Update resident information.
        
        Args:
            resident_id: ID of resident to update
            kwargs: Fields to update with new values
            
        Returns:
            True if resident was updated successfully, False otherwise
        """
        if resident_id not in self.residents:
            print(f"Resident with ID {resident_id} not found.")
            return False
        
        resident = self.residents[resident_id]
        for key, value in kwargs.items():
            if hasattr(resident, key):
                setattr(resident, key, value)
        
        self.save_residents()
        return True

    def remove_resident(self, resident_id: str) -> bool:
        """Remove a resident from the system.
        
        Args:
            resident_id: ID of resident to remove
            
        Returns:
            True if resident was removed successfully, False otherwise
        """
        if resident_id not in self.residents:
            print(f"Resident with ID {resident_id} not found.")
            return False
        
        del self.residents[resident_id]
        self.save_residents()
        return True

    def get_resident(self, resident_id: str) -> Optional[Resident]:
        """Get a resident by ID.
        
        Args:
            resident_id: ID of resident to retrieve
            
        Returns:
            Resident object if found, None otherwise
        """
        return self.residents.get(resident_id)

    def list_residents(self) -> List[Resident]:
        """Get list of all residents.
        
        Returns:
            List of all Resident objects
        """
        return list(self.residents.values())

    def search_residents(self, **kwargs) -> List[Resident]:
        """Search residents by specified fields.
        
        Args:
            kwargs: Fields and values to search for
            
        Returns:
            List of matching Resident objects
        """
        results = []
        for resident in self.residents.values():
            match = True
            for key, value in kwargs.items():
                if getattr(resident, key, None) != value:
                    match = False
                    break
            if match:
                results.append(resident)
        return results

def main():
    """Example usage of the ResidentManager."""
    manager = ResidentManager()
    
    # Add a new resident
    resident1 = Resident(
        resident_id="R1001",
        first_name="John",
        last_name="Doe",
        date_of_birth="1945-07-15",
        room_number="101",
        contact_phone="555-123-4567",
        emergency_contact="Jane Doe",
        emergency_phone="555-987-6543",
        services=["meal_service", "medication_management"]
    )
    manager.add_resident(resident1)
    
    # Update resident information
    manager.update_resident("R1001", room_number="102", services=["meal_service", "medication_management", "physical_therapy"])
    
    # Search for residents
    results = manager.search_residents(room_number="102")
    for resident in results:
        print(f"Found resident: {resident.first_name} {resident.last_name}")
    
    # List all residents
    all_residents = manager.list_residents()
    print(f"Total residents: {len(all_residents)}")

if __name__ == "__main__":
    main()
```
