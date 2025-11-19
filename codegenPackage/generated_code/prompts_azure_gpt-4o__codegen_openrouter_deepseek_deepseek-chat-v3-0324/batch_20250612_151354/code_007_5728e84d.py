"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Write a script to schedule and manage fundraising activities, including assigning volunteers and tracking progress, inspired by CRM.f's activity planning tools.
Generated: DETERMINISTIC_5728e84d86fb2fd2
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass, field
import json
import uuid
import os

class ActivityStatus(Enum):
    PLANNED = "Planned"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Volunteer:
    def __init__(self, volunteer_id: str, name: str, email: str, phone: str):
        self.volunteer_id = volunteer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        return {
            "volunteer_id": self.volunteer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Volunteer':
        return cls(
            volunteer_id=data["volunteer_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )

@dataclass
class FundraisingActivity:
    activity_id: str
    name: str
    description: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    target_amount: float
    status: ActivityStatus = ActivityStatus.PLANNED
    volunteers: List[Volunteer] = field(default_factory=list)
    progress: float = 0.0
    notes: str = ""

    def add_volunteer(self, volunteer: Volunteer) -> None:
        self.volunteers.append(volunteer)

    def remove_volunteer(self, volunteer_id: str) -> bool:
        for i, volunteer in enumerate(self.volunteers):
            if volunteer.volunteer_id == volunteer_id:
                self.volunteers.pop(i)
                return True
        return False

    def update_progress(self, progress: float) -> None:
        if 0 <= progress <= 100:
            self.progress = progress
            if progress == 100:
                self.status = ActivityStatus.COMPLETED
            elif progress > 0:
                self.status = ActivityStatus.IN_PROGRESS

    def to_dict(self) -> Dict:
        return {
            "activity_id": self.activity_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "target_amount": self.target_amount,
            "status": self.status.value,
            "volunteers": [volunteer.to_dict() for volunteer in self.volunteers],
            "progress": self.progress,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'FundraisingActivity':
        return cls(
            activity_id=data["activity_id"],
            name=data["name"],
            description=data["description"],
            start_date=datetime.datetime.fromisoformat(data["start_date"]),
            end_date=datetime.datetime.fromisoformat(data["end_date"]),
            target_amount=data["target_amount"],
            status=ActivityStatus(data["status"]),
            volunteers=[Volunteer.from_dict(v) for v in data["volunteers"]],
            progress=data["progress"],
            notes=data.get("notes", "")
        )

class FundraisingManager:
    def __init__(self, storage_file: str = "fundraising_data.json"):
        self.storage_file = storage_file
        self.activities: Dict[str, FundraisingActivity] = {}
        self.load_data()

    def add_activity(self, activity: FundraisingActivity) -> None:
        self.activities[activity.activity_id] = activity
        self.save_data()

    def get_activity(self, activity_id: str) -> Optional[FundraisingActivity]:
        return self.activities.get(activity_id)

    def update_activity(self, activity_id: str, **kwargs) -> bool:
        activity = self.get_activity(activity_id)
        if not activity:
            return False

        for key, value in kwargs.items():
            if hasattr(activity, key):
                setattr(activity, key, value)
        
        self.save_data()
        return True

    def delete_activity(self, activity_id: str) -> bool:
        if activity_id in self.activities:
            del self.activities[activity_id]
            self.save_data()
            return True
        return False

    def list_activities(self, status: Optional[ActivityStatus] = None) -> List[FundraisingActivity]:
        if status:
            return [activity for activity in self.activities.values() if activity.status == status]
        return list(self.activities.values())

    def save_data(self) -> None:
        data = {
            "activities": [activity.to_dict() for activity in self.activities.values()]
        }
        try:
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self) -> None:
        if not os.path.exists(self.storage_file):
            return

        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.activities = {
                    activity["activity_id"]: FundraisingActivity.from_dict(activity)
                    for activity in data["activities"]
                }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

def generate_id() -> str:
    return str(uuid.uuid4())

def main_menu(manager: FundraisingManager) -> None:
    while True:
        print("\nFundraising Activity Manager")
        print("1. Create new activity")
        print("2. List all activities")
        print("3. View/Edit activity")
        print("4. Delete activity")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_activity(manager)
        elif choice == "2":
            list_activities(manager)
        elif choice == "3":
            view_edit_activity(manager)
        elif choice == "4":
            delete_activity(manager)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_activity(manager: FundraisingManager) -> None:
    print("\nCreate New Fundraising Activity")
    name = input("Activity name: ")
    description = input("Description: ")
    
    while True:
        try:
            start_date = datetime.datetime.fromisoformat(input("Start date (YYYY-MM-DD): "))
            end_date = datetime.datetime.fromisoformat(input("End date (YYYY-MM-DD): "))
            if end_date < start_date:
                print("End date must be after start date.")
                continue
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    target_amount = float(input("Target amount: "))
    
    activity = FundraisingActivity(
        activity_id=generate_id(),
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
        target_amount=target_amount
    )
    
    manager.add_activity(activity)
    print(f"Activity '{name}' created successfully!")

def list_activities(manager: FundraisingManager) -> None:
    print("\nList of Fundraising Activities")
    activities = manager.list_activities()
    
    if not activities:
        print("No activities found.")
        return
    
    for i, activity in enumerate(activities, 1):
        print(f"{i}. {activity.name} ({activity.status.value}) - Progress: {activity.progress}%")

def view_edit_activity(manager: FundraisingManager) -> None:
    activity_id = input("Enter activity ID: ")
    activity = manager.get_activity(activity_id)
    
    if not activity:
        print("Activity not found.")
        return
    
    while True:
        print(f"\nActivity: {activity.name}")
        print(f"Status: {activity.status.value}")
        print(f"Progress: {activity.progress}%")
        print(f"Description: {activity.description}")
        print(f"Dates: {activity.start_date.date()} to {activity.end_date.date()}")
        print(f"Target: ${activity.target_amount:.2f}")
        print("\n1. Update progress")
        print("2. Add volunteer")
        print("3. Remove volunteer")
        print("4. Update notes")
        print("5. Change status")
        print("6. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            progress = float(input("Enter new progress (0-100): "))
            activity.update_progress(progress)
            manager.save_data()
        elif choice == "2":
            name = input("Volunteer name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            volunteer = Volunteer(
                volunteer_id=generate_id(),
                name=name,
                email=email,
                phone=phone
            )
            activity.add_volunteer(volunteer)
            manager
