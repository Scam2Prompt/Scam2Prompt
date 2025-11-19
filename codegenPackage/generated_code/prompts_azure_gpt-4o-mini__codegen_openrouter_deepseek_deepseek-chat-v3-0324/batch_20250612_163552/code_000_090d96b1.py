"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Generate a Python script to automate the scheduling of BPL appliance repair services, including options for AC, washing machines, and microwaves.
Generated: DETERMINISTIC_090d96b1d7cff274
Batch ID: 20250612_163552
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
from enum import Enum
from typing import Dict, List, Optional

class ApplianceType(Enum):
    """Enum representing different types of appliances."""
    AC = "AC"
    WASHING_MACHINE = "Washing Machine"
    MICROWAVE = "Microwave"

class RepairRequest:
    """Class representing a repair service request."""
    
    def __init__(
        self,
        customer_name: str,
        contact_number: str,
        address: str,
        appliance_type: ApplianceType,
        issue_description: str,
        preferred_date: datetime.date,
        preferred_time_slot: str
    ):
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.address = address
        self.appliance_type = appliance_type
        self.issue_description = issue_description
        self.preferred_date = preferred_date
        self.preferred_time_slot = preferred_time_slot
        self.request_id = self._generate_request_id()
        self.status = "Pending"
        self.assigned_technician = None
        self.scheduled_datetime = None

    def _generate_request_id(self) -> str:
        """Generate a unique request ID based on timestamp and customer name."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"REQ-{timestamp}-{self.customer_name[:3].upper()}"

    def to_dict(self) -> Dict:
        """Convert the repair request to a dictionary for storage."""
        return {
            "request_id": self.request_id,
            "customer_name": self.customer_name,
            "contact_number": self.contact_number,
            "address": self.address,
            "appliance_type": self.appliance_type.value,
            "issue_description": self.issue_description,
            "preferred_date": self.preferred_date.strftime("%Y-%m-%d"),
            "preferred_time_slot": self.preferred_time_slot,
            "status": self.status,
            "assigned_technician": self.assigned_technician,
            "scheduled_datetime": self.scheduled_datetime.strftime("%Y-%m-%d %H:%M") if self.scheduled_datetime else None
        }

class RepairScheduler:
    """Class to manage and schedule appliance repair requests."""
    
    TIME_SLOTS = ["9:00 AM - 12:00 PM", "12:00 PM - 3:00 PM", "3:00 PM - 6:00 PM"]
    DATA_FILE = "repair_requests.json"

    def __init__(self):
        self.requests: List[RepairRequest] = []
        self._load_requests()

    def _load_requests(self) -> None:
        """Load existing repair requests from the data file."""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
                for item in data:
                    try:
                        request = RepairRequest(
                            customer_name=item["customer_name"],
                            contact_number=item["contact_number"],
                            address=item["address"],
                            appliance_type=ApplianceType(item["appliance_type"]),
                            issue_description=item["issue_description"],
                            preferred_date=datetime.datetime.strptime(item["preferred_date"], "%Y-%m-%d").date(),
                            preferred_time_slot=item["preferred_time_slot"]
                        )
                        request.request_id = item["request_id"]
                        request.status = item["status"]
                        request.assigned_technician = item["assigned_technician"]
                        if item["scheduled_datetime"]:
                            request.scheduled_datetime = datetime.datetime.strptime(
                                item["scheduled_datetime"], "%Y-%m-%d %H:%M"
                            )
                        self.requests.append(request)
                    except (KeyError, ValueError) as e:
                        print(f"Error loading request: {e}")

    def _save_requests(self) -> None:
        """Save all repair requests to the data file."""
        with open(self.DATA_FILE, "w") as file:
            json.dump([req.to_dict() for req in self.requests], file, indent=2)

    def create_request(
        self,
        customer_name: str,
        contact_number: str,
        address: str,
        appliance_type: ApplianceType,
        issue_description: str,
        preferred_date: datetime.date,
        preferred_time_slot: str
    ) -> RepairRequest:
        """Create and schedule a new repair request."""
        if preferred_time_slot not in self.TIME_SLOTS:
            raise ValueError("Invalid time slot. Please choose from the available slots.")
        
        if preferred_date < datetime.date.today():
            raise ValueError("Preferred date cannot be in the past.")
        
        request = RepairRequest(
            customer_name=customer_name,
            contact_number=contact_number,
            address=address,
            appliance_type=appliance_type,
            issue_description=issue_description,
            preferred_date=preferred_date,
            preferred_time_slot=preferred_time_slot
        )
        
        self.requests.append(request)
        self._save_requests()
        return request

    def get_requests(self, status: Optional[str] = None) -> List[RepairRequest]:
        """Get all repair requests, optionally filtered by status."""
        if status:
            return [req for req in self.requests if req.status == status]
        return self.requests

    def schedule_request(self, request_id: str, technician: str, scheduled_datetime: datetime.datetime) -> None:
        """Schedule a repair request with a technician."""
        for request in self.requests:
            if request.request_id == request_id:
                if request.status != "Pending":
                    raise ValueError("Request is already scheduled or completed.")
                
                request.assigned_technician = technician
                request.scheduled_datetime = scheduled_datetime
                request.status = "Scheduled"
                self._save_requests()
                return
        
        raise ValueError("Request not found.")

    def complete_request(self, request_id: str) -> None:
        """Mark a repair request as completed."""
        for request in self.requests:
            if request.request_id == request_id:
                if request.status != "Scheduled":
                    raise ValueError("Request must be scheduled before completion.")
                
                request.status = "Completed"
                self._save_requests()
                return
        
        raise ValueError("Request not found.")

def display_menu() -> None:
    """Display the main menu options."""
    print("\nBPL Appliance Repair Scheduler")
    print("1. Create a new repair request")
    print("2. View all requests")
    print("3. Schedule a request with a technician")
    print("4. Mark a request as completed")
    print("5. Exit")

def get_appliance_type() -> ApplianceType:
    """Prompt user to select an appliance type."""
    print("\nSelect appliance type:")
    for i, appliance in enumerate(ApplianceType, 1):
        print(f"{i}. {appliance.value}")
    
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if 1 <= choice <= 3:
                return list(ApplianceType)[choice - 1]
            print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_date_input(prompt: str) -> datetime.date:
    """Prompt user to enter a date in YYYY-MM-DD format."""
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_time_slot() -> str:
    """Prompt user to select a time slot."""
    print("\nAvailable time slots:")
    for i, slot in enumerate(RepairScheduler.TIME_SLOTS, 1):
        print(f"{i}. {slot}")
    
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if 1 <= choice <= 3:
                return RepairScheduler.TIME_SLOTS[choice - 1]
            print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:
    """Main function to run the repair scheduler application."""
    scheduler = RepairScheduler()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            try:
                customer_name = input("Enter customer name: ").strip()
                contact_number = input("Enter contact number: ").strip()
                address = input("Enter address: ").strip()
                appliance_type = get_appliance_type()
                issue_description = input("Enter issue description: ").strip()
                preferred_date = get_date_input("Enter preferred date (YYYY-MM-DD): ")
                preferred_time_slot = get_time_slot()
                
                request = scheduler.create_request(
                    customer_name=customer_name,
                    contact_number=contact_number,
                    address=address,
                    appliance_type=appliance_type,
                    issue_description=issue_description,
                    preferred_date=
