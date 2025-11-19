"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate a Python script that implements educational projects similar to those described by the I.E. Benjamín Correa Álvarez, focusing on enhancing academic quality.
Generated: DETERMINISTIC_3fec470d8a1cc44f
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Educational Projects Enhancement Script

This script implements educational projects aimed at enhancing academic quality,
inspired by the work of I.E. Benjamín Correa Álvarez. It includes functionality
for managing projects, tracking progress, and evaluating outcomes.

Features:
- Project creation and management
- Progress tracking
- Outcome evaluation
- Reporting capabilities
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class EducationalProject:
    """Class representing an educational project."""

    def __init__(self, name: str, description: str, objectives: List[str], target_audience: str):
        """
        Initialize an educational project.

        Args:
            name: Name of the project
            description: Project description
            objectives: List of learning objectives
            target_audience: Intended audience (e.g., "primary school students")
        """
        self.name = name
        self.description = description
        self.objectives = objectives
        self.target_audience = target_audience
        self.start_date = datetime.now().date()
        self.end_date = None
        self.tasks = []
        self.metrics = {}
        self.status = "planned"
        self.participants = []

    def add_task(self, task_name: str, deadline: str, responsible: str) -> None:
        """
        Add a task to the project.

        Args:
            task_name: Name of the task
            deadline: Deadline in YYYY-MM-DD format
            responsible: Person responsible for the task
        """
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
            self.tasks.append({
                "name": task_name,
                "deadline": deadline_date,
                "responsible": responsible,
                "completed": False
            })
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e

    def complete_task(self, task_name: str) -> None:
        """
        Mark a task as completed.

        Args:
            task_name: Name of the task to mark as completed
        """
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                return
        raise ValueError(f"Task '{task_name}' not found")

    def add_metric(self, metric_name: str, target_value: float) -> None:
        """
        Add a performance metric to track.

        Args:
            metric_name: Name of the metric
            target_value: Target value to achieve
        """
        self.metrics[metric_name] = {
            "target": target_value,
            "current": None,
            "unit": ""
        }

    def update_metric(self, metric_name: str, current_value: float, unit: str = "") -> None:
        """
        Update a performance metric.

        Args:
            metric_name: Name of the metric to update
            current_value: Current value achieved
            unit: Unit of measurement (optional)
        """
        if metric_name not in self.metrics:
            raise ValueError(f"Metric '{metric_name}' not found")
        self.metrics[metric_name]["current"] = current_value
        self.metrics[metric_name]["unit"] = unit

    def add_participant(self, participant_name: str, role: str) -> None:
        """
        Add a participant to the project.

        Args:
            participant_name: Name of the participant
            role: Role in the project
        """
        self.participants.append({
            "name": participant_name,
            "role": role
        })

    def set_status(self, new_status: str) -> None:
        """
        Set the project status.

        Args:
            new_status: New status (planned, in_progress, completed, cancelled)
        """
        valid_statuses = ["planned", "in_progress", "completed", "cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        self.status = new_status

    def to_dict(self) -> Dict:
        """Convert project data to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "objectives": self.objectives,
            "target_audience": self.target_audience,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date) if self.end_date else None,
            "tasks": self.tasks,
            "metrics": self.metrics,
            "status": self.status,
            "participants": self.participants
        }


class ProjectManager:
    """Class for managing multiple educational projects."""

    def __init__(self, storage_file: str = "projects.json"):
        """
        Initialize the project manager.

        Args:
            storage_file: Path to JSON file for storing projects
        """
        self.storage_file = storage_file
        self.projects = {}
        self._load_projects()

    def _load_projects(self) -> None:
        """Load projects from storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    projects_data = json.load(f)
                    for name, data in projects_data.items():
                        project = EducationalProject(
                            name=data["name"],
                            description=data["description"],
                            objectives=data["objectives"],
                            target_audience=data["target_audience"]
                        )
                        project.start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
                        if data["end_date"]:
                            project.end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
                        project.tasks = data["tasks"]
                        project.metrics = data["metrics"]
                        project.status = data["status"]
                        project.participants = data["participants"]
                        self.projects[name] = project
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                raise RuntimeError(f"Error loading projects: {str(e)}") from e

    def _save_projects(self) -> None:
        """Save projects to storage file."""
        projects_data = {name: project.to_dict() for name, project in self.projects.items()}
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(projects_data, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Error saving projects: {str(e)}") from e

    def create_project(self, name: str, description: str, objectives: List[str], target_audience: str) -> EducationalProject:
        """
        Create a new educational project.

        Args:
            name: Name of the project
            description: Project description
            objectives: List of learning objectives
            target_audience: Intended audience

        Returns:
            The created project
        """
        if name in self.projects:
            raise ValueError(f"Project '{name}' already exists")
        project = EducationalProject(name, description, objectives, target_audience)
        self.projects[name] = project
        self._save_projects()
        return project

    def get_project(self, name: str) -> EducationalProject:
        """
        Get a project by name.

        Args:
            name: Name of the project to retrieve

        Returns:
            The requested project
        """
        if name not in self.projects:
            raise ValueError(f"Project '{name}' not found")
        return self.projects[name]

    def delete_project(self, name: str) -> None:
        """
        Delete a project.

        Args:
            name: Name of the project to delete
        """
        if name not in self.projects:
            raise ValueError(f"Project '{name}' not found")
        del self.projects[name]
        self._save_projects()

    def list_projects(self, status_filter: Optional[str] = None) -> List[Dict]:
        """
        List all projects, optionally filtered by status.

        Args:
            status_filter: Optional status filter (planned, in_progress, completed, cancelled)

        Returns:
            List of project summaries
        """
        if status_filter:
            valid_statuses = ["planned", "in_progress", "completed", "cancelled"]
            if status_filter not in valid_statuses:
                raise ValueError(f"Invalid status filter. Must be one of: {', '.join(valid_statuses)}")
            return [project.to_dict() for project in self.projects.values() if project.status == status_filter]
        return [project.to_dict() for project in self.projects.values()]

    def generate_report(self, name: str) -> Dict:
        """
        Generate a report for a project.

        Args:
            name: Name of the project to report on

        Returns:
            Dictionary containing project report
        """
        project = self.get_project(name)
        report = {
            "project_name": project.name,
            "status": project.status,
            "start_date": str(project.start_date),
            "end_date": str(project.end_date) if project.end_date else "Ongoing",
            "participants": len(project.participants),
            "tasks": {
                "
