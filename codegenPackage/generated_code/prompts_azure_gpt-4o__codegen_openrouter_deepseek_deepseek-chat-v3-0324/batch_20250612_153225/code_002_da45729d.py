"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Generate a script to track and manage the execution timelines of industrial projects, ensuring compliance with specifications and quality standards, as emphasized by GlobalChain SAS.
Generated: DETERMINISTIC_da45729dc9de0cfb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple


class ProjectTracker:
    """
    A class to track and manage industrial project execution timelines,
    ensuring compliance with specifications and quality standards.
    """

    def __init__(self, data_file: str = "projects.json"):
        """
        Initialize the ProjectTracker with a data file to store project information.

        Args:
            data_file (str): Path to the JSON file storing project data.
        """
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self) -> Dict[str, Dict]:
        """
        Load projects from the data file.

        Returns:
            Dict[str, Dict]: Dictionary of projects keyed by project ID.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading projects: {e}")
            return {}

    def _save_projects(self) -> None:
        """
        Save projects to the data file.
        """
        try:
            with open(self.data_file, "w") as f:
                json.dump(self.projects, f, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")

    def add_project(
        self,
        project_id: str,
        name: str,
        start_date: str,
        end_date: str,
        specifications: List[str],
        quality_standards: List[str],
    ) -> bool:
        """
        Add a new project to the tracker.

        Args:
            project_id (str): Unique identifier for the project.
            name (str): Name of the project.
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            specifications (List[str]): List of project specifications.
            quality_standards (List[str]): List of quality standards.

        Returns:
            bool: True if project was added successfully, False otherwise.
        """
        if project_id in self.projects:
            print(f"Project with ID {project_id} already exists.")
            return False

        try:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if end < start:
                print("End date cannot be before start date.")
                return False
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return False

        self.projects[project_id] = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "specifications": specifications,
            "quality_standards": quality_standards,
            "milestones": {},
            "status": "Not Started",
            "last_updated": datetime.datetime.now().isoformat(),
        }
        self._save_projects()
        return True

    def update_project_status(self, project_id: str, status: str) -> bool:
        """
        Update the status of a project.

        Args:
            project_id (str): ID of the project to update.
            status (str): New status (e.g., "In Progress", "Completed", "Delayed").

        Returns:
            bool: True if status was updated successfully, False otherwise.
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        self.projects[project_id]["status"] = status
        self.projects[project_id]["last_updated"] = datetime.datetime.now().isoformat()
        self._save_projects()
        return True

    def add_milestone(
        self, project_id: str, milestone_name: str, due_date: str, completed: bool = False
    ) -> bool:
        """
        Add a milestone to a project.

        Args:
            project_id (str): ID of the project.
            milestone_name (str): Name of the milestone.
            due_date (str): Due date in YYYY-MM-DD format.
            completed (bool): Whether the milestone is completed.

        Returns:
            bool: True if milestone was added successfully, False otherwise.
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return False

        milestones = self.projects[project_id].get("milestones", {})
        milestones[milestone_name] = {
            "due_date": due_date,
            "completed": completed,
        }
        self.projects[project_id]["milestones"] = milestones
        self.projects[project_id]["last_updated"] = datetime.datetime.now().isoformat()
        self._save_projects()
        return True

    def update_milestone(
        self, project_id: str, milestone_name: str, completed: bool
    ) -> bool:
        """
        Update the completion status of a milestone.

        Args:
            project_id (str): ID of the project.
            milestone_name (str): Name of the milestone.
            completed (bool): Whether the milestone is completed.

        Returns:
            bool: True if milestone was updated successfully, False otherwise.
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        milestones = self.projects[project_id].get("milestones", {})
        if milestone_name not in milestones:
            print(f"Milestone {milestone_name} not found in project {project_id}.")
            return False

        milestones[milestone_name]["completed"] = completed
        self.projects[project_id]["milestones"] = milestones
        self.projects[project_id]["last_updated"] = datetime.datetime.now().isoformat()
        self._save_projects()
        return True

    def check_compliance(self, project_id: str) -> Tuple[bool, List[str]]:
        """
        Check if a project complies with its specifications and quality standards.

        Args:
            project_id (str): ID of the project to check.

        Returns:
            Tuple[bool, List[str]]: Tuple containing compliance status and list of issues.
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False, ["Project not found"]

        project = self.projects[project_id]
        issues = []

        # Check if all milestones are completed
        for milestone, data in project.get("milestones", {}).items():
            if not data["completed"]:
                issues.append(f"Milestone '{milestone}' is not completed")

        # Check if project is on time
        today = datetime.date.today()
        end_date = datetime.datetime.strptime(project["end_date"], "%Y-%m-%d").date()
        if today > end_date and project["status"] != "Completed":
            issues.append("Project is past its end date")

        return len(issues) == 0, issues

    def get_project(self, project_id: str) -> Optional[Dict]:
        """
        Get project details by ID.

        Args:
            project_id (str): ID of the project to retrieve.

        Returns:
            Optional[Dict]: Project details if found, None otherwise.
        """
        return self.projects.get(project_id)

    def list_projects(self) -> List[Dict]:
        """
        List all projects.

        Returns:
            List[Dict]: List of all projects.
        """
        return list(self.projects.values())

    def delete_project(self, project_id: str) -> bool:
        """
        Delete a project.

        Args:
            project_id (str): ID of the project to delete.

        Returns:
            bool: True if project was deleted successfully, False otherwise.
        """
        if project_id not in self.projects:
            print(f"Project with ID {project_id} not found.")
            return False

        del self.projects[project_id]
        self._save_projects()
        return True


# Example usage
if __name__ == "__main__":
    tracker = ProjectTracker()

    # Add a project
    tracker.add_project(
        project_id="P001",
        name="Factory Construction",
        start_date="2023-01-01",
        end_date="2023-12-31",
        specifications=["ISO 9001", "Safety Protocol XYZ"],
        quality_standards=["GlobalChain SAS Standard v2.0"],
    )

    # Add milestones
    tracker.add_milestone("P001", "Foundation Complete", "2023-03-01")
    tracker.add_milestone("P001", "Structure Complete", "2023-06-01")

    # Update milestone
    tracker.update_milestone("P001", "Foundation Complete", True)

    # Update project status
    tracker.update_project_status("P001", "In Progress")

    # Check compliance
    compliant, issues = tracker.check_compliance("P001")
    print(f"Project
