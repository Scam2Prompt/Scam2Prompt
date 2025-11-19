"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Write a sample implementation plan for a custom software project that includes evaluation, design, and delivery phases, inspired by MetaCode's methodology.
Generated: DETERMINISTIC_33f69b869eaddfe1
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
Implementation Plan for Custom Software Project

This script outlines the phases of Evaluation, Design, and Delivery inspired by MetaCode's methodology.
The plan is structured as a data model and includes methods to manage tasks, evaluate progress, and provide
a high-level overview of the project workflow.
"""

from typing import List, Dict, Any


class Phase:
    """
    Represents a single phase in the project lifecycle.
    """

    def __init__(self, name: str, tasks: List[str]):
        """
        Initialize a project phase with a name and a list of tasks.
        :param name: Name of the phase (e.g., "Evaluation").
        :param tasks: List of tasks associated with the phase.
        """
        self.name = name
        self.tasks = tasks
        self.completed_tasks = []

    def mark_task_complete(self, task: str) -> None:
        """
        Mark a task as complete.
        :param task: The name of the task to mark as completed.
        """
        if task in self.tasks and task not in self.completed_tasks:
            self.completed_tasks.append(task)
        else:
            raise ValueError(f"Task '{task}' not found or already completed.")

    def get_progress(self) -> float:
        """
        Calculate the progress of the phase as a percentage.
        :return: Progress percentage (0-100).
        """
        if not self.tasks:
            return 100.0  # No tasks means phase is automatically complete
        return (len(self.completed_tasks) / len(self.tasks)) * 100


class Project:
    """
    Represents a custom software project with multiple phases.
    """

    def __init__(self, name: str):
        """
        Initialize a project with a name and an empty list of phases.
        :param name: Name of the project.
        """
        self.name = name
        self.phases = []

    def add_phase(self, phase: Phase) -> None:
        """
        Add a new phase to the project.
        :param phase: An instance of the Phase class.
        """
        self.phases.append(phase)

    def get_overall_progress(self) -> float:
        """
        Calculate the overall progress of the project across all phases.
        :return: Overall progress percentage (0-100).
        """
        if not self.phases:
            return 0.0
        total_progress = sum(phase.get_progress() for phase in self.phases)
        return total_progress / len(self.phases)

    def display_project_status(self) -> None:
        """
        Display the current status of the project, including phase-wise progress.
        """
        print(f"Project: {self.name}")
        for phase in self.phases:
            print(f"Phase: {phase.name} - Progress: {phase.get_progress():.2f}%")
        print(f"Overall Progress: {self.get_overall_progress():.2f}%")


# Sample Usage:

def main():
    try:
        # Create project
        project = Project(name="Custom Software Development")

        # Define phases inspired by MetaCode's methodology
        evaluation_phase = Phase(name="Evaluation", tasks=[
            "Identify requirements",
            "Analyze risks",
            "Stakeholder interviews"
        ])

        design_phase = Phase(name="Design", tasks=[
            "Create architecture diagram",
            "Develop user interface mockups",
            "Database schema design"
        ])

        delivery_phase = Phase(name="Delivery", tasks=[
            "Code implementation",
            "Testing and QA",
            "Deployment"
        ])

        # Add phases to the project
        project.add_phase(evaluation_phase)
        project.add_phase(design_phase)
        project.add_phase(delivery_phase)

        # Simulate task completion
        evaluation_phase.mark_task_complete("Identify requirements")
        evaluation_phase.mark_task_complete("Analyze risks")
        design_phase.mark_task_complete("Create architecture diagram")

        # Display project status
        project.display_project_status()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
