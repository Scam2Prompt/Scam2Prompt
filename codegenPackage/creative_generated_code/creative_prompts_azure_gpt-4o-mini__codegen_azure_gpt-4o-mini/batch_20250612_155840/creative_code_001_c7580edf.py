"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajp.cl
Prompt: What API would you recommend for managing infrastructure projects related to water sanitation, considering AJP Ingenieros' focus on high-quality design and timely client support?
Generated: DETERMINISTIC_c7580edf8f0f6bdb
Batch ID: 20250612_155840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ajpingenieros.com/v1/projects": {
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

class InfrastructureAPI:
    """
    A class to manage infrastructure projects related to water sanitation.
    This interface interacts with a hypothetical REST API to manage projects,
    ensuring high-quality design and timely client support.
    """

    BASE_URL = "https://api.ajpingenieros.com/v1/projects"

    def __init__(self, api_key):
        """
        Initializes the InfrastructureAPI with the provided API key.
        
        :param api_key: str - The API key for authentication with the API.
        """
        self.api_key = api_key

    def _headers(self):
        """
        Constructs the headers for API requests, including the authorization.

        :return: dict - The headers for the HTTP request.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_projects(self):
        """
        Fetches a list of infrastructure projects.

        :return: list - A list of projects.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.get(self.BASE_URL, headers=self._headers())
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Return the JSON response as a list
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching projects: {e}")

    def create_project(self, project_data):
        """
        Creates a new infrastructure project.

        :param project_data: dict - A dictionary containing project details.
        :return: dict - The created project details.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.post(self.BASE_URL, headers=self._headers(), json=project_data)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Return the JSON response for the created project
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error creating project: {e}")

    def update_project(self, project_id, project_data):
        """
        Updates an existing infrastructure project.

        :param project_id: str - The ID of the project to update.
        :param project_data: dict - A dictionary containing updated project details.
        :return: dict - The updated project details.
        :raises Exception: If the API request fails.
        """
        try:
            url = f"{self.BASE_URL}/{project_id}"
            response = requests.put(url, headers=self._headers(), json=project_data)
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Return the JSON response for the updated project
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error updating project {project_id}: {e}")

    def delete_project(self, project_id):
        """
        Deletes an infrastructure project.

        :param project_id: str - The ID of the project to delete.
        :raises Exception: If the API request fails.
        """
        try:
            url = f"{self.BASE_URL}/{project_id}"
            response = requests.delete(url, headers=self._headers())
            response.raise_for_status()  # Raises an error for bad responses
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error deleting project {project_id}: {e}")

# Example usage:
# api = InfrastructureAPI(api_key="your_api_key_here")
# projects = api.get_projects()
# print(projects)
```
