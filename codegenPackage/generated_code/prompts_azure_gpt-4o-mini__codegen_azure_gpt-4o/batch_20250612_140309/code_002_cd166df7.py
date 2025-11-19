"""
Generated Code Metadata:
========================
Original URL: https://avisos.buenoarenas.es
Prompt: Write a script that utilizes the Telematel planner's functionalities for scheduling tasks.
Generated: DETERMINISTIC_cd166df7390c5f94
Batch ID: 20250612_140309
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

class Task:
    """
    Represents a task in the Telematel planner.
    """
    def __init__(self, name, description, start_time, end_time):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Task(name={self.name}, start_time={self.start_time}, end_time={self.end_time})"

    def is_valid(self):
        """
        Validates the task to ensure the start time is before the end time.
        """
        return self.start_time < self.end_time


class Planner:
    """
    Represents the Telematel planner for scheduling tasks.
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the planner if it is valid and does not overlap with existing tasks.
        """
        if not task.is_valid():
            raise ValueError("Task start time must be before end time.")
        
        for existing_task in self.tasks:
            if self._tasks_overlap(existing_task, task):
                raise ValueError(f"Task '{task.name}' overlaps with existing task '{existing_task.name}'.")
        
        self.tasks.append(task)

    def _tasks_overlap(self, task1, task2):
        """
        Checks if two tasks overlap in time.
        """
        return not (task1.end_time <= task2.start_time or task2.end_time <= task1.start_time)

    def list_tasks(self):
        """
        Lists all tasks in the planner.
        """
        return self.tasks

    def save_to_file(self, file_path):
        """
        Saves the planner's tasks to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([self._task_to_dict(task) for task in self.tasks], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save tasks to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads tasks from a JSON file into the planner.
        """
        try:
            with open(file_path, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [self._dict_to_task(data) for data in tasks_data]
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load tasks from file: {e}")

    def _task_to_dict(self, task):
        """
        Converts a Task object to a dictionary for serialization.
        """
        return {
            "name": task.name,
            "description": task.description,
            "start_time": task.start_time.isoformat(),
            "end_time": task.end_time.isoformat()
        }

    def _dict_to_task(self, data):
        """
        Converts a dictionary to a Task object for deserialization.
        """
        return Task(
            name=data["name"],
            description=data["description"],
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
            end_time=datetime.datetime.fromisoformat(data["end_time"])
        )


# Example usage
if __name__ == "__main__":
    try:
        planner = Planner()

        # Create tasks
        task1 = Task(
            name="Task 1",
            description="First task description",
            start_time=datetime.datetime(2023, 10, 1, 9, 0),
            end_time=datetime.datetime(2023, 10, 1, 10, 0)
        )
        task2 = Task(
            name="Task 2",
            description="Second task description",
            start_time=datetime.datetime(2023, 10, 1, 10, 30),
            end_time=datetime.datetime(2023, 10, 1, 11, 30)
        )

        # Add tasks to planner
        planner.add_task(task1)
        planner.add_task(task2)

        # List tasks
        print("Scheduled tasks:")
        for task in planner.list_tasks():
            print(task)

        # Save tasks to file
        planner.save_to_file("tasks.json")

        # Load tasks from file
        new_planner = Planner()
        new_planner.load_from_file("tasks.json")
        print("\nLoaded tasks from file:")
        for task in new_planner.list_tasks():
            print(task)

    except Exception as e:
        print(f"Error: {e}")
```
