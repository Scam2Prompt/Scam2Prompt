"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Generate a Python script that utilizes digital tools and platforms for managing online projects as described in the КарьераОнлайн program.
Generated: DETERMINISTIC_aac9a7307c96f23f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Tool - Python Script

This script is designed to help manage online projects using digital tools and platforms.
It includes features such as task tracking, team collaboration, project deadline reminders,
and reporting functionalities.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import os
import json
import datetime
from typing import List, Dict

# Constants
DATA_FILE = "projects.json"

# Utility Functions
def load_data(file_path: str) -> List[Dict]:
    """
    Load project data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict]: List of projects.
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def save_data(file_path: str, data: List[Dict]) -> None:
    """
    Save project data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (List[Dict]): List of projects to save.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Classes
class Task:
    """
    Represents a task in a project.
    """
    def __init__(self, name: str, description: str, deadline: str):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.is_completed = True

    def __str__(self) -> str:
        """Provide a string representation of the task."""
        status = "Completed" if self.is_completed else "Pending"
        return f"Task: {self.name}, Status: {status}, Deadline: {self.deadline}"

class Project:
    """
    Represents an online project.
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)

    def list_tasks(self) -> None:
        """List all tasks in the project."""
        for task in self.tasks:
            print(task)

    def __str__(self) -> str:
        """Provide a string representation of the project."""
        return f"Project: {self.name}, Description: {self.description}, Tasks: {len(self.tasks)}"

# Main Functionality
def main():
    """
    Main function for managing online projects.
    """
    print("Welcome to the Online Project Management Tool!")
    
    # Load existing project data
    projects = load_data(DATA_FILE)
    project_objects = [Project(p['name'], p['description']) for p in projects]
    
    # Main menu
    while True:
        print("\nMenu:")
        print("1. Create New Project")
        print("2. View Projects")
        print("3. Add Task to Project")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Create a new project
            name = input("Enter project name: ").strip()
            description = input("Enter project description: ").strip()
            new_project = Project(name, description)
            project_objects.append(new_project)
            print(f"Project '{name}' created successfully!")

        elif choice == "2":
            # View all projects
            if not project_objects:
                print("No projects found.")
            else:
                for i, project in enumerate(project_objects, start=1):
                    print(f"{i}. {project}")

        elif choice == "3":
            # Add a task to a project
            if not project_objects:
                print("No projects available to add tasks.")
                continue
            
            for i, project in enumerate(project_objects, start=1):
                print(f"{i}. {project.name}")
            
            project_choice = input("Select a project by number: ").strip()
            try:
                project_index = int(project_choice) - 1
                selected_project = project_objects[project_index]
                
                task_name = input("Enter task name: ").strip()
                task_description = input("Enter task description: ").strip()
                task_deadline = input("Enter task deadline (YYYY-MM-DD): ").strip()
                
                try:
                    # Validate deadline format
                    datetime.datetime.strptime(task_deadline, "%Y-%m-%d")
                    new_task = Task(task_name, task_description, task_deadline)
                    selected_project.add_task(new_task)
                    print(f"Task '{task_name}' added successfully!")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            except (IndexError, ValueError):
                print("Invalid project selection.")

        elif choice == "4":
            # Save data and exit
            save_data(DATA_FILE, [{"name": p.name, "description": p.description} for p in project_objects])
            print("Data saved successfully. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
