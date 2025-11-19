"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tracker for Building Projects

This script tracks the progress of a building project using project management principles
emphasized by TWM Associates, including task tracking, milestone management, resource allocation,
and progress reporting.

Features:
- Task creation and status tracking
- Milestone management
- Resource allocation and tracking
- Progress reporting and analytics
- Error handling and data validation
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ProjectTracker:
    """Main class to track building project progress."""

    def __init__(self, project_name: str, start_date: str, end_date: str):
        """
        Initialize the project tracker with basic project information.

        Args:
            project_name: Name of the project
            start_date: Project start date (YYYY-MM-DD)
            end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.tasks: List[Dict] = []
        self.milestones: List[Dict] = []
        self.resources: List[Dict] = []
        self._validate_dates()

    def _validate_dates(self) -> None:
        """Validate that start date is before end date."""
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date")

    def add_task(
        self,
        task_name: str,
        description: str,
        assigned_to: str,
        estimated_hours: float,
        dependencies: Optional[List[str]] = None,
    ) -> None:
        """
        Add a new task to the project.

        Args:
            task_name: Name of the task
            description: Task description
            assigned_to: Resource assigned to the task
            estimated_hours: Estimated hours to complete
            dependencies: List of task names this task depends on
        """
        if dependencies is None:
            dependencies = []

        task = {
            "name": task_name,
            "description": description,
            "assigned_to": assigned_to,
            "estimated_hours": estimated_hours,
            "actual_hours": 0.0,
            "status": "Not Started",
            "dependencies": dependencies,
            "start_date": None,
            "end_date": None,
        }
        self.tasks.append(task)

    def update_task_status(
        self, task_name: str, status: str, actual_hours: Optional[float] = None
    ) -> None:
        """
        Update the status of a task.

        Args:
            task_name: Name of the task to update
            status: New status (Not Started, In Progress, Completed)
            actual_hours: Actual hours spent (optional)
        """
        task = self._find_task(task_name)
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")

        task["status"] = status
        if actual_hours is not None:
            task["actual_hours"] = actual_hours

        if status == "In Progress" and task["start_date"] is None:
            task["start_date"] = datetime.now().date()
        elif status == "Completed" and task["end_date"] is None:
            task["end_date"] = datetime.now().date()

    def add_milestone(self, name: str, target_date: str, description: str) -> None:
        """
        Add a milestone to the project.

        Args:
            name: Name of the milestone
            target_date: Target completion date (YYYY-MM-DD)
            description: Milestone description
        """
        target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
        milestone = {
            "name": name,
            "target_date": target_date,
            "description": description,
            "completed": False,
            "completion_date": None,
        }
        self.milestones.append(milestone)

    def complete_milestone(self, name: str) -> None:
        """Mark a milestone as completed."""
        milestone = self._find_milestone(name)
        milestone["completed"] = True
        milestone["completion_date"] = datetime.now().date()

    def add_resource(
        self, name: str, role: str, hourly_rate: float, max_hours_per_week: float
    ) -> None:
        """
        Add a resource to the project.

        Args:
            name: Name of the resource
            role: Role in the project
            hourly_rate: Hourly rate
            max_hours_per_week: Maximum available hours per week
        """
        resource = {
            "name": name,
            "role": role,
            "hourly_rate": hourly_rate,
            "max_hours_per_week": max_hours_per_week,
            "assigned_hours": 0.0,
        }
        self.resources.append(resource)

    def get_project_progress(self) -> Dict:
        """
        Calculate and return project progress metrics.

        Returns:
            Dictionary containing progress metrics
        """
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["status"] == "Completed")
        progress_percentage = (
            (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        )

        total_estimated_hours = sum(task["estimated_hours"] for task in self.tasks)
        total_actual_hours = sum(task["actual_hours"] for task in self.tasks)

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": progress_percentage,
            "total_estimated_hours": total_estimated_hours,
            "total_actual_hours": total_actual_hours,
        }

    def get_resource_utilization(self) -> List[Dict]:
        """
        Calculate resource utilization.

        Returns:
            List of resources with their utilization metrics
        """
        utilization = []
        for resource in self.resources:
            assigned_tasks = [
                task
                for task in self.tasks
                if task["assigned_to"] == resource["name"]
            ]
            assigned_hours = sum(task["estimated_hours"] for task in assigned_tasks)
            utilization_percentage = (
                (assigned_hours / resource["max_hours_per_week"]) * 100
                if resource["max_hours_per_week"] > 0
                else 0
            )

            utilization.append({
                "name": resource["name"],
                "role": resource["role"],
                "assigned_hours": assigned_hours,
                "max_hours": resource["max_hours_per_week"],
                "utilization_percentage": utilization_percentage,
            })

        return utilization

    def _find_task(self, task_name: str) -> Dict:
        """Find a task by name or raise error if not found."""
        for task in self.tasks:
            if task["name"] == task_name:
                return task
        raise ValueError(f"Task not found: {task_name}")

    def _find_milestone(self, milestone_name: str) -> Dict:
        """Find a milestone by name or raise error if not found."""
        for milestone in self.milestones:
            if milestone["name"] == milestone_name:
                return milestone
        raise ValueError(f"Milestone not found: {milestone_name}")

    def save_to_file(self, filename: str) -> None:
        """Save project data to a JSON file."""
        data = {
            "project_name": self.project_name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": self.tasks,
            "milestones": self.milestones,
            "resources": self.resources,
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> "ProjectTracker":
        """Load project data from a JSON file."""
        with open(filename) as f:
            data = json.load(f)

        tracker = cls(
            data["project_name"],
            data["start_date"],
            data["end_date"],
        )
        tracker.tasks = data["tasks"]
        tracker.milestones = data["milestones"]
        tracker.resources = data["resources"]
        return tracker


# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = ProjectTracker(
            "Office Building Construction",
            "2023-01-01",
            "2023-12-31"
        )

        # Add resources
        project.add_resource("John Doe", "Project Manager", 75.0, 40.0)
        project.add_resource("Jane Smith", "Architect", 60.0, 35.0)
        project.add_resource("Bob Johnson", "Engineer", 50.0, 40.0)

        # Add tasks
        project.add_task(
            "Site Preparation",
