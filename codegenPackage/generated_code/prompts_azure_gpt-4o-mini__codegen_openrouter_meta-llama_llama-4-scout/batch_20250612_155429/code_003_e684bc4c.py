"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Create a function that allows users to submit their interior design project ideas, inspired by the client collaboration process at Zirciulit.
Generated: DETERMINISTIC_e684bc4ccd0625dc
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_project.py

class InteriorDesignProject:
    def __init__(self, project_name, client_name, description, inspiration_sources):
        """
        Initialize an interior design project.

        Args:
            project_name (str): The name of the project.
            client_name (str): The name of the client.
            description (str): A brief description of the project.
            inspiration_sources (list): A list of inspiration sources for the project.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.description = description
        self.inspiration_sources = inspiration_sources

    def __str__(self):
        return f"Project: {self.project_name}\nClient: {self.client_name}\nDescription: {self.description}\nInspiration Sources: {', '.join(self.inspiration_sources)}"


class InteriorDesignProjectManager:
    def __init__(self):
        """
        Initialize a project manager.
        """
        self.projects = []

    def submit_project(self, project_name, client_name, description, inspiration_sources):
        """
        Submit a new interior design project.

        Args:
            project_name (str): The name of the project.
            client_name (str): The name of the client.
            description (str): A brief description of the project.
            inspiration_sources (list): A list of inspiration sources for the project.

        Returns:
            InteriorDesignProject: The newly created project.

        Raises:
            ValueError: If any of the required fields are empty.
        """
        if not all([project_name, client_name, description, inspiration_sources]):
            raise ValueError("All fields are required")

        project = InteriorDesignProject(project_name, client_name, description, inspiration_sources)
        self.projects.append(project)
        return project

    def get_all_projects(self):
        """
        Get all submitted projects.

        Returns:
            list: A list of all submitted projects.
        """
        return self.projects


def main():
    try:
        manager = InteriorDesignProjectManager()

        while True:
            print("\n1. Submit a project")
            print("2. View all projects")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                project_name = input("Enter project name: ")
                client_name = input("Enter client name: ")
                description = input("Enter project description: ")
                inspiration_sources = input("Enter inspiration sources (comma-separated): ").split(',')

                # Strip leading/trailing whitespaces from inspiration sources
                inspiration_sources = [source.strip() for source in inspiration_sources]

                project = manager.submit_project(project_name, client_name, description, inspiration_sources)
                print("\nProject submitted successfully!")
                print(project)

            elif choice == "2":
                projects = manager.get_all_projects()
                if not projects:
                    print("No projects submitted yet.")
                else:
                    for i, project in enumerate(projects, start=1):
                        print(f"\nProject {i}:")
                        print(project)

            elif choice == "3":
                break

            else:
                print("Invalid option. Please choose again.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
