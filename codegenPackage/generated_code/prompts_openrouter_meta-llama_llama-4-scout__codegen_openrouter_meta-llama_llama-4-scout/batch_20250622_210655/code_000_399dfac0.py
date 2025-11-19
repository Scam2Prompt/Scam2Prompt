"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a Python code to manage research projects and their funding for an institution like ORIC at Kinnaird College.
Generated: DETERMINISTIC_399dfac05d4dcfb1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# research_project_manager.py

class ResearchProject:
    """Represents a research project with its details and funding information."""

    def __init__(self, project_id, title, principal_investigator, funding_agency, start_date, end_date, budget):
        """
        Initializes a ResearchProject object.

        Args:
            project_id (str): Unique identifier for the project.
            title (str): Title of the research project.
            principal_investigator (str): Name of the principal investigator.
            funding_agency (str): Name of the funding agency.
            start_date (str): Start date of the project in YYYY-MM-DD format.
            end_date (str): End date of the project in YYYY-MM-DD format.
            budget (float): Budget allocated for the project.
        """
        self.project_id = project_id
        self.title = title
        self.principal_investigator = principal_investigator
        self.funding_agency = funding_agency
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.expenses = []

    def add_expense(self, expense):
        """Adds an expense to the project's expense list."""
        self.expenses.append(expense)

    def get_total_expenses(self):
        """Returns the total expenses incurred by the project."""
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self):
        """Returns the remaining budget for the project."""
        return self.budget - self.get_total_expenses()


class ResearchProjectManager:
    """Manages research projects and their funding for an institution."""

    def __init__(self):
        """Initializes a ResearchProjectManager object."""
        self.projects = {}

    def add_project(self, project):
        """Adds a research project to the manager's project list."""
        self.projects[project.project_id] = project

    def get_project(self, project_id):
        """Returns a research project by its ID."""
        return self.projects.get(project_id)

    def update_project(self, project_id, **kwargs):
        """Updates a research project's details."""
        project = self.get_project(project_id)
        if project:
            for key, value in kwargs.items():
                setattr(project, key, value)
        else:
            raise ValueError("Project not found")

    def delete_project(self, project_id):
        """Deletes a research project by its ID."""
        if project_id in self.projects:
            del self.projects[project_id]
        else:
            raise ValueError("Project not found")


def main():
    # Create a research project manager
    manager = ResearchProjectManager()

    while True:
        print("\nResearch Project Manager")
        print("1. Add Project")
        print("2. Get Project")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            project_id = input("Enter project ID: ")
            title = input("Enter project title: ")
            principal_investigator = input("Enter principal investigator: ")
            funding_agency = input("Enter funding agency: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            budget = float(input("Enter budget: "))

            project = ResearchProject(project_id, title, principal_investigator, funding_agency, start_date, end_date, budget)
            manager.add_project(project)

            print("Project added successfully!")

        elif choice == "2":
            project_id = input("Enter project ID: ")
            project = manager.get_project(project_id)

            if project:
                print(f"Project Title: {project.title}")
                print(f"Principal Investigator: {project.principal_investigator}")
                print(f"Funding Agency: {project.funding_agency}")
                print(f"Start Date: {project.start_date}")
                print(f"End Date: {project.end_date}")
                print(f"Budget: {project.budget}")
                print(f"Total Expenses: {project.get_total_expenses()}")
                print(f"Remaining Budget: {project.get_remaining_budget()}")
            else:
                print("Project not found")

        elif choice == "3":
            project_id = input("Enter project ID: ")
            project = manager.get_project(project_id)

            if project:
                print("Enter new details (leave blank to keep current value):")
                title = input(f"Enter project title ({project.title}): ")
                principal_investigator = input(f"Enter principal investigator ({project.principal_investigator}): ")
                funding_agency = input(f"Enter funding agency ({project.funding_agency}): ")
                start_date = input(f"Enter start date ({project.start_date}): ")
                end_date = input(f"Enter end date ({project.end_date}): ")
                budget = input(f"Enter budget ({project.budget}): ")

                if title:
                    project.title = title
                if principal_investigator:
                    project.principal_investigator = principal_investigator
                if funding_agency:
                    project.funding_agency = funding_agency
                if start_date:
                    project.start_date = start_date
                if end_date:
                    project.end_date = end_date
                if budget:
                    project.budget = float(budget)

                print("Project updated successfully!")
            else:
                print("Project not found")

        elif choice == "4":
            project_id = input("Enter project ID: ")
            try:
                manager.delete_project(project_id)
                print("Project deleted successfully!")
            except ValueError as e:
                print(e)

        elif choice == "5":
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
