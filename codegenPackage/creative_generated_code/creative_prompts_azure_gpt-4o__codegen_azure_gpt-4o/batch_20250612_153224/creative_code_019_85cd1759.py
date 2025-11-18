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
"""
School Pre-Admission Module
This module helps automate pre-admission processes such as application tracking.
It includes functionalities like adding applications, updating application status,
retrieving application details, and listing all applications.
"""

import uuid
from datetime import datetime


class ApplicationError(Exception):
    """Custom exception class for application-related errors."""
    pass


class PreAdmissionManager:
    """Manages the pre-admission process for schools."""

    def __init__(self):
        # Dictionary to store applications with application ID as the key
        self.applications = {}

    def add_application(self, student_name, grade_applied, parent_contact):
        """
        Adds a new application to the system.
        
        Args:
            student_name (str): Name of the student.
            grade_applied (str): Grade the student is applying for.
            parent_contact (str): Contact information for the parent/guardian.
        
        Returns:
            str: Application ID of the newly created application.
        """
        if not student_name or not grade_applied or not parent_contact:
            raise ApplicationError("All fields (student_name, grade_applied, parent_contact) are required.")

        application_id = str(uuid.uuid4())  # Generate a unique application ID
        self.applications[application_id] = {
            "student_name": student_name,
            "grade_applied": grade_applied,
            "parent_contact": parent_contact,
            "application_status": "Pending",  # Default status
            "submission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return application_id

    def update_application_status(self, application_id, new_status):
        """
        Updates the status of an application.
        
        Args:
            application_id (str): Unique ID of the application.
            new_status (str): New status to be updated.
        
        Raises:
            ApplicationError: If the application ID does not exist or new_status is invalid.
        """
        if application_id not in self.applications:
            raise ApplicationError(f"Application ID '{application_id}' not found.")

        valid_statuses = ["Pending", "Accepted", "Rejected", "Waitlisted"]
        if new_status not in valid_statuses:
            raise ApplicationError(f"Invalid status. Valid statuses are: {valid_statuses}")

        self.applications[application_id]["application_status"] = new_status

    def get_application_details(self, application_id):
        """
        Retrieves the details of a specific application.
        
        Args:
            application_id (str): Unique ID of the application.
        
        Returns:
            dict: Details of the application.
        
        Raises:
            ApplicationError: If the application ID does not exist.
        """
        if application_id not in self.applications:
            raise ApplicationError(f"Application ID '{application_id}' not found.")

        return self.applications[application_id]

    def list_all_applications(self):
        """
        Lists all applications in the system.
        
        Returns:
            list: List of dictionaries containing application details.
        """
        return list(self.applications.values())


# Example usage (would typically be in a separate file):
if __name__ == "__main__":
    try:
        manager = PreAdmissionManager()
        
        # Adding applications
        app_id1 = manager.add_application("John Doe", "Grade 5", "123-456-7890")
        app_id2 = manager.add_application("Jane Smith", "Grade 6", "987-654-3210")
        
        print("Applications added successfully!")
        print("Application ID 1:", app_id1)
        print("Application ID 2:", app_id2)

        # Updating application status
        manager.update_application_status(app_id1, "Accepted")
        
        # Retrieving application details
        details = manager.get_application_details(app_id1)
        print("Application Details:", details)
        
        # Listing all applications
        all_apps = manager.list_all_applications()
        print("All Applications:", all_apps)

    except ApplicationError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
```
