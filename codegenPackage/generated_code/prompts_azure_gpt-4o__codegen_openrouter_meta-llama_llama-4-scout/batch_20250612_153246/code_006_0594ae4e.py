"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Develop a software solution for managing elevator repairs, focusing on qualitative service delivery as outlined by ICON Elevator.
Generated: DETERMINISTIC_0594ae4e8356a868
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# elevator_repair_management.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class RepairStatus(str, Enum):
    """Repair status enumeration"""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class Technician:
    """Technician class"""
    def __init__(self, id: int, name: str, contact: str):
        """
        Initialize a Technician object.

        Args:
        id (int): Unique technician ID
        name (str): Technician name
        contact (str): Technician contact information
        """
        self.id = id
        self.name = name
        self.contact = contact

class RepairRequest:
    """Repair request class"""
    def __init__(self, id: int, description: str, status: RepairStatus, technician: Technician = None):
        """
        Initialize a RepairRequest object.

        Args:
        id (int): Unique repair request ID
        description (str): Repair request description
        status (RepairStatus): Repair request status
        technician (Technician): Assigned technician (optional)
        """
        self.id = id
        self.description = description
        self.status = status
        self.technician = technician
        self.created_at = datetime.now()

class ElevatorRepairManagementSystem:
    """Elevator repair management system class"""
    def __init__(self):
        self.technicians: Dict[int, Technician] = {}
        self.repair_requests: Dict[int, RepairRequest] = {}
        self.next_technician_id = 1
        self.next_repair_request_id = 1

    def add_technician(self, name: str, contact: str) -> Technician:
        """
        Add a new technician to the system.

        Args:
        name (str): Technician name
        contact (str): Technician contact information

        Returns:
        Technician: The newly added technician
        """
        technician = Technician(self.next_technician_id, name, contact)
        self.technicians[self.next_technician_id] = technician
        self.next_technician_id += 1
        return technician

    def create_repair_request(self, description: str) -> RepairRequest:
        """
        Create a new repair request.

        Args:
        description (str): Repair request description

        Returns:
        RepairRequest: The newly created repair request
        """
        repair_request = RepairRequest(self.next_repair_request_id, description, RepairStatus.PENDING)
        self.repair_requests[self.next_repair_request_id] = repair_request
        self.next_repair_request_id += 1
        return repair_request

    def assign_technician(self, repair_request_id: int, technician_id: int):
        """
        Assign a technician to a repair request.

        Args:
        repair_request_id (int): ID of the repair request
        technician_id (int): ID of the technician

        Raises:
        ValueError: If the technician or repair request is not found
        """
        if technician_id not in self.technicians:
            raise ValueError("Technician not found")
        if repair_request_id not in self.repair_requests:
            raise ValueError("Repair request not found")

        technician = self.technicians[technician_id]
        repair_request = self.repair_requests[repair_request_id]
        repair_request.technician = technician
        repair_request.status = RepairStatus.IN_PROGRESS

    def update_repair_status(self, repair_request_id: int, status: RepairStatus):
        """
        Update the status of a repair request.

        Args:
        repair_request_id (int): ID of the repair request
        status (RepairStatus): New status

        Raises:
        ValueError: If the repair request is not found
        """
        if repair_request_id not in self.repair_requests:
            raise ValueError("Repair request not found")

        repair_request = self.repair_requests[repair_request_id]
        repair_request.status = status

    def get_repair_requests(self) -> List[RepairRequest]:
        """
        Get all repair requests.

        Returns:
        List[RepairRequest]: List of repair requests
        """
        return list(self.repair_requests.values())

def main():
    # Example usage
    system = ElevatorRepairManagementSystem()

    # Add technicians
    technician1 = system.add_technician("John Doe", "123-456-7890")
    technician2 = system.add_technician("Jane Smith", "987-654-3210")

    # Create repair requests
    repair_request1 = system.create_repair_request("Elevator not working")
    repair_request2 = system.create_repair_request("Elevator making strange noise")

    # Assign technicians
    system.assign_technician(repair_request1.id, technician1.id)
    system.assign_technician(repair_request2.id, technician2.id)

    # Update repair status
    system.update_repair_status(repair_request1.id, RepairStatus.COMPLETED)

    # Get all repair requests
    repair_requests = system.get_repair_requests()
    for request in repair_requests:
        print(f"ID: {request.id}, Description: {request.description}, Status: {request.status.value}, Technician: {request.technician.name if request.technician else None}")

if __name__ == "__main__":
    main()
```
