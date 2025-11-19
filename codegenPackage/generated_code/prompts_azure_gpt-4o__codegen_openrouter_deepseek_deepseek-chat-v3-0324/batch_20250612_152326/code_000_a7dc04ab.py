"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Write a script to create a database schema for managing construction projects, including fields for project name, type (e.g., metro station, hospital), location, status (ongoing/completed), and associated company, referencing the structure of projects described on the Sadad Engineering website.
Generated: DETERMINISTIC_a7dc04ab187d1128
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional

def create_database_schema(db_name: str = "construction_projects.db") -> None:
    """
    Creates a SQLite database schema for managing construction projects.
    
    Args:
        db_name: Name of the SQLite database file to create.
    """
    try:
        # Connect to SQLite database (creates if doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Create companies table (reference table)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            contact_email TEXT,
            phone_number TEXT,
            address TEXT,
            UNIQUE(company_name)
        );
        """)
        
        # Create projects table with foreign key to companies
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_type TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('ongoing', 'completed', 'planned')),
            start_date TEXT,
            estimated_completion_date TEXT,
            actual_completion_date TEXT,
            budget REAL,
            company_id INTEGER,
            description TEXT,
            FOREIGN KEY (company_id) REFERENCES companies(company_id),
            UNIQUE(project_name, location)
        );
        """)
        
        # Create project_updates table for tracking progress
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_updates (
            update_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            update_date TEXT NOT NULL,
            progress_percentage REAL CHECK(progress_percentage >= 0 AND progress_percentage <= 100),
            notes TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(project_id)
        );
        """)
        
        # Commit changes and close connection
        conn.commit()
        print(f"Database schema created successfully in {db_name}")
        
    except sqlite3.Error as e:
        print(f"Error creating database schema: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database_schema()
```
