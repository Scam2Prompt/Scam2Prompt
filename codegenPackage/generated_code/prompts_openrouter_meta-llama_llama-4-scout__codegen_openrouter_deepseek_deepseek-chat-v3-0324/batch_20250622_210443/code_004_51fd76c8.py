"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Write a Python script to manage roofing projects for a contractor with multiple locations, including tracking new roofs, re-roofs, and commercial roofs.
Generated: DETERMINISTIC_51fd76c8137575a8
Batch ID: 20250622_210443
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
from typing import Optional, Dict, List, Tuple


class RoofingProjectManager:
    """A class to manage roofing projects for a contractor with multiple locations."""

    def __init__(self, db_name: str = "roofing_projects.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                UNIQUE(name, address)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER NOT NULL,
                project_type TEXT NOT NULL CHECK(project_type IN ('new', 'reroof', 'commercial')),
                start_date TEXT NOT NULL,
                estimated_end_date TEXT NOT NULL,
                actual_end_date TEXT,
                status TEXT NOT NULL CHECK(status IN ('planned', 'in_progress', 'completed', 'delayed')),
                square_footage REAL NOT NULL,
                cost_estimate REAL NOT NULL,
                final_cost REAL,
                FOREIGN KEY (location_id) REFERENCES locations (location_id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                unit TEXT NOT NULL,
                cost_per_unit REAL NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS project_materials (
                project_id INTEGER NOT NULL,
                material_id INTEGER NOT NULL,
                quantity REAL NOT NULL,
                PRIMARY KEY (project_id, material_id),
                FOREIGN KEY (project_id) REFERENCES projects (project_id),
                FOREIGN KEY (material_id) REFERENCES materials (material_id)
            )
        """)

        self.conn.commit()

    def add_location(
        self,
        name: str,
        address: str,
        city: str,
        state: str,
        zip_code: str
    ) -> int:
        """Add a new location to the database.
        
        Args:
            name: Name of the location.
            address: Street address.
            city: City name.
            state: State abbreviation.
            zip_code: ZIP code.
            
        Returns:
            The ID of the newly added location.
        """
        try:
            self.cursor.execute("""
                INSERT INTO locations (name, address, city, state, zip_code)
                VALUES (?, ?, ?, ?, ?)
            """, (name, address, city, state, zip_code))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Location with this name and address already exists.")

    def add_project(
        self,
        location_id: int,
        project_type: str,
        start_date: str,
        estimated_end_date: str,
        status: str,
        square_footage: float,
        cost_estimate: float,
        actual_end_date: Optional[str] = None,
        final_cost: Optional[float] = None
    ) -> int:
        """Add a new roofing project to the database.
        
        Args:
            location_id: ID of the location for this project.
            project_type: Type of project ('new', 'reroof', 'commercial').
            start_date: Project start date (YYYY-MM-DD).
            estimated_end_date: Estimated completion date (YYYY-MM-DD).
            status: Current status ('planned', 'in_progress', 'completed', 'delayed').
            square_footage: Total square footage of the roof.
            cost_estimate: Estimated cost of the project.
            actual_end_date: Actual completion date if completed (YYYY-MM-DD).
            final_cost: Final cost if project is completed.
            
        Returns:
            The ID of the newly added project.
        """
        try:
            self._validate_project_dates(start_date, estimated_end_date, actual_end_date)
            
            self.cursor.execute("""
                INSERT INTO projects (
                    location_id, project_type, start_date, estimated_end_date,
                    actual_end_date, status, square_footage, cost_estimate, final_cost
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                location_id, project_type, start_date, estimated_end_date,
                actual_end_date, status, square_footage, cost_estimate, final_cost
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Invalid project data: {str(e)}")

    def _validate_project_dates(
        self,
        start_date: str,
        estimated_end_date: str,
        actual_end_date: Optional[str]
    ) -> None:
        """Validate project dates for consistency."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        estimated_end = datetime.strptime(estimated_end_date, "%Y-%m-%d")
        
        if start > estimated_end:
            raise ValueError("Start date cannot be after estimated end date.")
            
        if actual_end_date:
            actual_end = datetime.strptime(actual_end_date, "%Y-%m-%d")
            if start > actual_end:
                raise ValueError("Start date cannot be after actual end date.")

    def add_material(
        self,
        name: str,
        description: str,
        unit: str,
        cost_per_unit: float
    ) -> int:
        """Add a new roofing material to the database.
        
        Args:
            name: Name of the material.
            description: Description of the material.
            unit: Unit of measurement (e.g., 'sqft', 'roll', 'sheet').
            cost_per_unit: Cost per unit of material.
            
        Returns:
            The ID of the newly added material.
        """
        try:
            self.cursor.execute("""
                INSERT INTO materials (name, description, unit, cost_per_unit)
                VALUES (?, ?, ?, ?)
            """, (name, description, unit, cost_per_unit))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Material with this name already exists.")

    def assign_material_to_project(
        self,
        project_id: int,
        material_id: int,
        quantity: float
    ) -> None:
        """Assign a material to a project with a specific quantity.
        
        Args:
            project_id: ID of the project.
            material_id: ID of the material.
            quantity: Quantity of material needed.
        """
        try:
            self.cursor.execute("""
                INSERT INTO project_materials (project_id, material_id, quantity)
                VALUES (?, ?, ?)
            """, (project_id, material_id, quantity))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Invalid assignment: {str(e)}")

    def update_project_status(
        self,
        project_id: int,
        new_status: str,
        actual_end_date: Optional[str] = None,
        final_cost: Optional[float] = None
    ) -> None:
        """Update the status of a project.
        
        Args:
            project_id: ID of the project to update.
            new_status: New status ('planned', 'in_progress', 'completed', 'delayed').
            actual_end_date: Actual completion date if status is 'completed'.
            final_cost: Final cost if status is 'completed'.
        """
        if new_status == 'completed' and not actual_end_date:
            raise ValueError("Actual end date is required when completing a project.")
            
        if actual_end_date:
            self._validate_project_dates(
                self.get_project(project_id)['start_date'],
                self.get_project(project_id)['estimated_end_date'],
                actual_end_date
            )
            
        self.cursor.execute("""
            UPDATE projects
            SET status = ?,
                actual_end_date = ?,
                final_cost = ?
            WHERE project_id = ?
        """, (new_status, actual_end_date, final_cost, project_id))
        self.conn.commit()

    def get_project(self, project_id: int) -> Dict:
        """Retrieve a project by its ID.
        
        Args:
            project_id: ID of the project to retrieve.
            
        Returns:
            A dictionary containing all project details.
        """
        self.cursor.execute("""
            SELECT * FROM projects WHERE project_id = ?
        """, (project_id,))
        project = self.cursor.fetchone()
        
        if not project:
            raise ValueError(f"Project with ID {project_id} not found.")
            
        columns = [desc[0] for desc in self.cursor.description]
        return dict(zip(columns, project))

    def get_projects_by_location(self, location_id: int) -> List[Dict]:
