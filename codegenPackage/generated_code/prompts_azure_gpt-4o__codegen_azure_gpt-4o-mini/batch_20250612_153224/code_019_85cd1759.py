"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a module to manage pre-admission processes for schools, automating tasks such as application tracking, inspired by Him Saral's Pre Admission module.
Generated: DETERMINISTIC_85cd17596cd25085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pre_admission.py

class Application:
    """
    Class to represent a student application for pre-admission.
    """

    def __init__(self, applicant_name, applicant_email):
        """
        Initializes a new application with the applicant's name and email.

        :param applicant_name: Name of the applicant
        :param applicant_email: Email of the applicant
        """
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email
        self.status = 'Pending'  # Initial status of the application

    def update_status(self, new_status):
        """
        Updates the status of the application.

        :param new_status: New status to set for the application
        """
        valid_statuses = ['Pending', 'Accepted', 'Rejected']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")


class ApplicationManager:
    """
    Class to manage multiple applications for pre-admission.
    """

    def __init__(self):
        """
        Initializes the ApplicationManager with an empty list of applications.
        """
        self.applications = []

    def add_application(self, applicant_name, applicant_email):
        """
        Adds a new application to the manager.

        :param applicant_name: Name of the applicant
        :param applicant_email: Email of the applicant
        :raises ValueError: If the application already exists
        """
        if any(app.applicant_email == applicant_email for app in self.applications):
            raise ValueError(f"Application for {applicant_email} already exists.")
        new_application = Application(applicant_name, applicant_email)
        self.applications.append(new_application)

    def update_application_status(self, applicant_email, new_status):
        """
        Updates the status of an existing application.

        :param applicant_email: Email of the applicant whose status is to be updated
        :param new_status: New status to set for the application
        :raises ValueError: If the application does not exist
        """
        application = self.find_application(applicant_email)
        application.update_status(new_status)

    def find_application(self, applicant_email):
        """
        Finds an application by applicant's email.

        :param applicant_email: Email of the applicant
        :return: Application object if found
        :raises ValueError: If the application does not exist
        """
        for app in self.applications:
            if app.applicant_email == applicant_email:
                return app
        raise ValueError(f"No application found for {applicant_email}")

    def list_applications(self):
        """
        Lists all applications with their statuses.

        :return: List of tuples containing applicant name and status
        """
        return [(app.applicant_name, app.status) for app in self.applications]


# Example usage
if __name__ == "__main__":
    manager = ApplicationManager()
    
    try:
        manager.add_application("John Doe", "john.doe@example.com")
        manager.add_application("Jane Smith", "jane.smith@example.com")
        
        print("Applications before status update:")
        print(manager.list_applications())
        
        manager.update_application_status("john.doe@example.com", "Accepted")
        
        print("Applications after status update:")
        print(manager.list_applications())
        
    except ValueError as e:
        print(f"Error: {e}")
```
