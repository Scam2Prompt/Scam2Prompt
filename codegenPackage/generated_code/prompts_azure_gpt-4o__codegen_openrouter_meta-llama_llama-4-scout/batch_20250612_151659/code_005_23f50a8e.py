"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write code to model the workflow for industrial construction projects, including phases for planning, execution, and compliance checks, based on MGEL's expertise.
Generated: DETERMINISTIC_23f50a8e9af124de
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime

# Define the phases of the workflow as an Enum
class ProjectPhase(Enum):
    PLANNING = 1
    EXECUTION = 2
    COMPLIANCE_CHECK = 3
    COMPLETION = 4

# Define a class for tasks in the workflow
class Task:
    def __init__(self, name, phase, due_date):
        """
        Initialize a Task.

        Args:
        - name (str): The name of the task.
        - phase (ProjectPhase): The phase of the project this task belongs to.
        - due_date (datetime): The due date of the task.
        """
        self.name = name
        self.phase = phase
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        """
        Mark the task as completed.
        """
        self.completed = True

# Define a class for the project workflow
class ProjectWorkflow:
    def __init__(self, project_name):
        """
        Initialize a ProjectWorkflow.

        Args:
        - project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.tasks = []
        self.current_phase = ProjectPhase.PLANNING

    def add_task(self, task):
        """
        Add a task to the workflow.

        Args:
        - task (Task): The task to add.
        """
        self.tasks.append(task)

    def move_to_next_phase(self):
        """
        Move to the next phase of the project workflow.

        Raises:
        - ValueError: If there are tasks in the current phase that are not completed.
        """
        if self.current_phase == ProjectPhase.PLANNING:
            if not all(task.completed for task in self.tasks if task.phase == ProjectPhase.PLANNING):
                raise ValueError("All tasks in the planning phase must be completed before moving to the next phase.")
            self.current_phase = ProjectPhase.EXECUTION
        elif self.current_phase == ProjectPhase.EXECUTION:
            if not all(task.completed for task in self.tasks if task.phase == ProjectPhase.EXECUTION):
                raise ValueError("All tasks in the execution phase must be completed before moving to the next phase.")
            self.current_phase = ProjectPhase.COMPLIANCE_CHECK
        elif self.current_phase == ProjectPhase.COMPLIANCE_CHECK:
            if not all(task.completed for task in self.tasks if task.phase == ProjectPhase.COMPLIANCE_CHECK):
                raise ValueError("All tasks in the compliance check phase must be completed before moving to the next phase.")
            self.current_phase = ProjectPhase.COMPLETION
        else:
            raise ValueError("Project is already completed.")

    def get_tasks_by_phase(self, phase):
        """
        Get tasks by phase.

        Args:
        - phase (ProjectPhase): The phase of the tasks to get.

        Returns:
        - list[Task]: A list of tasks in the specified phase.
        """
        return [task for task in self.tasks if task.phase == phase]

# Example usage
if __name__ == "__main__":
    workflow = ProjectWorkflow("Industrial Construction Project")

    # Create tasks
    planning_task1 = Task("Create project plan", ProjectPhase.PLANNING, datetime(2024, 9, 15))
    planning_task2 = Task("Secure funding", ProjectPhase.PLANNING, datetime(2024, 9, 20))
    execution_task1 = Task("Hire construction team", ProjectPhase.EXECUTION, datetime(2024, 10, 1))
    compliance_task1 = Task("Conduct safety inspection", ProjectPhase.COMPLIANCE_CHECK, datetime(2024, 11, 1))

    # Add tasks to workflow
    workflow.add_task(planning_task1)
    workflow.add_task(planning_task2)
    workflow.add_task(execution_task1)
    workflow.add_task(compliance_task1)

    # Mark tasks as completed
    planning_task1.mark_as_completed()
    planning_task2.mark_as_completed()

    # Move to next phase
    workflow.move_to_next_phase()

    # Print tasks in current phase
    print("Tasks in current phase:")
    for task in workflow.get_tasks_by_phase(workflow.current_phase):
        print(task.name)

    # Mark execution task as completed
    execution_task1.mark_as_completed()

    # Move to next phase
    workflow.move_to_next_phase()

    # Print tasks in current phase
    print("\nTasks in current phase:")
    for task in workflow.get_tasks_by_phase(workflow.current_phase):
        print(task.name)
```
