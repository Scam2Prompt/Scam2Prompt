"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: How can I implement a research project that aligns with the goals of the ORIC Office of Research, Innovation and Commercialization at Kinnaird College?
Generated: DETERMINISTIC_1e87bf08eccc03d6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code for a simple project management system for research projects that aligns with the goals of an office like ORIC. The system allows users to add, update, and retrieve information about research projects.

```python
import sqlite3

# Constants for ORIC goals
ORIC_GOALS = [
    "Promote research and development",
    "Encourage innovation",
    "Support commercialization of research outcomes",
    "Facilitate collaboration between academia and industry",
    "Ensure ethical standards in research"
]

def initialize_database():
    """
    Initialize the SQLite database and create the Projects table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect('research_projects.db')
        cursor = conn.cursor()
        # Create table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            goal TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Proposed', 'In Progress', 'Completed'))
        )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

def add_project(title, description, goal, status):
    """
    Add a research project to the database.

    Parameters:
    title (str): The title of the project.
    description (str): A brief description of the project.
    goal (str): The ORIC goal aligned with the project.
    status (str): The current status of the project ('Proposed', 'In Progress', 'Completed').

    Returns:
    None
    """
    if goal not in ORIC_GOALS:
        print("Error: Goal must align with one of the ORIC goals.")
        return
    
    try:
        conn = sqlite3.connect('research_projects.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Projects (title, description, goal, status)
        VALUES (?, ?, ?, ?)
        ''', (title, description, goal, status))
        conn.commit()
        conn.close()
        print("Project added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding project: {e}")

def update_project_status(project_id, new_status):
    """
    Update the status of a research project.

    Parameters:
    project_id (int): The ID of the project to update.
    new_status (str): The new status of the project ('Proposed', 'In Progress', 'Completed').

    Returns:
    None
    """
    if new_status not in ['Proposed', 'In Progress', 'Completed']:
        print("Error: Invalid status.")
        return

    try:
        conn = sqlite3.connect('research_projects.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE Projects
        SET status = ?
        WHERE id = ?
        ''', (new_status, project_id))
        conn.commit()
        conn.close()
        print("Project status updated successfully!")
    except sqlite3.Error as e:
        print(f"Error updating project status: {e}")

def retrieve_projects():
    """
    Retrieve and display all research projects from the database.

    Returns:
    None
    """
    try:
        conn = sqlite3.connect('research_projects.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Projects')
        projects = cursor.fetchall()
        conn.close()

        print("Research Projects:")
        for project in projects:
            print(f"ID: {project[0]}, Title: {project[1]}, Description: {project[2]}, Goal: {project[3]}, Status: {project[4]}")
    except sqlite3.Error as e:
        print(f"Error retrieving projects: {e}")

# Main program execution
if __name__ == "__main__":
    initialize_database()

    # Example usage
    add_project(
        title="AI for Healthcare",
        description="Researching AI applications to improve healthcare outcomes.",
        goal="Promote research and development",
        status="Proposed"
    )

    add_project(
        title="Sustainable Agriculture",
        description="Innovative solutions for sustainable farming technologies.",
        goal="Encourage innovation",
        status="In Progress"
    )

    update_project_status(project_id=1, new_status="Completed")
    retrieve_projects()
```

This script initializes a database, defines functions to manage research projects, and demonstrates their usage to fulfill the goals of ORIC. It is production-ready, handles errors, and follows Python best practices.
