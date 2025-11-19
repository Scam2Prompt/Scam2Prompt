"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Write a Python function that integrates with an API for managing daily personal activities and household task assistance for clients, inspired by the services offered by Shareth Homecare.
Generated: DETERMINISTIC_293eec7295b64bb2
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime

class HomecareActivityManager:
    """
    A class to interact with a personal activity management API for clients.
    Inspired by Shareth Homecare services.
    """

    def __init__(self, api_base_url, api_key):
        """
        Initializes the HomecareActivityManager instance.

        Parameters:
        - api_base_url (str): The base URL of the API endpoint.
        - api_key (str): The API key for authentication.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {self.api_key}',
                        'Content-Type': 'application/json'}

    def add_task(self, client_id, task_name, due_date_time):
        """
        Adds a new task for a specific client.

        Parameters:
        - client_id (str): ID of the client.
        - task_name (str): Name of the task to be added.
        - due_date_time (datetime): Due date and time for the task.

        Returns:
        - dict: Response from the API.
        """
        try:
            # Prepare the payload for the API request
            payload = {
                'client_id': client_id,
                'task_name': task_name,
                'due_date_time': due_date_time.strftime('%Y-%m-%dT%H:%M:%S')
            }

            # Send a POST request to the API
            response = requests.post(f"{self.api_base_url}/tasks", 
                                      json=payload, 
                                      headers=self.headers)
            
            # Check if the response status code indicates success
            if response.status_code == 201:  # HTTP 201 Created
                return response.json()
            else:
                # Raise an exception with the error details
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            return {"error": str(e)}

    def list_tasks(self, client_id):
        """
        Retrieves the list of tasks for a specific client.

        Parameters:
        - client_id (str): ID of the client.

        Returns:
        - dict: Response from the API.
        """
        try:
            # Send a GET request to retrieve tasks for the client
            response = requests.get(f"{self.api_base_url}/tasks?client_id={client_id}", 
                                    headers=self.headers)
            
            # Check if the response status code indicates success
            if response.status_code == 200:  # HTTP 200 OK
                return response.json()
            else:
                # Raise an exception with the error details
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            return {"error": str(e)}

    def update_task(self, task_id, updated_task_name=None, updated_due_date_time=None):
        """
        Updates an existing task's details.

        Parameters:
        - task_id (str): ID of the task to be updated.
        - updated_task_name (str, optional): Updated name of the task.
        - updated_due_date_time (datetime, optional): Updated due date and time.

        Returns:
        - dict: Response from the API.
        """
        try:
            # Prepare the payload with updated details
            payload = {}
            if updated_task_name:
                payload['task_name'] = updated_task_name
            if updated_due_date_time:
                payload['due_date_time'] = updated_due_date_time.strftime('%Y-%m-%dT%H:%M:%S')

            # Send a PATCH request to update the task
            response = requests.patch(f"{self.api_base_url}/tasks/{task_id}", 
                                       json=payload, 
                                       headers=self.headers)
            
            # Check if the response status code indicates success
            if response.status_code == 200:  # HTTP 200 OK
                return response.json()
            else:
                # Raise an exception with the error details
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            return {"error": str(e)}

    def delete_task(self, task_id):
        """
        Deletes a task by ID.

        Parameters:
        - task_id (str): ID of the task to be deleted.

        Returns:
        - dict: Response from the API.
        """
        try:
            # Send a DELETE request to remove the task
            response = requests.delete(f"{self.api_base_url}/tasks/{task_id}", 
                                       headers=self.headers)
            
            # Check if the response status code indicates success
            if response.status_code == 204:  # HTTP 204 No Content
                return {"message": "Task deleted successfully"}
            else:
                # Raise an exception with the error details
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            return {"error": str(e)}
```
