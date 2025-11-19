"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Write a Python script that integrates with an API to manage construction project data, similar to the projects executed by Sadad Engineering.
Generated: DETERMINISTIC_e70bd44cec635bcf
Batch ID: 20250612_161042
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sadadengineering.com": {
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

class ConstructionProjectAPI:
    """Class to manage construction project data using an external API."""

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the API client with the base URL and API key.

        :param api_base_url: The base URL for the API.
        :param api_key: The API key for authentication.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_projects(self) -> list:
        """Fetch all construction projects.

        :return: A list of projects.
        :raises Exception: If the API call fails.
        """
        try:
            response = requests.get(f'{self.api_base_url}/projects', headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch projects: {e}")

    def create_project(self, project_data: dict) -> dict:
        """Create a new construction project.

        :param project_data: A dictionary containing project data.
        :return: The created project data.
        :raises Exception: If the API call fails.
        """
        try:
            response = requests.post(f'{self.api_base_url}/projects', headers=self.headers, data=json.dumps(project_data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create project: {e}")

    def update_project(self, project_id: str, project_data: dict) -> dict:
        """Update an existing construction project.

        :param project_id: The ID of the project to update.
        :param project_data: A dictionary containing updated project data.
        :return: The updated project data.
        :raises Exception: If the API call fails.
        """
        try:
            response = requests.put(f'{self.api_base_url}/projects/{project_id}', headers=self.headers, data=json.dumps(project_data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to update project {project_id}: {e}")

    def delete_project(self, project_id: str) -> bool:
        """Delete a construction project.

        :param project_id: The ID of the project to delete.
        :return: True if the project was deleted, otherwise False.
        :raises Exception: If the API call fails.
        """
        try:
            response = requests.delete(f'{self.api_base_url}/projects/{project_id}', headers=self.headers)
            response.raise_for_status()
            return response.status_code == 204  # No content status code signifies successful deletion
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to delete project {project_id}: {e}")


if __name__ == "__main__":
    # Example usage of the ConstructionProjectAPI class
    api_base_url = "https://api.sadadengineering.com"  # Replace with the actual API base URL
    api_key = "your_api_key_here"  # Replace with your actual API key

    project_api = ConstructionProjectAPI(api_base_url, api_key)

    try:
        # Fetch and print existing projects
        projects = project_api.get_projects()
        print("Existing Projects:", projects)
        
        # Create a new project example
        new_project = {
            "name": "New Building",
            "location": "Downtown",
            "budget": 500000,
            "deadline": "2024-12-31"
        }
        created_project = project_api.create_project(new_project)
        print("Created Project:", created_project)
        
    except Exception as e:
        print("An error occurred:", e)
```
