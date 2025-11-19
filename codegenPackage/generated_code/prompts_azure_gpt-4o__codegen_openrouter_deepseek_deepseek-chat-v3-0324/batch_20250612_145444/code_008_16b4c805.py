"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: Create a script that integrates university registration functionality for establishing Bridges to Professions branches, allowing users to apply as directors or team leads.
Generated: DETERMINISTIC_16b4c805c0c95269
Batch ID: 20250612_145444
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
from enum import Enum
from typing import Dict, List, Optional, Tuple

class ApplicationStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class UserRole(Enum):
    DIRECTOR = "Director"
    TEAM_LEAD = "Team Lead"

class Application:
    """Represents a user's application to become a director or team lead."""
    
    def __init__(
        self,
        user_id: str,
        full_name: str,
        email: str,
        university: str,
        role: UserRole,
        experience: str,
        motivation: str,
        application_date: Optional[datetime] = None,
        status: ApplicationStatus = ApplicationStatus.PENDING,
    ):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.university = university
        self.role = role
        self.experience = experience
        self.motivation = motivation
        self.application_date = application_date or datetime.now()
        self.status = status

    def to_dict(self) -> Dict:
        """Convert the application to a dictionary for storage."""
        return {
            "user_id": self.user_id,
            "full_name": self.full_name,
            "email": self.email,
            "university": self.university,
            "role": self.role.value,
            "experience": self.experience,
            "motivation": self.motivation,
            "application_date": self.application_date.isoformat(),
            "status": self.status.value,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Application':
        """Create an Application instance from a dictionary."""
        return cls(
            user_id=data["user_id"],
            full_name=data["full_name"],
            email=data["email"],
            university=data["university"],
            role=UserRole(data["role"]),
            experience=data["experience"],
            motivation=data["motivation"],
            application_date=datetime.fromisoformat(data["application_date"]),
            status=ApplicationStatus(data["status"]),
        )

class UniversityRegistrationSystem:
    """Handles university registration for Bridges to Professions branches."""
    
    def __init__(self, storage_file: str = "applications.json"):
        self.storage_file = storage_file
        self.applications: Dict[str, Application] = {}
        self._load_applications()

    def _load_applications(self) -> None:
        """Load applications from the storage file."""
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                self.applications = {
                    app_id: Application.from_dict(app_data)
                    for app_id, app_data in data.items()
                }
        except FileNotFoundError:
            self.applications = {}
        except json.JSONDecodeError:
            raise ValueError("Invalid data in storage file")

    def _save_applications(self) -> None:
        """Save applications to the storage file."""
        with open(self.storage_file, "w") as file:
            json.dump(
                {app_id: app.to_dict() for app_id, app in self.applications.items()},
                file,
                indent=2,
            )

    def submit_application(
        self,
        user_id: str,
        full_name: str,
        email: str,
        university: str,
        role: UserRole,
        experience: str,
        motivation: str,
    ) -> str:
        """Submit a new application and return the application ID."""
        if not all([user_id, full_name, email, university, role, experience, motivation]):
            raise ValueError("All fields are required")
        
        application = Application(
            user_id=user_id,
            full_name=full_name,
            email=email,
            university=university,
            role=role,
            experience=experience,
            motivation=motivation,
        )
        
        application_id = f"app_{datetime.now().timestamp()}"
        self.applications[application_id] = application
        self._save_applications()
        
        return application_id

    def get_application(self, application_id: str) -> Optional[Application]:
        """Retrieve an application by its ID."""
        return self.applications.get(application_id)

    def get_applications_by_university(self, university: str) -> List[Application]:
        """Retrieve all applications for a specific university."""
        return [
            app for app in self.applications.values()
            if app.university.lower() == university.lower()
        ]

    def update_application_status(
        self, application_id: str, status: ApplicationStatus
    ) -> bool:
        """Update the status of an application."""
        if application_id not in self.applications:
            return False
        
        self.applications[application_id].status = status
        self._save_applications()
        return True

    def get_pending_applications(self) -> List[Tuple[str, Application]]:
        """Retrieve all pending applications."""
        return [
            (app_id, app) for app_id, app in self.applications.items()
            if app.status == ApplicationStatus.PENDING
        ]

# Example usage
if __name__ == "__main__":
    system = UniversityRegistrationSystem()
    
    # Submit an application
    app_id = system.submit_application(
        user_id="user123",
        full_name="John Doe",
        email="john.doe@example.com",
        university="Tech University",
        role=UserRole.DIRECTOR,
        experience="5 years in education",
        motivation="I want to help students bridge to professions",
    )
    print(f"Application submitted with ID: {app_id}")
    
    # Get application status
    application = system.get_application(app_id)
    if application:
        print(f"Application status: {application.status.value}")
    
    # Update application status
    system.update_application_status(app_id, ApplicationStatus.APPROVED)
    print("Application status updated")
    
    # Get pending applications
    pending = system.get_pending_applications()
    print(f"Pending applications: {len(pending)}")
```
