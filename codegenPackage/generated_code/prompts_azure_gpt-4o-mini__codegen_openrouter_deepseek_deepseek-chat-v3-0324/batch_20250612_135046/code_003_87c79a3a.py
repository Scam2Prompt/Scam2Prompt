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
from typing import List, Dict, Optional, Callable

class ChecklistItem:
    """Represents a single item in a checklist."""
    
    def __init__(self, description: str, is_completed: bool = False):
        self.description = description
        self.is_completed = is_completed
    
    def toggle(self) -> None:
        """Toggle the completion status of the item."""
        self.is_completed = not self.is_completed
    
    def __str__(self) -> str:
        status = "[x]" if self.is_completed else "[ ]"
        return f"{status} {self.description}"

class Checklist:
    """Represents a digital checklist with multiple items."""
    
    def __init__(self, name: str, items: Optional[List[ChecklistItem]] = None):
        self.name = name
        self.items = items if items is not None else []
    
    def add_item(self, description: str) -> None:
        """Add a new item to the checklist."""
        self.items.append(ChecklistItem(description))
    
    def remove_item(self, index: int) -> None:
        """Remove an item from the checklist by index."""
        if 0 <= index < len(self.items):
            self.items.pop(index)
        else:
            raise IndexError("Item index out of range")
    
    def toggle_item(self, index: int) -> None:
        """Toggle the completion status of an item by index."""
        if 0 <= index < len(self.items):
            self.items[index].toggle()
        else:
            raise IndexError("Item index out of range")
    
    def clear_completed(self) -> None:
        """Remove all completed items from the checklist."""
        self.items = [item for item in self.items if not item.is_completed]
    
    def __str__(self) -> str:
        items_str = "\n".join(str(item) for item in self.items)
        return f"Checklist: {self.name}\n{items_str}"

class ChecklistManager:
    """Manages multiple checklists with CRUD operations."""
    
    def __init__(self):
        self.checklists: Dict[str, Checklist] = {}
    
    def create_checklist(self, name: str) -> Checklist:
        """Create a new checklist with the given name."""
        if name in self.checklists:
            raise ValueError(f"Checklist '{name}' already exists")
        checklist = Checklist(name)
        self.checklists[name] = checklist
        return checklist
    
    def get_checklist(self, name: str) -> Optional[Checklist]:
        """Retrieve a checklist by name."""
        return self.checklists.get(name)
    
    def delete_checklist(self, name: str) -> None:
        """Delete a checklist by name."""
        if name not in self.checklists:
            raise KeyError(f"Checklist '{name}' not found")
        del self.checklists[name]
    
    def list_checklists(self) -> List[str]:
        """List all checklist names."""
        return list(self.checklists.keys())
    
    def __str__(self) -> str:
        return "\n".join(f"- {name}" for name in self.list_checklists())

def inspect_checklist(checklist: Checklist) -> None:
    """Inspect a checklist object using the inspect module."""
    print(f"Inspecting checklist: {checklist.name}")
    print("\nAttributes:")
    for name, value in inspect.getmembers(checklist):
        if not name.startswith('_'):
            print(f"{name}: {value}")
    
    print("\nMethods:")
    for name, method in inspect.getmembers(checklist, inspect.ismethod):
        if not name.startswith('_'):
            print(f"{name}()")

def main():
    """Demonstrate the checklist functionality."""
    manager = ChecklistManager()
    
    # Create a new checklist
    shopping = manager.create_checklist("Shopping List")
    shopping.add_item("Milk")
    shopping.add_item("Eggs")
    shopping.add_item("Bread")
    
    # Toggle an item
    shopping.toggle_item(0)
    
    # Print the checklist
    print(shopping)
    
    # Inspect the checklist
    inspect_checklist(shopping)
    
    # List all checklists
    print("\nAll Checklists:")
    print(manager)

if __name__ == "__main__":
    main()
```
