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
# checklist_inspect.py

import inspect

class Checklist:
    """
    A class representing a digital checklist.

    Attributes:
        name (str): The name of the checklist.
        items (list): A list of items in the checklist.
    """

    def __init__(self, name):
        """
        Initializes a new Checklist instance.

        Args:
            name (str): The name of the checklist.

        Raises:
            TypeError: If the name is not a string.
            ValueError: If the name is empty.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")

        self.name = name
        self.items = []

    def add_item(self, item):
        """
        Adds a new item to the checklist.

        Args:
            item (str): The item to add.

        Raises:
            TypeError: If the item is not a string.
            ValueError: If the item is empty.
        """
        if not isinstance(item, str):
            raise TypeError("Item must be a string")
        if not item.strip():
            raise ValueError("Item cannot be empty")

        self.items.append(item)

    def remove_item(self, item_index):
        """
        Removes an item from the checklist.

        Args:
            item_index (int): The index of the item to remove.

        Raises:
            IndexError: If the item index is out of range.
        """
        try:
            del self.items[item_index]
        except IndexError:
            raise IndexError("Item index out of range")

    def mark_item_as_done(self, item_index):
        """
        Marks an item as done.

        Args:
            item_index (int): The index of the item to mark as done.

        Raises:
            IndexError: If the item index is out of range.
        """
        try:
            self.items[item_index] = f"[x] {self.items[item_index].lstrip('[x] ')}"
        except IndexError:
            raise IndexError("Item index out of range")

    def __str__(self):
        """
        Returns a string representation of the checklist.

        Returns:
            str: A string representation of the checklist.
        """
        checklist_str = f"{self.name}:\n"
        for i, item in enumerate(self.items):
            checklist_str += f"{i+1}. {item}\n"
        return checklist_str


def create_checklist():
    """
    Creates a new checklist.

    Returns:
        Checklist: A new Checklist instance.
    """
    name = input("Enter checklist name: ")
    return Checklist(name)


def manage_checklist(checklist):
    """
    Manages a checklist.

    Args:
        checklist (Checklist): The checklist to manage.
    """
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Mark item as done")
        print("4. View checklist")
        print("5. Quit")

        option = input("Choose an option: ")

        if option == "1":
            item = input("Enter item: ")
            checklist.add_item(item)
        elif option == "2":
            try:
                item_index = int(input("Enter item index: ")) - 1
                checklist.remove_item(item_index)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif option == "3":
            try:
                item_index = int(input("Enter item index: ")) - 1
                checklist.mark_item_as_done(item_index)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif option == "4":
            print(checklist)
        elif option == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")


def main():
    checklist = create_checklist()
    manage_checklist(checklist)


if __name__ == "__main__":
    main()
```
