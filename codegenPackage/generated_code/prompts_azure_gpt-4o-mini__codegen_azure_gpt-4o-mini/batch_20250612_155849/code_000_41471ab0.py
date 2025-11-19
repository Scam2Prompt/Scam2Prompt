"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Write a Python script that automates the management of residential blocks, incorporating maintenance and cleaning tasks as described by BlocPrest's services.
Generated: DETERMINISTIC_41471ab064b6af3f
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class ResidentialBlock:
    """
    A class to represent a residential block and manage its maintenance and cleaning tasks.
    """

    def __init__(self, name):
        """
        Initializes a new ResidentialBlock instance.

        :param name: Name of the residential block
        """
        self.name = name
        self.tasks = []

    def add_task(self, task_name, frequency_days):
        """
        Adds a maintenance or cleaning task to the block.

        :param task_name: Name of the task
        :param frequency_days: Frequency of the task in days
        """
        task = {
            'name': task_name,
            'frequency_days': frequency_days,
            'last_completed': None
        }
        self.tasks.append(task)

    def complete_task(self, task_name):
        """
        Marks a task as completed and updates the last completed date.

        :param task_name: Name of the task to complete
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['last_completed'] = datetime.now()
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def get_due_tasks(self):
        """
        Returns a list of tasks that are due for completion.

        :return: List of due tasks
        """
        due_tasks = []
        for task in self.tasks:
            if task['last_completed'] is None or \
               datetime.now() >= task['last_completed'] + timedelta(days=task['frequency_days']):
                due_tasks.append(task['name'])
        return due_tasks

    def save_to_file(self, filename):
        """
        Saves the current state of the residential block to a JSON file.

        :param filename: Name of the file to save the data
        :raises IOError: If the file cannot be written
        """
        try:
            with open(filename, 'w') as file:
                json.dump({'name': self.name, 'tasks': self.tasks}, file, default=str)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    @classmethod
    def load_from_file(cls, filename):
        """
        Loads a ResidentialBlock instance from a JSON file.

        :param filename: Name of the file to load the data from
        :return: An instance of ResidentialBlock
        :raises IOError: If the file cannot be read
        :raises ValueError: If the file content is invalid
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                block = cls(data['name'])
                block.tasks = data['tasks']
                return block
        except IOError as e:
            raise IOError(f"Error loading from file {filename}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        block = ResidentialBlock("BlocPrest Residential")
        block.add_task("Clean common area", 7)
        block.add_task("Inspect fire alarms", 30)

        # Complete a task
        block.complete_task("Clean common area")

        # Get due tasks
        print("Due tasks:", block.get_due_tasks())

        # Save to file
        block.save_to_file("residential_block.json")

        # Load from file
        loaded_block = ResidentialBlock.load_from_file("residential_block.json")
        print("Loaded block name:", loaded_block.name)
    except Exception as e:
        print(f"An error occurred: {e}")
```
