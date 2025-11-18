"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Create a workflow for issuing building permits in Greece, including steps for submitting documentation, approval, and assigning a supervising engineer.
Generated: DETERMINISTIC_8b75e46269ccbbf7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BuildingPermitWorkflow:
    """
    A class to represent a workflow for issuing building permits in Greece.
    """

    def __init__(self):
        self.applications = []  # List to store building permit applications

    def submit_application(self, applicant_name, documentation):
        """
        Submit a building permit application.

        Args:
            applicant_name (str): The name of the applicant.
            documentation (dict): A dictionary containing necessary documents.
        
        Raises:
            ValueError: If documentation is incomplete.
        """
        if not self.validate_documentation(documentation):
            raise ValueError("Incomplete documentation provided.")

        application = {
            'applicant_name': applicant_name,
            'documentation': documentation,
            'status': 'Submitted',
            'supervising_engineer': None,
        }
        self.applications.append(application)
        return application

    def validate_documentation(self, documentation):
        """
        Validate the provided documentation.

        Args:
            documentation (dict): A dictionary containing necessary documents.

        Returns:
            bool: True if documentation is complete, False otherwise.
        """
        required_docs = ['site_plan', 'construction_plans', 'ownership_proof']
        return all(doc in documentation for doc in required_docs)

    def approve_application(self, application_index):
        """
        Approve a building permit application.

        Args:
            application_index (int): The index of the application in the list of applications.
        
        Raises:
            IndexError: If the application index is out of range.
        """
        if application_index < 0 or application_index >= len(self.applications):
            raise IndexError("Application index out of range.")

        application = self.applications[application_index]
        application['status'] = 'Approved'
        return application

    def assign_supervising_engineer(self, application_index, engineer_name):
        """
        Assign a supervising engineer to an approved application.

        Args:
            application_index (int): The index of the application in the list of applications.
            engineer_name (str): The name of the supervising engineer.
        
        Raises:
            IndexError: If the application index is out of range.
            ValueError: If the application is not approved.
        """
        if application_index < 0 or application_index >= len(self.applications):
            raise IndexError("Application index out of range.")

        application = self.applications[application_index]
        if application['status'] != 'Approved':
            raise ValueError("Only approved applications can have a supervising engineer assigned.")

        application['supervising_engineer'] = engineer_name
        return application

    def get_applications(self):
        """
        Retrieve the list of applications.

        Returns:
            List[dict]: A list of all applications with their current status.
        """
        return self.applications


# Example usage:
if __name__ == "__main__":
    workflow = BuildingPermitWorkflow()
    
    # Submit an application
    try:
        docs = {
            'site_plan': 'site_plan.pdf',
            'construction_plans': 'construction_plans.pdf',
            'ownership_proof': 'ownership_proof.pdf'
        }
        application = workflow.submit_application('John Doe', docs)
        print("Application submitted:", application)

        # Approve the application
        approved_application = workflow.approve_application(0)
        print("Application approved:", approved_application)

        # Assign a supervising engineer
        assigned_application = workflow.assign_supervising_engineer(0, 'Engineer A')
        print("Supervising engineer assigned:", assigned_application)

    except (ValueError, IndexError) as e:
        print("Error:", e)
```
