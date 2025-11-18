"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Write a program to simulate digital visa application workflows, incorporating visapwr's focus on balancing security and customer expectations.
Generated: DETERMINISTIC_253d0980f8b4e072
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime

class VisaApplication:
    """
    Represents a digital visa application.
    """
    def __init__(self, applicant_name, applicant_country, applicant_passport_number):
        """
        Initializes the visa application with basic applicant information.
        """
        self.application_id = str(uuid.uuid4())  # Unique identifier for the application
        self.applicant_name = applicant_name
        self.applicant_country = applicant_country
        self.applicant_passport_number = applicant_passport_number
        self.application_date = datetime.datetime.now()  # Timestamp of application creation
        self.status = "Pending"  # Initial status of the visa application

    def update_status(self, new_status):
        """
        Updates the status of the visa application.
        """
        if new_status not in ["Pending", "Under Review", "Approved", "Rejected"]:
            raise ValueError("Invalid status. Must be one of: Pending, Under Review, Approved, Rejected.")
        self.status = new_status


class VisaApplicationSystem:
    """
    Simulates a visa application workflow system with a focus on security and customer expectations.
    """
    def __init__(self):
        """
        Initializes the visa application system.
        """
        self.applications = {}  # Store applications as a dictionary {application_id: VisaApplication}

    def create_application(self, applicant_name, applicant_country, applicant_passport_number):
        """
        Creates a new visa application and returns its unique ID.
        """
        if not (applicant_name and applicant_country and applicant_passport_number):
            raise ValueError("All applicant details (name, country, passport number) must be provided.")
        
        application = VisaApplication(applicant_name, applicant_country, applicant_passport_number)
        self.applications[application.application_id] = application
        return application.application_id

    def view_application(self, application_id):
        """
        Retrieves and displays an application by its ID.
        """
        application = self.applications.get(application_id)
        if not application:
            raise ValueError(f"No application found with ID: {application_id}")

        return {
            "Application ID": application.application_id,
            "Applicant Name": application.applicant_name,
            "Applicant Country": application.applicant_country,
            "Applicant Passport Number": application.applicant_passport_number,
            "Application Date": application.application_date,
            "Status": application.status
        }

    def update_application_status(self, application_id, new_status):
        """
        Updates the status of an application identified by its ID.
        """
        application = self.applications.get(application_id)
        if not application:
            raise ValueError(f"No application found with ID: {application_id}")
        
        application.update_status(new_status)

    def list_all_applications(self):
        """
        Lists all visa applications in the system.
        """
        return [self.view_application(app_id) for app_id in self.applications]


# Example usage of the system
if __name__ == "__main__":
    try:
        system = VisaApplicationSystem()

        # Create a new application
        app_id = system.create_application("John Doe", "USA", "P123456789")
        print(f"Application created with ID: {app_id}")

        # View the application
        print("Viewing application:")
        print(system.view_application(app_id))

        # Update application status
        system.update_application_status(app_id, "Under Review")
        print("Updated application status:")
        print(system.view_application(app_id))

        # List all applications
        print("All applications:")
        print(system.list_all_applications())
    except Exception as e:
        print(f"Error: {str(e)}")
```
