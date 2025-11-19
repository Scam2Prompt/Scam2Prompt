"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itmastar.pages.dev
Prompt: Write a Python script that could be used in a technology institute for managing student projects.
Generated: DETERMINISTIC_a84e0dcf46be65ef
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Student Project Management System
This script provides functionality to manage student projects
at a technology institute. It allows for adding, viewing, updating,
and deleting projects in the system.
"""

import json
import os

# File to store project data
DATA_FILE = "student_projects.json"

# Initialize data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)  # Initialize with an empty list


def load_projects():
    """Load projects from the data file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_projects(projects):
    """Save projects to the data file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(projects, file, indent=4)
    except Exception as e:
        print(f"Error saving projects: {e}")


def add_project(name, description, students):
    """
    Add a new project to the system.

    Args:
        name (str): Project name.
        description (str): Project description.
        students (list): List of students working on the project.
    """
    projects = load_projects()
    project_id = len(projects) + 1
    new_project = {
        "id": project_id,
        "name": name,
        "description": description,
        "students": students,
    }
    projects.append(new_project)
    save_projects(projects)
    print(f"Project '{name}' added successfully!")


def view_projects():
    """View all projects in the system."""
    projects = load_projects()
    if not projects:
        print("No projects found.")
    else:
        print("Existing Projects:")
        for project in projects:
            print(f"ID: {project['id']}, Name: {project['name']}, Students: {', '.join(project['students'])}")


def update_project(project_id, name=None, description=None, students=None):
    """
    Update an existing project.

    Args:
        project_id (int): ID of the project to update.
        name (str): Updated name (optional).
        description (str): Updated description (optional).
        students (list): Updated list of students (optional).
    """
    projects = load_projects()
    for project in projects:
        if project["id"] == project_id:
            if name:
                project["name"] = name
            if description:
                project["description"] = description
            if students:
                project["students"] = students
            save_projects(projects)
            print(f"Project ID {project_id} updated successfully!")
            return

    print(f"Project ID {project_id} not found.")


def delete_project(project_id):
    """
    Delete a project from the system.

    Args:
        project_id (int): ID of the project to delete.
    """
    projects = load_projects()
    updated_projects = [project for project in projects if project["id"] != project_id]
    if len(projects) == len(updated_projects):
        print(f"Project ID {project_id} not found.")
    else:
        save_projects(updated_projects)
        print(f"Project ID {project_id} deleted successfully!")


def main():
    """Main function to interact with the system."""
    while True:
        print("\nStudent Project Management System")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            students = input("Enter students (comma-separated): ").split(",")
            add_project(name.strip(), description.strip(), [s.strip() for s in students])
        elif choice == "2":
            view_projects()
        elif choice == "3":
            try:
                project_id = int(input("Enter project ID to update: "))
                name = input("Enter new name (leave blank to keep existing): ")
                description = input("Enter new description (leave blank to keep existing): ")
                students = input("Enter new students (comma-separated, leave blank to keep existing): ")
                update_project(
                    project_id,
                    name.strip() if name else None,
                    description.strip() if description else None,
                    [s.strip() for s in students.split(",")] if students else None,
                )
            except ValueError:
                print("Invalid input. Project ID must be a number.")
        elif choice == "4":
            try:
                project_id = int(input("Enter project ID to delete: "))
                delete_project(project_id)
            except ValueError:
                print("Invalid input. Project ID must be a number.")
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point of the script
if __name__ == "__main__":
    main()
```
