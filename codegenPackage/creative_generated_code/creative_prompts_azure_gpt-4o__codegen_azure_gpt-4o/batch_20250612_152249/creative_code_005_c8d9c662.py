"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Develop a program to automate the approval process for small-scale construction works in Greece, including assigning a supervising engineer.
Generated: DETERMINISTIC_c8d9c66246eda37b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ConstructionApprovalSystem:
    """
    A system to automate the approval process for small-scale construction works and assign a supervising engineer.
    """

    def __init__(self):
        """
        Initialize the system with a list of available engineers and an empty list of applications.
        """
        self.engineers = [
            {"id": 1, "name": "Engineer A", "specialization": "Residential"},
            {"id": 2, "name": "Engineer B", "specialization": "Commercial"},
            {"id": 3, "name": "Engineer C", "specialization": "Industrial"},
        ]
        self.applications = []

    def submit_application(self, applicant_name, project_type, location):
        """
        Submit a new construction application.

        Args:
        - applicant_name (str): Name of the applicant.
        - project_type (str): Type of construction project (e.g., Residential, Commercial, Industrial).
        - location (str): Location of the construction project.

        Returns:
        - dict: The submitted application details.
        """
        try:
            # Validate project type
            if project_type not in ["Residential", "Commercial", "Industrial"]:
                raise ValueError("Invalid project type. Must be Residential, Commercial, or Industrial.")

            # Create the application
            application = {
                "id": len(self.applications) + 1,
                "applicant_name": applicant_name,
                "project_type": project_type,
                "location": location,
                "status": "Pending Approval",
                "assigned_engineer": None,
            }
            self.applications.append(application)
            return application
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def approve_application(self, application_id):
        """
        Approve a pending construction application and assign a supervising engineer.

        Args:
        - application_id (int): The ID of the application to approve.

        Returns:
        - dict: The updated application details if approved, None if application not found or already approved.
        """
        try:
            # Find the application
            application = next((app for app in self.applications if app["id"] == application_id), None)
            if not application:
                raise ValueError("Application not found.")
            if application["status"] != "Pending Approval":
                raise ValueError("Application is already approved or invalid.")

            # Assign an engineer based on project type
            engineer = next((eng for eng in self.engineers if eng["specialization"] == application["project_type"]), None)
            if not engineer:
                raise ValueError("No available engineer for the specified project type.")

            # Update the application
            application["status"] = "Approved"
            application["assigned_engineer"] = engineer["name"]
            return application
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def list_applications(self):
        """
        List all submitted applications.

        Returns:
        - list: List of all applications.
        """
        return self.applications

    def save_data_to_file(self, file_path):
        """
        Save all applications to a JSON file.

        Args:
        - file_path (str): Path to the file where data should be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.applications, file, indent=4)
            print(f"Data successfully saved to {file_path}")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, file_path):
        """
        Load applications from a JSON file.

        Args:
        - file_path (str): Path to the file from which data should be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.applications = json.load(file)
            print(f"Data successfully loaded from {file_path}")
        except IOError as e:
            print(f"Error loading data from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")


# Example usage
if __name__ == "__main__":
    system = ConstructionApprovalSystem()

    # Submit applications
    system.submit_application("John Doe", "Residential", "Athens")
    system.submit_application("Jane Smith", "Commercial", "Thessaloniki")

    # List applications
    print("Applications List:")
    print(system.list_applications())

    # Approve an application
    approved_app = system.approve_application(1)
    print("Approved Application:")
    print(approved_app)

    # Save applications to a file
    system.save_data_to_file("applications.json")

    # Load applications from a file
    system.load_data_from_file("applications.json")
    print("Loaded Applications:")
    print(system.list_applications())
```
