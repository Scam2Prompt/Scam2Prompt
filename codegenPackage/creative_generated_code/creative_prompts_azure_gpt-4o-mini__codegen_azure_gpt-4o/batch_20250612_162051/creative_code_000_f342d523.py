"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://settlement.owlspriority.ca
Prompt: How can I create a checklist for new arrivals in Canada to help them settle in effectively?
Generated: DETERMINISTIC_f342d5233fa8f81d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Checklist Application for New Arrivals in Canada

This script creates a checklist for new arrivals in Canada to help them settle in effectively.
Users can view, update, and mark items as completed in the checklist.

Author: [Your Name]
Date: [Insert Date]
"""

import json


class Checklist:
    def __init__(self, checklist_file="checklist.json"):
        """
        Initialize the Checklist class with a JSON file to store the checklist items.
        """
        self.checklist_file = checklist_file
        self.checklist = {}
        self.load_checklist()

    def load_checklist(self):
        """
        Load checklist items from the JSON file. Creates a default checklist if file is empty or missing.
        """
        try:
            with open(self.checklist_file, "r") as file:
                self.checklist = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Default checklist for new arrivals in Canada
            self.checklist = {
                "Obtain SIN": False,
                "Open a bank account": False,
                "Find housing": False,
                "Apply for health insurance (e.g., OHIP)": False,
                "Get a phone plan": False,
                "Explore public transportation options": False,
                "Register children for school (if applicable)": False,
                "Learn about local emergency services": False,
                "Understand taxes and benefits": False,
                "Join community centers or language classes": False,
            }
            self.save_checklist()

    def save_checklist(self):
        """
        Save the checklist items to the JSON file.
        """
        try:
            with open(self.checklist_file, "w") as file:
                json.dump(self.checklist, file, indent=4)
        except IOError as e:
            print(f"Error saving checklist: {e}")

    def show_checklist(self):
        """
        Display the checklist items and their completion status.
        """
        print("\nChecklist for New Arrivals in Canada:")
        print("-" * 40)
        for item, completed in self.checklist.items():
            status = "✔️" if completed else "❌"
            print(f"{status} {item}")
        print("-" * 40)

    def mark_completed(self, item):
        """
        Mark a checklist item as completed.
        :param item: The item from the checklist to mark as completed.
        """
        if item in self.checklist:
            self.checklist[item] = True
            self.save_checklist()
            print(f"'{item}' marked as completed.")
        else:
            print(f"'{item}' not found in the checklist.")

    def add_item(self, item):
        """
        Add a new item to the checklist.
        :param item: The checklist item to add.
        """
        if item not in self.checklist:
            self.checklist[item] = False
            self.save_checklist()
            print(f"'{item}' added to the checklist.")
        else:
            print(f"'{item}' already exists in the checklist.")

    def remove_item(self, item):
        """
        Remove an item from the checklist.
        :param item: The checklist item to remove.
        """
        if item in self.checklist:
            del self.checklist[item]
            self.save_checklist()
            print(f"'{item}' removed from the checklist.")
        else:
            print(f"'{item}' not found in the checklist.")


def main():
    """
    Main function to interact with the checklist.
    """
    checklist = Checklist()

    while True:
        print("\nOptions:")
        print("1. Show checklist")
        print("2. Mark item as completed")
        print("3. Add new item")
        print("4. Remove item")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            checklist.show_checklist()
        elif choice == "2":
            item = input("Enter the item to mark as completed: ").strip()
            checklist.mark_completed(item)
        elif choice == "3":
            item = input("Enter the new item to add: ").strip()
            checklist.add_item(item)
        elif choice == "4":
            item = input("Enter the item to remove: ").strip()
            checklist.remove_item(item)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
