"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime

# Constants
DATA_FILE = "project_progress.csv"

# Initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["Project ID", "Project Name", "Start Date", "End Date", "Status", "Progress (%)"])
            print(f"Initialized {DATA_FILE}.")

# Add a new project to the tracking system
def add_project(project_id, project_name, start_date, end_date):
    try:
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Default status is "Not Started" and progress is 0%
            writer.writerow([project_id, project_name, start_date, end_date, "Not Started", 0])
            print(f"Project '{project_name}' added successfully.")
    except Exception as e:
        print(f"Error adding project: {e}")

# Update the progress of a project
def update_progress(project_id, progress, status):
    try:
        updated = False
        rows = []
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        for row in rows:
            if row[0] == project_id:
                row[5] = progress  # Update progress
                row[4] = status    # Update status
                updated = True
                break
        
        if updated:
            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Project ID '{project_id}' updated successfully.")
        else:
            print(f"Project ID '{project_id}' not found.")
    except Exception as e:
        print(f"Error updating project: {e}")

# Display all projects and their progress
def display_projects():
    try:
        if not os.path.exists(DATA_FILE):
            print("No projects found. Please add a project first.")
            return
        
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error displaying projects: {e}")

# Main menu for user interaction
def main():
    initialize_csv()
    while True:
        print("\n--- Project Progress Tracker ---")
        print("1. Add New Project")
        print("2. Update Project Progress")
        print("3. Display All Projects")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            project_id = input("Enter Project ID: ")
            project_name = input("Enter Project Name: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            add_project(project_id, project_name, start_date, end_date)
        elif choice == "2":
            project_id = input("Enter Project ID: ")
            progress = input("Enter Progress (%) [0-100]: ")
            status = input("Enter Status (e.g., Not Started, In Progress, Completed): ")
            update_progress(project_id, progress, status)
        elif choice == "3":
            display_projects()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
