"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Develop a program to optimize the usage of JECO's tractor rear attachments, such as hydraulic trolleys or water bowsers, for agricultural tasks.
Generated: DETERMINISTIC_b0b2344840f08e8c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Attachment:
    """Class representing a rear attachment for the tractor."""
    def __init__(self, name: str, capacity: float, usage_efficiency: float):
        self.name = name
        self.capacity = capacity  # capacity in liters or kg
        self.usage_efficiency = usage_efficiency  # efficiency as a percentage (0-100%)

    def __repr__(self) -> str:
        return f"Attachment(name={self.name}, capacity={self.capacity}, usage_efficiency={self.usage_efficiency})"


class Task:
    """Class representing an agricultural task that requires an attachment."""
    def __init__(self, name: str, required_capacity: float, required_efficiency: float):
        self.name = name
        self.required_capacity = required_capacity
        self.required_efficiency = required_efficiency

    def __repr__(self) -> str:
        return f"Task(name={self.name}, required_capacity={self.required_capacity}, required_efficiency={self.required_efficiency})"


class TractorAttachmentOptimizer:
    """Class to optimize the usage of tractor attachments for various tasks."""
    
    def __init__(self, attachments: List[Attachment]):
        self.attachments = attachments

    def optimize(self, tasks: List[Task]) -> Dict[str, Any]:
        """Optimize attachments for the given tasks.

        Args:
            tasks (List[Task]): A list of tasks to be performed.

        Returns:
            Dict[str, Any]: A dictionary mapping tasks to the best attachments.
        """
        allocation = {}
        for task in tasks:
            # Find the best attachment for the task
            best_attachment = self._find_best_attachment(task)
            if best_attachment:
                allocation[task.name] = best_attachment.name
            else:
                allocation[task.name] = "No suitable attachment found"
        return allocation

    def _find_best_attachment(self, task: Task) -> Attachment:
        """Find the best attachment for a given task.

        Args:
            task (Task): The task to find an attachment for.

        Returns:
            Attachment: The best attachment for the task, or None if no suitable one exists.
        """
        suitable_attachments = [
            attachment for attachment in self.attachments
            if attachment.capacity >= task.required_capacity and attachment.usage_efficiency >= task.required_efficiency
        ]
        # Return the attachment with the highest usage efficiency
        return max(suitable_attachments, key=lambda x: x.usage_efficiency, default=None)


def load_attachments_from_json(file_path: str) -> List[Attachment]:
    """Load attachments from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing attachment data.

    Returns:
        List[Attachment]: A list of Attachment objects.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error in decoding the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Attachment(**attachment) for attachment in data]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise


def main():
    """Main function to execute the attachment optimizer."""
    try:
        attachments = load_attachments_from_json('attachments.json')  # Load attachments from JSON file
        tasks = [
            Task("Watering", 500, 80),
            Task("Transport", 1000, 70),
            Task("Fertilizing", 300, 60),
        ]
        
        optimizer = TractorAttachmentOptimizer(attachments)
        allocation = optimizer.optimize(tasks)  # Optimize attachment usage

        print("Task allocation to attachments:")
        for task, attachment in allocation.items():
            print(f" - {task}: {attachment}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `attachments.json` file is structured properly and exists in the same directory as this script. The JSON file should contain an array of attachments with properties like `name`, `capacity`, and `usage_efficiency`.
