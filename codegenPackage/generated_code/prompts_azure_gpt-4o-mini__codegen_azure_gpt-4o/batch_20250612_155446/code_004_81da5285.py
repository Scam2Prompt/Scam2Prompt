"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: How can I apply the programming techniques from the Ejecutor Tecnico's "Presentaciones de Python" in a real-world project?
Generated: DETERMINISTIC_81da5285d62f7773
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the application of Python programming techniques 
from a technical presentation in a real-world project. The example project 
is a simple task management system that uses Python's best practices, 
error handling, and clean code principles.
"""

import json
import os
from datetime import datetime

# Define constants for file storage
TASKS_FILE = "tasks.json"

# Error classes for custom exceptions
class TaskError(Exception):
    """Custom exception for task-related errors."""
    pass

# Utility functions
def load_tasks():
    """
    Load tasks from a JSON file. If the file does not exist, return an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise TaskError("Failed to decode tasks file. Ensure the file is properly formatted.")

def save_tasks(tasks):
    """
    Save tasks to a JSON file.
    """
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        raise TaskError(f"Failed to save tasks: {e}")

def validate_task(task):
    """
    Validate the structure of a task dictionary.
    """
    if not isinstance(task, dict):
        raise TaskError("Task must be a dictionary.")
    if "title" not in task or not isinstance(task["title"], str):
        raise TaskError("Task must have a 'title' field of type string.")
    if "description" not in task or not isinstance(task["description"], str):
        raise TaskError("Task must have a 'description' field of type string.")
    if "due_date" not in task or not isinstance(task["due_date"], str):
        raise TaskError("Task must have a 'due_date' field of type string.")

# Core functions
def add_task(title, description, due_date):
    """
    Add a new task to the task list.
    """
    tasks = load_tasks()
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    validate_task(new_task)
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def list_tasks():
    """
    List all tasks in the task list.
    """
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"Task {idx}:")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Created At: {task['created_at']}")
        print(f"  Completed: {'Yes' if task['completed'] else 'No'}")
        print("-" * 40)

def mark_task_completed(task_index):
    """
    Mark a task as completed.
    """
    tasks = load_tasks()
    if task_index < 1 or task_index > len(tasks):
        raise TaskError("Invalid task index.")
    tasks[task_index - 1]["completed"] = True
    save_tasks(tasks)
    print(f"Task {task_index} marked as completed.")

def delete_task(task_index):
    """
    Delete a task from the task list.
    """
    tasks = load_tasks()
    if task_index < 1 or task_index > len(tasks):
        raise TaskError("Invalid task index.")
    deleted_task = tasks.pop(task_index - 1)
    save_tasks(tasks)
    print(f"Task '{deleted_task['title']}' deleted successfully.")

# Main function
def main():
    """
    Main function to demonstrate the task management system.
    """
    print("Task Management System")
    print("=======================")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
                add_task(title, description, due_date)
            elif choice == "2":
                list_tasks()
            elif choice == "3":
                task_index = int(input("Enter task index to mark as completed: "))
                mark_task_completed(task_index)
            elif choice == "4":
                task_index = int(input("Enter task index to delete: "))
                delete_task(task_index)
            elif choice == "5":
                print("Exiting Task Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except TaskError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Entry point
if __name__ == "__main__":
    main()
```
