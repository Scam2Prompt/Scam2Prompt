"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-chiliz.net
Prompt: Provide an example of using the Microsoft Planner API to create and assign tasks, with Copilot's AI assisting in task prioritization.
Generated: DETERMINISTIC_b048852c4a7fc9d4
Batch ID: 20250612_150658
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.microsoft.com/v1.0/planner": {
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

# Microsoft Planner API URL
BASE_URL = "https://graph.microsoft.com/v1.0/planner"

# Your Microsoft Graph access token (ensure this is securely stored and managed in production)
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"

# Headers for the API requests
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_task(plan_id, title, description, due_date, assigned_user_id):
    """
    Create a new task in Microsoft Planner.

    Args:
        plan_id (str): The ID of the plan where the task will be created.
        title (str): Title of the task.
        description (str): Description of the task.
        due_date (str): Due date of the task in ISO 8601 format.
        assigned_user_id (str): ID of the user to whom the task will be assigned.

    Returns:
        dict: Response from the Microsoft Planner API.
    """
    try:
        # Task creation payload
        task_payload = {
            "planId": plan_id,
            "title": title,
            "details": {"description": description},
            "dueDateTime": due_date,
            "assignments": {
                assigned_user_id: {
                    "@odata.type": "microsoft.graph.plannerAssignment",
                    "orderHint": " !"
                }
            }
        }

        # Send POST request to create task
        response = requests.post(f"{BASE_URL}/tasks", headers=HEADERS, data=json.dumps(task_payload))

        # Check for successful response
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error creating task: {e}")
        return None

def prioritize_tasks_with_ai(tasks):
    """
    Use AI (e.g., Copilot or other AI services) to prioritize a list of tasks.

    Args:
        tasks (list): List of task dictionaries with 'title' and 'description'.

    Returns:
        list: List of tasks sorted by priority.
    """
    try:
        # Simulating AI prioritization (replace with actual AI API integration if available)
        # Here, we simply sort tasks alphabetically based on title as a placeholder
        prioritized_tasks = sorted(tasks, key=lambda t: t['title'])
        return prioritized_tasks
    except Exception as e:
        print(f"Error during AI prioritization: {e}")
        return tasks

# Example usage
if __name__ == "__main__":
    # Plan ID where tasks will be created
    PLAN_ID = "YOUR_PLAN_ID_HERE"

    # Example list of tasks to be prioritized by AI
    task_list = [
        {"title": "Write report", "description": "Draft the quarterly financial report."},
        {"title": "Team meeting", "description": "Schedule a meeting with team to discuss project roadmap."},
        {"title": "Code review", "description": "Review recent commits for quality assurance."}
    ]

    # Prioritize tasks using AI
    prioritized_tasks = prioritize_tasks_with_ai(task_list)

    # Loop through prioritized tasks and create them in Microsoft Planner
    for task in prioritized_tasks:
        task_due_date = "2023-12-31T23:59:59Z"  # Example due date in ISO 8601 format
        assigned_user_id = "YOUR_USER_ID_HERE"  # Replace with actual user ID for assignment

        # Create the task in Microsoft Planner
        created_task = create_task(PLAN_ID, task["title"], task["description"], task_due_date, assigned_user_id)
        
        if created_task:
            print(f"Task '{task['title']}' created successfully: {created_task}")
        else:
            print(f"Failed to create task: {task['title']}")
```
