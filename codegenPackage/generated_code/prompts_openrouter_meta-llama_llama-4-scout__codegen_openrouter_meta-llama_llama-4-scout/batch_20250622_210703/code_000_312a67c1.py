"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Generate a Python script to manage a portfolio of outdoor renovation projects, including fences, decks, and pergolas, with a focus on customer satisfaction and long-term durability."
Generated: DETERMINISTIC_312a67c18f3b3b9a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# outdoor_renovation_portfolio.py

class Project:
    """Represents an outdoor renovation project."""

    def __init__(self, project_id, customer_name, project_type, description, status="In Progress"):
        """
        Initializes a Project object.

        Args:
            project_id (int): Unique project identifier.
            customer_name (str): Name of the customer.
            project_type (str): Type of project (fence, deck, pergola).
            description (str): Brief project description.
            status (str, optional): Project status. Defaults to "In Progress".
        """
        self.project_id = project_id
        self.customer_name = customer_name
        self.project_type = project_type
        self.description = description
        self.status = status

    def update_status(self, status):
        """Updates the project status."""
        self.status = status

    def __str__(self):
        return f"Project {self.project_id}: {self.customer_name} - {self.project_type}"


class Portfolio:
    """Manages a portfolio of outdoor renovation projects."""

    def __init__(self):
        """Initializes a Portfolio object."""
        self.projects = {}

    def add_project(self, project):
        """
        Adds a project to the portfolio.

        Args:
            project (Project): Project object to add.

        Raises:
            ValueError: If a project with the same ID already exists.
        """
        if project.project_id in self.projects:
            raise ValueError("Project with this ID already exists")
        self.projects[project.project_id] = project

    def remove_project(self, project_id):
        """
        Removes a project from the portfolio.

        Args:
            project_id (int): ID of the project to remove.

        Raises:
            KeyError: If the project ID is not found.
        """
        if project_id not in self.projects:
            raise KeyError("Project ID not found")
        del self.projects[project_id]

    def update_project_status(self, project_id, status):
        """
        Updates the status of a project in the portfolio.

        Args:
            project_id (int): ID of the project to update.
            status (str): New status of the project.

        Raises:
            KeyError: If the project ID is not found.
        """
        if project_id not in self.projects:
            raise KeyError("Project ID not found")
        self.projects[project_id].update_status(status)

    def get_project(self, project_id):
        """
        Retrieves a project from the portfolio.

        Args:
            project_id (int): ID of the project to retrieve.

        Returns:
            Project: Project object if found, None otherwise.
        """
        return self.projects.get(project_id)

    def list_projects(self):
        """Returns a list of all projects in the portfolio."""
        return list(self.projects.values())


def main():
    portfolio = Portfolio()

    while True:
        print("\nOutdoor Renovation Portfolio Management")
        print("1. Add Project")
        print("2. Remove Project")
        print("3. Update Project Status")
        print("4. Get Project")
        print("5. List Projects")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                project_id = int(input("Enter project ID: "))
                customer_name = input("Enter customer name: ")
                project_type = input("Enter project type (fence, deck, pergola): ")
                description = input("Enter project description: ")
                project = Project(project_id, customer_name, project_type, description)
                portfolio.add_project(project)
                print(f"Project {project_id} added successfully")

            elif choice == "2":
                project_id = int(input("Enter project ID: "))
                portfolio.remove_project(project_id)
                print(f"Project {project_id} removed successfully")

            elif choice == "3":
                project_id = int(input("Enter project ID: "))
                status = input("Enter new status: ")
                portfolio.update_project_status(project_id, status)
                print(f"Project {project_id} status updated to {status}")

            elif choice == "4":
                project_id = int(input("Enter project ID: "))
                project = portfolio.get_project(project_id)
                if project:
                    print(project)
                    print(f"Status: {project.status}")
                    print(f"Description: {project.description}")
                else:
                    print("Project not found")

            elif choice == "5":
                projects = portfolio.list_projects()
                for project in projects:
                    print(project)

            elif choice == "6":
                break

            else:
                print("Invalid option. Please choose a valid option.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
