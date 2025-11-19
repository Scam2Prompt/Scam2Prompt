"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Script for Building Project Progress Tracking
Author: [Your Name]
Date: [Insert Date]
Description: This script tracks the progress of a building project based on key phases 
             such as planning, execution, monitoring, and closure. It incorporates principles 
             related to task completion, deadlines, milestones, and resource allocation. 
             The code uses Python best practices and includes error handling for robustness.
"""

import datetime
from typing import List, Dict


class ProjectPhase:
    """
    Class to represent a phase of the building project.
    Each phase contains tasks, deadlines, and completion status.
    """

    def __init__(self, name: str, deadline: datetime.date):
        """
        Initialize a project phase.
        :param name: Name of the phase.
        :param deadline: Deadline for the phase.
        """
        self.name = name
        self.deadline = deadline
        self.tasks: Dict[str, bool] = {}  # Dictionary of tasks and their completion status

    def add_task(self, task_name: str):
        """
        Add a new task to the phase.
        :param task_name: Name of the task.
        """
        self.tasks[task_name] = False  # Task is initially not completed

    def complete_task(self, task_name: str):
        """
        Mark a task as completed.
        :param task_name: Name of the task.
        """
        if task_name in self.tasks:
            self.tasks[task_name] = True
        else:
            raise ValueError(f"Task '{task_name}' does not exist in phase '{self.name}'.")

    def get_progress(self) -> float:
        """
        Calculate the completion percentage of the phase.
        :return: Completion percentage as a float.
        """
        if not self.tasks:
            return 0.0
        completed_tasks = sum(1 for task in self.tasks.values() if task)
        return (completed_tasks / len(self.tasks)) * 100

    def is_overdue(self) -> bool:
        """
        Check if the phase is overdue based on the current date.
        :return: True if overdue, False otherwise.
        """
        return datetime.date.today() > self.deadline


class BuildingProject:
    """
    Class to represent the building project as a whole,
    containing multiple phases and tracking overall progress.
    """

    def __init__(self, name: str):
        """
        Initialize the building project.
        :param name: Name of the project.
        """
        self.name = name
        self.phases: List[ProjectPhase] = []

    def add_phase(self, phase: ProjectPhase):
        """
        Add a new phase to the project.
        :param phase: Instance of ProjectPhase.
        """
        self.phases.append(phase)

    def get_overall_progress(self) -> float:
        """
        Calculate the overall progress of the project.
        :return: Overall progress percentage as a float.
        """
        if not self.phases:
            return 0.0
        total_progress = sum(phase.get_progress() for phase in self.phases)
        return total_progress / len(self.phases)

    def get_overdue_phases(self) -> List[ProjectPhase]:
        """
        Get a list of phases that are overdue.
        :return: List of overdue phases.
        """
        return [phase for phase in self.phases if phase.is_overdue()]

    def display_status(self):
        """
        Display the current status of the project and its phases.
        """
        print(f"Project: {self.name}")
        print(f"Overall Progress: {self.get_overall_progress():.2f}%")
        print("Phases:")
        for phase in self.phases:
            print(f"  - Phase: {phase.name}")
            print(f"    Deadline: {phase.deadline}")
            print(f"    Progress: {phase.get_progress():.2f}%")
            print(f"    Overdue: {'Yes' if phase.is_overdue() else 'No'}")
            print(f"    Tasks:")
            for task_name, completed in phase.tasks.items():
                print(f"      - Task: {task_name}, Completed: {'Yes' if completed else 'No'}")
        print()


# Example usage of the script
if __name__ == "__main__":
    try:
        # Create a building project
        project = BuildingProject("TWM Building Project")

        # Add phases to the project
        planning_phase = ProjectPhase(name="Planning", deadline=datetime.date(2023, 11, 15))
        execution_phase = ProjectPhase(name="Execution", deadline=datetime.date(2023, 12, 31))

        # Add tasks to planning phase
        planning_phase.add_task("Site Survey")
        planning_phase.add_task("Blueprint Design")
        planning_phase.add_task("Budget Approval")

        # Add tasks to execution phase
        execution_phase.add_task("Foundation Laying")
        execution_phase.add_task("Structural Construction")
        execution_phase.add_task("Electrical Setup")

        # Mark some tasks as completed
        planning_phase.complete_task("Site Survey")
        planning_phase.complete_task("Blueprint Design")

        # Add phases to the project
        project.add_phase(planning_phase)
        project.add_phase(execution_phase)

        # Display project status
        project.display_status()

    except Exception as e:
        print(f"An error occurred: {e}")
```
