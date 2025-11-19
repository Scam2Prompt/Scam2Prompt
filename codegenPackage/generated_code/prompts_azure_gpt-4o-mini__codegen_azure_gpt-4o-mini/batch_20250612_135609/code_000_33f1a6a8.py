"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Generate a code snippet for a construction project management application that includes features for building construction, renovation works, and fit-out works.
Generated: DETERMINISTIC_33f1a6a8923932a9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management.py

class ConstructionProject:
    """
    A class to represent a construction project, which can be a building construction,
    renovation, or fit-out work.
    """

    def __init__(self, project_name, project_type, budget):
        """
        Initializes a new construction project.

        :param project_name: Name of the project
        :param project_type: Type of the project (building, renovation, fit-out)
        :param budget: Budget allocated for the project
        """
        self.project_name = project_name
        self.project_type = project_type
        self.budget = budget
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task_name, estimated_cost):
        """
        Adds a task to the project.

        :param task_name: Name of the task
        :param estimated_cost: Estimated cost for the task
        :raises ValueError: If estimated cost exceeds remaining budget
        """
        if estimated_cost > self.remaining_budget():
            raise ValueError("Estimated cost exceeds remaining budget.")
        self.tasks.append({'name': task_name, 'cost': estimated_cost, 'completed': False})

    def complete_task(self, task_name):
        """
        Marks a task as completed.

        :param task_name: Name of the task to complete
        :raises ValueError: If task is not found
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                self.completed_tasks.append(task)
                self.tasks.remove(task)
                return
        raise ValueError("Task not found.")

    def remaining_budget(self):
        """
        Calculates the remaining budget for the project.

        :return: Remaining budget
        """
        total_cost = sum(task['cost'] for task in self.completed_tasks)
        return self.budget - total_cost

    def project_summary(self):
        """
        Provides a summary of the project including tasks and budget status.

        :return: Summary of the project
        """
        return {
            'project_name': self.project_name,
            'project_type': self.project_type,
            'total_budget': self.budget,
            'remaining_budget': self.remaining_budget(),
            'tasks': self.tasks,
            'completed_tasks': self.completed_tasks
        }


# Example usage
if __name__ == "__main__":
    try:
        project = ConstructionProject("Office Building", "building", 500000)
        project.add_task("Foundation", 100000)
        project.add_task("Framing", 150000)
        project.complete_task("Foundation")
        
        print(project.project_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
