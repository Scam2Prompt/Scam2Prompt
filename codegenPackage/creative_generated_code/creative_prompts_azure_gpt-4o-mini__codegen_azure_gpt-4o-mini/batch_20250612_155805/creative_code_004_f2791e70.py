"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uueims.com
Prompt: Create a checklist for duct cleaning services that aligns with the standards set by UUEIMS.
Generated: DETERMINISTIC_f2791e70224dc738
Batch ID: 20250612_155805
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

class DuctCleaningChecklist:
    """
    A class to represent the checklist for duct cleaning services
    according to UUEIMS standards.
    """

    def __init__(self) -> None:
        """
        Initializes the checklist with standard items.
        """
        self.checklist: List[Dict[str, str]] = [
            {"task": "Inspect ductwork", "status": "incomplete"},
            {"task": "Verify air flow", "status": "incomplete"},
            {"task": "Check for visible mold", "status": "incomplete"},
            {"task": "Inspect insulation", "status": "incomplete"},
            {"task": "Test system operation", "status": "incomplete"},
            {"task": "Clean duct surfaces", "status": "incomplete"},
            {"task": "Remove debris", "status": "incomplete"},
            {"task": "Seal ducts if needed", "status": "incomplete"},
            {"task": "Conduct post-cleaning inspection", "status": "incomplete"},
            {"task": "Document findings", "status": "incomplete"}
        ]

    def update_status(self, task: str, status: str) -> None:
        """
        Updates the status of a specific task in the checklist.

        :param task: The task to update.
        :param status: The new status for the task (e.g., 'complete' or 'incomplete').
        :raises ValueError: If the task does not exist or if the status is invalid.
        """
        valid_statuses = ['complete', 'incomplete']
        for item in self.checklist:
            if item['task'] == task:
                if status not in valid_statuses:
                    raise ValueError(f"Invalid status: {status}. Valid statuses are {valid_statuses}.")
                item['status'] = status
                return
        raise ValueError(f"Task '{task}' not found in checklist.")

    def to_json(self) -> str:
        """
        Converts the checklist to a JSON string.

        :return: JSON representation of the checklist.
        """
        return json.dumps(self.checklist, indent=4)

    def load_from_json(self, json_data: str) -> None:
        """
        Loads checklist items from a JSON string.

        :param json_data: JSON string containing checklist items.
        :raises json.JSONDecodeError: If the JSON data is invalid.
        """
        try:
            self.checklist = json.loads(json_data)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")

    def display_checklist(self) -> None:
        """
        Displays the current checklist in a user-friendly format.
        """
        for item in self.checklist:
            print(f"Task: {item['task']}, Status: {item['status']}")

# Example usage
if __name__ == "__main__":
    checklist = DuctCleaningChecklist()
    checklist.display_checklist()

    try:
        checklist.update_status("Inspect ductwork", "complete")
        checklist.display_checklist()
    except ValueError as e:
        print(e)

    # Example of saving to JSON
    json_data = checklist.to_json()
    print(json_data)

    # Load from JSON (example)
    new_checklist = DuctCleaningChecklist()
    new_checklist.load_from_json(json_data)
    new_checklist.display_checklist()
```
