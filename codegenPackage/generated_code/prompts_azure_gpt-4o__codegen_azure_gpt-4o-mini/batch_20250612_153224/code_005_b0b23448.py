"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Develop a program to optimize the usage of JECO's tractor rear attachments, such as hydraulic trolleys or water bowsers, for agricultural tasks.
Generated: DETERMINISTIC_b0b2344840f08e8c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Attachment:
    """Class representing a tractor rear attachment."""
    
    def __init__(self, name: str, type: str, capacity: float):
        """
        Initialize an attachment with a name, type, and capacity.

        :param name: Name of the attachment
        :param type: Type of the attachment (e.g., 'hydraulic trolley', 'water bowser')
        :param capacity: Capacity of the attachment in liters
        """
        self.name = name
        self.type = type
        self.capacity = capacity

    def __repr__(self):
        return f"Attachment(name={self.name}, type={self.type}, capacity={self.capacity})"


class Task:
    """Class representing an agricultural task."""
    
    def __init__(self, name: str, required_capacity: float):
        """
        Initialize a task with a name and required capacity.

        :param name: Name of the task
        :param required_capacity: Required capacity for the task in liters
        """
        self.name = name
        self.required_capacity = required_capacity

    def __repr__(self):
        return f"Task(name={self.name}, required_capacity={self.required_capacity})"


class TractorOptimizer:
    """Class to optimize the usage of tractor attachments for agricultural tasks."""
    
    def __init__(self, attachments: List[Attachment]):
        """
        Initialize the optimizer with a list of attachments.

        :param attachments: List of available attachments
        """
        self.attachments = attachments

    def optimize(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Optimize the usage of attachments for the given tasks.

        :param tasks: List of tasks to optimize for
        :return: A dictionary mapping tasks to the best-suited attachment
        """
        allocation = {}
        for task in tasks:
            suitable_attachments = [att for att in self.attachments if att.capacity >= task.required_capacity]
            if suitable_attachments:
                # Sort by capacity to find the best fit
                best_fit = min(suitable_attachments, key=lambda x: x.capacity)
                allocation[task.name] = best_fit
            else:
                allocation[task.name] = None  # No suitable attachment found
        return allocation


def load_attachments_from_json(file_path: str) -> List[Attachment]:
    """
    Load attachments from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of Attachment objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Attachment(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading attachments: {e}")
        return []


def main():
    # Load attachments from a JSON file
    attachments = load_attachments_from_json('attachments.json')
    
    # Define some tasks
    tasks = [
        Task(name='Irrigation', required_capacity=500),
        Task(name='Transport', required_capacity=300),
        Task(name='Fertilization', required_capacity=700)
    ]
    
    # Create an optimizer instance
    optimizer = TractorOptimizer(attachments)
    
    # Optimize the attachments for the tasks
    allocation = optimizer.optimize(tasks)
    
    # Print the allocation results
    for task_name, attachment in allocation.items():
        if attachment:
            print(f"Task '{task_name}' is best suited for attachment: {attachment.name}")
        else:
            print(f"Task '{task_name}' has no suitable attachment available.")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `attachments.json` file exists in the same directory as the script and contains valid JSON data representing the attachments. The JSON structure should look like this:

```json
[
    {"name": "Hydraulic Trolley", "type": "hydraulic trolley", "capacity": 600},
    {"name": "Water Bowser", "type": "water bowser", "capacity": 1000},
    {"name": "Small Trolley", "type": "hydraulic trolley", "capacity": 250}
]
```
