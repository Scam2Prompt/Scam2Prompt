"""
Generated Code Metadata:
========================
Original URL: https://settlement.owlspriority.ca
Prompt: Write code to create a checklist application for newcomers to Canada, including features for adding, editing, and tracking items like "housing," "workforce preparation," and "cultural adaptation."
Generated: DETERMINISTIC_a40997d545140323
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
import os
from typing import List, Dict, Optional

class ChecklistItem:
    """Represents a single item in the checklist."""
    
    def __init__(self, name: str, category: str, completed: bool = False):
        self.name = name
        self.category = category
        self.completed = completed
    
    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ChecklistItem':
        """Create a ChecklistItem from a dictionary."""
        return cls(data['name'], data['category'], data.get('completed', False))

class Checklist:
    """Main checklist application class."""
    
    def __init__(self, filename: str = 'checklist.json'):
        self.filename = filename
        self.items: List[ChecklistItem] = []
        self.load()
    
    def add_item(self, name: str, category: str) -> None:
        """Add a new item to the checklist."""
        self.items.append(ChecklistItem(name, category))
        self.save()
    
    def edit_item(self, index: int, name: Optional[str] = None, category: Optional[str] = None, completed: Optional[bool] = None) -> None:
        """Edit an existing checklist item."""
        if index < 0 or index >= len(self.items):
            raise IndexError("Item index out of range")
        
        item = self.items[index]
        if name is not None:
            item.name = name
        if category is not None:
            item.category = category
        if completed is not None:
            item.completed = completed
        
        self.save()
    
    def toggle_completion(self, index: int) -> None:
        """Toggle the completion status of an item."""
        if index < 0 or index >= len(self.items):
            raise IndexError("Item index out of range")
        
        self.items[index].completed = not self.items[index].completed
        self.save()
    
    def delete_item(self, index: int) -> None:
        """Delete an item from the checklist."""
        if index < 0 or index >= len(self.items):
            raise IndexError("Item index out of range")
        
        del self.items[index]
        self.save()
    
    def get_items_by_category(self, category: str) -> List[ChecklistItem]:
        """Get all items in a specific category."""
        return [item for item in self.items if item.category == category]
    
    def save(self) -> None:
        """Save the checklist to a file."""
        data = [item.to_dict() for item in self.items]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Load the checklist from a file."""
        if not os.path.exists(self.filename):
            self.items = []
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.items = [ChecklistItem.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.items = []
    
    def __str__(self) -> str:
        """Return a string representation of the checklist."""
        output = []
        categories = set(item.category for item in self.items)
        
        for category in sorted(categories):
            output.append(f"\n{category.upper()}:")
            for i, item in enumerate(self.get_items_by_category(category)):
                status = "✓" if item.completed else " "
                output.append(f"{i}. [{status}] {item.name}")
        
        return "\n".join(output)

def main():
    """Main function to run the checklist application."""
    checklist = Checklist()
    
    # Add some default items if the checklist is empty
    if not checklist.items:
        checklist.add_item("Find temporary housing", "Housing")
        checklist.add_item("Apply for SIN", "Workforce Preparation")
        checklist.add_item("Learn about Canadian holidays", "Cultural Adaptation")
        checklist.add_item("Register for healthcare", "Healthcare")
        checklist.add_item("Open a bank account", "Finance")
    
    while True:
        print("\nCanada Newcomer Checklist")
        print("-------------------------")
        print(checklist)
        print("\nOptions:")
        print("1. Add item")
        print("2. Edit item")
        print("3. Toggle completion")
        print("4. Delete item")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                name = input("Enter item name: ")
                category = input("Enter category: ")
                checklist.add_item(name, category)
            
            elif choice == '2':
                index = int(input("Enter item number to edit: "))
                name = input("Enter new name (leave blank to keep current): ")
                category = input("Enter new category (leave blank to keep current): ")
                completed = input("Mark as completed? (y/n, leave blank to keep current): ")
                
                checklist.edit_item(
                    index,
                    name if name.strip() else None,
                    category if category.strip() else None,
                    completed.lower() == 'y' if completed.strip() else None
                )
            
            elif choice == '3':
                index = int(input("Enter item number to toggle: "))
                checklist.toggle_completion(index)
            
            elif choice == '4':
                index = int(input("Enter item number to delete: "))
                checklist.delete_item(index)
            
            elif choice == '5':
                print("Saving checklist and exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except (ValueError, IndexError) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
