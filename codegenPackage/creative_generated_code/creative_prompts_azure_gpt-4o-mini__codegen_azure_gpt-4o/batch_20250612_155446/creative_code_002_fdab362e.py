"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ejecutortecnico.github.io
Prompt: Write a code snippet that utilizes Python to implement a basic project discussed in the Talento Tech Programacion section of the Ejecutor Tecnico webpage.
Generated: DETERMINISTIC_fdab362e4a3753a4
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script is a basic implementation of a project management tool 
inspired by a generic project management section. It allows users to 
create, list, update, and delete projects. It includes error handling 
and follows best practices for clean, maintainable code.
"""

# Import necessary modules
import sys

class ProjectManager:
    """Class to manage projects."""
    
    def __init__(self):
        # Initialize with an empty list of projects
        self.projects = []
    
    def create_project(self, name, description):
        """
        Create a new project with a name and description.
        Args:
            name (str): The name of the project.
            description (str): A brief description of the project.
        """
        if not name or not description:
            raise ValueError("Both name and description are required.")
        
        project = {
            "id": len(self.projects) + 1,
            "name": name,
            "description": description
        }
        self.projects.append(project)
        print(f"Project '{name}' created successfully!")
    
    def list_projects(self):
        """List all the projects."""
        if not self.projects:
            print("No projects available.")
            return
        
        print("Projects:")
        for project in self.projects:
            print(f"ID: {project['id']}, Name: {project['name']}, Description: {project['description']}")
    
    def update_project(self, project_id, new_name=None, new_description=None):
        """
        Update an existing project.
        Args:
            project_id (int): The ID of the project to update.
            new_name (str): The new name of the project (optional).
            new_description (str): The new description of the project (optional).
        """
        for project in self.projects:
            if project["id"] == project_id:
                if new_name:
                    project["name"] = new_name
                if new_description:
                    project["description"] = new_description
                print(f"Project ID {project_id} updated successfully!")
                return
        
        print(f"Project ID {project_id} not found.")
    
    def delete_project(self, project_id):
        """
        Delete a project by its ID.
        Args:
            project_id (int): The ID of the project to delete.
        """
        for project in self.projects:
            if project["id"] == project_id:
                self.projects.remove(project)
                print(f"Project ID {project_id} deleted successfully!")
                return
        
        print(f"Project ID {project_id} not found.")

def main():
    """Main function to interact with the ProjectManager."""
    manager = ProjectManager()
    
    while True:
        print("\nProject Management Tool")
        print("1. Create Project")
        print("2. List Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            try:
                manager.create_project(name, description)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            manager.list_projects()
        elif choice == 3:
            try:
                project_id = int(input("Enter project ID to update: "))
                new_name = input("Enter new project name (or press Enter to skip): ")
                new_description = input("Enter new project description (or press Enter to skip): ")
                manager.update_project(project_id, new_name or None, new_description or None)
            except ValueError:
                print("Invalid input for project ID.")
        elif choice == 4:
            try:
                project_id = int(input("Enter project ID to delete: "))
                manager.delete_project(project_id)
            except ValueError:
                print("Invalid input for project ID.")
        elif choice == 5:
            print("Exiting the Project Management Tool. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
```
