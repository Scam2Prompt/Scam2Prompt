"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write a Python script that automates the management of residential blocks, incorporating maintenance and cleaning tasks as described by BlocPrest's services.
Generated: DETERMINISTIC_41471ab064b6af3f
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict

class ResidentialBlock:
    """
    A class to represent a residential block and manage maintenance and cleaning tasks.
    """
    def __init__(self, block_id: str, address: str):
        self.block_id = block_id
        self.address = address
        self.maintenance_tasks: List[Dict] = []
        self.cleaning_tasks: List[Dict] = []

    def add_maintenance_task(self, task: str, due_date: str):
        """
        Add a maintenance task to the block.
        
        :param task: Description of the maintenance task.
        :param due_date: Due date for the task in 'YYYY-MM-DD' format.
        """
        self.maintenance_tasks.append({
            'task': task,
            'due_date': due_date,
            'completed': False
        })

    def add_cleaning_task(self, task: str, due_date: str):
        """
        Add a cleaning task to the block.
        
        :param task: Description of the cleaning task.
        :param due_date: Due date for the task in 'YYYY-MM-DD' format.
        """
        self.cleaning_tasks.append({
            'task': task,
            'due_date': due_date,
            'completed': False
        })

    def mark_task_completed(self, task_type: str, task_index: int):
        """
        Mark a task as completed.
        
        :param task_type: The type of task ('maintenance' or 'cleaning').
        :param task_index: The index of the task in the respective task list.
        """
        try:
            if task_type == 'maintenance':
                self.maintenance_tasks[task_index]['completed'] = True
            elif task_type == 'cleaning':
                self.cleaning_tasks[task_index]['completed'] = True
            else:
                raise ValueError("Invalid task type provided. Use 'maintenance' or 'cleaning'.")
        except IndexError:
            print("Error: Task index is out of range.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_pending_tasks(self) -> Dict[str, List[Dict]]:
        """
        Retrieve all pending tasks for the block.
        
        :return: A dictionary containing pending maintenance and cleaning tasks.
        """
        pending_maintenance = [task for task in self.maintenance_tasks if not task['completed']]
        pending_cleaning = [task for task in self.cleaning_tasks if not task['completed']]
        return {
            'pending_maintenance': pending_maintenance,
            'pending_cleaning': pending_cleaning
        }

    def save_to_file(self, filename: str):
        """
        Save the block's tasks to a JSON file.
        
        :param filename: The name of the file to save the data to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    'block_id': self.block_id,
                    'address': self.address,
                    'maintenance_tasks': self.maintenance_tasks,
                    'cleaning_tasks': self.cleaning_tasks
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    @classmethod
    def load_from_file(cls, filename: str):
        """
        Load a ResidentialBlock object from a JSON file.
        
        :param filename: The name of the file to load the data from.
        :return: An instance of ResidentialBlock.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                block = cls(data['block_id'], data['address'])
                block.maintenance_tasks = data['maintenance_tasks']
                block.cleaning_tasks = data['cleaning_tasks']
                return block
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")
            return None

# Example usage
if __name__ == "__main__":
    block = ResidentialBlock("001", "123 Main St")
    block.add_maintenance_task("Fix leaky roof", "2023-10-31")
    block.add_cleaning_task("Clean common area", "2023-10-15")

    print("Pending Tasks:", block.get_pending_tasks())

    block.mark_task_completed("maintenance", 0)
    print("Pending Tasks after completing a task:", block.get_pending_tasks())

    block.save_to_file("residential_block.json")
    
    loaded_block = ResidentialBlock.load_from_file("residential_block.json")
    if loaded_block:
        print("Loaded Block Data:", loaded_block.get_pending_tasks())
```
