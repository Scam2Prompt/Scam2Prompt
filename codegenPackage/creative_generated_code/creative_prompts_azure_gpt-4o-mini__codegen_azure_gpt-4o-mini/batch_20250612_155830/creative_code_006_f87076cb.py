"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimisenow.net
Prompt: What are the key features of a workflow analysis tool that can help streamline operations and enhance productivity in a business?
Generated: DETERMINISTIC_f87076cbdca5bf62
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WorkflowAnalysisTool:
    """
    A class to represent a Workflow Analysis Tool.
    
    Attributes
    ----------
    tasks : list
        A list of tasks in the workflow.
    metrics : dict
        A dictionary to store performance metrics.
    """

    def __init__(self):
        """Initializes a new instance of WorkflowAnalysisTool."""
        self.tasks = []
        self.metrics = {}

    def add_task(self, task_name):
        """
        Adds a new task to the workflow.

        Parameters
        ----------
        task_name : str
            The name of the task to be added.

        Raises
        ------
        ValueError
            If the task name is empty or already exists.
        """
        if not task_name:
            raise ValueError("Task name cannot be empty.")
        if task_name in self.tasks:
            raise ValueError(f"Task '{task_name}' already exists.")
        self.tasks.append(task_name)

    def remove_task(self, task_name):
        """
        Removes a task from the workflow.

        Parameters
        ----------
        task_name : str
            The name of the task to be removed.

        Raises
        ------
        ValueError
            If the task name does not exist.
        """
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' does not exist.")
        self.tasks.remove(task_name)

    def log_metric(self, task_name, duration):
        """
        Logs a performance metric for a specific task.

        Parameters
        ----------
        task_name : str
            The name of the task.
        duration : float
            The time taken to complete the task.

        Raises
        ------
        ValueError
            If the task name does not exist or duration is negative.
        """
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' does not exist.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        
        self.metrics[task_name] = self.metrics.get(task_name, []) + [duration]

    def get_average_time(self, task_name):
        """
        Returns the average time taken for a specific task.

        Parameters
        ----------
        task_name : str
            The name of the task.

        Returns
        -------
        float
            The average time taken for the task, or None if no data.

        Raises
        ------
        ValueError
            If the task name does not exist.
        """
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' does not exist.")
        
        times = self.metrics.get(task_name, [])
        return sum(times) / len(times) if times else None

    def get_workflow_overview(self):
        """
        Returns a summary of the workflow including tasks and their average times.

        Returns
        -------
        dict
            A dictionary containing task names and their average times.
        """
        overview = {}
        for task in self.tasks:
            average_time = self.get_average_time(task)
            overview[task] = average_time
        return overview


# Example usage
if __name__ == "__main__":
    try:
        workflow_tool = WorkflowAnalysisTool()
        workflow_tool.add_task("Task A")
        workflow_tool.add_task("Task B")
        workflow_tool.log_metric("Task A", 2.5)
        workflow_tool.log_metric("Task A", 3.0)
        workflow_tool.log_metric("Task B", 5.0)
        
        print(workflow_tool.get_workflow_overview())
    except ValueError as e:
        print(f"Error: {e}")
```
