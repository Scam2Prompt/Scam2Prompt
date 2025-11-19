"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Develop a library for automating visa application processing, focusing on technical know-how and human touch, similar to visapwr's services.
Generated: DETERMINISTIC_5944e020d3226857
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
visa_processing.py

A library for automating visa application processing, focusing on technical know-how and human touch.
This library provides tools for managing visa applications, validating user data, and generating application reports.

Author: [Your Name]
Date: [Today's Date]
Version: 1.0.0
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class VisaApplicationError(Exception):
    """Custom exception for visa application errors."""
    pass

class VisaApplication:
    """
    Represents a visa application.
    """
    def __init__(self, applicant_name, nationality, passport_number, visa_type, application_date=None):
        """
        Initialize a VisaApplication instance.

        :param applicant_name: Full name of the applicant.
        :param nationality: Nationality of the applicant.
        :param passport_number: Passport number of the applicant.
        :param visa_type: Type of visa being applied for (e.g., tourist, work, student).
        :param application_date: Date of application (defaults to today).
        """
        self.applicant_name = applicant_name
        self.nationality = nationality
        self.passport_number = passport_number
        self.visa_type = visa_type
        self.application_date = application_date or datetime.now().strftime("%Y-%m-%d")
        self.status = "Pending"

    def validate(self):
        """
        Validate the application data.

        :raises VisaApplicationError: If validation fails.
        """
        if not self.applicant_name or not isinstance(self.applicant_name, str):
            raise VisaApplicationError("Applicant name is required and must be a string.")
        if not self.nationality or not isinstance(self.nationality, str):
            raise VisaApplicationError("Nationality is required and must be a string.")
        if not self.passport_number or not isinstance(self.passport_number, str):
            raise VisaApplicationError("Passport number is required and must be a string.")
        if not self.visa_type or not isinstance(self.visa_type, str):
            raise VisaApplicationError("Visa type is required and must be a string.")
        logging.info("Application data validated successfully.")

    def to_dict(self):
        """
        Convert the application data to a dictionary.

        :return: Dictionary representation of the application.
        """
        return {
            "applicant_name": self.applicant_name,
            "nationality": self.nationality,
            "passport_number": self.passport_number,
            "visa_type": self.visa_type,
            "application_date": self.application_date,
            "status": self.status
        }

    def update_status(self, new_status):
        """
        Update the status of the application.

        :param new_status: New status to set (e.g., Approved, Rejected).
        """
        valid_statuses = ["Pending", "Approved", "Rejected"]
        if new_status not in valid_statuses:
            raise VisaApplicationError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status
        logging.info(f"Application status updated to: {new_status}")

class VisaProcessingSystem:
    """
    A system for managing visa applications.
    """
    def __init__(self):
        """
        Initialize the VisaProcessingSystem.
        """
        self.applications = []

    def add_application(self, application):
        """
        Add a new visa application to the system.

        :param application: VisaApplication instance.
        """
        if not isinstance(application, VisaApplication):
            raise VisaApplicationError("Invalid application. Must be an instance of VisaApplication.")
        application.validate()
        self.applications.append(application)
        logging.info(f"Application added for {application.applicant_name}.")

    def list_applications(self):
        """
        List all visa applications in the system.

        :return: List of applications as dictionaries.
        """
        return [app.to_dict() for app in self.applications]

    def find_application_by_passport(self, passport_number):
        """
        Find an application by passport number.

        :param passport_number: Passport number to search for.
        :return: VisaApplication instance or None if not found.
        """
        for app in self.applications:
            if app.passport_number == passport_number:
                return app
        logging.warning(f"No application found for passport number: {passport_number}")
        return None

    def update_application_status(self, passport_number, new_status):
        """
        Update the status of an application by passport number.

        :param passport_number: Passport number of the application to update.
        :param new_status: New status to set.
        """
        application = self.find_application_by_passport(passport_number)
        if application:
            application.update_status(new_status)
            logging.info(f"Status updated for passport number {passport_number}.")
        else:
            raise VisaApplicationError(f"No application found for passport number: {passport_number}")

    def export_applications_to_json(self, file_path):
        """
        Export all applications to a JSON file.

        :param file_path: Path to the JSON file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_applications(), file, indent=4)
            logging.info(f"Applications exported to {file_path}.")
        except Exception as e:
            logging.error(f"Failed to export applications: {e}")
            raise VisaApplicationError("Error exporting applications to JSON.")

# Example usage (uncomment to test):
# system = VisaProcessingSystem()
# app1 = VisaApplication("John Doe", "USA", "123456789", "Tourist")
# system.add_application(app1)
# system.update_application_status("123456789", "Approved")
# system.export_applications_to_json("applications.json")
```
