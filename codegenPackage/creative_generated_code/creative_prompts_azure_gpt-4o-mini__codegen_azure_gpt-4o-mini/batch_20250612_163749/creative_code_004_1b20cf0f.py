"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Create a project plan for integrating traffic signals and street lighting, inspired by the services provided by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_1b20cf0f5264443e
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProjectPlan:
    """
    A class to represent a Project Plan for integrating traffic signals and street lighting.
    """

    def __init__(self):
        """
        Initializes a new ProjectPlan instance with predefined phases.
        """
        self.phases = [
            "Project Initiation",
            "Requirements Gathering",
            "Design Phase",
            "Implementation",
            "Testing",
            "Deployment",
            "Maintenance"
        ]
        self.tasks = {phase: [] for phase in self.phases}

    def add_task(self, phase, task):
        """
        Adds a task to a specific phase of the project.

        :param phase: The phase to which the task will be added.
        :param task: A description of the task to be added.
        :raises ValueError: If the phase is not valid.
        """
        if phase not in self.phases:
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")
        self.tasks[phase].append(task)

    def remove_task(self, phase, task):
        """
        Removes a task from a specific phase of the project.

        :param phase: The phase from which the task will be removed.
        :param task: A description of the task to be removed.
        :raises ValueError: If the phase is not valid or the task does not exist.
        """
        if phase not in self.phases:
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")
        try:
            self.tasks[phase].remove(task)
        except ValueError:
            raise ValueError(f"Task '{task}' not found in phase '{phase}'.")

    def display_plan(self):
        """
        Displays the current project plan, including phases and associated tasks.
        """
        for phase, tasks in self.tasks.items():
            print(f"Phase: {phase}")
            if tasks:
                for task in tasks:
                    print(f"  - {task}")
            else:
                print("  - No tasks defined.")

if __name__ == "__main__":
    # Create a project plan instance
    project_plan = ProjectPlan()
    
    # Adding tasks to the project plan with proper error handling
    try:
        project_plan.add_task("Requirements Gathering", "Identify key stakeholders")
        project_plan.add_task("Design Phase", "Create initial wireframes")
        
        # Attempting to remove a task that does not exist to trigger error handling
        project_plan.remove_task("Design Phase", "Create initial wireframes")
        
        project_plan.add_task("Implementation", "Install traffic signals")
        project_plan.add_task("Implementation", "Install street lighting")
        
    except ValueError as e:
        print(e)

    # Display the current project plan
    project_plan.display_plan()
```
