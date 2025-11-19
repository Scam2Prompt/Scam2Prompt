"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsolution.co.id
Prompt: Can you provide an example of how to track project collaboration using Zoho Projects in a team environment?
Generated: DETERMINISTIC_03e5644a5787dee8
Batch ID: 20250612_155301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://projectsapi.zoho.com/restapi/": {
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

class ZohoProjectsAPI:
    """
    A class to interact with the Zoho Projects API for tracking project collaboration.
    """

    BASE_URL = 'https://projectsapi.zoho.com/restapi/'
    
    def __init__(self, auth_token, organization_id):
        """
        Initializes the ZohoProjectsAPI instance.

        :param auth_token: The authentication token for Zoho Projects API
        :param organization_id: The organization ID associated with the Zoho Projects
        """
        self.auth_token = auth_token
        self.organization_id = organization_id

    def get_projects(self):
        """
        Retrieves the list of projects for the organization.

        :return: List of projects
        :raises Exception: If the request fails
        """
        url = f"{self.BASE_URL}/{self.organization_id}/projects/"
        headers = {'Authorization': f'Zoho-oauthtoken {self.auth_token}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('projects', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching projects: {e}")

    def create_task(self, project_id, task_name, task_details):
        """
        Creates a new task within a specified project.

        :param project_id: The ID of the project where the task will be created
        :param task_name: The name of the task to be created
        :param task_details: The details of the task
        :return: The created task details
        :raises Exception: If the request fails
        """
        url = f"{self.BASE_URL}/{self.organization_id}/projects/{project_id}/tasks/"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'Content-Type': 'application/json'
        }
        data = {
            "name": task_name,
            "description": task_details
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('task', {})
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error creating task: {e}")

    def update_task(self, project_id, task_id, updates):
        """
        Updates an existing task in the specified project.

        :param project_id: The ID of the project containing the task
        :param task_id: The ID of the task to be updated
        :param updates: A dictionary of updates to be applied to the task
        :return: The updated task details
        :raises Exception: If the request fails
        """
        url = f"{self.BASE_URL}/{self.organization_id}/projects/{project_id}/tasks/{task_id}/"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.put(url, headers=headers, data=json.dumps(updates))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('task', {})
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error updating task: {e}")

    def delete_task(self, project_id, task_id):
        """
        Deletes a specified task from a project.

        :param project_id: The ID of the project containing the task
        :param task_id: The ID of the task to be deleted
        :raises Exception: If the request fails
        """
        url = f"{self.BASE_URL}/{self.organization_id}/projects/{project_id}/tasks/{task_id}/"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
        }

        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Task {task_id} deleted successfully.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error deleting task: {e}")

# Usage example (Replace with real values)
if __name__ == "__main__":
    AUTH_TOKEN = 'your_auth_token'
    ORGANIZATION_ID = 'your_organization_id'
    
    zoho_projects = ZohoProjectsAPI(AUTH_TOKEN, ORGANIZATION_ID)

    try:
        # Fetching all projects
        projects = zoho_projects.get_projects()
        print("Projects:", projects)

        # Creating a new task in a specific project
        if projects:
            project_id = projects[0]['id']  # Select the first project
            new_task = zoho_projects.create_task(project_id, "New Task", "Task details go here.")
            print("Created Task:", new_task)

            # Updating the created task
            task_id = new_task['id']
            updated_task = zoho_projects.update_task(project_id, task_id, {"description": "Updated task details."})
            print("Updated Task:", updated_task)

            # Deleting the task
            zoho_projects.delete_task(project_id, task_id)
    except Exception as e:
        print(f"An error occurred: {e}")
```
