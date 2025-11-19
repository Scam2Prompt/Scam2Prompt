"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: Write a Python script that integrates with an API to manage construction project details, inspired by the project management philosophy of Albatros SPA.
Generated: DETERMINISTIC_f0b27974b0f8a7d0
Batch ID: 20250612_155840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ConstructionProjectManager:
    """
    A class to manage construction projects through an API.
    Inspired by Albatros SPA's project management philosophy.
    """
    
    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the ConstructionProjectManager with API credentials.
        
        Args:
            api_base_url (str): Base URL of the construction API
            api_key (str): API key for authentication
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (Optional[Dict]): Request payload
            
        Returns:
            Dict: Response data
            
        Raises:
            ValueError: If the request fails
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise ValueError(f"API request failed: {http_err}")
        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise ValueError(f"API request failed: {err}")
        except json.JSONDecodeError as json_err:
            logger.error(f"JSON decode error: {json_err}")
            raise ValueError("Failed to decode API response")
    
    def create_project(self, project_data: Dict) -> Dict:
        """
        Create a new construction project.
        
        Args:
            project_data (Dict): Project details including:
                - name (str): Project name
                - description (str): Project description
                - start_date (str): ISO format start date
                - end_date (str): ISO format end date
                - budget (float): Project budget
                - location (str): Project location
                
        Returns:
            Dict: Created project data
        """
        required_fields = ['name', 'start_date', 'budget', 'location']
        if not all(field in project_data for field in required_fields):
            raise ValueError("Missing required project fields")
            
        try:
            datetime.fromisoformat(project_data['start_date'])
            if 'end_date' in project_data:
                datetime.fromisoformat(project_data['end_date'])
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
            
        return self._make_request('POST', 'projects', project_data)
    
    def get_project(self, project_id: str) -> Dict:
        """
        Get details of a specific project.
        
        Args:
            project_id (str): ID of the project to retrieve
            
        Returns:
            Dict: Project details
        """
        return self._make_request('GET', f'projects/{project_id}')
    
    def update_project(self, project_id: str, update_data: Dict) -> Dict:
        """
        Update an existing project.
        
        Args:
            project_id (str): ID of the project to update
            update_data (Dict): Fields to update
            
        Returns:
            Dict: Updated project data
        """
        return self._make_request('PUT', f'projects/{project_id}', update_data)
    
    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project.
        
        Args:
            project_id (str): ID of the project to delete
            
        Returns:
            bool: True if deletion was successful
        """
        self._make_request('DELETE', f'projects/{project_id}')
        return True
    
    def list_projects(self, filters: Optional[Dict] = None) -> List[Dict]:
        """
        List all projects with optional filters.
        
        Args:
            filters (Optional[Dict]): Filter criteria
            
        Returns:
            List[Dict]: List of projects
        """
        endpoint = 'projects'
        if filters:
            query_params = '&'.join(f"{k}={v}" for k, v in filters.items())
            endpoint = f"{endpoint}?{query_params}"
        return self._make_request('GET', endpoint)
    
    def add_project_member(self, project_id: str, user_id: str, role: str) -> Dict:
        """
        Add a member to a project.
        
        Args:
            project_id (str): ID of the project
            user_id (str): ID of the user to add
            role (str): Role of the user in the project
            
        Returns:
            Dict: Membership details
        """
        data = {
            'user_id': user_id,
            'role': role
        }
        return self._make_request('POST', f'projects/{project_id}/members', data)
    
    def get_project_members(self, project_id: str) -> List[Dict]:
        """
        Get all members of a project.
        
        Args:
            project_id (str): ID of the project
            
        Returns:
            List[Dict]: List of project members
        """
        return self._make_request('GET', f'projects/{project_id}/members')
    
    def remove_project_member(self, project_id: str, user_id: str) -> bool:
        """
        Remove a member from a project.
        
        Args:
            project_id (str): ID of the project
            user_id (str): ID of the user to remove
            
        Returns:
            bool: True if removal was successful
        """
        self._make_request('DELETE', f'projects/{project_id}/members/{user_id}')
        return True
    
    def get_project_tasks(self, project_id: str) -> List[Dict]:
        """
        Get all tasks for a project.
        
        Args:
            project_id (str): ID of the project
            
        Returns:
            List[Dict]: List of project tasks
        """
        return self._make_request('GET', f'projects/{project_id}/tasks')
    
    def create_project_task(self, project_id: str, task_data: Dict) -> Dict:
        """
        Create a new task for a project.
        
        Args:
            project_id (str): ID of the project
            task_data (Dict): Task details including:
                - name (str): Task name
                - description (str): Task description
                - due_date (str): ISO format due date
                - status (str): Task status
                - assigned_to (str): User ID of assignee
                
        Returns:
            Dict: Created task data
        """
        required_fields = ['name', 'due_date', 'status']
        if not all(field in task_data for field in required_fields):
            raise ValueError("Missing required task fields")
            
        try:
            datetime.fromisoformat(task_data['due_date'])
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
            
        return self._make_request('POST', f'projects/{project_id}/tasks', task_data)

# Example usage
if __name__ == "__main__":
    # Initialize with your API credentials
    manager = ConstructionProjectManager(
        api_base_url="https://api.example.com/v1",
        api_key="your_api_key_here"
    )
    
    # Example: Create a project
    try:
        new_project = manager.create_project({
            "name": "New Office Building",
            "description": "Construction of 10-story office building",
            "start_date": "2023-01-15",
            "end_date": "2024-06-30",
            "budget": 5000000,
            "location": "New York"
        })
        print(f"Created project: {new_project}")
    except ValueError as e:
        print(f"Error creating project: {e}")
```
