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
# job_tracker.py

class JobApplication:
    """Represents a job application."""

    def __init__(self, company, position, application_date, status="Applied"):
        """
        Initializes a JobApplication instance.

        Args:
            company (str): The company name.
            position (str): The job position.
            application_date (str): The date of application.
            status (str, optional): The current status. Defaults to "Applied".
        """
        self.company = company
        self.position = position
        self.application_date = application_date
        self.status = status

    def update_status(self, status):
        """Updates the status of the job application."""
        self.status = status

    def __str__(self):
        return f"{self.company} - {self.position} ({self.status})"


class JobTracker:
    """Manages multiple job applications."""

    def __init__(self):
        """Initializes a JobTracker instance."""
        self.applications = []

    def add_application(self, company, position, application_date):
        """
        Adds a new job application.

        Args:
            company (str): The company name.
            position (str): The job position.
            application_date (str): The date of application.
        """
        new_application = JobApplication(company, position, application_date)
        self.applications.append(new_application)

    def view_applications(self):
        """Displays all job applications."""
        for i, application in enumerate(self.applications, start=1):
            print(f"{i}. {application}")

    def update_application_status(self, application_index, status):
        """
        Updates the status of a job application.

        Args:
            application_index (int): The index of the application.
            status (str): The new status.

        Raises:
            IndexError: If the application index is out of range.
        """
        try:
            application_index -= 1  # adjust for 0-based indexing
            if application_index < 0:
                raise IndexError
            self.applications[application_index].update_status(status)
        except IndexError:
            print("Invalid application index.")

    def delete_application(self, application_index):
        """
        Deletes a job application.

        Args:
            application_index (int): The index of the application.

        Raises:
            IndexError: If the application index is out of range.
        """
        try:
            application_index -= 1  # adjust for 0-based indexing
            if application_index < 0:
                raise IndexError
            del self.applications[application_index]
        except IndexError:
            print("Invalid application index.")


def main():
    tracker = JobTracker()

    while True:
        print("\nJob Application Tracker")
        print("1. Add Job Application")
        print("2. View Job Applications")
        print("3. Update Job Application Status")
        print("4. Delete Job Application")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            company = input("Enter company name: ")
            position = input("Enter job position: ")
            application_date = input("Enter application date: ")
            tracker.add_application(company, position, application_date)
        elif choice == "2":
            tracker.view_applications()
        elif choice == "3":
            tracker.view_applications()
            application_index = int(input("Enter the application number to update: "))
            status = input("Enter new status: ")
            tracker.update_application_status(application_index, status)
        elif choice == "4":
            tracker.view_applications()
            application_index = int(input("Enter the application number to delete: "))
            tracker.delete_application(application_index)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
