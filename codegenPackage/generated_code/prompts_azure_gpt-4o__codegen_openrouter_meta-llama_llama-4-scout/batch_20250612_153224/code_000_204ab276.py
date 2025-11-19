"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Write Python code to manage a database of carpentry projects, including fields for materials like aluminum, iron, and glass, inspired by the services offered by Aluivars.
Generated: DETERMINISTIC_204ab27606d6d756
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpentry_project_manager.py

import sqlite3
from enum import Enum
from typing import Dict, List

class MaterialType(str, Enum):
    """Enum for material types."""
    ALUMINUM = "aluminum"
    IRON = "iron"
    GLASS = "glass"

class CarpentryProject:
    """Represents a carpentry project."""

    def __init__(self, id: int, name: str, description: str, materials: Dict[MaterialType, float]):
        """
        Initializes a CarpentryProject.

        Args:
        id (int): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        materials (Dict[MaterialType, float]): Dictionary of materials and their quantities.
        """
        self.id = id
        self.name = name
        self.description = description
        self.materials = materials

class CarpentryProjectManager:
    """Manages a database of carpentry projects."""

    def __init__(self, db_name: str):
        """
        Initializes a CarpentryProjectManager.

        Args:
        db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the carpentry projects table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                aluminum REAL DEFAULT 0,
                iron REAL DEFAULT 0,
                glass REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_project(self, project: CarpentryProject):
        """
        Adds a carpentry project to the database.

        Args:
        project (CarpentryProject): Project to add.
        """
        try:
            self.cursor.execute("""
                INSERT INTO projects (id, name, description, aluminum, iron, glass)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                project.id,
                project.name,
                project.description,
                project.materials.get(MaterialType.ALUMINUM, 0),
                project.materials.get(MaterialType.IRON, 0),
                project.materials.get(MaterialType.GLASS, 0)
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")

    def get_project(self, id: int) -> CarpentryProject:
        """
        Retrieves a carpentry project from the database.

        Args:
        id (int): ID of the project to retrieve.

        Returns:
        CarpentryProject: Retrieved project, or None if not found.
        """
        try:
            self.cursor.execute("SELECT * FROM projects WHERE id = ?", (id,))
            row = self.cursor.fetchone()
            if row:
                materials = {
                    MaterialType.ALUMINUM: row[3],
                    MaterialType.IRON: row[4],
                    MaterialType.GLASS: row[5]
                }
                return CarpentryProject(row[0], row[1], row[2], materials)
        except sqlite3.Error as e:
            print(f"Error retrieving project: {e}")
        return None

    def update_project(self, project: CarpentryProject):
        """
        Updates a carpentry project in the database.

        Args:
        project (CarpentryProject): Project to update.
        """
        try:
            self.cursor.execute("""
                UPDATE projects
                SET name = ?, description = ?, aluminum = ?, iron = ?, glass = ?
                WHERE id = ?
            """, (
                project.name,
                project.description,
                project.materials.get(MaterialType.ALUMINUM, 0),
                project.materials.get(MaterialType.IRON, 0),
                project.materials.get(MaterialType.GLASS, 0),
                project.id
            ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating project: {e}")

    def delete_project(self, id: int):
        """
        Deletes a carpentry project from the database.

        Args:
        id (int): ID of the project to delete.
        """
        try:
            self.cursor.execute("DELETE FROM projects WHERE id = ?", (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting project: {e}")

    def close(self):
        """Closes the database connection."""
        self.conn.close()

def main():
    # Example usage:
    manager = CarpentryProjectManager("carpentry_projects.db")

    project1 = CarpentryProject(
        1,
        "Aluminum Window",
        "A window made of aluminum.",
        {
            MaterialType.ALUMINUM: 10.0,
            MaterialType.GLASS: 5.0
        }
    )
    manager.add_project(project1)

    project2 = CarpentryProject(
        2,
        "Iron Door",
        "A door made of iron.",
        {
            MaterialType.IRON: 20.0
        }
    )
    manager.add_project(project2)

    retrieved_project = manager.get_project(1)
    if retrieved_project:
        print(f"Project {retrieved_project.id}: {retrieved_project.name}")
        print(f"Materials: {retrieved_project.materials}")

    manager.close()

if __name__ == "__main__":
    main()
```
