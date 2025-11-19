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
import sqlite3
from typing import List, Dict, Optional

class CarpentryProjectManager:
    """A class to manage carpentry projects in a SQLite database."""

    def __init__(self, db_name: str = "carpentry_projects.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create the database and tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    client_name TEXT NOT NULL,
                    start_date TEXT,
                    end_date TEXT,
                    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delivered')),
                    total_cost REAL
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS materials (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    material_type TEXT CHECK(material_type IN ('aluminum', 'iron', 'glass', 'other')) NOT NULL,
                    quantity REAL NOT NULL,
                    unit_cost REAL NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            if self.conn:
                self.conn.rollback()
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def add_project(
        self,
        name: str,
        client_name: str,
        description: str = "",
        start_date: str = None,
        end_date: str = None,
        status: str = "pending",
        total_cost: float = 0.0
    ) -> int:
        """Add a new project to the database.
        
        Args:
            name: Name of the project.
            client_name: Name of the client.
            description: Description of the project.
            start_date: Start date in YYYY-MM-DD format.
            end_date: End date in YYYY-MM-DD format.
            status: Project status (pending, in_progress, completed, delivered).
            total_cost: Total cost of the project.
            
        Returns:
            The ID of the newly created project.
        """
        try:
            self.cursor.execute("""
                INSERT INTO projects (
                    name, description, client_name, start_date, end_date, status, total_cost
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, client_name, start_date, end_date, status, total_cost))
            
            project_id = self.cursor.lastrowid
            self.conn.commit()
            return project_id
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def add_material(
        self,
        project_id: int,
        material_type: str,
        quantity: float,
        unit_cost: float
    ) -> int:
        """Add material to a project.
        
        Args:
            project_id: ID of the project.
            material_type: Type of material (aluminum, iron, glass, other).
            quantity: Quantity of material.
            unit_cost: Cost per unit of material.
            
        Returns:
            The ID of the newly created material record.
        """
        try:
            self.cursor.execute("""
                INSERT INTO materials (
                    project_id, material_type, quantity, unit_cost
                ) VALUES (?, ?, ?, ?)
            """, (project_id, material_type, quantity, unit_cost))
            
            material_id = self.cursor.lastrowid
            self._update_project_cost(project_id)
            self.conn.commit()
            return material_id
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def _update_project_cost(self, project_id: int) -> None:
        """Update the total cost of a project based on its materials."""
        try:
            self.cursor.execute("""
                SELECT SUM(quantity * unit_cost) 
                FROM materials 
                WHERE project_id = ?
            """, (project_id,))
            
            total_cost = self.cursor.fetchone()[0] or 0.0
            
            self.cursor.execute("""
                UPDATE projects 
                SET total_cost = ? 
                WHERE id = ?
            """, (total_cost, project_id))
            
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise

    def get_project(self, project_id: int) -> Optional[Dict]:
        """Retrieve a project by its ID.
        
        Args:
            project_id: ID of the project to retrieve.
            
        Returns:
            A dictionary containing project details, or None if not found.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM projects WHERE id = ?
            """, (project_id,))
            
            project = self.cursor.fetchone()
            if not project:
                return None
                
            columns = [desc[0] for desc in self.cursor.description]
            project_dict = dict(zip(columns, project))
            
            self.cursor.execute("""
                SELECT * FROM materials WHERE project_id = ?
            """, (project_id,))
            
            materials = self.cursor.fetchall()
            if materials:
                material_columns = [desc[0] for desc in self.cursor.description]
                project_dict['materials'] = [
                    dict(zip(material_columns, material)) 
                    for material in materials
                ]
            else:
                project_dict['materials'] = []
                
            return project_dict
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def get_all_projects(self) -> List[Dict]:
        """Retrieve all projects from the database.
        
        Returns:
            A list of dictionaries containing all projects and their materials.
        """
        try:
            self.cursor.execute("SELECT id FROM projects")
            project_ids = [row[0] for row in self.cursor.fetchall()]
            return [self.get_project(pid) for pid in project_ids]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def update_project(
        self,
        project_id: int,
        name: str = None,
        client_name: str = None,
        description: str = None,
        start_date: str = None,
        end_date: str = None,
        status: str = None,
        total_cost: float = None
    ) -> bool:
        """Update project details.
        
        Args:
            project_id: ID of the project to update.
            name: New project name.
            client_name: New client name.
            description: New description.
            start_date: New start date.
            end_date: New end date.
            status: New status.
            total_cost: New total cost.
            
        Returns:
            True if the update was successful, False otherwise.
        """
        try:
            updates = []
            params = []
            
            if name is not None:
                updates.append("name = ?")
                params.append(name)
            if client_name is not None:
                updates.append("client_name = ?")
                params.append(client_name)
            if description is not None:
                updates.append("description = ?")
                params.append(description)
            if start_date is not None:
                updates.append("start_date = ?")
                params.append(start_date)
            if end_date is not None:
                updates.append("end_date = ?")
                params.append(end_date)
            if status is not None:
                updates.append("status = ?")
                params.append(status)
            if total_cost is not None:
                updates.append("total_cost = ?")
                params.append(total_cost)
                
            if not updates:
                return False
                
            query = f"UPDATE projects SET {', '.join(updates)} WHERE id = ?"
            params.append(project_id)
            
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def delete_project(self, project_id: int) -> bool:
        """Delete a project and all its associated materials.
        
        Args:
            project_id: ID of the project to delete.
            
        Returns:
            True if the deletion was successful, False otherwise.
        """
        try:
            self.cursor.execute("DELETE FROM projects WHERE id = ?
