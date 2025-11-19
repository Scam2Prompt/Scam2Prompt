"""
Generated Code Metadata:
========================
Original URL: https://turpymobileapps.com
Prompt: Create a Python script for managing product development workflows, incorporating features relevant to Turpy Mobile Apps' product management services.
Generated: DETERMINISTIC_6816c173104eb0f0
Batch ID: 20250612_154854
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
from typing import Dict, List, Optional, Union

class ProductWorkflowManager:
    """
    A class to manage product development workflows for Turpy Mobile Apps.
    Handles tasks, sprints, and product lifecycle management.
    """
    
    def __init__(self, data_file: str = "workflow_data.json"):
        """
        Initialize the workflow manager with a data file.
        
        Args:
            data_file (str): Path to JSON file storing workflow data
        """
        self.data_file = data_file
        self.workflows = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load workflow data from JSON file.
        Creates file if it doesn't exist.
        
        Returns:
            Dict: Workflow data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {
                "products": {},
                "sprints": {},
                "tasks": {},
                "last_id": 0
            }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {
                "products": {},
                "sprints": {},
                "tasks": {},
                "last_id": 0
            }
    
    def _save_data(self) -> None:
        """
        Save workflow data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.workflows, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def _generate_id(self) -> int:
        """
        Generate a new unique ID for workflow items.
        
        Returns:
            int: New unique ID
        """
        self.workflows["last_id"] += 1
        return self.workflows["last_id"]
    
    def create_product(self, name: str, description: str, owner: str) -> Dict:
        """
        Create a new product.
        
        Args:
            name (str): Product name
            description (str): Product description
            owner (str): Product owner/manager
            
        Returns:
            Dict: Created product data
        """
        product_id = self._generate_id()
        product = {
            "id": product_id,
            "name": name,
            "description": description,
            "owner": owner,
            "created_at": datetime.now().isoformat(),
            "status": "planning",
            "sprints": []
        }
        self.workflows["products"][str(product_id)] = product
        self._save_data()
        return product
    
    def create_sprint(self, product_id: int, name: str, duration_days: int) -> Dict:
        """
        Create a new sprint for a product.
        
        Args:
            product_id (int): ID of the product
            name (str): Sprint name
            duration_days (int): Duration in days
            
        Returns:
            Dict: Created sprint data
        """
        if str(product_id) not in self.workflows["products"]:
            raise ValueError("Product not found")
            
        sprint_id = self._generate_id()
        sprint = {
            "id": sprint_id,
            "product_id": product_id,
            "name": name,
            "duration_days": duration_days,
            "start_date": None,
            "end_date": None,
            "status": "planned",
            "tasks": []
        }
        
        self.workflows["sprints"][str(sprint_id)] = sprint
        self.workflows["products"][str(product_id)]["sprints"].append(sprint_id)
        self._save_data()
        return sprint
    
    def create_task(self, sprint_id: int, title: str, description: str, assignee: str) -> Dict:
        """
        Create a new task in a sprint.
        
        Args:
            sprint_id (int): ID of the sprint
            title (str): Task title
            description (str): Task description
            assignee (str): Person assigned to the task
            
        Returns:
            Dict: Created task data
        """
        if str(sprint_id) not in self.workflows["sprints"]:
            raise ValueError("Sprint not found")
            
        task_id = self._generate_id()
        task = {
            "id": task_id,
            "sprint_id": sprint_id,
            "title": title,
            "description": description,
            "assignee": assignee,
            "created_at": datetime.now().isoformat(),
            "status": "todo",
            "comments": []
        }
        
        self.workflows["tasks"][str(task_id)] = task
        self.workflows["sprints"][str(sprint_id)]["tasks"].append(task_id)
        self._save_data()
        return task
    
    def update_task_status(self, task_id: int, new_status: str) -> Dict:
        """
        Update a task's status.
        
        Args:
            task_id (int): ID of the task
            new_status (str): New status (todo, in_progress, review, done)
            
        Returns:
            Dict: Updated task data
        """
        if str(task_id) not in self.workflows["tasks"]:
            raise ValueError("Task not found")
            
        valid_statuses = ["todo", "in_progress", "review", "done"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
            
        self.workflows["tasks"][str(task_id)]["status"] = new_status
        self._save_data()
        return self.workflows["tasks"][str(task_id)]
    
    def add_comment_to_task(self, task_id: int, author: str, text: str) -> Dict:
        """
        Add a comment to a task.
        
        Args:
            task_id (int): ID of the task
            author (str): Comment author
            text (str): Comment text
            
        Returns:
            Dict: Updated task data
        """
        if str(task_id) not in self.workflows["tasks"]:
            raise ValueError("Task not found")
            
        comment = {
            "author": author,
            "text": text,
            "timestamp": datetime.now().isoformat()
        }
        
        self.workflows["tasks"][str(task_id)]["comments"].append(comment)
        self._save_data()
        return self.workflows["tasks"][str(task_id)]
    
    def start_sprint(self, sprint_id: int) -> Dict:
        """
        Start a sprint by setting its start date and updating status.
        
        Args:
            sprint_id (int): ID of the sprint
            
        Returns:
            Dict: Updated sprint data
        """
        if str(sprint_id) not in self.workflows["sprints"]:
            raise ValueError("Sprint not found")
            
        sprint = self.workflows["sprints"][str(sprint_id)]
        if sprint["status"] != "planned":
            raise ValueError("Sprint can only be started from planned status")
            
        sprint["start_date"] = datetime.now().isoformat()
        sprint["status"] = "active"
        self._save_data()
        return sprint
    
    def complete_sprint(self, sprint_id: int) -> Dict:
        """
        Complete a sprint by setting its end date and updating status.
        
        Args:
            sprint_id (int): ID of the sprint
            
        Returns:
            Dict: Updated sprint data
        """
        if str(sprint_id) not in self.workflows["sprints"]:
            raise ValueError("Sprint not found")
            
        sprint = self.workflows["sprints"][str(sprint_id)]
        if sprint["status"] != "active":
            raise ValueError("Sprint can only be completed from active status")
            
        sprint["end_date"] = datetime.now().isoformat()
        sprint["status"] = "completed"
        self._save_data()
        return sprint
    
    def get_product(self, product_id: int) -> Dict:
        """
        Get product details.
        
        Args:
            product_id (int): ID of the product
            
        Returns:
            Dict: Product data
        """
        if str(product_id) not in self.workflows["products"]:
            raise ValueError("Product not found")
        return self.workflows["products"][str(product_id)]
    
    def get_sprint(self, sprint_id: int) -> Dict:
        """
        Get sprint details.
        
        Args:
            sprint_id (int): ID of the sprint
            
        Returns:
            Dict: Sprint data
        """
        if str(sprint_id) not in self.workflows["sprints"]:
            raise ValueError("Sprint not found")
        return self.workflows["sprints"][str(sprint_id)]
    
    def get_task(self, task_id: int) -> Dict:
        """
        Get task details.
        
        Args:
            task_id (int): ID of the task
            
        Returns:
            Dict: Task data
        """
        if str(task_id) not in self.workflows["tasks"]:
            raise ValueError("Task not found")
        return self.workflows["tasks"][str(task
