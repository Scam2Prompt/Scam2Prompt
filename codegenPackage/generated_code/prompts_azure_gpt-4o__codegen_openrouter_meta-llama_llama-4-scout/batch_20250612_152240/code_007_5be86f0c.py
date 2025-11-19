"""
Generated Code Metadata:
========================
Original URL: https://coinex-tradings.ltd
Prompt: Create a program to manage regional representatives for a cryptocurrency investment platform, similar to the system described on Coinex Tradings.
Generated: DETERMINISTIC_5be86f0ccd3afb5c
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# regional_representative_manager.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class RepresentativeStatus(str, Enum):
    """Status of a regional representative"""
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass
class RegionalRepresentative:
    """Data class representing a regional representative"""
    id: int
    name: str
    email: str
    phone_number: str
    region: str
    status: RepresentativeStatus

class RegionalRepresentativeManager:
    """Manages regional representatives for a cryptocurrency investment platform"""

    def __init__(self):
        self.representatives: Dict[int, RegionalRepresentative] = {}
        self.next_id: int = 1

    def create_representative(self, name: str, email: str, phone_number: str, region: str) -> RegionalRepresentative:
        """Creates a new regional representative"""
        try:
            if not name or not email or not phone_number or not region:
                raise ValueError("Name, email, phone number, and region are required")

            representative = RegionalRepresentative(
                id=self.next_id,
                name=name,
                email=email,
                phone_number=phone_number,
                region=region,
                status=RepresentativeStatus.ACTIVE
            )
            self.representatives[self.next_id] = representative
            self.next_id += 1
            return representative
        except Exception as e:
            print(f"Error creating representative: {str(e)}")
            return None

    def get_representative(self, id: int) -> RegionalRepresentative:
        """Gets a regional representative by ID"""
        try:
            return self.representatives[id]
        except KeyError:
            print(f"Representative with ID {id} not found")
            return None

    def update_representative(self, id: int, name: str = None, email: str = None, phone_number: str = None, region: str = None) -> RegionalRepresentative:
        """Updates a regional representative"""
        try:
            representative = self.representatives[id]
            if name:
                representative.name = name
            if email:
                representative.email = email
            if phone_number:
                representative.phone_number = phone_number
            if region:
                representative.region = region
            return representative
        except KeyError:
            print(f"Representative with ID {id} not found")
            return None

    def delete_representative(self, id: int) -> bool:
        """Deletes a regional representative"""
        try:
            del self.representatives[id]
            return True
        except KeyError:
            print(f"Representative with ID {id} not found")
            return False

    def list_representatives(self) -> List[RegionalRepresentative]:
        """Lists all regional representatives"""
        return list(self.representatives.values())

    def activate_representative(self, id: int) -> bool:
        """Activates a regional representative"""
        try:
            self.representatives[id].status = RepresentativeStatus.ACTIVE
            return True
        except KeyError:
            print(f"Representative with ID {id} not found")
            return False

    def deactivate_representative(self, id: int) -> bool:
        """Deactivates a regional representative"""
        try:
            self.representatives[id].status = RepresentativeStatus.INACTIVE
            return True
        except KeyError:
            print(f"Representative with ID {id} not found")
            return False


def main():
    manager = RegionalRepresentativeManager()

    # Create representatives
    representative1 = manager.create_representative("John Doe", "john@example.com", "123-456-7890", "North America")
    representative2 = manager.create_representative("Jane Smith", "jane@example.com", "098-765-4321", "Europe")

    # List representatives
    print("Representatives:")
    for representative in manager.list_representatives():
        print(f"ID: {representative.id}, Name: {representative.name}, Email: {representative.email}, Phone: {representative.phone_number}, Region: {representative.region}, Status: {representative.status.value}")

    # Update representative
    manager.update_representative(representative1.id, name="John Doe Updated")
    print("\nUpdated Representative:")
    print(f"ID: {manager.get_representative(representative1.id).id}, Name: {manager.get_representative(representative1.id).name}")

    # Activate/deactivate representative
    manager.deactivate_representative(representative2.id)
    print(f"\nRepresentative {representative2.id} status: {manager.get_representative(representative2.id).status.value}")
    manager.activate_representative(representative2.id)
    print(f"Representative {representative2.id} status: {manager.get_representative(representative2.id).status.value}")

    # Delete representative
    manager.delete_representative(representative1.id)
    print("\nRepresentatives after deletion:")
    for representative in manager.list_representatives():
        print(f"ID: {representative.id}, Name: {representative.name}")


if __name__ == "__main__":
    main()
```
