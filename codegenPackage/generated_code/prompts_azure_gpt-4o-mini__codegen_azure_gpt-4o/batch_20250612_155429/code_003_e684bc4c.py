"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Create a function that allows users to submit their interior design project ideas, inspired by the client collaboration process at Zirciulit.
Generated: DETERMINISTIC_e684bc4ccd0625dc
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def submit_design_project(project_name, client_name, project_description, budget, contact_email):
    """
    Function to submit an interior design project idea.
    
    Parameters:
        project_name (str): Name of the project.
        client_name (str): Name of the client submitting the project.
        project_description (str): Detailed description of the project idea.
        budget (float): Estimated budget for the project.
        contact_email (str): Email address of the client for communication.
    
    Returns:
        dict: A dictionary containing the submission status and project details.
    """
    try:
        # Validate inputs
        if not project_name or not isinstance(project_name, str):
            raise ValueError("Project name must be a non-empty string.")
        if not client_name or not isinstance(client_name, str):
            raise ValueError("Client name must be a non-empty string.")
        if not project_description or not isinstance(project_description, str):
            raise ValueError("Project description must be a non-empty string.")
        if not isinstance(budget, (int, float)) or budget <= 0:
            raise ValueError("Budget must be a positive number.")
        if not contact_email or not isinstance(contact_email, str) or "@" not in contact_email:
            raise ValueError("Contact email must be a valid email address.")

        # Create a project submission dictionary
        project_submission = {
            "project_name": project_name,
            "client_name": client_name,
            "project_description": project_description,
            "budget": budget,
            "contact_email": contact_email,
            "status": "Submitted"
        }

        # Simulate saving the project submission (e.g., to a database or file)
        # Here, we'll save it to a JSON file for demonstration purposes
        with open("design_project_submissions.json", "a") as file:
            file.write(json.dumps(project_submission) + "\n")

        # Return success response
        return {
            "status": "Success",
            "message": "Project submitted successfully.",
            "project_details": project_submission
        }

    except ValueError as ve:
        # Handle validation errors
        return {
            "status": "Error",
            "message": str(ve)
        }
    except Exception as e:
        # Handle unexpected errors
        return {
            "status": "Error",
            "message": "An unexpected error occurred: " + str(e)
        }

# Example usage:
# response = submit_design_project(
#     project_name="Modern Living Room",
#     client_name="John Doe",
#     project_description="A sleek and modern living room design with neutral tones.",
#     budget=5000.00,
#     contact_email="john.doe@example.com"
# )
# print(response)
```
