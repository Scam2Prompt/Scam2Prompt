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
import uuid
from datetime import datetime

# Define custom exceptions
class PermitError(Exception):
    """Base class for permit-related errors."""
    pass

class InvalidDocumentError(PermitError):
    """Raised when submitted documents are invalid."""
    pass

class ApprovalError(PermitError):
    """Raised when approval fails."""
    pass

class SupervisingEngineerError(PermitError):
    """Raised when assigning a supervising engineer fails."""
    pass


# Define a function for submitting documentation
def submit_documentation(documents):
    """
    Simulates the submission of required documentation.
    Args:
        documents (list): A list of document names submitted.
    Returns:
        bool: True if all required documents are submitted, False otherwise.
    Raises:
        InvalidDocumentError: If required documents are not submitted.
    """
    required_documents = {"building_plan", "ownership_title", "environmental_impact_study"}
    
    # Check if all required documents are present
    missing_documents = required_documents - set(documents)
    if missing_documents:
        raise InvalidDocumentError(f"Missing required documents: {', '.join(missing_documents)}")
    return True


# Define a function for approval
def approve_application(application_id):
    """
    Simulates approval of the building permit application.
    Args:
        application_id (str): The unique ID of the application.
    Returns:
        bool: True if approved, False otherwise.
    Raises:
        ApprovalError: If the application cannot be approved.
    """
    # Simulating approval process
    if not application_id:
        raise ApprovalError("Invalid application ID.")
    return True


# Define a function to assign a supervising engineer
def assign_supervising_engineer(project_id, engineer_name):
    """
    Simulates the assignment of a supervising engineer to the project.
    Args:
        project_id (str): The unique ID of the project.
        engineer_name (str): Name of the supervising engineer.
    Returns:
        dict: Details of the assignment.
    Raises:
        SupervisingEngineerError: If assignment fails.
    """
    if not project_id or not engineer_name:
        raise SupervisingEngineerError("Invalid project ID or engineer name.")
    
    assignment_details = {
        "project_id": project_id,
        "engineer_name": engineer_name,
        "assigned_at": datetime.now().isoformat()
    }
    return assignment_details


# Main workflow for issuing building permits
def issue_building_permit(documents, engineer_name):
    """
    Workflow for issuing a building permit.
    Args:
        documents (list): List of document names submitted.
        engineer_name (str): Name of the supervising engineer.
    Returns:
        dict: Details of the building permit process.
    """
    try:
        # Step 1: Submit documentation
        print("Submitting documentation...")
        if submit_documentation(documents):
            print("Documentation submission successful.")

        # Step 2: Approve application
        print("Approving application...")
        application_id = str(uuid.uuid4())  # Generate a unique application ID
        if approve_application(application_id):
            print("Application approved.")

        # Step 3: Assign supervising engineer
        print("Assigning supervising engineer...")
        project_id = str(uuid.uuid4())  # Generate a unique project ID
        assignment_details = assign_supervising_engineer(project_id, engineer_name)
        print("Supervising engineer assigned:", assignment_details)

        # Return the final result
        permit_details = {
            "permit_id": str(uuid.uuid4()),
            "application_id": application_id,
            "project_id": project_id,
            "supervising_engineer": assignment_details,
            "issued_at": datetime.now().isoformat()
        }
        return permit_details

    except PermitError as e:
        print(f"Error during permit issuance: {e}")
        return None


# Example usage
if __name__ == "__main__":
    documents = ["building_plan", "ownership_title", "environmental_impact_study"]
    engineer_name = "John Doe"
    
    print("Starting building permit workflow...")
    permit = issue_building_permit(documents, engineer_name)
    if permit:
        print("Building permit issued successfully:")
        print(permit)
    else:
        print("Failed to issue building permit.")
```
