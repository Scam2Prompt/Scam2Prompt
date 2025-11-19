"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Create a Python script to track and display PSHP's collaborations, such as the MoU with BIPS, on the website's achievements page.
Generated: DETERMINISTIC_fe019d572477d0b0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# collaboration_tracker.py

"""
Module to track and display PSHP's collaborations.

Classes:
    Collaboration: Represents a collaboration with attributes for name, partner, and date.
    CollaborationTracker: Manages a list of collaborations and provides methods to add, remove, and display them.

Functions:
    load_collaborations: Loads collaborations from a JSON file.
    save_collaborations: Saves collaborations to a JSON file.
"""

import json
from datetime import datetime

class Collaboration:
    """Represents a collaboration."""

    def __init__(self, name, partner, date):
        """
        Initializes a Collaboration object.

        Args:
            name (str): Name of the collaboration.
            partner (str): Partner organization.
            date (str): Date of the collaboration in YYYY-MM-DD format.
        """
        self.name = name
        self.partner = partner
        self.date = datetime.strptime(date, "%Y-%m-%d")

    def __repr__(self):
        return f"Collaboration('{self.name}', '{self.partner}', '{self.date.date()}')"

    def to_dict(self):
        """Returns a dictionary representation of the collaboration."""
        return {
            "name": self.name,
            "partner": self.partner,
            "date": self.date.strftime("%Y-%m-%d")
        }

class CollaborationTracker:
    """Manages a list of collaborations."""

    def __init__(self, collaborations=None):
        """
        Initializes a CollaborationTracker object.

        Args:
            collaborations (list, optional): List of Collaboration objects. Defaults to None.
        """
        self.collaborations = collaborations if collaborations else []

    def add_collaboration(self, collaboration):
        """
        Adds a collaboration to the tracker.

        Args:
            collaboration (Collaboration): Collaboration object to add.
        """
        self.collaborations.append(collaboration)
        self.collaborations.sort(key=lambda x: x.date)

    def remove_collaboration(self, name):
        """
        Removes a collaboration by name.

        Args:
            name (str): Name of the collaboration to remove.

        Returns:
            bool: True if the collaboration was removed, False otherwise.
        """
        self.collaborations = [c for c in self.collaborations if c.name != name]
        return len(self.collaborations) < len([c for c in self.collaborations if c.name == name]) + 1

    def display_collaborations(self):
        """Prints a list of collaborations."""
        for collaboration in self.collaborations:
            print(f"{collaboration.name} with {collaboration.partner} on {collaboration.date.date()}")

def load_collaborations(filename):
    """
    Loads collaborations from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        CollaborationTracker: CollaborationTracker object with loaded collaborations.
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            collaborations = [Collaboration(c["name"], c["partner"], c["date"]) for c in data]
            return CollaborationTracker(collaborations)
    except FileNotFoundError:
        return CollaborationTracker()
    except json.JSONDecodeError as e:
        print(f"Error loading collaborations: {e}")
        return CollaborationTracker()

def save_collaborations(tracker, filename):
    """
    Saves collaborations to a JSON file.

    Args:
        tracker (CollaborationTracker): CollaborationTracker object.
        filename (str): Name of the JSON file.
    """
    data = [c.to_dict() for c in tracker.collaborations]
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving collaborations: {e}")

def main():
    filename = "collaborations.json"
    tracker = load_collaborations(filename)

    # Example usage:
    mou = Collaboration("MoU", "BIPS", "2022-01-01")
    tracker.add_collaboration(mou)

    print("Collaborations:")
    tracker.display_collaborations()

    save_collaborations(tracker, filename)

if __name__ == "__main__":
    main()
```
