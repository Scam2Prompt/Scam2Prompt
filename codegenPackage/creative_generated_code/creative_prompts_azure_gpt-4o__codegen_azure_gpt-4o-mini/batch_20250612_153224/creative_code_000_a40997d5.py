"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://settlement.owlspriority.ca
Prompt: Write code to create a checklist application for newcomers to Canada, including features for adding, editing, and tracking items like "housing," "workforce preparation," and "cultural adaptation."
Generated: DETERMINISTIC_a40997d545140323
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
from typing import List, Dict

class ChecklistItem:
    """Class representing an item in the checklist."""
    
    def __init__(self, name: str, completed: bool = False) -> None:
        """Initialize a checklist item with a name and completion status."""
        self.name = name
        self.completed = completed

    def __repr__(self) -> str:
        """Return a string representation of the checklist item."""
        return f"ChecklistItem(name='{self.name}', completed={self.completed})"

class Checklist:
    """Class representing a checklist for newcomers to Canada."""
    
    def __init__(self) -> None:
        """Initialize the checklist with an empty list of items."""
        self.items: List[ChecklistItem] = []

    def add_item(self, name: str) -> None:
        """Add a new item to the checklist."""
        if name:
            self.items.append(ChecklistItem(name))
            print(f"Added item: {name}")
        else:
            raise ValueError("Item name cannot be empty.")

    def edit_item(self, index: int, new_name: str) -> None:
        """Edit an existing item in the checklist."""
        if 0 <= index < len(self.items):
            self.items[index].name = new_name
            print(f"Updated item at index {index} to: {new_name}")
        else:
            raise IndexError("Item index out of range.")

    def toggle_item(self, index: int) -> None:
        """Toggle the completion status of an item in the checklist."""
        if 0 <= index < len(self.items):
            self.items[index].completed = not self.items[index].completed
            print(f"Toggled item at index {index}. Now completed: {self.items[index].completed}")
        else:
            raise IndexError("Item index out of range.")

    def get_items(self) -> List[Dict[str, str]]:
        """Return a list of checklist items as dictionaries."""
        return [{"name": item.name, "completed": item.completed} for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the checklist items to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_items(), file, indent=4)
            print(f"Checklist saved to {filename}.")
        except IOError as e:
            print(f"Error saving checklist to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load checklist items from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.items = [ChecklistItem(item['name'], item['completed']) for item in items]
            print(f"Checklist loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading checklist from file: {e}")

def main() -> None:
    """Main function to demonstrate the checklist functionality."""
    checklist = Checklist()
    
    # Demo: Adding items
    checklist.add_item("Housing")
    checklist.add_item("Workforce Preparation")
    checklist.add_item("Cultural Adaptation")

    # Demo: Editing an item
    checklist.edit_item(1, "Job Preparation")

    # Demo: Toggling completion status
    checklist.toggle_item(0)

    # Demo: Saving to file
    checklist.save_to_file("checklist.json")
    
    # Demo: Loading from file
    new_checklist = Checklist()
    new_checklist.load_from_file("checklist.json")
    print(new_checklist.get_items())

if __name__ == "__main__":
    main()
```
