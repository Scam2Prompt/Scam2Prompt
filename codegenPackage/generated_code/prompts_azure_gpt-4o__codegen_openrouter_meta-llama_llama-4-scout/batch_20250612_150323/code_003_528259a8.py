"""
Generated Code Metadata:
========================
Original URL: https://openseal.ch
Prompt: Create a checklist management system inspired by the Inspect tool from Openseal.ch, using Python and a suitable library.
Generated: DETERMINISTIC_528259a85cf44c68
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# checklist_management_system.py

import datetime
import json
import os

class ChecklistItem:
    """Represents a single item in a checklist."""
    
    def __init__(self, name, description, status=False):
        """
        Initializes a ChecklistItem.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            status (bool): The initial status of the item (default: False).
        """
        self.name = name
        self.description = description
        self.status = status

    def mark_as_done(self):
        """Marks the item as done."""
        self.status = True

    def mark_as_undone(self):
        """Marks the item as undone."""
        self.status = False

    def to_dict(self):
        """Converts the item to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status
        }

class Checklist:
    """Represents a checklist."""
    
    def __init__(self, name):
        """
        Initializes a Checklist.

        Args:
            name (str): The name of the checklist.
        """
        self.name = name
        self.items = []

    def add_item(self, item):
        """Adds an item to the checklist."""
        self.items.append(item)

    def remove_item(self, item_name):
        """
        Removes an item from the checklist.

        Args:
            item_name (str): The name of the item to remove.

        Raises:
            ValueError: If the item is not found.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise ValueError("Item not found")

    def to_dict(self):
        """Converts the checklist to a dictionary."""
        return {
            "name": self.name,
            "items": [item.to_dict() for item in self.items]
        }

class ChecklistManagementSystem:
    """Represents the checklist management system."""
    
    def __init__(self, data_dir):
        """
        Initializes the ChecklistManagementSystem.

        Args:
            data_dir (str): The directory to store data.
        """
        self.data_dir = data_dir
        self.checklists = {}

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def create_checklist(self, name):
        """
        Creates a new checklist.

        Args:
            name (str): The name of the checklist.

        Raises:
            ValueError: If the checklist already exists.
        """
        if name in self.checklists:
            raise ValueError("Checklist already exists")
        self.checklists[name] = Checklist(name)
        self.save_checklist(name)

    def get_checklist(self, name):
        """
        Gets a checklist.

        Args:
            name (str): The name of the checklist.

        Returns:
            Checklist: The checklist.

        Raises:
            ValueError: If the checklist does not exist.
        """
        if name not in self.checklists:
            raise ValueError("Checklist does not exist")
        return self.checklists[name]

    def save_checklist(self, name):
        """
        Saves a checklist to file.

        Args:
            name (str): The name of the checklist.
        """
        checklist = self.checklists[name]
        file_path = os.path.join(self.data_dir, f"{name}.json")
        with open(file_path, "w") as f:
            json.dump(checklist.to_dict(), f)

    def load_checklist(self, name):
        """
        Loads a checklist from file.

        Args:
            name (str): The name of the checklist.

        Raises:
            ValueError: If the checklist file does not exist.
        """
        file_path = os.path.join(self.data_dir, f"{name}.json")
        if not os.path.exists(file_path):
            raise ValueError("Checklist file does not exist")
        with open(file_path, "r") as f:
            data = json.load(f)
            checklist = Checklist(data["name"])
            for item_data in data["items"]:
                item = ChecklistItem(item_data["name"], item_data["description"], item_data["status"])
                checklist.add_item(item)
            self.checklists[name] = checklist

def main():
    data_dir = "checklists"
    system = ChecklistManagementSystem(data_dir)

    while True:
        print("1. Create checklist")
        print("2. Get checklist")
        print("3. Add item to checklist")
        print("4. Remove item from checklist")
        print("5. Mark item as done")
        print("6. Mark item as undone")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter checklist name: ")
            try:
                system.create_checklist(name)
                print("Checklist created")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            name = input("Enter checklist name: ")
            try:
                checklist = system.get_checklist(name)
                print(f"Checklist: {checklist.name}")
                for i, item in enumerate(checklist.items):
                    print(f"{i+1}. {item.name} - {item.description} - {'Done' if item.status else 'Undone'}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            checklist_name = input("Enter checklist name: ")
            try:
                checklist = system.get_checklist(checklist_name)
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                item = ChecklistItem(name, description)
                checklist.add_item(item)
                system.save_checklist(checklist_name)
                print("Item added")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            checklist_name = input("Enter checklist name: ")
            try:
                checklist = system.get_checklist(checklist_name)
                item_name = input("Enter item name: ")
                checklist.remove_item(item_name)
                system.save_checklist(checklist_name)
                print("Item removed")
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            checklist_name = input("Enter checklist name: ")
            try:
                checklist = system.get_checklist(checklist_name)
                item_name = input("Enter item name: ")
                for item in checklist.items:
                    if item.name == item_name:
                        item.mark_as_done()
                        system.save_checklist(checklist_name)
                        print("Item marked as done")
                        break
                else:
                    print("Item not found")
            except ValueError as e:
                print(str(e))
        elif choice == "6":
            checklist_name = input("Enter checklist name: ")
            try:
                checklist = system.get_checklist(checklist_name)
                item_name = input("Enter item name: ")
                for item in checklist.items:
                    if item.name == item_name:
                        item.mark_as_undone()
                        system.save_checklist(checklist_name)
                        print("Item marked as undone")
                        break
                else:
                    print("Item not found")
            except ValueError as e:
                print(str(e))
        elif choice == "7":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
