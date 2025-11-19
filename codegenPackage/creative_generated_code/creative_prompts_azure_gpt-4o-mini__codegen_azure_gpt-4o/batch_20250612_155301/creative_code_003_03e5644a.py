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
  "https://projectsapi.zoho.com/restapi": {
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

# Constants
ZOHO_API_BASE_URL = "https://projectsapi.zoho.com/restapi"
ACCESS_TOKEN = "your_access_token_here"  # Replace with your Zoho Projects access token
PROJECT_ID = "your_project_id_here"      # Replace with your Zoho Projects project ID

# Function to retrieve list of tasks for a specific project
def get_project_tasks(project_id):
    """
    Fetches all tasks for a given project in Zoho Projects.

    Args:
        project_id (str): The ID of the project whose tasks need to be fetched.

    Returns:
        list: A list of tasks if successful, empty list otherwise.
    """
    url = f"{ZOHO_API_BASE_URL}/portal/your_portal_name/projects/{project_id}/tasks/"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        tasks = response.json().get('tasks', [])
        return tasks
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tasks: {e}")
        return []

# Function to add a new task to a project
def create_new_task(project_id, task_name, task_owner):
    """
    Creates a new task in the specified Zoho project.

    Args:
        project_id (str): The ID of the project where the task will be added.
        task_name (str): The name of the task to create.
        task_owner (str): The email or user ID of the task owner.

    Returns:
        dict: The created task details if successful, None otherwise.
    """
    url = f"{ZOHO_API_BASE_URL}/portal/your_portal_name/projects/{project_id}/tasks/"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": task_name,
        "owner": task_owner
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating task: {e}")
        return None

# Function to update the status of a task
def update_task_status(project_id, task_id, new_status):
    """
    Updates the status of an existing task in Zoho Projects.

    Args:
        project_id (str): The ID of the project containing the task.
        task_id (str): The ID of the task to update.
        new_status (str): The new status of the task.

    Returns:
        dict: The updated task details if successful, None otherwise.
    """
    url = f"{ZOHO_API_BASE_URL}/portal/your_portal_name/projects/{project_id}/tasks/{task_id}/"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "status": new_status
    }

    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating task status: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Fetch tasks for the specified project
    tasks = get_project_tasks(PROJECT_ID)
    print("Tasks in Project:")
    for task in tasks:
        print(f"- {task['name']} (Status: {task['status']})")

    # Create a new task in the project
    new_task = create_new_task(PROJECT_ID, "Design Mockups", "owner_email@example.com")
    if new_task:
        print(f"New Task Created: {new_task['name']}")

    # Update the status of an existing task
    updated_task = update_task_status(PROJECT_ID, "task_id_here", "In Progress")
    if updated_task:
        print(f"Task Updated: {updated_task['name']} (Status: {updated_task['status']})")
```
