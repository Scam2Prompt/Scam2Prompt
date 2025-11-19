"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: What are some best practices for implementing a sistema de gestão in a construction company like MGEL, and how can they be coded into a software application?
Generated: DETERMINISTIC_e0132afdd9eea63d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a basic construction company management system (`sistema de gestão`) that follows best practices. It includes features like project management, employee management, and inventory tracking. The code is clean, well-documented, and production-ready.

```python
import json
import os

# Constants for file storage
DATA_DIR = "data"
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
EMPLOYEES_FILE = os.path.join(DATA_DIR, "employees.json")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Utility functions for file operations
def load_data(file_path):
    """Load data from a JSON file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Project Management
def add_project(name, deadline, budget):
    """Add a new project to the system."""
    projects = load_data(PROJECTS_FILE)
    project = {
        "id": len(projects) + 1,
        "name": name,
        "deadline": deadline,
        "budget": budget,
        "status": "Active"
    }
    projects.append(project)
    save_data(PROJECTS_FILE, projects)
    print(f"Project '{name}' added successfully.")

def list_projects():
    """List all projects."""
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        print(f"ID: {project['id']}, Name: {project['name']}, Deadline: {project['deadline']}, Budget: {project['budget']}, Status: {project['status']}")

# Employee Management
def add_employee(name, role, salary):
    """Add a new employee to the system."""
    employees = load_data(EMPLOYEES_FILE)
    employee = {
        "id": len(employees) + 1,
        "name": name,
        "role": role,
        "salary": salary
    }
    employees.append(employee)
    save_data(EMPLOYEES_FILE, employees)
    print(f"Employee '{name}' added successfully.")

def list_employees():
    """List all employees."""
    employees = load_data(EMPLOYEES_FILE)
    if not employees:
        print("No employees found.")
        return
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['name']}, Role: {employee['role']}, Salary: {employee['salary']}")

# Inventory Management
def add_inventory_item(name, quantity, unit_price):
    """Add a new inventory item to the system."""
    inventory = load_data(INVENTORY_FILE)
    item = {
        "id": len(inventory) + 1,
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price
    }
    inventory.append(item)
    save_data(INVENTORY_FILE, inventory)
    print(f"Inventory item '{name}' added successfully.")

def list_inventory():
    """List all inventory items."""
    inventory = load_data(INVENTORY_FILE)
    if not inventory:
        print("No inventory items found.")
        return
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Unit Price: {item['unit_price']}")

# Error Handling Example
def delete_project(project_id):
    """Delete a project by ID."""
    projects = load_data(PROJECTS_FILE)
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        print(f"Project with ID {project_id} not found.")
        return
    projects.remove(project)
    save_data(PROJECTS_FILE, projects)
    print(f"Project with ID {project_id} deleted successfully.")

# Main Menu
def main():
    """Main menu for the management system."""
    while True:
        print("\nConstruction Company Management System")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Add Employee")
        print("4. List Employees")
        print("5. Add Inventory Item")
        print("6. List Inventory")
        print("7. Delete Project")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter project name: ")
            deadline = input("Enter project deadline (YYYY-MM-DD): ")
            budget = float(input("Enter project budget: "))
            add_project(name, deadline, budget)
        elif choice == "2":
            list_projects()
        elif choice == "3":
            name = input("Enter employee name: ")
            role = input("Enter employee role: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, role, salary)
        elif choice == "4":
            list_employees()
        elif choice == "5":
            name = input("Enter inventory item name: ")
            quantity = int(input("Enter item quantity: "))
            unit_price = float(input("Enter item unit price: "))
            add_inventory_item(name, quantity, unit_price)
        elif choice == "6":
            list_inventory()
        elif choice == "7":
            project_id = int(input("Enter project ID to delete: "))
            delete_project(project_id)
        elif choice == "8":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```

This code provides a basic structure for a construction company management system. It uses JSON files for data storage, includes error handling, and follows best practices for readability and maintainability.
