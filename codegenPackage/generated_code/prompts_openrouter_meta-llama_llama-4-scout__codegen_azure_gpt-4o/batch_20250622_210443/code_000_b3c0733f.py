"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Write a Python script to manage and track glass, aluminum, and PVC projects, including client information and product details, similar to CristalesGraf's services."
Generated: DETERMINISTIC_b3c0733ffc32559c
Batch ID: 20250622_210443
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

# Constants for file storage
DATA_FILE = "projects_data.json"

# Initialize data storage
def initialize_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump({"projects": []}, file)

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"projects": []}

# Save data to file
def save_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Add a new project
def add_project(client_name, client_contact, product_type, product_details):
    if product_type not in ["Glass", "Aluminum", "PVC"]:
        print("Invalid product type. Please choose 'Glass', 'Aluminum', or 'PVC'.")
        return

    project = {
        "client_name": client_name,
        "client_contact": client_contact,
        "product_type": product_type,
        "product_details": product_details
    }

    data = load_data()
    data["projects"].append(project)
    save_data(data)
    print("Project added successfully.")

# List all projects
def list_projects():
    data = load_data()
    if not data["projects"]:
        print("No projects found.")
        return

    for idx, project in enumerate(data["projects"], start=1):
        print(f"Project {idx}:")
        print(f"  Client Name: {project['client_name']}")
        print(f"  Client Contact: {project['client_contact']}")
        print(f"  Product Type: {project['product_type']}")
        print(f"  Product Details: {project['product_details']}")
        print()

# Delete a project by index
def delete_project(index):
    data = load_data()
    if index < 1 or index > len(data["projects"]):
        print("Invalid project index.")
        return

    deleted_project = data["projects"].pop(index - 1)
    save_data(data)
    print(f"Deleted project for client: {deleted_project['client_name']}")

# Main menu
def main():
    initialize_data()

    while True:
        print("\nProject Management System")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Delete Project")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            client_name = input("Enter client name: ")
            client_contact = input("Enter client contact: ")
            product_type = input("Enter product type (Glass/Aluminum/PVC): ")
            product_details = input("Enter product details: ")
            add_project(client_name, client_contact, product_type, product_details)
        elif choice == "2":
            list_projects()
        elif choice == "3":
            try:
                index = int(input("Enter project index to delete: "))
                delete_project(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
