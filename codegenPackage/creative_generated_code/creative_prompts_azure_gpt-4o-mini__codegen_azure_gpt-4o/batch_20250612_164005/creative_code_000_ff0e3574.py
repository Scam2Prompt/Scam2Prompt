"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Generate a Python script to automate the application process for the Professor Substitute positions in Geography at IGEOG/UERJ, including handling document submissions and tracking application statuses.
Generated: DETERMINISTIC_ff0e3574f088f33a
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime


class Application:
    """
    A class to represent an application for the Professor Substitute position.
    Handles document submissions and application statuses.
    """

    def __init__(self, applicant_name, department="Geography", position="Professor Substitute"):
        """
        Initializes an application instance.
        
        Args:
            applicant_name (str): Name of the applicant.
            department (str): Department name. Default is "Geography".
            position (str): Job position. Default is "Professor Substitute".
        """
        self.applicant_name = applicant_name
        self.department = department
        self.position = position
        self.submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.documents = {}
        self.status = "Pending"  # Initial status of the application

    def add_document(self, doc_name, file_path):
        """
        Adds a document to the application.
        
        Args:
            doc_name (str): Name of the document.
            file_path (str): Path to the document file.
            
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        self.documents[doc_name] = file_path

    def update_status(self, new_status):
        """
        Updates the status of the application.
        
        Args:
            new_status (str): New status to set for the application.
        """
        self.status = new_status

    def to_dict(self):
        """
        Converts the application data into a dictionary format.
        
        Returns:
            dict: Dictionary representation of the application.
        """
        return {
            "Applicant Name": self.applicant_name,
            "Department": self.department,
            "Position": self.position,
            "Submission Date": self.submission_date,
            "Documents": self.documents,
            "Status": self.status
        }


class ApplicationSystem:
    """
    A system to manage applications for Professor Substitute positions.
    Handles creating, saving, and tracking applications.
    """

    def __init__(self, storage_file="applications.json"):
        """
        Initializes the application system.
        
        Args:
            storage_file (str): File to store application data. Default is 'applications.json'.
        """
        self.storage_file = storage_file
        self.applications = self._load_applications()

    def _load_applications(self):
        """
        Loads applications from the storage file.
        
        Returns:
            dict: Dictionary of applications data.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                return json.load(file)
        return {}

    def save_applications(self):
        """
        Saves applications to the storage file.
        """
        with open(self.storage_file, "w") as file:
            json.dump(self.applications, file, indent=4)

    def create_application(self, applicant_name):
        """
        Creates a new application.
        
        Args:
            applicant_name (str): Name of the applicant.
            
        Returns:
            Application: The created application instance.
        """
        application = Application(applicant_name)
        self.applications[applicant_name] = application.to_dict()
        self.save_applications()
        return application

    def update_application_status(self, applicant_name, new_status):
        """
        Updates the status of an existing application.
        
        Args:
            applicant_name (str): Name of the applicant.
            new_status (str): New status to set.
            
        Raises:
            KeyError: If the application does not exist.
        """
        if applicant_name not in self.applications:
            raise KeyError(f"Application for '{applicant_name}' not found.")
        
        self.applications[applicant_name]["Status"] = new_status
        self.save_applications()

    def get_application(self, applicant_name):
        """
        Retrieves application details.
        
        Args:
            applicant_name (str): Name of the applicant.
            
        Returns:
            dict: Dictionary representation of the application.
            
        Raises:
            KeyError: If the application does not exist.
        """
        if applicant_name not in self.applications:
            raise KeyError(f"Application for '{applicant_name}' not found.")
        
        return self.applications[applicant_name]


# Example usage:
if __name__ == "__main__":
    system = ApplicationSystem()

    try:
        # Create a new application
        new_application = system.create_application(applicant_name="John Doe")
        print(f"Application created for {new_application.applicant_name}.")

        # Add documents to the application
        new_application.add_document("Curriculum Vitae", "path/to/cv.pdf")
        new_application.add_document("Cover Letter", "path/to/cover_letter.pdf")
        
        # Update application status
        system.update_application_status("John Doe", "Under Review")
        print(f"Application status updated for John Doe.")

        # Retrieve application details
        application_details = system.get_application("John Doe")
        print(f"Application Details: {application_details}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
