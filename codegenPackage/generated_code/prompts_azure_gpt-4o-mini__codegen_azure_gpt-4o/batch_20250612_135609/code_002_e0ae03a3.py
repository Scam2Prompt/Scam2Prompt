"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script that automates the tracking of special paint works and renovation tasks for a contracting business.
Generated: DETERMINISTIC_e0ae03a36bfba924
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

# Define the file where tasks will be stored
TASKS_FILE = "tasks.json"

# Ensure the tasks file exists
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns:
        list: A list of tasks.
    """
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    Args:
        tasks (list): A list of tasks to save.
    """
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(description, category, deadline):
    """
    Add a new task to the list.
    Args:
        description (str): Description of the task.
        category (str): Category of the task (e.g., 'Paint', 'Renovation').
        deadline (str): Deadline for the task in YYYY-MM-DD format.
    """
    tasks = load_tasks()
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        task = {
            "id": len(tasks) + 1,
            "description": description,
            "category": category,
            "deadline": deadline_date.strftime("%Y-%m-%d"),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Pending"
        }
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    except ValueError:
        print("Invalid deadline format. Please use YYYY-MM-DD.")

def list_tasks():
    """
    List all tasks.
    """
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, "
              f"Category: {task['category']}, Deadline: {task['deadline']}, "
              f"Status: {task['status']}")

def update_task_status(task_id, status):
    """
    Update the status of a task.
    Args:
        task_id (int): ID of the task to update.
        status (str): New status of the task (e.g., 'Completed', 'In Progress').
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_tasks(tasks)
            print("Task status updated successfully!")
            return
    print("Task not found.")

def delete_task(task_id):
    """
    Delete a task by its ID.
    Args:
        task_id (int): ID of the task to delete.
    """
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print("Task deleted successfully!")

def main():
    """
    Main function to interact with the task tracker.
    """
    while True:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Paint, Renovation): ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            add_task(description, category, deadline)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                status = input("Enter new status (e.g., Completed, In Progress): ")
                update_task_status(task_id, status)
            except ValueError:
                print("Invalid input. Task ID must be a number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Task ID must be a number.")
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
