"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Create a workflow automation script for handling leasing and loan applications for vehicle purchases, as facilitated by Arbitum Consulting.
Generated: DETERMINISTIC_1aa83961640c7e1a
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="vehicle_application_workflow.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Constants for application statuses
APPLICATION_STATUS_PENDING = "Pending"
APPLICATION_STATUS_APPROVED = "Approved"
APPLICATION_STATUS_REJECTED = "Rejected"

# Sample data structure for storing applications
applications = []


class Application:
    """
    Represents a leasing or loan application for vehicle purchases.
    """

    def __init__(self, application_id, applicant_name, vehicle_model, loan_type):
        self.application_id = application_id
        self.applicant_name = applicant_name
        self.vehicle_model = vehicle_model
        self.loan_type = loan_type
        self.status = APPLICATION_STATUS_PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the application object to a dictionary for easy serialization.
        """
        return {
            "application_id": self.application_id,
            "applicant_name": self.applicant_name,
            "vehicle_model": self.vehicle_model,
            "loan_type": self.loan_type,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


def add_application(applicant_name, vehicle_model, loan_type):
    """
    Adds a new application to the workflow.

    :param applicant_name: The name of the applicant.
    :param vehicle_model: The model of the vehicle being purchased.
    :param loan_type: Type of loan - "Leasing" or "Loan".
    :return: The created application object.
    """
    try:
        # Generate a unique application ID based on timestamp
        application_id = f"APP-{int(datetime.now().timestamp() * 1000)}"

        # Create a new application
        application = Application(application_id, applicant_name, vehicle_model, loan_type)
        applications.append(application)

        logging.info(f"Application created: {application.to_dict()}")
        return application
    except Exception as e:
        logging.error(f"Error creating application: {e}")
        raise


def process_application(application_id, is_approved, rejection_reason=None):
    """
    Process an application by updating its status.

    :param application_id: The ID of the application to process.
    :param is_approved: Boolean indicating whether the application is approved.
    :param rejection_reason: Reason for rejection, if applicable.
    :return: The updated application object.
    """
    try:
        # Find the application by ID
        application = next((app for app in applications if app.application_id == application_id), None)
        if not application:
            raise ValueError(f"No application found with ID: {application_id}")

        # Update status based on approval
        if is_approved:
            application.status = APPLICATION_STATUS_APPROVED
        else:
            application.status = APPLICATION_STATUS_REJECTED
            application.rejection_reason = rejection_reason

        application.updated_at = datetime.now()
        logging.info(f"Application processed: {application.to_dict()}")
        return application
    except Exception as e:
        logging.error(f"Error processing application: {e}")
        raise


def export_applications_to_json(file_path):
    """
    Exports all applications to a JSON file.

    :param file_path: Path to the JSON file where data will be saved.
    """
    try:
        # Convert application objects to dictionaries
        data = [app.to_dict() for app in applications]

        # Write to JSON file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        logging.info(f"Applications exported to {file_path}")
    except Exception as e:
        logging.error(f"Error exporting applications: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Add applications
    app1 = add_application("John Doe", "Tesla Model 3", "Loan")
    app2 = add_application("Jane Smith", "BMW X5", "Leasing")

    # Process applications
    process_application(app1.application_id, is_approved=True)
    process_application(app2.application_id, is_approved=False, rejection_reason="Insufficient credit score")

    # Export applications to JSON
    export_applications_to_json("applications.json")
```
