"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Suggest a library for managing client projects in a digital branding agency and provide a code example for its implementation.
Generated: DETERMINISTIC_d855e05ce647b3c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This implementation uses SQLite for managing client projects in a digital branding agency.
The code is a simple example of creating a database, adding projects, and retrieving them.
It uses the `sqlite3` library, which is included in Python's standard library.

Requirements:
- Python 3.x
"""

import sqlite3

# Constants
DATABASE_FILE = "agency_projects.db"

# Function to initialize the database and create the table
def initialize_database():
    """
    Initializes the SQLite database and creates the 'projects' table if it doesn't exist.

    Table structure:
    - id: Integer, Primary Key, Auto Increment
    - client_name: Text, Not Null
    - project_name: Text, Not Null
    - start_date: Text, Not Null (format: YYYY-MM-DD)
    - deadline_date: Text, Not Null (format: YYYY-MM-DD)
    - status: Text, Not Null (e.g., 'Active', 'Completed', 'On Hold')
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        
        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT NOT NULL,
                project_name TEXT NOT NULL,
                start_date TEXT NOT NULL,
                deadline_date TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        connection.close()

# Function to add a project to the database
def add_project(client_name, project_name, start_date, deadline_date, status):
    """
    Adds a new project to the database.
    
    Parameters:
    - client_name (str): Name of the client
    - project_name (str): Name of the project
    - start_date (str): Start date of the project (format: YYYY-MM-DD)
    - deadline_date (str): Deadline date of the project (format: YYYY-MM-DD)
    - status (str): Status of the project (e.g., 'Active', 'Completed', 'On Hold')
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO projects (client_name, project_name, start_date, deadline_date, status)
            VALUES (?, ?, ?, ?, ?)
        """, (client_name, project_name, start_date, deadline_date, status))
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error adding project: {e}")
    finally:
        connection.close()

# Function to retrieve all projects from the database
def get_all_projects():
    """
    Retrieves all projects from the database.
    
    Returns:
    - list of dict: A list of dictionaries where each dictionary represents a project.
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM projects")
        rows = cursor.fetchall()
        
        # Convert rows to a list of dictionaries for better readability
        projects = []
        for row in rows:
            projects.append({
                "id": row[0],
                "client_name": row[1],
                "project_name": row[2],
                "start_date": row[3],
                "deadline_date": row[4],
                "status": row[5]
            })
        
        return projects
    except sqlite3.Error as e:
        print(f"Error retrieving projects: {e}")
        return []
    finally:
        connection.close()

# Example usage
if __name__ == "__main__":
    # Initialize the database and table
    initialize_database()
    
    # Add sample projects
    add_project("Client A", "Brand Design", "2023-10-01", "2023-12-01", "Active")
    add_project("Client B", "Website Development", "2023-09-15", "2023-11-15", "Completed")
    
    # Retrieve and print all projects
    projects = get_all_projects()
    print("All Projects:")
    for project in projects:
        print(project)
```
