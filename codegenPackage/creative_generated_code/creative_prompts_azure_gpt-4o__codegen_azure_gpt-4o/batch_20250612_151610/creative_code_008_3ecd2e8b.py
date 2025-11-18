"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Design a workflow in Python for scheduling field technical assistance for machinery repairs, incorporating Track Diesel Peru's focus on on-site and workshop services.
Generated: DETERMINISTIC_3ecd2e8b18f31aa2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional


class FieldAssistanceScheduler:
    """
    A class to handle scheduling of field technical assistance for machinery repairs.

    Track Diesel Peru offers on-site and workshop services. This scheduler manages
    requests and ensures proper allocation of resources.
    """

    def __init__(self):
        """
        Initialize the scheduler with empty lists for requests and technicians.
        """
        self.service_requests: List[Dict] = []  # List to store service request data
        self.technicians: List[Dict] = []  # List to store technician data

    def add_technician(self, technician_id: int, name: str, skill_level: str, available: bool = True):
        """
        Add a technician to the pool of available technicians.

        Parameters:
          - technician_id (int): Unique identifier for the technician.
          - name (str): Technician's name.
          - skill_level (str): Skill level (e.g., 'Beginner', 'Intermediate', 'Expert').
          - available (bool): Availability status of the technician (default is True).
        """
        self.technicians.append({
            "technician_id": technician_id,
            "name": name,
            "skill_level": skill_level,
            "available": available
        })

    def create_service_request(self, machine_id: int, issue_description: str, service_type: str,
                                preferred_date: Optional[datetime.date] = None):
        """
        Create a service request for machinery repair.

        Parameters:
          - machine_id (int): Unique identifier of the machine.
          - issue_description (str): Description of the issue.
          - service_type (str): Type of service ('on-site' or 'workshop').
          - preferred_date (datetime.date, optional): Preferred date for service.

        Returns:
          - request_id (int): Unique identifier of the created request.
        """
        if service_type not in ["on-site", "workshop"]:
            raise ValueError("Invalid service type. Choose 'on-site' or 'workshop'.")

        request_id = len(self.service_requests) + 1
        self.service_requests.append({
            "request_id": request_id,
            "machine_id": machine_id,
            "issue_description": issue_description,
            "service_type": service_type,
            "preferred_date": preferred_date,
            "status": "Pending"
        })
        return request_id

    def assign_technician(self, request_id: int):
        """
        Assign an available technician to a service request.

        Parameters:
          - request_id (int): Unique identifier of the service request.

        Returns:
          - technician (dict): Assigned technician details, or None if no technician is available.
        """
        # Find the request by ID
        request = next((req for req in self.service_requests if req["request_id"] == request_id), None)
        if not request:
            raise ValueError("Service request not found.")

        if request["status"] != "Pending":
            raise ValueError("Cannot assign technician. Request is not in 'Pending' status.")

        # Select the first available technician
        technician = next((tech for tech in self.technicians if tech["available"]), None)
        if technician:
            technician["available"] = False  # Mark technician as unavailable
            request["status"] = "Assigned"
            request["technician"] = technician
            return technician

        return None  # No technician available

    def complete_service_request(self, request_id: int):
        """
        Mark a service request as completed and update technician availability.

        Parameters:
          - request_id (int): Unique identifier of the service request.
        """
        # Find the request by ID
        request = next((req for req in self.service_requests if req["request_id"] == request_id), None)
        if not request:
            raise ValueError("Service request not found.")

        if request["status"] != "Assigned":
            raise ValueError("Cannot complete request. Technician has not been assigned.")

        # Update the technician's availability
        if "technician" in request:
            technician = request["technician"]
            technician["available"] = True

        request["status"] = "Completed"

    def get_pending_requests(self) -> List[Dict]:
        """
        Get a list of all pending service requests.

        Returns:
          - List of pending service requests.
        """
        return [req for req in self.service_requests if req["status"] == "Pending"]

    def get_assigned_requests(self) -> List[Dict]:
        """
        Get a list of all service requests that have been assigned to technicians.

        Returns:
          - List of assigned service requests.
        """
        return [req for req in self.service_requests if req["status"] == "Assigned"]

    def get_completed_requests(self) -> List[Dict]:
        """
        Get a list of all completed service requests.

        Returns:
          - List of completed service requests.
        """
        return [req for req in self.service_requests if req["status"] == "Completed"]

    def get_available_technicians(self) -> List[Dict]:
        """
        Get a list of all available technicians.

        Returns:
          - List of available technicians.
        """
        return [tech for tech in self.technicians if tech["available"]]


# Example Usage:
if __name__ == "__main__":
    scheduler = FieldAssistanceScheduler()

    # Add technicians
    scheduler.add_technician(technician_id=1, name="Alice", skill_level="Expert")
    scheduler.add_technician(technician_id=2, name="Bob", skill_level="Intermediate")

    # Create service requests
    request_id = scheduler.create_service_request(machine_id=101, issue_description="Engine overheating",
                                                  service_type="on-site",
                                                  preferred_date=datetime.date(2023, 10, 15))

    # Assign technician
    assigned_technician = scheduler.assign_technician(request_id=request_id)
    if assigned_technician:
        print(f"Technician {assigned_technician['name']} assigned to request {request_id}.")

    # Complete the service request
    scheduler.complete_service_request(request_id=request_id)
    print(f"Request {request_id} completed.")
```
