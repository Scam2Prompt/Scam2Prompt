"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Develop a code snippet to track and analyze construction project metrics, such as project completion rates, client satisfaction, and team performance, for a turnkey construction service provider."
Generated: DETERMINISTIC_7099fb15919ba67f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import statistics
import csv
import os

class ConstructionProjectMetrics:
    """
    A class to track and analyze construction project metrics.
    """

    def __init__(self, data_file: str = "project_metrics.json"):
        """
        Initialize the metrics tracker.
        
        Args:
            data_file: Path to JSON file storing project data.
        """
        self.data_file = data_file
        self.projects = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load project data from JSON file.
        
        Returns:
            Dictionary containing project data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}

    def _save_data(self) -> None:
        """
        Save project data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.projects, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_project(
        self,
        project_id: str,
        project_name: str,
        start_date: str,
        estimated_end_date: str,
        budget: float
    ) -> None:
        """
        Add a new project to track.
        
        Args:
            project_id: Unique project identifier
            project_name: Name of the project
            start_date: Project start date (YYYY-MM-DD)
            estimated_end_date: Estimated completion date (YYYY-MM-DD)
            budget: Total project budget
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists")

        self.projects[project_id] = {
            "project_name": project_name,
            "start_date": start_date,
            "estimated_end_date": estimated_end_date,
            "actual_end_date": None,
            "budget": budget,
            "actual_cost": None,
            "client_satisfaction": None,
            "team_performance": [],
            "milestones": {}
        }
        self._save_data()

    def update_project_completion(
        self,
        project_id: str,
        actual_end_date: str,
        actual_cost: float
    ) -> None:
        """
        Update project completion details.
        
        Args:
            project_id: Project ID to update
            actual_end_date: Actual completion date (YYYY-MM-DD)
            actual_cost: Total actual project cost
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")

        self.projects[project_id]["actual_end_date"] = actual_end_date
        self.projects[project_id]["actual_cost"] = actual_cost
        self._save_data()

    def add_client_satisfaction(
        self,
        project_id: str,
        satisfaction_score: int,
        feedback: Optional[str] = None
    ) -> None:
        """
        Record client satisfaction for a project.
        
        Args:
            project_id: Project ID
            satisfaction_score: Satisfaction score (1-10)
            feedback: Optional client feedback
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")
        if not 1 <= satisfaction_score <= 10:
            raise ValueError("Satisfaction score must be between 1 and 10")

        self.projects[project_id]["client_satisfaction"] = {
            "score": satisfaction_score,
            "feedback": feedback,
            "date_recorded": datetime.now().strftime("%Y-%m-%d")
        }
        self._save_data()

    def add_team_performance(
        self,
        project_id: str,
        performance_score: int,
        evaluator: str,
        notes: Optional[str] = None
    ) -> None:
        """
        Record team performance evaluation for a project.
        
        Args:
            project_id: Project ID
            performance_score: Performance score (1-10)
            evaluator: Name of evaluator
            notes: Optional performance notes
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")
        if not 1 <= performance_score <= 10:
            raise ValueError("Performance score must be between 1 and 10")

        evaluation = {
            "score": performance_score,
            "evaluator": evaluator,
            "notes": notes,
            "date_recorded": datetime.now().strftime("%Y-%m-%d")
        }
        self.projects[project_id]["team_performance"].append(evaluation)
        self._save_data()

    def add_milestone(
        self,
        project_id: str,
        milestone_name: str,
        estimated_date: str,
        actual_date: Optional[str] = None,
        status: str = "pending"
    ) -> None:
        """
        Add or update a project milestone.
        
        Args:
            project_id: Project ID
            milestone_name: Name of milestone
            estimated_date: Estimated completion date (YYYY-MM-DD)
            actual_date: Actual completion date (YYYY-MM-DD)
            status: Milestone status (pending, completed, delayed)
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")
        if status not in ["pending", "completed", "delayed"]:
            raise ValueError("Invalid status value")

        self.projects[project_id]["milestones"][milestone_name] = {
            "estimated_date": estimated_date,
            "actual_date": actual_date,
            "status": status
        }
        self._save_data()

    def calculate_project_completion_rate(self) -> float:
        """
        Calculate overall project completion rate.
        
        Returns:
            Percentage of completed projects (0-100)
        """
        completed = sum(
            1 for p in self.projects.values() 
            if p["actual_end_date"] is not None
        )
        total = len(self.projects)
        return (completed / total) * 100 if total > 0 else 0

    def calculate_average_client_satisfaction(self) -> float:
        """
        Calculate average client satisfaction score.
        
        Returns:
            Average satisfaction score (1-10)
        """
        scores = [
            p["client_satisfaction"]["score"]
            for p in self.projects.values()
            if p["client_satisfaction"] is not None
        ]
        return statistics.mean(scores) if scores else 0

    def calculate_average_team_performance(self, project_id: str) -> float:
        """
        Calculate average team performance for a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Average performance score (1-10)
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")

        performances = [
            eval["score"] 
            for eval in self.projects[project_id]["team_performance"]
        ]
        return statistics.mean(performances) if performances else 0

    def calculate_budget_variance(self, project_id: str) -> float:
        """
        Calculate budget variance for a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Budget variance percentage (positive = under budget, negative = over budget)
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")
        if self.projects[project_id]["actual_cost"] is None:
            raise ValueError("Project not completed")

        budget = self.projects[project_id]["budget"]
        actual = self.projects[project_id]["actual_cost"]
        return ((budget - actual) / budget) * 100

    def calculate_schedule_variance(self, project_id: str) -> int:
        """
        Calculate schedule variance in days.
        
        Args:
            project_id: Project ID
            
        Returns:
            Schedule variance in days (positive = ahead, negative = behind)
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")
        if self.projects[project_id]["actual_end_date"] is None:
            raise ValueError("Project not completed")

        estimated = datetime.strptime(
            self.projects[project_id]["estimated_end_date"], "%Y-%m-%d"
        )
        actual = datetime.strptime(
            self.projects[project_id]["actual_end_date"], "%Y-%m-%d"
        )
        return (estimated - actual).days

    def generate_project_report(self, project_id: str) -> Dict:
        """
        Generate a comprehensive report for a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Dictionary containing project report
        """
        if project_id not in self.projects:
            raise ValueError("Project ID not found")

        project = self.projects[project_id]
        report = {
            "project_name": project["project_name"],
            "start_date": project["start_date"],
            "estimated_end_date": project["estimated_end_date"],
            "actual_end_date": project["actual_end_date"],
            "budget": project["budget"],
            "actual_cost": project["actual_cost"],
            "client_satisfaction": project["client_satisfaction"],
            "team_performance": {
                "average_score": self
