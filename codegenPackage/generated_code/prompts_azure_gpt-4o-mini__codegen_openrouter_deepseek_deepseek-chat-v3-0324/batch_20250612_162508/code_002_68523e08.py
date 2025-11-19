"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ProjectTracker:
    """
    A class to track project progress for an engineering consultancy.
    Inspired by Remas Engineering Consultants' project management strategies.
    """

    def __init__(self, data_file: str = "projects.json"):
        """
        Initialize the ProjectTracker with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing project data.
        """
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self) -> Dict:
        """
        Load projects from the JSON data file.
        If file doesn't exist, return an empty dictionary.
        
        Returns:
            Dict: Dictionary of projects.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading projects: {e}")
            return {}

    def _save_projects(self) -> None:
        """
        Save projects to the JSON data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.projects, f, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")

    def add_project(self, project_id: str, name: str, client: str, 
                    start_date: str, deadline: str, budget: float) -> bool:
        """
        Add a new project to the tracker.
        
        Args:
            project_id (str): Unique project identifier
            name (str): Project name
            client (str): Client name
            start_date (str): Start date (YYYY-MM-DD)
            deadline (str): Deadline date (YYYY-MM-DD)
            budget (float): Project budget
            
        Returns:
            bool: True if project was added successfully, False otherwise
        """
        if project_id in self.projects:
            print(f"Project with ID {project_id} already exists.")
            return False

        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        self.projects[project_id] = {
            "name": name,
            "client": client,
            "start_date": start_date,
            "deadline": deadline,
            "budget": budget,
            "progress": 0.0,
            "tasks": [],
            "expenses": 0.0,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self._save_projects()
        return True

    def update_progress(self, project_id: str, progress: float) -> bool:
        """
        Update project progress percentage.
        
        Args:
            project_id (str): Project ID
            progress (float): Progress percentage (0-100)
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        if not 0 <= progress <= 100:
            print("Progress must be between 0 and 100.")
            return False

        self.projects[project_id]["progress"] = progress
        self.projects[project_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_projects()
        return True

    def add_task(self, project_id: str, task_name: str, 
                assigned_to: str, due_date: str) -> bool:
        """
        Add a task to a project.
        
        Args:
            project_id (str): Project ID
            task_name (str): Task name
            assigned_to (str): Person assigned to task
            due_date (str): Due date (YYYY-MM-DD)
            
        Returns:
            bool: True if task was added successfully, False otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        task = {
            "name": task_name,
            "assigned_to": assigned_to,
            "due_date": due_date,
            "completed": False
        }

        self.projects[project_id]["tasks"].append(task)
        self.projects[project_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_projects()
        return True

    def complete_task(self, project_id: str, task_index: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            project_id (str): Project ID
            task_index (int): Index of task in project's task list
            
        Returns:
            bool: True if task was marked as completed, False otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        try:
            self.projects[project_id]["tasks"][task_index]["completed"] = True
            self.projects[project_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_projects()
            return True
        except IndexError:
            print(f"Task index {task_index} is invalid.")
            return False

    def add_expense(self, project_id: str, amount: float, description: str) -> bool:
        """
        Add an expense to a project.
        
        Args:
            project_id (str): Project ID
            amount (float): Expense amount
            description (str): Expense description
            
        Returns:
            bool: True if expense was added successfully, False otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        if amount <= 0:
            print("Expense amount must be positive.")
            return False

        self.projects[project_id]["expenses"] += amount
        self.projects[project_id]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_projects()
        return True

    def get_project_status(self, project_id: str) -> Optional[Dict]:
        """
        Get the status of a project.
        
        Args:
            project_id (str): Project ID
            
        Returns:
            Optional[Dict]: Project status dictionary if found, None otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return None

        return self.projects[project_id]

    def get_all_projects(self) -> List[Dict]:
        """
        Get a list of all projects.
        
        Returns:
            List[Dict]: List of all projects
        """
        return list(self.projects.values())

    def get_overdue_projects(self) -> List[Tuple[str, Dict]]:
        """
        Get projects that are past their deadline and not 100% complete.
        
        Returns:
            List[Tuple[str, Dict]]: List of (project_id, project_data) tuples
        """
        today = datetime.now().date()
        overdue = []

        for project_id, project in self.projects.items():
            if project["progress"] < 100:
                try:
                    deadline = datetime.strptime(project["deadline"], "%Y-%m-%d").date()
                    if deadline < today:
                        overdue.append((project_id, project))
                except ValueError:
                    continue

        return overdue

    def get_projects_by_client(self, client_name: str) -> List[Dict]:
        """
        Get all projects for a specific client.
        
        Args:
            client_name (str): Client name
            
        Returns:
            List[Dict]: List of projects for the client
        """
        return [p for p in self.projects.values() if p["client"].lower() == client_name.lower()]

    def calculate_budget_utilization(self, project_id: str) -> Optional[float]:
        """
        Calculate budget utilization percentage for a project.
        
        Args:
            project_id (str): Project ID
            
        Returns:
            Optional[float]: Budget utilization percentage if project exists, None otherwise
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return None

        project = self.projects[project_id]
        if project["budget"] == 0:
            return 0.0

        return (project["expenses"] / project["budget"]) * 100

# Example usage
if __name__ == "__main__":
    tracker = ProjectTracker()
    
    # Add a new project
    tracker.add_project(
        project_id="PRJ
