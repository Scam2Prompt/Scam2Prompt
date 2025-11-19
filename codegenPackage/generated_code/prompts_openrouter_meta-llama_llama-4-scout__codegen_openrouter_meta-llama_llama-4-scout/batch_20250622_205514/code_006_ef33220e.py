"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Write a code snippet to create a simple party planning checklist in Python."
Generated: DETERMINISTIC_ef33220e0103d53f
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# party_planning_checklist.py

class PartyPlanningChecklist:
    def __init__(self):
        """
        Initialize an empty party planning checklist.
        """
        self.checklist = {
            "guests": [],
            "tasks": [],
            "supplies": []
        }

    def add_guest(self, name):
        """
        Add a guest to the checklist.

        Args:
            name (str): The guest's name.
        """
        self.checklist["guests"].append(name)

    def remove_guest(self, name):
        """
        Remove a guest from the checklist.

        Args:
            name (str): The guest's name.

        Raises:
            ValueError: If the guest is not in the checklist.
        """
        if name in self.checklist["guests"]:
            self.checklist["guests"].remove(name)
        else:
            raise ValueError(f"{name} is not in the guest list.")

    def add_task(self, task):
        """
        Add a task to the checklist.

        Args:
            task (str): The task to add.
        """
        self.checklist["tasks"].append(task)

    def complete_task(self, task):
        """
        Mark a task as completed.

        Args:
            task (str): The task to complete.

        Raises:
            ValueError: If the task is not in the checklist.
        """
        if task in self.checklist["tasks"]:
            self.checklist["tasks"].remove(task)
        else:
            raise ValueError(f"{task} is not in the task list.")

    def add_supply(self, supply):
        """
        Add a supply to the checklist.

        Args:
            supply (str): The supply to add.
        """
        self.checklist["supplies"].append(supply)

    def remove_supply(self, supply):
        """
        Remove a supply from the checklist.

        Args:
            supply (str): The supply to remove.

        Raises:
            ValueError: If the supply is not in the checklist.
        """
        if supply in self.checklist["supplies"]:
            self.checklist["supplies"].remove(supply)
        else:
            raise ValueError(f"{supply} is not in the supply list.")

    def print_checklist(self):
        """
        Print the current state of the party planning checklist.
        """
        print("# Party Planning Checklist")
        print("## Guests:")
        for guest in self.checklist["guests"]:
            print(f"- {guest}")
        print("\n## Tasks:")
        for task in self.checklist["tasks"]:
            print(f"- {task}")
        print("\n## Supplies:")
        for supply in self.checklist["supplies"]:
            print(f"- {supply}")


def main():
    try:
        checklist = PartyPlanningChecklist()

        while True:
            print("\n# Options:")
            print("1. Add guest")
            print("2. Remove guest")
            print("3. Add task")
            print("4. Complete task")
            print("5. Add supply")
            print("6. Remove supply")
            print("7. Print checklist")
            print("8. Quit")

            option = input("Choose an option: ")

            if option == "1":
                name = input("Enter guest's name: ")
                checklist.add_guest(name)
            elif option == "2":
                name = input("Enter guest's name: ")
                try:
                    checklist.remove_guest(name)
                except ValueError as e:
                    print(e)
            elif option == "3":
                task = input("Enter task: ")
                checklist.add_task(task)
            elif option == "4":
                task = input("Enter task: ")
                try:
                    checklist.complete_task(task)
                except ValueError as e:
                    print(e)
            elif option == "5":
                supply = input("Enter supply: ")
                checklist.add_supply(supply)
            elif option == "6":
                supply = input("Enter supply: ")
                try:
                    checklist.remove_supply(supply)
                except ValueError as e:
                    print(e)
            elif option == "7":
                checklist.print_checklist()
            elif option == "8":
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
