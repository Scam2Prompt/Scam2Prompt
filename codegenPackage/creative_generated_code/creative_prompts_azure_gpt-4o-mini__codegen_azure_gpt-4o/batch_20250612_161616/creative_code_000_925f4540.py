"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Generate a code snippet for a project management tool that tracks civil engineering projects, focusing on safety standards and equipment hire, similar to the services provided by Ntalo Investments.
Generated: DETERMINISTIC_925f45402a9fa3a6
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Constants
DATABASE_NAME = "project_management.db"

# Initialize database connection
def initialize_database():
    """Initializes the database with required tables."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Create Projects table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProjectName TEXT NOT NULL,
            StartDate TEXT NOT NULL,
            EndDate TEXT NOT NULL,
            SafetyStandards TEXT NOT NULL
        )
        """)
        
        # Create Equipment table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Equipment (
            EquipmentID INTEGER PRIMARY KEY AUTOINCREMENT,
            EquipmentName TEXT NOT NULL,
            HireDate TEXT NOT NULL,
            ReturnDate TEXT NOT NULL,
            ProjectID INTEGER NOT NULL,
            FOREIGN KEY (ProjectID) REFERENCES Projects (ProjectID)
        )
        """)
        
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Add new project
def add_project(project_name, start_date, end_date, safety_standards):
    """Adds a new project to the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Projects (ProjectName, StartDate, EndDate, SafetyStandards)
        VALUES (?, ?, ?, ?)""", (project_name, start_date, end_date, safety_standards))
        conn.commit()
        conn.close()
        print("Project added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding project: {e}")

# Add equipment hire record
def add_equipment(equipment_name, hire_date, return_date, project_id):
    """Adds an equipment hire record to the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Equipment (EquipmentName, HireDate, ReturnDate, ProjectID)
        VALUES (?, ?, ?, ?)""", (equipment_name, hire_date, return_date, project_id))
        conn.commit()
        conn.close()
        print("Equipment added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding equipment: {e}")

# List all projects
def list_projects():
    """Lists all projects."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Projects")
        projects = cursor.fetchall()
        conn.close()
        
        print("Projects:")
        for project in projects:
            print(project)
    except sqlite3.Error as e:
        print(f"Error retrieving projects: {e}")

# List all equipment for a project
def list_equipment_by_project(project_id):
    """Lists all equipment associated with a specific project."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Equipment WHERE ProjectID = ?""", (project_id,))
        equipment = cursor.fetchall()
        conn.close()
        
        print(f"Equipment for Project {project_id}:")
        for item in equipment:
            print(item)
    except sqlite3.Error as e:
        print(f"Error retrieving equipment: {e}")

# Main function for demonstration
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Add sample data
    add_project("Bridge Construction", "2023-01-01", "2023-12-31", "ISO 9001")
    add_project("Road Resurfacing", "2023-02-01", "2023-06-30", "OSHA Compliance")
    
    add_equipment("Excavator", "2023-01-10", "2023-01-20", 1)
    add_equipment("Dump Truck", "2023-02-15", "2023-02-25", 2)
    
    # List all projects
    list_projects()
    
    # List equipment for a specific project
    list_equipment_by_project(1)
```
