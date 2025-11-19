"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "Discuss the benefits of using a centralized time management service for freelancers."
Generated: DETERMINISTIC_96bb382fe2219c1d
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script discusses the benefits of using a centralized time management service for freelancers.
It simulates a scenario where freelancers can track their tasks, time spent, and productivity using a centralized service.
"""

# Import necessary modules
import datetime

class CentralizedTimeManagementService:
    """
    A class representing a centralized time management service for freelancers.
    """

    def __init__(self):
        """
        Initializes the service with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task_name, estimated_hours):
        """
        Adds a new task to the service.

        Args:
            task_name (str): The name of the task.
            estimated_hours (float): The estimated hours to complete the task.

        Returns:
            None
        """
        task = {
            "task_name": task_name,
            "estimated_hours": estimated_hours,
            "start_time": None,
            "end_time": None,
            "status": "Pending"
        }
        self.tasks.append(task)
        print(f"Task '{task_name}' added successfully.")

    def start_task(self, task_name):
        """
        Starts a task by recording the start time.

        Args:
            task_name (str): The name of the task to start.

        Returns:
            None
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                if task["status"] == "Pending":
                    task["start_time"] = datetime.datetime.now()
                    task["status"] = "In Progress"
                    print(f"Task '{task_name}' started at {task['start_time']}.")
                    return
                else:
                    print(f"Task '{task_name}' is already in progress or completed.")
                    return
        print(f"Task '{task_name}' not found.")

    def complete_task(self, task_name):
        """
        Completes a task by recording the end time and calculating the time spent.

        Args:
            task_name (str): The name of the task to complete.

        Returns:
            None
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                if task["status"] == "In Progress":
                    task["end_time"] = datetime.datetime.now()
                    task["status"] = "Completed"
                    time_spent = (task["end_time"] - task["start_time"]).total_seconds() / 3600
                    print(f"Task '{task_name}' completed at {task['end_time']}.")
                    print(f"Time spent on task: {time_spent:.2f} hours.")
                    return
                else:
                    print(f"Task '{task_name}' is not in progress or already completed.")
                    return
        print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        """
        Displays all tasks with their details.

        Returns:
            None
        """
        if not self.tasks:
            print("No tasks available.")
            return

        print("Tasks:")
        for task in self.tasks:
            print(f"Name: {task['task_name']}, Estimated Hours: {task['estimated_hours']}, "
                  f"Status: {task['status']}, Start Time: {task['start_time']}, End Time: {task['end_time']}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the service
        service = CentralizedTimeManagementService()

        # Add tasks
        service.add_task("Write blog post", 2.5)
        service.add_task("Design website mockup", 5)

        # Start and complete tasks
        service.start_task("Write blog post")
        service.complete_task("Write blog post")

        # View all tasks
        service.view_tasks()

    except Exception as e:
        print(f"An error occurred: {e}")
```
