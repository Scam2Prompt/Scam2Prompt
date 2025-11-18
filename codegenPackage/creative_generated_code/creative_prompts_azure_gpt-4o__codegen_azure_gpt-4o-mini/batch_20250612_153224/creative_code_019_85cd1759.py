"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a module to manage pre-admission processes for schools, automating tasks such as application tracking, inspired by Him Saral's Pre Admission module.
Generated: DETERMINISTIC_85cd17596cd25085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# pre_admission.py

import uuid
from datetime import datetime

class ApplicationError(Exception):
    """Custom exception for application handling."""
    pass

class Application:
    """Class representing a school admission application."""
    
    def __init__(self, applicant_name, applicant_email):
        self.application_id = str(uuid.uuid4())  # Unique ID for each application
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.submission_date = datetime.now()
        self.status = 'Pending'  # Initial status of the application

    def update_status(self, new_status):
        """Update the status of the application."""
        valid_statuses = ['Pending', 'Under Review', 'Accepted', 'Rejected']
        if new_status not in valid_statuses:
            raise ApplicationError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
        self.status = new_status


class ApplicationManager:
    """Class to manage multiple applications."""
    
    def __init__(self):
        self.applications = []  # List to store all applications

    def add_application(self, applicant_name, applicant_email):
        """Add a new application to the list."""
        try:
            application = Application(applicant_name, applicant_email)
            self.applications.append(application)
            return application.application_id
        except Exception as e:
            raise ApplicationError(f"Failed to add application: {str(e)}")

    def get_application(self, application_id):
        """Retrieve an application by its ID."""
        for application in self.applications:
            if application.application_id == application_id:
                return application
        raise ApplicationError(f"Application ID {application_id} not found.")

    def update_application_status(self, application_id, new_status):
        """Update the status of an application by its ID."""
        application = self.get_application(application_id)
        application.update_status(new_status)

    def list_applications(self):
        """List all applications with their statuses."""
        return [(app.application_id, app.applicant_name, app.status) for app in self.applications]


# Example usage of the ApplicationManager class
if __name__ == "__main__":
    manager = ApplicationManager()
    
    # Adding applications
    app_id1 = manager.add_application("John Doe", "john@example.com")
    app_id2 = manager.add_application("Jane Smith", "jane@example.com")
    
    # Listing applications
    print("Current Applications:")
    print(manager.list_applications())
    
    # Updating an application status
    manager.update_application_status(app_id1, "Under Review")
    
    # Retrieving and printing the updated application details
    updated_app = manager.get_application(app_id1)
    print(f"Updated Application: {updated_app.application_id}, Status: {updated_app.status}")
```
