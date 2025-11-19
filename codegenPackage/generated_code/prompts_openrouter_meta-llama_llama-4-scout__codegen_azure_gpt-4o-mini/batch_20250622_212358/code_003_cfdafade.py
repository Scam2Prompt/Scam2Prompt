"""
Generated Code Metadata:
========================
Original URL: https://freejobsindubai.com
Prompt: Create a job application tracker for managing multiple job applications, including positions like DULSCO Careers, DOCIB Pharmacy, or MILAHA Qatar.
Generated: DETERMINISTIC_cfdafadeb8595064
Batch ID: 20250622_212358
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

class JobApplication:
    """Class to represent a job application."""
    
    def __init__(self, company, position, status, date_applied):
        """
        Initialize a new job application.

        :param company: Name of the company
        :param position: Job position applied for
        :param status: Current status of the application (e.g., 'Applied', 'Interview', 'Rejected', 'Offer')
        :param date_applied: Date when the application was submitted
        """
        self.company = company
        self.position = position
        self.status = status
        self.date_applied = date_applied

    def to_dict(self):
        """Convert the job application to a dictionary."""
        return {
            'company': self.company,
            'position': self.position,
            'status': self.status,
            'date_applied': self.date_applied.isoformat()
        }

class JobApplicationTracker:
    """Class to manage a collection of job applications."""
    
    def __init__(self, filename='job_applications.json'):
        """
        Initialize the job application tracker.

        :param filename: Name of the file to store job applications
        """
        self.filename = filename
        self.applications = []
        self.load_applications()

    def load_applications(self):
        """Load job applications from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                applications_data = json.load(file)
                for app in applications_data:
                    app['date_applied'] = datetime.fromisoformat(app['date_applied'])
                    self.applications.append(JobApplication(**app))
        except FileNotFoundError:
            # File does not exist, starting with an empty list
            self.applications = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file. Starting fresh.")
            self.applications = []

    def save_applications(self):
        """Save job applications to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([app.to_dict() for app in self.applications], file, indent=4)

    def add_application(self, company, position, status='Applied'):
        """
        Add a new job application.

        :param company: Name of the company
        :param position: Job position applied for
        :param status: Current status of the application
        """
        new_application = JobApplication(company, position, status, datetime.now())
        self.applications.append(new_application)
        self.save_applications()

    def update_application(self, index, status):
        """
        Update the status of an existing job application.

        :param index: Index of the application to update
        :param status: New status of the application
        """
        if 0 <= index < len(self.applications):
            self.applications[index].status = status
            self.save_applications()
        else:
            print("Error: Application index out of range.")

    def list_applications(self):
        """List all job applications."""
        for index, app in enumerate(self.applications):
            print(f"{index}: {app.company} - {app.position} - {app.status} - {app.date_applied.date()}")

if __name__ == "__main__":
    tracker = JobApplicationTracker()

    # Example usage
    tracker.add_application("DULSCO Careers", "HR Manager")
    tracker.add_application("DOCIB Pharmacy", "Pharmacist")
    tracker.add_application("MILAHA Qatar", "Logistics Coordinator")

    print("Current Job Applications:")
    tracker.list_applications()

    # Update the status of the first application
    tracker.update_application(0, "Interview")
    
    print("\nUpdated Job Applications:")
    tracker.list_applications()
```
