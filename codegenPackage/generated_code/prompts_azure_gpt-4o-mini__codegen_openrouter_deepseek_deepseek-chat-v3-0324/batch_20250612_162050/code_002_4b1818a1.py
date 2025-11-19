"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Write a Python script that integrates with a project management API to monitor construction project progress, reflecting SSTCO's approach to maintaining project timelines and quality.
Generated: DETERMINISTIC_4b1818a11441c4c0
Batch ID: 20250612_162050
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
from datetime import datetime
import logging
from typing import Dict, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectMonitor:
    """
    A class to monitor construction project progress by integrating with a project management API.
    """
    
    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the ProjectMonitor with API credentials.
        
        Args:
            api_base_url (str): Base URL of the project management API
            api_key (str): API key for authentication
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
    def _make_api_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Optional[Dict]:
        """
        Make an API request to the project management system.
        
        Args:
            endpoint (str): API endpoint to call
            method (str): HTTP method (GET, POST, PUT, etc.)
            data (Optional[Dict]): Data to send with the request
            
        Returns:
            Optional[Dict]: JSON response from the API or None if request fails
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return None
    
    def get_project_details(self, project_id: str) -> Optional[Dict]:
        """
        Get details for a specific project.
        
        Args:
            project_id (str): ID of the project to retrieve
            
        Returns:
            Optional[Dict]: Project details or None if request fails
        """
        return self._make_api_request(f"projects/{project_id}")
    
    def get_project_tasks(self, project_id: str) -> Optional[List[Dict]]:
        """
        Get all tasks for a specific project.
        
        Args:
            project_id (str): ID of the project to retrieve tasks for
            
        Returns:
            Optional[List[Dict]]: List of tasks or None if request fails
        """
        return self._make_api_request(f"projects/{project_id}/tasks")
    
    def update_task_status(self, project_id: str, task_id: str, status: str, notes: str = "") -> bool:
        """
        Update the status of a project task.
        
        Args:
            project_id (str): ID of the project
            task_id (str): ID of the task to update
            status (str): New status for the task
            notes (str): Optional notes about the status update
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        data = {
            "status": status,
            "notes": notes,
            "updated_at": datetime.utcnow().isoformat()
        }
        response = self._make_api_request(
            f"projects/{project_id}/tasks/{task_id}",
            method="PUT",
            data=data
        )
        return response is not None
    
    def check_project_progress(self, project_id: str) -> Optional[Dict]:
        """
        Check overall project progress and timeline adherence.
        
        Args:
            project_id (str): ID of the project to check
            
        Returns:
            Optional[Dict]: Project progress report or None if request fails
        """
        project = self.get_project_details(project_id)
        if not project:
            return None
            
        tasks = self.get_project_tasks(project_id)
        if not tasks:
            return None
            
        completed_tasks = [t for t in tasks if t.get('status') == 'completed']
        overdue_tasks = [
            t for t in tasks 
            if t.get('due_date') and 
            datetime.fromisoformat(t['due_date']) < datetime.utcnow() and
            t.get('status') != 'completed'
        ]
        
        progress = {
            'project_id': project_id,
            'project_name': project.get('name'),
            'total_tasks': len(tasks),
            'completed_tasks': len(completed_tasks),
            'overdue_tasks': len(overdue_tasks),
            'completion_percentage': round(len(completed_tasks) / len(tasks) * 100, 2) if tasks else 0,
            'last_updated': datetime.utcnow().isoformat(),
            'tasks': tasks
        }
        
        return progress
    
    def generate_progress_report(self, project_id: str) -> Optional[str]:
        """
        Generate a human-readable progress report for a project.
        
        Args:
            project_id (str): ID of the project to generate report for
            
        Returns:
            Optional[str]: Formatted progress report or None if data unavailable
        """
        progress = self.check_project_progress(project_id)
        if not progress:
            return None
            
        report_lines = [
            f"Project Progress Report - {progress['project_name']}",
            f"Generated at: {progress['last_updated']}",
            "",
            f"Overall Completion: {progress['completion_percentage']}%",
            f"Total Tasks: {progress['total_tasks']}",
            f"Completed Tasks: {progress['completed_tasks']}",
            f"Overdue Tasks: {progress['overdue_tasks']}",
            "",
            "Task Status Summary:"
        ]
        
        for task in progress['tasks']:
            due_date = task.get('due_date', 'No due date')
            status = task.get('status', 'unknown')
            report_lines.append(
                f"- {task.get('name')}: {status} (Due: {due_date})"
            )
            
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Configuration - these should come from environment variables or config files in production
    API_BASE_URL = "https://api.example.com/v1"
    API_KEY = "your_api_key_here"
    PROJECT_ID = "proj_12345"
    
    # Initialize monitor
    monitor = ProjectMonitor(api_base_url=API_BASE_URL, api_key=API_KEY)
    
    # Get and print progress report
    report = monitor.generate_progress_report(PROJECT_ID)
    if report:
        print(report)
    else:
        logger.error("Failed to generate progress report")
```
