"""
Generated Code Metadata:
========================
Original URL: https://metatask.co.kr
Prompt: "Write a code snippet to interact with a task management API, inspired by the features of 메타태스크."
Generated: DETERMINISTIC_f9c6110332056a63
Batch ID: 20250622_204946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional

class TaskManagementAPI:
    """
    A client for interacting with a task management API similar to 메타태스크.
    Handles authentication, task operations, and error handling.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client with base URL and API key.
        
        Args:
            base_url: Base URL of the task management API
            api_key: API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            data: Optional payload for POST/PUT requests
            
        Returns:
            Response JSON data
            
        Raises:
            ValueError: For invalid input parameters
            requests.exceptions.RequestException: For API request failures
        """
        if not method or not endpoint:
            raise ValueError("Method and endpoint must be provided")
            
        url = f"{self.base_url}/{endpoint}"
        
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
            raise requests.exceptions.RequestException(
                f"HTTP error occurred: {http_err}. Response: {response.text}"
            )
        except Exception as err:
            raise requests.exceptions.RequestException(
                f"An error occurred: {err}"
            )

    def create_task(self, title: str, description: str = "", due_date: str = None) -> Dict:
        """
        Create a new task.
        
        Args:
            title: Task title (required)
            description: Task description
            due_date: Due date in ISO format (YYYY-MM-DD)
            
        Returns:
            Created task data
        """
        task_data = {
            'title': title,
            'description': description,
            'due_date': due_date
        }
        return self._make_request('POST', 'tasks', task_data)

    def get_tasks(self, status: str = None, limit: int = 100) -> List[Dict]:
        """
        Retrieve tasks with optional filters.
        
        Args:
            status: Filter by task status (e.g., 'pending', 'completed')
            limit: Maximum number of tasks to return
            
        Returns:
            List of task dictionaries
        """
        params = {}
        if status:
            params['status'] = status
        if limit:
            params['limit'] = limit
            
        endpoint = 'tasks'
        if params:
            endpoint += '?' + '&'.join(f"{k}={v}" for k, v in params.items())
            
        return self._make_request('GET', endpoint)

    def update_task(self, task_id: str, **kwargs) -> Dict:
        """
        Update an existing task.
        
        Args:
            task_id: ID of the task to update
            **kwargs: Fields to update (title, description, status, due_date)
            
        Returns:
            Updated task data
        """
        if not task_id:
            raise ValueError("Task ID must be provided")
            
        return self._make_request('PUT', f'tasks/{task_id}', kwargs)

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if deletion was successful
        """
        if not task_id:
            raise ValueError("Task ID must be provided")
            
        self._make_request('DELETE', f'tasks/{task_id}')
        return True

    def get_task_details(self, task_id: str) -> Dict:
        """
        Get detailed information about a specific task.
        
        Args:
            task_id: ID of the task to retrieve
            
        Returns:
            Task details
        """
        if not task_id:
            raise ValueError("Task ID must be provided")
            
        return self._make_request('GET', f'tasks/{task_id}')
```
