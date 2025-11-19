"""
Generated Code Metadata:
========================
Original URL: https://notclosn.top
Prompt: Generate a Python script that utilizes digital tools and platforms for managing online projects as described in the КарьераОнлайн program.
Generated: DETERMINISTIC_aac9a7307c96f23f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python Script for Managing Online Projects
This script utilizes digital tools and platforms to manage online projects effectively.
It includes features for task management, team collaboration, and progress tracking.
"""

import json
import os
from datetime import datetime

# Constants for file paths
PROJECTS_FILE = "projects.json"

# Error handling for file operations
def load_projects():
    """Load projects from a JSON file."""
    if not os.path.exists(PROJECTS_FILE):
        return {}
    try:
        with open(PROJECTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return {}
    except Exception as e:
        print(f"Error: {e}")
        return {}

def save_projects(projects):
    """Save projects to a JSON file."""
    try:
        with open(PROJECTS_FILE, "w") as file:
            json.dump(projects, file, indent=4)
    except Exception as e:
        print(f"Error: {e}")

# Core functionality
def create_project(projects, name, description, deadline):
    """Create a new project."""
    if name in projects:
        print("Error: Project with this name already exists.")
        return
    projects[name] = {
        "description": description,
        "deadline": deadline,
        "tasks": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    print(f"Project '{name}' created successfully.")

def add_task_to_project(projects, project_name, task_name, assignee, status="Pending"):
    """Add a task to an existing project."""
    if project_name not in projects:
        print("Error: Project not found.")
        return
    projects[project_name]["tasks"].append({
        "task_name": task_name,
        "assignee": assignee,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"Task '{task_name}' added to project '{project_name}'.")

def update_task_status(projects, project_name, task_name, new_status):
    """Update the status of a task in a project."""
    if project_name not in projects:
        print("Error: Project not found.")
        return
    for task in projects[project_name]["tasks"]:
        if task["task_name"] == task_name:
            task["status"] = new_status
            print(f"Task '{task_name}' status updated to '{new_status}'.")
            return
    print("Error: Task not found.")

def list_projects(projects):
    """List all projects."""
    if not projects:
        print("No projects found.")
        return
    for name, details in projects.items():
        print(f"Project: {name}")
        print(f"  Description: {details['description']}")
        print(f"  Deadline: {details['deadline']}")
        print(f"  Created At: {details['created_at']}")
        print(f"  Tasks:")
        for task in details["tasks"]:
            print(f"    - {task['task_name']} (Assignee: {task['assignee']}, Status: {task['status']})")
        print()

# Main function
def main():
    """Main function to manage projects."""
    projects = load_projects()

    while True:
        print("\nOnline Project Management")
        print("1. Create Project")
        print("2. Add Task to Project")
        print("3. Update Task Status")
        print("4. List Projects")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            deadline = input("Enter project deadline (YYYY-MM-DD): ")
            create_project(projects, name, description, deadline)
        elif choice == "2":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            assignee = input("Enter assignee name: ")
            add_task_to_project(projects, project_name, task_name, assignee)
        elif choice == "3":
            project_name = input("Enter project name: ")
            task_name = input("Enter task name: ")
            new_status = input("Enter new status: ")
            update_task_status(projects, project_name, task_name, new_status)
        elif choice == "4":
            list_projects(projects)
        elif choice == "5":
            save_projects(projects)
            print("Exiting. Projects saved.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
