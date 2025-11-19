"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Design a simple database schema to store information about brick and stone restoration projects, including client details, project scope, and service types like tuckpointing and remedial wall tie replacement."
Generated: DETERMINISTIC_21e239799bb80a78
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

def create_database_schema(db_path='restoration_projects.db'):
    """
    Creates a SQLite database schema for brick and stone restoration projects.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create clients table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Create service_types table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS service_types (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            cost_per_unit REAL,
            unit TEXT
        )
        ''')

        # Create projects table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            start_date DATE,
            estimated_end_date DATE,
            status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'cancelled')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(client_id)
        )
        ''')

        # Create project_services junction table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_services (
            project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            quantity REAL,
            notes TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(project_id),
            FOREIGN KEY (service_id) REFERENCES service_types(service_id)
        )
        ''')

        # Create materials table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS materials (
            material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            unit_cost REAL,
            unit TEXT
        )
        ''')

        # Create project_materials junction table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_materials (
            project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            material_id INTEGER NOT NULL,
            quantity REAL,
            notes TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(project_id),
            FOREIGN KEY (material_id) REFERENCES materials(material_id)
        )
        ''')

        # Create project_updates table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_updates (
            update_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            update_text TEXT NOT NULL,
            update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(project_id)
        )
        ''')

        # Insert common service types
        cursor.executemany('''
        INSERT OR IGNORE INTO service_types (name, description, cost_per_unit, unit)
        VALUES (?, ?, ?, ?)
        ''', [
            ('Tuckpointing', 'Repairing mortar joints between bricks or stones', 5.50, 'linear foot'),
            ('Remedial Wall Tie Replacement', 'Replacing corroded or damaged wall ties', 12.75, 'each'),
            ('Brick Replacement', 'Removing and replacing damaged bricks', 8.25, 'brick'),
            ('Stone Restoration', 'Cleaning and repairing natural stone surfaces', 15.00, 'square foot'),
            ('Chimney Repair', 'Repairing or rebuilding chimney structures', 0.00, 'project')
        ])

        conn.commit()
        print("Database schema created successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database_schema()
```
