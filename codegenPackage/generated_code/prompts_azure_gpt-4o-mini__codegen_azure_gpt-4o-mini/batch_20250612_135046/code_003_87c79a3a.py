"""
Generated Code Metadata:
========================
Original URL: https://openseal.ch
Prompt: Generate a script that utilizes Inspect for creating and managing digital checklists.
Generated: DETERMINISTIC_87c79a3a29f46f00
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import inspect
from typing import List, Dict, Any

class ChecklistItem:
    """Represents a single item in a checklist."""
    
    def __init__(self, description: str):
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Marks the checklist item as completed."""
        self.completed = True

    def __repr__(self) -> str:
        return f"{'[x]' if self.completed else '[ ]'} {self.description}"


class DigitalChecklist:
    """Manages a checklist of items."""
    
    def __init__(self, title: str):
        self.title = title
        self.items: List[ChecklistItem] = []

    def add_item(self, description: str):
        """Adds a new item to the checklist."""
        if not description:
            raise ValueError("Description cannot be empty.")
        self.items.append(ChecklistItem(description))

    def complete_item(self, index: int):
        """Marks an item as completed by its index."""
        try:
            self.items[index].mark_completed()
        except IndexError:
            raise IndexError("Item index out of range.")

    def remove_item(self, index: int):
        """Removes an item from the checklist by its index."""
        try:
            del self.items[index]
        except IndexError:
            raise IndexError("Item index out of range.")

    def display(self) -> None:
        """Displays the checklist items."""
        print(f"Checklist: {self.title}")
        for index, item in enumerate(self.items):
            print(f"{index}. {item}")

    def to_dict(self) -> Dict[str, Any]:
        """Converts the checklist to a dictionary representation."""
        return {
            "title": self.title,
            "items": [{"description": item.description, "completed": item.completed} for item in self.items]
        }


def main():
    """Main function to demonstrate the DigitalChecklist functionality."""
    try:
        checklist = DigitalChecklist("My Daily Tasks")
        checklist.add_item("Wake up early")
        checklist.add_item("Exercise")
        checklist.add_item("Read a book")
        
        checklist.display()
        
        checklist.complete_item(1)  # Mark "Exercise" as completed
        checklist.display()
        
        checklist.remove_item(2)  # Remove "Read a book"
        checklist.display()
        
        # Convert to dictionary and print
        checklist_dict = checklist.to_dict()
        print(checklist_dict)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
