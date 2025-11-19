"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Write a Python script to create a database schema for storing residential interior design project details, including fields for client preferences, design concepts, and completion timelines, inspired by Zirciulit Design Firm's approach.
Generated: DETERMINISTIC_181ea515652e26cd
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime

# Define database schema
class InteriorDesignDB:
    def __init__(self, db_name):
        """
        Initialize database connection.

        Args:
            db_name (str): Name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create tables for storing residential interior design project details.
        """
        # Create clients table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                address TEXT
            )
        ''')

        # Create design_projects table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS design_projects (
                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                project_name TEXT NOT NULL,
                start_date DATE,
                completion_date DATE,
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        ''')

        # Create client_preferences table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS client_preferences (
                preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                style TEXT,
                color_scheme TEXT,
                furniture_type TEXT,
                FOREIGN KEY (project_id) REFERENCES design_projects (project_id)
            )
        ''')

        # Create design_concepts table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS design_concepts (
                concept_id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                concept_name TEXT NOT NULL,
                description TEXT,
                FOREIGN KEY (project_id) REFERENCES design_projects (project_id)
            )
        ''')

        # Create project_timelines table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS project_timelines (
                timeline_id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                milestone TEXT NOT NULL,
                due_date DATE NOT NULL,
                completion_status TEXT,
                FOREIGN KEY (project_id) REFERENCES design_projects (project_id)
            )
        ''')

        self.conn.commit()

    def insert_client(self, name, email, phone=None, address=None):
        """
        Insert client details into the database.

        Args:
            name (str): Client name.
            email (str): Client email.
            phone (str, optional): Client phone number. Defaults to None.
            address (str, optional): Client address. Defaults to None.

        Returns:
            int: Client ID.
        """
        try:
            self.cursor.execute('''
                INSERT INTO clients (name, email, phone, address)
                VALUES (?, ?, ?, ?)
            ''', (name, email, phone, address))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting client: {e}")
            return None

    def insert_design_project(self, client_id, project_name, start_date=None, completion_date=None):
        """
        Insert design project details into the database.

        Args:
            client_id (int): Client ID.
            project_name (str): Project name.
            start_date (str, optional): Project start date. Defaults to None.
            completion_date (str, optional): Project completion date. Defaults to None.

        Returns:
            int: Project ID.
        """
        try:
            self.cursor.execute('''
                INSERT INTO design_projects (client_id, project_name, start_date, completion_date)
                VALUES (?, ?, ?, ?)
            ''', (client_id, project_name, start_date, completion_date))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting design project: {e}")
            return None

    def insert_client_preferences(self, project_id, style=None, color_scheme=None, furniture_type=None):
        """
        Insert client preferences into the database.

        Args:
            project_id (int): Project ID.
            style (str, optional): Design style. Defaults to None.
            color_scheme (str, optional): Color scheme. Defaults to None.
            furniture_type (str, optional): Furniture type. Defaults to None.

        Returns:
            int: Preference ID.
        """
        try:
            self.cursor.execute('''
                INSERT INTO client_preferences (project_id, style, color_scheme, furniture_type)
                VALUES (?, ?, ?, ?)
            ''', (project_id, style, color_scheme, furniture_type))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting client preferences: {e}")
            return None

    def insert_design_concept(self, project_id, concept_name, description=None):
        """
        Insert design concept into the database.

        Args:
            project_id (int): Project ID.
            concept_name (str): Concept name.
            description (str, optional): Concept description. Defaults to None.

        Returns:
            int: Concept ID.
        """
        try:
            self.cursor.execute('''
                INSERT INTO design_concepts (project_id, concept_name, description)
                VALUES (?, ?, ?)
            ''', (project_id, concept_name, description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting design concept: {e}")
            return None

    def insert_project_timeline(self, project_id, milestone, due_date, completion_status=None):
        """
        Insert project timeline into the database.

        Args:
            project_id (int): Project ID.
            milestone (str): Milestone.
            due_date (str): Due date.
            completion_status (str, optional): Completion status. Defaults to None.

        Returns:
            int: Timeline ID.
        """
        try:
            self.cursor.execute('''
                INSERT INTO project_timelines (project_id, milestone, due_date, completion_status)
                VALUES (?, ?, ?, ?)
            ''', (project_id, milestone, due_date, completion_status))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting project timeline: {e}")
            return None

    def close_connection(self):
        """
        Close database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    db = InteriorDesignDB("interior_design.db")

    # Insert client
    client_id = db.insert_client("John Doe", "john.doe@example.com", "123-456-7890", "123 Main St")

    # Insert design project
    project_id = db.insert_design_project(client_id, "Living Room Renovation")

    # Insert client preferences
    preference_id = db.insert_client_preferences(project_id, "Modern", "Neutral", "Custom")

    # Insert design concept
    concept_id = db.insert_design_concept(project_id, "Concept 1", "Description of concept 1")

    # Insert project timeline
    timeline_id = db.insert_project_timeline(project_id, "Design Concept Finalization", datetime.now().strftime("%Y-%m-%d"))

    db.close_connection()
```
