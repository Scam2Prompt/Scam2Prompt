"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Generate a Python script for automating project management tasks in architecture, such as tracking milestones and generating reports, as described in Études' project management services.
Generated: DETERMINISTIC_32d50de10a92c075
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class ProjectManagement:
    """
    A class to handle project management tasks such as tracking milestones
    and generating reports for architectural projects.
    """

    def __init__(self, project_name):
        """
        Initializes the project with a name and sets up the milestones list.

        :param project_name: The name of the project.
        """
        self.project_name = project_name
        self.milestones = []
        self.data_file = f"{project_name.lower().replace(' ', '_')}_milestones.json"
        self._load_data()

    def _load_data(self):
        """
        Load existing milestones from a JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.milestones = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading milestone data: {e}")
                self.milestones = []

    def _save_data(self):
        """
        Save milestones to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.milestones, file, indent=4)
        except IOError as e:
            print(f"Error saving milestone data: {e}")

    def add_milestone(self, name, due_date):
        """
        Add a new milestone to the project.

        :param name: The name of the milestone.
        :param due_date: The due date for the milestone in 'YYYY-MM-DD' format.
        """
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            milestone = {
                "name": name,
                "due_date": due_date_obj.strftime("%Y-%m-%d"),
                "status": "Pending"
            }
            self.milestones.append(milestone)
            self._save_data()
            print(f"Milestone '{name}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")

    def update_milestone_status(self, name, status):
        """
        Update the status of a milestone.

        :param name: The name of the milestone.
        :param status: The new status of the milestone (e.g., 'Completed', 'In Progress').
        """
        for milestone in self.milestones:
            if milestone["name"] == name:
                milestone["status"] = status
                self._save_data()
                print(f"Milestone '{name}' status updated to '{status}'.")
                return
        print(f"Error: Milestone '{name}' not found.")

    def generate_report(self):
        """
        Generate a summary report of the project's milestones.
        """
        print(f"Project Report for '{self.project_name}':")
        print(f"{'Name':<20} {'Due Date':<12} {'Status':<12}")
        print("=" * 44)
        for milestone in self.milestones:
            print(f"{milestone['name']:<20} {milestone['due_date']:<12} {milestone['status']:<12}")

    def delete_milestone(self, name):
        """
        Delete a milestone from the project.

        :param name: The name of the milestone to delete.
        """
        self.milestones = [m for m in self.milestones if m["name"] != name]
        self._save_data()
        print(f"Milestone '{name}' deleted successfully.")

def main():
    """
    Main function to interact with the ProjectManagement class.
    """
    print("Welcome to the Architecture Project Management Tool!")
    project_name = input("Enter the name of your project: ")
    manager = ProjectManagement(project_name)

    while True:
        print("\nOptions:")
        print("1. Add Milestone")
        print("2. Update Milestone Status")
        print("3. Generate Report")
        print("4. Delete Milestone")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter milestone name: ")
            due_date = input("Enter milestone due date (YYYY-MM-DD): ")
            manager.add_milestone(name, due_date)
        elif choice == "2":
            name = input("Enter milestone name: ")
            status = input("Enter new status (e.g., Completed, In Progress): ")
            manager.update_milestone_status(name, status)
        elif choice == "3":
            manager.generate_report()
        elif choice == "4":
            name = input("Enter milestone name to delete: ")
            manager.delete_milestone(name)
        elif choice == "5":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
