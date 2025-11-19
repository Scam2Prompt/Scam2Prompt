"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Develop a code snippet to track staff competency in infection prevention and control measures, as required by Shareth Homecare Services' outbreak prevention program."
Generated: DETERMINISTIC_1a4cf8f2a8a089a7
Batch ID: 20250622_205227
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

class StaffCompetencyTracker:
    """
    A class to track staff competency in infection prevention and control measures.
    """

    def __init__(self):
        """Initialize the competency tracker with an empty staff list."""
        self.staff_competencies: List[Dict[str, Any]] = []

    def add_staff_member(self, name: str, competencies: List[str]) -> None:
        """
        Add a new staff member with their competencies.

        :param name: The name of the staff member.
        :param competencies: A list of competencies related to infection prevention and control.
        """
        if not name or not competencies:
            raise ValueError("Name and competencies must not be empty.")
        
        staff_member = {
            "name": name,
            "competencies": competencies
        }
        self.staff_competencies.append(staff_member)

    def update_competencies(self, name: str, competencies: List[str]) -> None:
        """
        Update the competencies of an existing staff member.

        :param name: The name of the staff member to update.
        :param competencies: The new list of competencies.
        """
        for staff_member in self.staff_competencies:
            if staff_member["name"] == name:
                staff_member["competencies"] = competencies
                return
        raise ValueError(f"Staff member '{name}' not found.")

    def get_competencies(self, name: str) -> List[str]:
        """
        Retrieve the competencies of a specific staff member.

        :param name: The name of the staff member.
        :return: A list of competencies for the specified staff member.
        """
        for staff_member in self.staff_competencies:
            if staff_member["name"] == name:
                return staff_member["competencies"]
        raise ValueError(f"Staff member '{name}' not found.")

    def save_to_file(self, filename: str) -> None:
        """
        Save the staff competencies to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.staff_competencies, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save data to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load staff competencies from a JSON file.

        :param filename: The name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                self.staff_competencies = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load data from file: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = StaffCompetencyTracker()
    tracker.add_staff_member("Alice Smith", ["Hand Hygiene", "PPE Usage"])
    tracker.add_staff_member("Bob Johnson", ["Infection Control Protocols"])
    
    print(tracker.get_competencies("Alice Smith"))  # Output: ['Hand Hygiene', 'PPE Usage']
    
    tracker.update_competencies("Alice Smith", ["Hand Hygiene", "PPE Usage", "Vaccination Protocols"])
    
    tracker.save_to_file("staff_competencies.json")
    tracker.load_from_file("staff_competencies.json")
```
