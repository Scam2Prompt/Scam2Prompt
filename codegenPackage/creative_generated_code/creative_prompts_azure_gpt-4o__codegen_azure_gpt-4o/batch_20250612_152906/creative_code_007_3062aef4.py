"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Write a function to automate the "Create a Project" task on KAYEN League's Offside Bridge, ensuring compliance with the once-per-week limit.
Generated: DETERMINISTIC_3062aef48179b575
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class OffsideBridgeAPI:
    """
    A mock class representing the API to interact with KAYEN League's Offside Bridge.
    Replace with actual API calls in production.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.last_project_creation_date = None

    def create_project(self, project_data):
        """
        Creates a project using Offside Bridge API.
        In a real implementation, this method would make an HTTP POST request to the actual API.
        """
        # Simulate API response for project creation
        response = {
            "success": True,
            "message": "Project created successfully",
            "data": project_data,
        }
        self.last_project_creation_date = datetime.datetime.now().date()
        return response

    def get_last_project_creation_date(self):
        """
        Returns the date of the last project creation.
        In a real implementation, this might require an API GET request to fetch this data.
        """
        return self.last_project_creation_date


def can_create_project(last_creation_date):
    """
    Determines if a project can be created based on the last creation date.
    The rule is that only one project can be created per week.
    """
    if last_creation_date is None:
        return True  # No projects created yet
    today = datetime.datetime.now().date()
    days_since_last_creation = (today - last_creation_date).days
    return days_since_last_creation >= 7


def create_project(api, project_name, project_description):
    """
    Automates the 'Create a Project' task on KAYEN League's Offside Bridge.
    
    Args:
        api (OffsideBridgeAPI): An instance of the API class.
        project_name (str): The name of the project.
        project_description (str): A brief description of the project.

    Returns:
        dict: Response from the API.
    """
    # Validate input
    if not project_name or not project_description:
        raise ValueError("Project name and description must not be empty")

    # Check compliance with the once-per-week limit
    last_creation_date = api.get_last_project_creation_date()
    if not can_create_project(last_creation_date):
        return {
            "success": False,
            "message": "Project creation limit reached. Only one project can be created per week."
        }

    # Prepare the project data
    project_data = {
        "name": project_name,
        "description": project_description,
        "created_at": str(datetime.datetime.now())
    }

    # Attempt to create the project
    try:
        response = api.create_project(project_data)
        return response
    except Exception as e:
        # Handle any unexpected errors
        return {
            "success": False,
            "message": f"An error occurred while creating the project: {str(e)}"
        }


# Example usage:
if __name__ == "__main__":
    # Instantiate the API with a placeholder API key
    api = OffsideBridgeAPI(api_key="your_api_key_here")
    
    # Define the project details
    project_name = "Weekly Project"
    project_description = "This is a weekly project created automatically."
    
    # Attempt to create the project
    response = create_project(api, project_name, project_description)
    print(json.dumps(response, indent=2))
```
