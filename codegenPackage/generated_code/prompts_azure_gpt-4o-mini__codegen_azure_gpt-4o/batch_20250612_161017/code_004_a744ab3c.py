"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Design an application that allows users to create still life photography projects, focusing on impactful visuals for products, as emphasized by Officine dell’Immagine.
Generated: DETERMINISTIC_a744ab3ce66b34b9
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Application: Still Life Photography Project Manager
Description: This application allows users to create and manage still life photography projects, 
focusing on impactful visuals for products, inspired by Officine dell’Immagine.
Language: Python
"""

import os
import json
from datetime import datetime

# Constants
DATA_FILE = "projects.json"

# Helper function to load existing projects from file
def load_projects():
    """Load projects from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return []

# Helper function to save projects to file
def save_projects(projects):
    """Save projects to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(projects, file, indent=4)
    except Exception as e:
        print(f"Error: Failed to save projects. {e}")

# Function to create a new project
def create_project():
    """Create a new still life photography project."""
    print("\n--- Create New Project ---")
    name = input("Enter project name: ").strip()
    description = input("Enter project description: ").strip()
    client = input("Enter client name: ").strip()
    deadline = input("Enter project deadline (YYYY-MM-DD): ").strip()

    # Validate deadline format
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return

    # Create project dictionary
    project = {
        "name": name,
        "description": description,
        "client": client,
        "deadline": deadline_date.strftime("%Y-%m-%d"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Load existing projects and add the new one
    projects = load_projects()
    projects.append(project)
    save_projects(projects)

    print(f"Project '{name}' created successfully!")

# Function to list all projects
def list_projects():
    """List all existing projects."""
    print("\n--- List of Projects ---")
    projects = load_projects()
    if not projects:
        print("No projects found.")
        return

    for idx, project in enumerate(projects, start=1):
        print(f"\nProject {idx}:")
        print(f"  Name: {project['name']}")
        print(f"  Description: {project['description']}")
        print(f"  Client: {project['client']}")
        print(f"  Deadline: {project['deadline']}")
        print(f"  Created At: {project['created_at']}")

# Function to delete a project
def delete_project():
    """Delete a project by name."""
    print("\n--- Delete Project ---")
    name = input("Enter the name of the project to delete: ").strip()

    projects = load_projects()
    updated_projects = [project for project in projects if project["name"] != name]

    if len(updated_projects) == len(projects):
        print(f"No project found with the name '{name}'.")
        return

    save_projects(updated_projects)
    print(f"Project '{name}' deleted successfully!")

# Main menu
def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n--- Still Life Photography Project Manager ---")
        print("1. Create New Project")
        print("2. List All Projects")
        print("3. Delete Project")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            create_project()
        elif choice == "2":
            list_projects()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()
```
