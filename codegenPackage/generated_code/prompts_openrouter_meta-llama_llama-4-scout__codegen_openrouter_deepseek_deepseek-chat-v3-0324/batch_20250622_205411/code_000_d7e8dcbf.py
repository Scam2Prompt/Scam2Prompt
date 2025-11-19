"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Write a Python script to manage construction projects, including tracking client information, project progress, and team assignments, similar to Clickmart Ltd's project management approach."
Generated: DETERMINISTIC_d7e8dcbf5af17876
Batch ID: 20250622_205411
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

class ConstructionProjectManager:
    """
    A class to manage construction projects, clients, and team assignments.
    """
    
    def __init__(self, data_file: str = "construction_projects.json"):
        """
        Initialize the project manager with a data file.
        
        Args:
            data_file (str): Path to JSON file storing project data.
        """
        self.data_file = data_file
        self.projects = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load project data from JSON file or initialize empty structure.
        
        Returns:
            Dict: Loaded or initialized project data.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {"projects": {}, "clients": {}, "teams": {}}
        return {"projects": {}, "clients": {}, "teams": {}}
    
    def _save_data(self) -> None:
        """
        Save current project data to JSON file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.projects, f, indent=4)
    
    def add_client(self, client_id: str, name: str, contact: str, address: str) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id (str): Unique identifier for the client.
            name (str): Client's name.
            contact (str): Contact information.
            address (str): Physical address.
            
        Returns:
            bool: True if client was added successfully.
        """
        if client_id in self.projects["clients"]:
            return False
            
        self.projects["clients"][client_id] = {
            "name": name,
            "contact": contact,
            "address": address,
            "projects": []
        }
        self._save_data()
        return True
    
    def add_project(self, project_id: str, client_id: str, name: str, 
                    start_date: str, deadline: str, budget: float) -> bool:
        """
        Add a new construction project.
        
        Args:
            project_id (str): Unique project identifier.
            client_id (str): ID of the client this project belongs to.
            name (str): Project name.
            start_date (str): Project start date (YYYY-MM-DD).
            deadline (str): Project deadline (YYYY-MM-DD).
            budget (float): Project budget.
            
        Returns:
            bool: True if project was added successfully.
        """
        if project_id in self.projects["projects"]:
            return False
            
        if client_id not in self.projects["clients"]:
            return False
            
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            return False
            
        self.projects["projects"][project_id] = {
            "client_id": client_id,
            "name": name,
            "start_date": start_date,
            "deadline": deadline,
            "budget": budget,
            "progress": 0.0,
            "status": "Not Started",
            "team_id": None,
            "milestones": {}
        }
        
        self.projects["clients"][client_id]["projects"].append(project_id)
        self._save_data()
        return True
    
    def update_project_progress(self, project_id: str, progress: float) -> bool:
        """
        Update project progress percentage.
        
        Args:
            project_id (str): ID of project to update.
            progress (float): New progress percentage (0-100).
            
        Returns:
            bool: True if update was successful.
        """
        if project_id not in self.projects["projects"]:
            return False
            
        if not 0 <= progress <= 100:
            return False
            
        self.projects["projects"][project_id]["progress"] = progress
        
        if progress == 0:
            status = "Not Started"
        elif progress == 100:
            status = "Completed"
        else:
            status = "In Progress"
            
        self.projects["projects"][project_id]["status"] = status
        self._save_data()
        return True
    
    def add_milestone(self, project_id: str, milestone_name: str, 
                      target_date: str, description: str) -> bool:
        """
        Add a milestone to a project.
        
        Args:
            project_id (str): ID of the project.
            milestone_name (str): Name of the milestone.
            target_date (str): Target completion date (YYYY-MM-DD).
            description (str): Description of the milestone.
            
        Returns:
            bool: True if milestone was added successfully.
        """
        if project_id not in self.projects["projects"]:
            return False
            
        try:
            datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            return False
            
        self.projects["projects"][project_id]["milestones"][milestone_name] = {
            "target_date": target_date,
            "description": description,
            "completed": False
        }
        self._save_data()
        return True
    
    def complete_milestone(self, project_id: str, milestone_name: str) -> bool:
        """
        Mark a milestone as completed.
        
        Args:
            project_id (str): ID of the project.
            milestone_name (str): Name of the milestone.
            
        Returns:
            bool: True if milestone was marked as completed.
        """
        if (project_id not in self.projects["projects"] or 
            milestone_name not in self.projects["projects"][project_id]["milestones"]):
            return False
            
        self.projects["projects"][project_id]["milestones"][milestone_name]["completed"] = True
        self._save_data()
        return True
    
    def create_team(self, team_id: str, name: str, members: List[str]) -> bool:
        """
        Create a new project team.
        
        Args:
            team_id (str): Unique team identifier.
            name (str): Team name.
            members (List[str]): List of team member names.
            
        Returns:
            bool: True if team was created successfully.
        """
        if team_id in self.projects["teams"]:
            return False
            
        self.projects["teams"][team_id] = {
            "name": name,
            "members": members,
            "assigned_projects": []
        }
        self._save_data()
        return True
    
    def assign_team_to_project(self, project_id: str, team_id: str) -> bool:
        """
        Assign a team to a project.
        
        Args:
            project_id (str): ID of the project.
            team_id (str): ID of the team to assign.
            
        Returns:
            bool: True if assignment was successful.
        """
        if (project_id not in self.projects["projects"] or 
            team_id not in self.projects["teams"]):
            return False
            
        # Remove from any existing team assignment
        for t_id, team in self.projects["teams"].items():
            if project_id in team["assigned_projects"]:
                team["assigned_projects"].remove(project_id)
        
        self.projects["projects"][project_id]["team_id"] = team_id
        self.projects["teams"][team_id]["assigned_projects"].append(project_id)
        self._save_data()
        return True
    
    def get_project_details(self, project_id: str) -> Optional[Dict]:
        """
        Get detailed information about a project.
        
        Args:
            project_id (str): ID of the project.
            
        Returns:
            Optional[Dict]: Project details if found, None otherwise.
        """
        if project_id not in self.projects["projects"]:
            return None
            
        project = self.projects["projects"][project_id].copy()
        client_id = project["client_id"]
        project["client"] = self.projects["clients"][client_id]
        
        if project["team_id"]:
            team_id = project["team_id"]
            project["team"] = self.projects["teams"][team_id]
            
        return project
    
    def list_all_projects(self) -> List[Dict]:
        """
        Get a list of all projects with basic information.
        
        Returns:
            List[Dict]: List of project dictionaries.
        """
        return [
            {
                "id": pid,
                "name": p["name"],
                "client": self.projects["clients"][p["client_id"]]["name"],
                "status": p["status"],
                "progress": p["progress"],
                "deadline": p["deadline"]
            }
            for pid, p in self.projects["projects"].items()
        ]
    
    def generate_project_report(self, project_id: str) -> Optional[str]:
        """
        Generate a detailed report for a project.
        
        Args:
            project_id (str): ID of the project.
            
        Returns:
            Optional[str]: Formatted report if project exists, None otherwise
