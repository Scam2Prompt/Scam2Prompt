"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Write a Python script to manage luxury property development projects, including features like quality control, timeline management, and fixed management fee calculation.
Generated: DETERMINISTIC_c7b658cd8b949066
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional


class ProjectStatus(Enum):
    """Enumeration for project status."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class QualityRating(Enum):
    """Enumeration for quality control ratings."""
    POOR = 1
    FAIR = 2
    GOOD = 3
    VERY_GOOD = 4
    EXCELLENT = 5


class LuxuryPropertyProject:
    """Class to manage luxury property development projects."""

    MANAGEMENT_FEE_PERCENTAGE = 0.05  # 5% fixed management fee

    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, budget: float):
        """Initialize a luxury property project.

        Args:
            name: Name of the project
            start_date: Project start date
            end_date: Project end date
            budget: Total project budget
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = ProjectStatus.NOT_STARTED
        self.tasks = []
        self.quality_checks = []
        self.actual_costs = 0.0

    def add_task(self, task_name: str, duration_days: int, dependencies: List[str] = None) -> None:
        """Add a task to the project.

        Args:
            task_name: Name of the task
            duration_days: Duration in days
            dependencies: List of task names this task depends on
        """
        if dependencies is None:
            dependencies = []
        self.tasks.append({
            'name': task_name,
            'duration': duration_days,
            'dependencies': dependencies,
            'completed': False
        })

    def update_task_status(self, task_name: str, completed: bool) -> None:
        """Update the completion status of a task.

        Args:
            task_name: Name of the task to update
            completed: Completion status
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = completed
                return
        raise ValueError(f"Task '{task_name}' not found")

    def add_quality_check(self, check_name: str, rating: QualityRating, notes: str = "") -> None:
        """Add a quality control check to the project.

        Args:
            check_name: Name of the quality check
            rating: Quality rating
            notes: Additional notes
        """
        self.quality_checks.append({
            'name': check_name,
            'rating': rating,
            'notes': notes,
            'date': datetime.date.today()
        })

    def record_cost(self, amount: float) -> None:
        """Record an actual cost against the project.

        Args:
            amount: Cost amount to record
        """
        if amount < 0:
            raise ValueError("Cost amount cannot be negative")
        self.actual_costs += amount

    def calculate_management_fee(self) -> float:
        """Calculate the fixed management fee.

        Returns:
            float: Calculated management fee amount
        """
        return self.budget * self.MANAGEMENT_FEE_PERCENTAGE

    def get_project_timeline(self) -> Dict:
        """Get project timeline information.

        Returns:
            Dict: Timeline information including days remaining and completion percentage
        """
        today = datetime.date.today()
        total_days = (self.end_date - self.start_date).days
        days_remaining = (self.end_date - today).days if self.end_date > today else 0
        elapsed_days = (today - self.start_date).days if today > self.start_date else 0

        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        total_tasks = len(self.tasks)
        completion_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

        return {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_days': total_days,
            'days_remaining': days_remaining,
            'elapsed_days': elapsed_days,
            'completion_percentage': completion_percentage,
            'on_schedule': days_remaining >= (total_days - elapsed_days)
        }

    def get_project_summary(self) -> Dict:
        """Get a summary of the project.

        Returns:
            Dict: Project summary information
        """
        timeline = self.get_project_timeline()
        avg_quality = self._calculate_average_quality()

        return {
            'name': self.name,
            'status': self.status.value,
            'budget': self.budget,
            'actual_costs': self.actual_costs,
            'remaining_budget': self.budget - self.actual_costs,
            'management_fee': self.calculate_management_fee(),
            'start_date': self.start_date,
            'end_date': self.end_date,
            'days_remaining': timeline['days_remaining'],
            'completion_percentage': timeline['completion_percentage'],
            'on_schedule': timeline['on_schedule'],
            'average_quality': avg_quality,
            'total_tasks': len(self.tasks),
            'completed_tasks': sum(1 for task in self.tasks if task['completed'])
        }

    def _calculate_average_quality(self) -> Optional[float]:
        """Calculate the average quality rating.

        Returns:
            Optional[float]: Average quality rating or None if no checks exist
        """
        if not self.quality_checks:
            return None
        total = sum(check['rating'].value for check in self.quality_checks)
        return total / len(self.quality_checks)


class LuxuryPropertyManager:
    """Class to manage multiple luxury property projects."""

    def __init__(self):
        """Initialize the property manager."""
        self.projects = {}

    def add_project(self, project: LuxuryPropertyProject) -> None:
        """Add a project to the manager.

        Args:
            project: Project to add
        """
        if project.name in self.projects:
            raise ValueError(f"Project with name '{project.name}' already exists")
        self.projects[project.name] = project

    def get_project(self, project_name: str) -> LuxuryPropertyProject:
        """Get a project by name.

        Args:
            project_name: Name of the project to retrieve

        Returns:
            LuxuryPropertyProject: The requested project
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found")
        return self.projects[project_name]

    def remove_project(self, project_name: str) -> None:
        """Remove a project from the manager.

        Args:
            project_name: Name of the project to remove
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found")
        del self.projects[project_name]

    def get_all_project_summaries(self) -> List[Dict]:
        """Get summaries for all projects.

        Returns:
            List[Dict]: List of project summaries
        """
        return [project.get_project_summary() for project in self.projects.values()]

    def get_projects_by_status(self, status: ProjectStatus) -> List[Dict]:
        """Get projects filtered by status.

        Args:
            status: Status to filter by

        Returns:
            List[Dict]: List of project summaries matching the status
        """
        return [
            project.get_project_summary()
            for project in self.projects.values()
            if project.status == status
        ]


# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = LuxuryPropertyManager()

    # Create a new project
    today = datetime.date.today()
    project = LuxuryPropertyProject(
        name="Oceanview Villa",
        start_date=today,
        end_date=today + datetime.timedelta(days=180),
        budget=5000000.00
    )

    # Add tasks to the project
    project.add_task("Site Preparation", 30)
    project.add_task("Foundation Work", 45, ["Site Preparation"])
    project.add_task("Structural Work", 60, ["Foundation Work"])
    project.add_task("Interior Finishing", 45, ["Structural Work"])
    project.add_task("Landscaping", 30, ["Structural Work"])

    # Add quality checks
    project.add_quality_check("Foundation Inspection", QualityRating.EXCELLENT)
    project.add_quality_check("Electrical Work", QualityRating.VERY_GOOD, "Minor issues found")

    # Record some costs
    project.record_cost(250000.00)
    project.record_cost(500000.00)

    # Add project to manager
    manager.add_project(project)

    # Print project summary
    summary = project.get_project_summary()
    print("Project Summary:")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
