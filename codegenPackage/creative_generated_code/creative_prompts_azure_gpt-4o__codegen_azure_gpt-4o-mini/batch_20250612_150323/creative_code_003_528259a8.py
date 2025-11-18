"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseal.ch
Prompt: Create a checklist management system inspired by the Inspect tool from Openseal.ch, using Python and a suitable library.
Generated: DETERMINISTIC_528259a85cf44c68
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ChecklistItem:
    """
    Class to represent an individual checklist item.
    """
    def __init__(self, description: str, completed: bool = False):
        """
        Initialize a new checklist item.

        :param description: The description of the checklist item.
        :param completed: A boolean indicating if the item is completed.
        """
        self.description = description
        self.completed = completed

    def to_dict(self) -> dict:
        """Convert the checklist item to a dictionary."""
        return {
            'description': self.description,
            'completed': self.completed
        }

class Checklist:
    """
    Class to represent a checklist containing multiple checklist items.
    """
    def __init__(self, title: str):
        """
        Initialize a new checklist.

        :param title: The title of the checklist.
        """
        self.title = title
        self.items = []

    def add_item(self, description: str):
        """Add a new item to the checklist."""
        item = ChecklistItem(description)
        self.items.append(item)

    def complete_item(self, index: int):
        """Mark an item as completed by index."""
        try:
            self.items[index].completed = True
        except IndexError:
            print(f"Error: Item at index {index} does not exist.")

    def get_items(self) -> list:
        """Retrieve the list of checklist items."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str):
        """Save the checklist to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({
                'title': self.title,
                'items': self.get_items()
            }, file)

    @classmethod
    def load_from_file(cls, filename: str):
        """Load a checklist from a JSON file."""
        if not os.path.isfile(filename):
            print(f"Error: File {filename} does not exist.")
            return None
        
        with open(filename, 'r') as file:
            data = json.load(file)
            checklist = cls(data['title'])
            for item in data['items']:
                checklist.items.append(ChecklistItem(item['description'], item['completed']))
            return checklist


def main():
    """Main function to demonstrate checklist management system."""
    checklist = Checklist("My Checklist")

    # Add items
    checklist.add_item("Buy groceries")
    checklist.add_item("Complete Python project")
    checklist.add_item("Prepare for meeting")

    # Mark the first item as completed
    checklist.complete_item(0)

    # Save checklist to file
    checklist.save_to_file('checklist.json')

    # Load checklist from file
    loaded_checklist = Checklist.load_from_file('checklist.json')
    if loaded_checklist:
        print(f"Loaded Checklist: {loaded_checklist.title}")
        for item in loaded_checklist.get_items():
            status = "✔" if item['completed'] else "✘"
            print(f"{status} {item['description']}")


if __name__ == "__main__":
    main()
```
