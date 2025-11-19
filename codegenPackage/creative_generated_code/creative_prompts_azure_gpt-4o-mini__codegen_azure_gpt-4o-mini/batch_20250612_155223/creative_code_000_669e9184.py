"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Generate a Python script that utilizes a project management API to track construction projects in the civil engineering sector, focusing on heavy construction and industrial projects.
Generated: DETERMINISTIC_669e9184cb8fee73
Batch ID: 20250612_155223
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.projectmanagement.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class ProjectManagementAPI:
    """
    A class to interact with a project management API for tracking construction projects.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client.
        
        Args:
            base_url (str): The base URL for the project management API.
            api_key (str): The API key for authentication with the API.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

    def _handle_response(self, response):
        """
        Handles the HTTP response from the API.
        
        Args:
            response (requests.Response): The response object from the requests library.
        
        Returns:
            dict: Parsed JSON response if successful, raises an error otherwise.
        """
        try:
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def get_projects(self):
        """
        Retrieves a list of all construction projects.
        
        Returns:
            list: A list of projects, or None if an error occurs.
        """
        url = f"{self.base_url}/projects"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def get_project(self, project_id):
        """
        Retrieves details for a specific project by ID.
        
        Args:
            project_id (str): The unique identifier for the project.
        
        Returns:
            dict: Project details, or None if an error occurs.
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def create_project(self, name, description):
        """
        Creates a new construction project.
        
        Args:
            name (str): The name of the project.
            description (str): A brief description of the project.
        
        Returns:
            dict: Created project details, or None if an error occurs.
        """
        url = f"{self.base_url}/projects"
        project_data = {
            'name': name,
            'description': description,
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(project_data))
        return self._handle_response(response)

    def update_project(self, project_id, updates):
        """
        Updates an existing project.
        
        Args:
            project_id (str): The unique identifier for the project.
            updates (dict): A dictionary of updates to apply to the project.
        
        Returns:
            dict: Updated project details, or None if an error occurs.
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, headers=self.headers, data=json.dumps(updates))
        return self._handle_response(response)

    def delete_project(self, project_id):
        """
        Deletes a specific project by ID.
        
        Args:
            project_id (str): The unique identifier for the project.
        
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:  # No content on successful delete
            return True
        self._handle_response(response)  # Handle any errors that occurred
        return False


if __name__ == "__main__":
    # Example usage of the ProjectManagementAPI class
    BASE_URL = "https://api.projectmanagement.com/v1"  # Replace with actual API URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    api = ProjectManagementAPI(BASE_URL, API_KEY)

    # Fetch all projects
    projects = api.get_projects()
    print("Projects:", projects)

    # Example to create a new project
    new_project = api.create_project("New Heavy Construction Project", "Description of the project.")
    print("Created Project:", new_project)

    # Update an existing project
    if new_project:
        project_id = new_project.get('id')
        updated_project = api.update_project(project_id, {'description': 'Updated description.'})
        print("Updated Project:", updated_project)

    # Delete the project
    if new_project:
        success = api.delete_project(project_id)
        print("Project deleted:", success)
```
