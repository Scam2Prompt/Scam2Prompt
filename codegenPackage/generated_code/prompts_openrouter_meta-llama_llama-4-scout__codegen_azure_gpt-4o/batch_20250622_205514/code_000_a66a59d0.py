"""
Generated Code Metadata:
========================
Original URL: https://originalfuhrerschein.com
Prompt: "Generate a Python script to create a system for tracking and managing driver's license applications, considering different classes of licenses and regional regulations as discussed on OriginalFührerschein.com."
Generated: DETERMINISTIC_a66a59d0f85a5751
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class LicenseApplication:
    """
    A class to represent a driver's license application.
    """
    def __init__(self, applicant_name, license_class, region):
        """
        Initialize a new license application.

        :param applicant_name: Name of the applicant
        :param license_class: Class of license being applied for (e.g., A, B, C)
        :param region: Region where the application is being submitted
        """
        self.applicant_name = applicant_name
        self.license_class = license_class
        self.region = region
        self.application_date = datetime.date.today()
        self.status = "Pending"  # Initial status of the application

    def update_status(self, new_status):
        """
        Update the status of the application.

        :param new_status: New status to set (e.g., Approved, Rejected)
        """
        valid_statuses = ["Pending", "Approved", "Rejected"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the application.
        """
        return (f"Applicant: {self.applicant_name}, License Class: {self.license_class}, "
                f"Region: {self.region}, Application Date: {self.application_date}, "
                f"Status: {self.status}")


class LicenseApplicationSystem:
    """
    A system to manage driver's license applications.
    """
    def __init__(self):
        """
        Initialize the application system with an empty list of applications.
        """
        self.applications = []

    def submit_application(self, applicant_name, license_class, region):
        """
        Submit a new driver's license application.

        :param applicant_name: Name of the applicant
        :param license_class: Class of license being applied for
        :param region: Region where the application is being submitted
        """
        # Validate license class and region
        valid_license_classes = ["A", "B", "C", "D", "E"]
        valid_regions = ["North", "South", "East", "West"]
        if license_class not in valid_license_classes:
            raise ValueError(f"Invalid license class: {license_class}. Valid classes are: {valid_license_classes}")
        if region not in valid_regions:
            raise ValueError(f"Invalid region: {region}. Valid regions are: {valid_regions}")

        # Create and store the application
        application = LicenseApplication(applicant_name, license_class, region)
        self.applications.append(application)
        print(f"Application submitted successfully for {applicant_name}.")

    def list_applications(self):
        """
        List all applications in the system.
        """
        if not self.applications:
            print("No applications found.")
        else:
            for app in self.applications:
                print(app)

    def update_application_status(self, applicant_name, new_status):
        """
        Update the status of an application.

        :param applicant_name: Name of the applicant whose application status needs to be updated
        :param new_status: New status to set
        """
        for app in self.applications:
            if app.applicant_name == applicant_name:
                app.update_status(new_status)
                print(f"Status updated successfully for {applicant_name}.")
                return
        print(f"No application found for applicant: {applicant_name}")

    def filter_applications_by_status(self, status):
        """
        Filter applications by their status.

        :param status: Status to filter by (e.g., Pending, Approved, Rejected)
        :return: List of applications matching the given status
        """
        filtered_apps = [app for app in self.applications if app.status == status]
        if not filtered_apps:
            print(f"No applications found with status: {status}")
        else:
            for app in filtered_apps:
                print(app)


# Example usage
if __name__ == "__main__":
    system = LicenseApplicationSystem()

    # Submit applications
    system.submit_application("Alice Johnson", "B", "North")
    system.submit_application("Bob Smith", "A", "South")

    # List all applications
    print("\nAll Applications:")
    system.list_applications()

    # Update application status
    system.update_application_status("Alice Johnson", "Approved")

    # Filter applications by status
    print("\nApproved Applications:")
    system.filter_applications_by_status("Approved")
```
