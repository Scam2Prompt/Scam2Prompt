"""
Generated Code Metadata:
========================
Original URL: https://nazarethhomeschool.in
Prompt: Write a code to manage student admissions for a school, including tracking application forms and selection tests.
Generated: DETERMINISTIC_1f9992050d5c6fa0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
import uuid
import json
import os


@dataclass
class StudentApplication:
    """Dataclass representing a student application."""
    application_id: str
    first_name: str
    last_name: str
    birth_date: str
    address: str
    previous_school: str
    application_date: str
    test_score: Optional[float] = None
    admission_status: str = "PENDING"  # PENDING, ACCEPTED, REJECTED

    def to_dict(self) -> dict:
        """Convert the application to a dictionary."""
        return {
            "application_id": self.application_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "address": self.address,
            "previous_school": self.previous_school,
            "application_date": self.application_date,
            "test_score": self.test_score,
            "admission_status": self.admission_status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'StudentApplication':
        """Create an application from a dictionary."""
        return cls(
            application_id=data["application_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            address=data["address"],
            previous_school=data["previous_school"],
            application_date=data["application_date"],
            test_score=data.get("test_score"),
            admission_status=data.get("admission_status", "PENDING")
        )


class AdmissionSystem:
    """Class to manage student admissions."""
    
    def __init__(self, storage_file: str = "admissions.json"):
        """Initialize the admission system with storage file."""
        self.storage_file = storage_file
        self.applications: List[StudentApplication] = []
        self._load_applications()

    def _load_applications(self) -> None:
        """Load applications from the storage file."""
        if not os.path.exists(self.storage_file):
            self.applications = []
            return

        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.applications = [StudentApplication.from_dict(app) for app in data]
        except (json.JSONDecodeError, IOError):
            self.applications = []

    def _save_applications(self) -> None:
        """Save applications to the storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([app.to_dict() for app in self.applications], f, indent=2)
        except IOError as e:
            print(f"Error saving applications: {e}")

    def submit_application(self, first_name: str, last_name: str, birth_date: str,
                          address: str, previous_school: str) -> StudentApplication:
        """Submit a new application."""
        application_id = str(uuid.uuid4())
        application_date = datetime.datetime.now().strftime("%Y-%m-%d")
        application = StudentApplication(
            application_id=application_id,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            address=address,
            previous_school=previous_school,
            application_date=application_date
        )
        self.applications.append(application)
        self._save_applications()
        return application

    def record_test_score(self, application_id: str, score: float) -> Optional[StudentApplication]:
        """Record a test score for an application."""
        for app in self.applications:
            if app.application_id == application_id:
                app.test_score = score
                self._save_applications()
                return app
        return None

    def update_admission_status(self, application_id: str, status: str) -> Optional[StudentApplication]:
        """Update the admission status of an application."""
        valid_statuses = ["PENDING", "ACCEPTED", "REJECTED"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        for app in self.applications:
            if app.application_id == application_id:
                app.admission_status = status
                self._save_applications()
                return app
        return None

    def get_application(self, application_id: str) -> Optional[StudentApplication]:
        """Get an application by ID."""
        for app in self.applications:
            if app.application_id == application_id:
                return app
        return None

    def get_all_applications(self) -> List[StudentApplication]:
        """Get all applications."""
        return self.applications

    def get_applications_by_status(self, status: str) -> List[StudentApplication]:
        """Get applications filtered by status."""
        valid_statuses = ["PENDING", "ACCEPTED", "REJECTED"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        return [app for app in self.applications if app.admission_status == status]

    def delete_application(self, application_id: str) -> bool:
        """Delete an application by ID."""
        for i, app in enumerate(self.applications):
            if app.application_id == application_id:
                del self.applications[i]
                self._save_applications()
                return True
        return False


# Example usage
if __name__ == "__main__":
    system = AdmissionSystem()
    
    # Submit a new application
    app = system.submit_application(
        first_name="John",
        last_name="Doe",
        birth_date="2005-05-15",
        address="123 Main St",
        previous_school="ABC Elementary"
    )
    print(f"Submitted application: {app.application_id}")

    # Record test score
    updated_app = system.record_test_score(app.application_id, 85.5)
    if updated_app:
        print(f"Recorded test score: {updated_app.test_score}")

    # Update admission status
    accepted_app = system.update_admission_status(app.application_id, "ACCEPTED")
    if accepted_app:
        print(f"Updated status to: {accepted_app.admission_status}")

    # Get all applications
    all_apps = system.get_all_applications()
    print(f"Total applications: {len(all_apps)}")
```
