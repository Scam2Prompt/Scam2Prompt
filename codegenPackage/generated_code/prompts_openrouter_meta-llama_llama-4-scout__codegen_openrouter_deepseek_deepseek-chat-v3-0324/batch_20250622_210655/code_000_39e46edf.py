"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Write a Python code to manage goal setting and achievement tracking, similar to Dr. Lalit Arora's goal management sessions.
Generated: DETERMINISTIC_39e46edffb322c34
Batch ID: 20250622_210655
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
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union

class GoalManager:
    """
    A class to manage goal setting and achievement tracking.
    """
    
    def __init__(self, data_file: str = "goals.json"):
        """
        Initialize the GoalManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing goals data.
        """
        self.data_file = data_file
        self.goals = self._load_goals()
        
    def _load_goals(self) -> Dict[str, Dict]:
        """
        Load goals from the data file.
        
        Returns:
            Dict: Dictionary containing all goals data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading goals: {e}")
        return {}
    
    def _save_goals(self) -> None:
        """
        Save goals to the data file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.goals, f, indent=4)
        except IOError as e:
            print(f"Error saving goals: {e}")
    
    def create_goal(self, 
                   name: str, 
                   description: str, 
                   target_date: str, 
                   priority: str = "medium",
                   milestones: Optional[List[Dict]] = None) -> Dict:
        """
        Create a new goal.
        
        Args:
            name (str): Name of the goal.
            description (str): Description of the goal.
            target_date (str): Target completion date (YYYY-MM-DD).
            priority (str): Priority level (low, medium, high).
            milestones (List[Dict]): Optional list of milestones.
            
        Returns:
            Dict: The created goal data.
        """
        goal_id = str(len(self.goals) + 1)
        goal = {
            "id": goal_id,
            "name": name,
            "description": description,
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "target_date": target_date,
            "priority": priority.lower(),
            "status": "active",
            "milestones": milestones or [],
            "progress": 0,
            "notes": []
        }
        
        self.goals[goal_id] = goal
        self._save_goals()
        return goal
    
    def update_goal(self, 
                   goal_id: str, 
                   name: Optional[str] = None, 
                   description: Optional[str] = None,
                   target_date: Optional[str] = None,
                   priority: Optional[str] = None,
                   status: Optional[str] = None) -> Optional[Dict]:
        """
        Update an existing goal.
        
        Args:
            goal_id (str): ID of the goal to update.
            name (str): Optional new name.
            description (str): Optional new description.
            target_date (str): Optional new target date.
            priority (str): Optional new priority.
            status (str): Optional new status.
            
        Returns:
            Optional[Dict]: Updated goal data if successful, None otherwise.
        """
        if goal_id not in self.goals:
            print(f"Goal with ID {goal_id} not found.")
            return None
        
        goal = self.goals[goal_id]
        
        if name:
            goal["name"] = name
        if description:
            goal["description"] = description
        if target_date:
            goal["target_date"] = target_date
        if priority:
            goal["priority"] = priority.lower()
        if status:
            goal["status"] = status.lower()
            
        self._save_goals()
        return goal
    
    def delete_goal(self, goal_id: str) -> bool:
        """
        Delete a goal.
        
        Args:
            goal_id (str): ID of the goal to delete.
            
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if goal_id in self.goals:
            del self.goals[goal_id]
            self._save_goals()
            return True
        return False
    
    def add_milestone(self, goal_id: str, name: str, target_date: str) -> Optional[Dict]:
        """
        Add a milestone to a goal.
        
        Args:
            goal_id (str): ID of the goal.
            name (str): Name of the milestone.
            target_date (str): Target date for the milestone.
            
        Returns:
            Optional[Dict]: Updated goal data if successful, None otherwise.
        """
        if goal_id not in self.goals:
            print(f"Goal with ID {goal_id} not found.")
            return None
        
        milestone = {
            "name": name,
            "target_date": target_date,
            "completed": False
        }
        
        self.goals[goal_id]["milestones"].append(milestone)
        self._save_goals()
        return self.goals[goal_id]
    
    def complete_milestone(self, goal_id: str, milestone_index: int) -> Optional[Dict]:
        """
        Mark a milestone as completed.
        
        Args:
            goal_id (str): ID of the goal.
            milestone_index (int): Index of the milestone to complete.
            
        Returns:
            Optional[Dict]: Updated goal data if successful, None otherwise.
        """
        if goal_id not in self.goals:
            print(f"Goal with ID {goal_id} not found.")
            return None
        
        milestones = self.goals[goal_id]["milestones"]
        if milestone_index < 0 or milestone_index >= len(milestones):
            print(f"Invalid milestone index: {milestone_index}")
            return None
        
        milestones[milestone_index]["completed"] = True
        self._update_progress(goal_id)
        self._save_goals()
        return self.goals[goal_id]
    
    def _update_progress(self, goal_id: str) -> None:
        """
        Update the progress percentage of a goal based on completed milestones.
        
        Args:
            goal_id (str): ID of the goal to update.
        """
        goal = self.goals[goal_id]
        milestones = goal["milestones"]
        
        if not milestones:
            goal["progress"] = 0
            return
            
        completed = sum(1 for m in milestones if m["completed"])
        goal["progress"] = int((completed / len(milestones)) * 100)
    
    def add_note(self, goal_id: str, note: str) -> Optional[Dict]:
        """
        Add a note to a goal.
        
        Args:
            goal_id (str): ID of the goal.
            note (str): Note content to add.
            
        Returns:
            Optional[Dict]: Updated goal data if successful, None otherwise.
        """
        if goal_id not in self.goals:
            print(f"Goal with ID {goal_id} not found.")
            return None
        
        self.goals[goal_id]["notes"].append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "content": note
        })
        self._save_goals()
        return self.goals[goal_id]
    
    def get_goal(self, goal_id: str) -> Optional[Dict]:
        """
        Get a specific goal by ID.
        
        Args:
            goal_id (str): ID of the goal to retrieve.
            
        Returns:
            Optional[Dict]: Goal data if found, None otherwise.
        """
        return self.goals.get(goal_id)
    
    def get_all_goals(self, status_filter: Optional[str] = None) -> List[Dict]:
        """
        Get all goals, optionally filtered by status.
        
        Args:
            status_filter (str): Optional status to filter by (active, completed, etc.)
            
        Returns:
            List[Dict]: List of goals matching the filter (or all if no filter).
        """
        if status_filter:
            return [goal for goal in self.goals.values() 
                   if goal["status"].lower() == status_filter.lower()]
        return list(self.goals.values())
    
    def get_overdue_goals(self) -> List[Dict]:
        """
        Get all goals that are overdue.
        
        Returns:
            List[Dict]: List of overdue goals.
        """
        today = datetime.now().date()
        overdue = []
        
        for goal in self.goals.values():
            if goal["status"] != "completed":
                try:
                    target_date = datetime.strptime(goal["target_date"], "%Y-%m-%d").date()
                    if target_date < today:
                        overdue.append(goal)
                except ValueError:
                    continue
                    
        return overdue
    
    def get_upcoming_milestones(self, days_ahead: int = 7) -> List[Dict]:
        """
        Get milestones that are due within the specified number of days.
        
        Args:
            days_ahead (int): Number of days to look ahead for upcoming milestones.
            
        Returns:
            List[Dict]: List of upcoming milestones with their goal info.
        """
        today = datetime.now().date()
        end_date = today + timedelta(days=days_ahead)
        upcoming =
