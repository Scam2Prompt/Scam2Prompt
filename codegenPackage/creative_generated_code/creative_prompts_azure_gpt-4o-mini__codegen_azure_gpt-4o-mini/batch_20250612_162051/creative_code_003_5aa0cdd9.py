"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Generate a checklist for property maintenance and cleaning management that aligns with the comprehensive services provided by Bee Property.
Generated: DETERMINISTIC_5aa0cdd946ffd986
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class PropertyMaintenanceChecklist:
    def __init__(self, property_name: str):
        """
        Initializes the PropertyMaintenanceChecklist with the property name.

        Args:
            property_name (str): The name of the property for which the checklist is created.
        """
        self.property_name = property_name
        self.checklist: List[Dict[str, str]] = []

    def add_task(self, task: str, frequency: str):
        """
        Adds a task to the checklist with its frequency.

        Args:
            task (str): The maintenance or cleaning task.
            frequency (str): How often the task should be completed (e.g., 'weekly', 'monthly').
        """
        self.checklist.append({"task": task, "frequency": frequency})

    def remove_task(self, task: str):
        """
        Removes a task from the checklist if it exists.

        Args:
            task (str): The task to be removed.

        Raises:
            ValueError: If the task is not found in the checklist.
        """
        for item in self.checklist:
            if item['task'] == task:
                self.checklist.remove(item)
                return
        raise ValueError(f'Task "{task}" not found in the checklist.')

    def get_checklist(self) -> List[Dict[str, str]]:
        """
        Returns the current checklist.

        Returns:
            List[Dict[str, str]]: The list of tasks and their frequencies.
        """
        return self.checklist

    def save_checklist_to_file(self, filename: str):
        """
        Saves the current checklist to a file in JSON format.

        Args:
            filename (str): The name of the file to save the checklist to.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

    def load_checklist_from_file(self, filename: str):
        """
        Loads a checklist from a file in JSON format and updates the current checklist.

        Args:
            filename (str): The name of the file to load the checklist from.

        Raises:
            IOError: If there is an error reading from the file.
            json.JSONDecodeError: If the file contents are not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.checklist = json.load(file)
        except IOError as e:
            raise IOError(f"Error reading from file {filename}: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from file {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize the checklist for Bee Property
    bee_property_checklist = PropertyMaintenanceChecklist("Bee Property")

    # Add tasks to the checklist
    bee_property_checklist.add_task("Inspect roof for leaks", "bi-annually")
    bee_property_checklist.add_task("Clean gutters", "seasonally")
    bee_property_checklist.add_task("Test smoke alarms", "monthly")
    bee_property_checklist.add_task("Check HVAC system", "annually")

    # Print the current checklist
    print("Current Property Maintenance Checklist:")
    for task in bee_property_checklist.get_checklist():
        print(f"- {task['task']} (Frequency: {task['frequency']})")

    # Save checklist to a file
    bee_property_checklist.save_checklist_to_file("bee_property_checklist.json")
```
