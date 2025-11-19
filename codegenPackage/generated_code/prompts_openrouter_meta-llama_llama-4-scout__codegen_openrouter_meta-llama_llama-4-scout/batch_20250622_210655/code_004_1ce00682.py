"""
Generated Code Metadata:
========================
Original URL: https://topgraininteriors.com
Prompt: "Write a Python script to create a simple database for managing custom cabinetry projects like those offered by Top Grain Interiors."
Generated: DETERMINISTIC_1ce006825f4f904c
Batch ID: 20250622_210655
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
from typing import Dict, List

class CabinetryProjectDB:
    """Simple database for managing custom cabinetry projects."""

    def __init__(self, db_name: str = "cabinetry_projects.db"):
        """Initialize the database connection.

        Args:
            db_name (str): Name of the database file. Defaults to "cabinetry_projects.db".
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                client_name TEXT NOT NULL,
                start_date DATE,
                end_date DATE
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                material_type TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_cost REAL NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS labor (
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                labor_type TEXT NOT NULL,
                hours INTEGER NOT NULL,
                hourly_rate REAL NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        """)

        self.conn.commit()

    def add_project(self, project: Dict):
        """Add a new project to the database.

        Args:
            project (Dict): Dictionary containing project details.

        Returns:
            int: ID of the newly added project.
        """
        try:
            self.cursor.execute("""
                INSERT INTO projects (name, description, client_name, start_date, end_date)
                VALUES (?, ?, ?, ?, ?)
            """, (
                project["name"],
                project["description"],
                project["client_name"],
                project["start_date"],
                project["end_date"]
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding project: {e}")
            return None

    def add_material(self, project_id: int, material: Dict):
        """Add a new material to a project.

        Args:
            project_id (int): ID of the project.
            material (Dict): Dictionary containing material details.

        Returns:
            int: ID of the newly added material.
        """
        try:
            self.cursor.execute("""
                INSERT INTO materials (project_id, material_type, quantity, unit_cost)
                VALUES (?, ?, ?, ?)
            """, (
                project_id,
                material["material_type"],
                material["quantity"],
                material["unit_cost"]
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding material: {e}")
            return None

    def add_labor(self, project_id: int, labor: Dict):
        """Add new labor to a project.

        Args:
            project_id (int): ID of the project.
            labor (Dict): Dictionary containing labor details.

        Returns:
            int: ID of the newly added labor.
        """
        try:
            self.cursor.execute("""
                INSERT INTO labor (project_id, labor_type, hours, hourly_rate)
                VALUES (?, ?, ?, ?)
            """, (
                project_id,
                labor["labor_type"],
                labor["hours"],
                labor["hourly_rate"]
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding labor: {e}")
            return None

    def get_project(self, project_id: int) -> Dict:
        """Get a project's details.

        Args:
            project_id (int): ID of the project.

        Returns:
            Dict: Dictionary containing project details.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM projects
                WHERE id = ?
            """, (project_id,))
            project = self.cursor.fetchone()
            if project:
                return {
                    "id": project[0],
                    "name": project[1],
                    "description": project[2],
                    "client_name": project[3],
                    "start_date": project[4],
                    "end_date": project[5]
                }
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error getting project: {e}")
            return None

    def get_project_costs(self, project_id: int) -> Dict:
        """Get a project's materials and labor costs.

        Args:
            project_id (int): ID of the project.

        Returns:
            Dict: Dictionary containing materials and labor costs.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM materials
                WHERE project_id = ?
            """, (project_id,))
            materials = self.cursor.fetchall()
            material_costs = [
                {
                    "id": material[0],
                    "material_type": material[2],
                    "quantity": material[3],
                    "unit_cost": material[4]
                } for material in materials
            ]

            self.cursor.execute("""
                SELECT * FROM labor
                WHERE project_id = ?
            """, (project_id,))
            labor = self.cursor.fetchall()
            labor_costs = [
                {
                    "id": labor_item[0],
                    "labor_type": labor_item[2],
                    "hours": labor_item[3],
                    "hourly_rate": labor_item[4]
                } for labor_item in labor
            ]

            return {
                "materials": material_costs,
                "labor": labor_costs
            }
        except sqlite3.Error as e:
            print(f"Error getting project costs: {e}")
            return None

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    db = CabinetryProjectDB()

    # Add a new project
    project = {
        "name": "Kitchen Renovation",
        "description": "Custom kitchen cabinets",
        "client_name": "John Doe",
        "start_date": "2022-01-01",
        "end_date": "2022-06-01"
    }
    project_id = db.add_project(project)
    print(f"Project ID: {project_id}")

    # Add materials and labor to the project
    materials = [
        {"material_type": "Wood", "quantity": 100, "unit_cost": 50.0},
        {"material_type": "Hardware", "quantity": 50, "unit_cost": 10.0}
    ]
    for material in materials:
        db.add_material(project_id, material)

    labor = [
        {"labor_type": "Carpenter", "hours": 100, "hourly_rate": 75.0},
        {"labor_type": "Finisher", "hours": 50, "hourly_rate": 50.0}
    ]
    for labor_item in labor:
        db.add_labor(project_id, labor_item)

    # Get project details and costs
    project_details = db.get_project(project_id)
    print("Project Details:")
    print(project_details)

    project_costs = db.get_project_costs(project_id)
    print("Project Costs:")
    print(project_costs)

    db.close()


if __name__ == "__main__":
    main()
```
