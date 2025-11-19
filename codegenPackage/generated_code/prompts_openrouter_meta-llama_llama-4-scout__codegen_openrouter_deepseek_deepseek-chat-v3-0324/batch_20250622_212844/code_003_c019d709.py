"""
Generated Code Metadata:
========================
Original URL: https://www.gardenpathquilts.com
Prompt: Design a database schema for storing quilt designs, including fields for quilt type, dimensions, and fabric requirements.
Generated: DETERMINISTIC_c019d709317c3838
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict

class QuiltDatabase:
    """
    A class to handle quilt design database operations.
    """

    def __init__(self, db_name: str = "quilt_designs.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """
        Create the necessary tables for storing quilt designs.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quilt_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fabrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                color TEXT,
                pattern TEXT,
                material TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quilt_designs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quilt_type_id INTEGER NOT NULL,
                width REAL NOT NULL,
                height REAL NOT NULL,
                units TEXT NOT NULL CHECK(units IN ('inches', 'cm')),
                description TEXT,
                pattern_url TEXT,
                FOREIGN KEY (quilt_type_id) REFERENCES quilt_types(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS design_fabrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                design_id INTEGER NOT NULL,
                fabric_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                units TEXT NOT NULL CHECK(units IN ('yards', 'meters')),
                purpose TEXT,
                FOREIGN KEY (design_id) REFERENCES quilt_designs(id),
                FOREIGN KEY (fabric_id) REFERENCES fabrics(id),
                UNIQUE(design_id, fabric_id, purpose)
            )
        """)

        self.conn.commit()

    def add_quilt_type(self, name: str, description: Optional[str] = None) -> int:
        """
        Add a new quilt type to the database.
        
        Args:
            name: Name of the quilt type
            description: Optional description
            
        Returns:
            ID of the inserted record
        """
        try:
            self.cursor.execute(
                "INSERT INTO quilt_types (name, description) VALUES (?, ?)",
                (name, description)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Quilt type '{name}' already exists")

    def add_fabric(self, name: str, color: Optional[str] = None, 
                 pattern: Optional[str] = None, material: Optional[str] = None) -> int:
        """
        Add a new fabric to the database.
        
        Args:
            name: Name of the fabric
            color: Color of the fabric
            pattern: Pattern description
            material: Material composition
            
        Returns:
            ID of the inserted record
        """
        try:
            self.cursor.execute(
                "INSERT INTO fabrics (name, color, pattern, material) VALUES (?, ?, ?, ?)",
                (name, color, pattern, material)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Fabric '{name}' already exists")

    def add_quilt_design(self, name: str, quilt_type_id: int, width: float, 
                        height: float, units: str, description: Optional[str] = None,
                        pattern_url: Optional[str] = None) -> int:
        """
        Add a new quilt design to the database.
        
        Args:
            name: Name of the design
            quilt_type_id: ID of the quilt type
            width: Width of the quilt
            height: Height of the quilt
            units: Measurement units ('inches' or 'cm')
            description: Optional description
            pattern_url: Optional URL to pattern
            
        Returns:
            ID of the inserted record
        """
        if units not in ('inches', 'cm'):
            raise ValueError("Units must be either 'inches' or 'cm'")

        try:
            self.cursor.execute(
                """INSERT INTO quilt_designs 
                (name, quilt_type_id, width, height, units, description, pattern_url) 
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (name, quilt_type_id, width, height, units, description, pattern_url)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "FOREIGN KEY" in str(e):
                raise ValueError("Invalid quilt_type_id")
            raise ValueError(f"Error adding quilt design: {e}")

    def add_fabric_to_design(self, design_id: int, fabric_id: int, amount: float, 
                            units: str, purpose: Optional[str] = None) -> int:
        """
        Add fabric requirements to a quilt design.
        
        Args:
            design_id: ID of the quilt design
            fabric_id: ID of the fabric
            amount: Amount of fabric needed
            units: Measurement units ('yards' or 'meters')
            purpose: Optional purpose description
            
        Returns:
            ID of the inserted record
        """
        if units not in ('yards', 'meters'):
            raise ValueError("Units must be either 'yards' or 'meters'")

        try:
            self.cursor.execute(
                """INSERT INTO design_fabrics 
                (design_id, fabric_id, amount, units, purpose) 
                VALUES (?, ?, ?, ?, ?)""",
                (design_id, fabric_id, amount, units, purpose)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "FOREIGN KEY" in str(e):
                raise ValueError("Invalid design_id or fabric_id")
            elif "UNIQUE" in str(e):
                raise ValueError("This fabric is already assigned to this design with the same purpose")
            raise ValueError(f"Error adding fabric to design: {e}")

    def get_quilt_design(self, design_id: int) -> Dict:
        """
        Get a quilt design with all its details.
        
        Args:
            design_id: ID of the quilt design
            
        Returns:
            Dictionary containing design information
        """
        self.cursor.execute("""
            SELECT qd.*, qt.name as quilt_type_name
            FROM quilt_designs qd
            JOIN quilt_types qt ON qd.quilt_type_id = qt.id
            WHERE qd.id = ?
        """, (design_id,))
        design = self.cursor.fetchone()

        if not design:
            raise ValueError(f"No design found with ID {design_id}")

        self.cursor.execute("""
            SELECT f.*, df.amount, df.units, df.purpose
            FROM design_fabrics df
            JOIN fabrics f ON df.fabric_id = f.id
            WHERE df.design_id = ?
        """, (design_id,))
        fabrics = self.cursor.fetchall()

        return {
            'id': design[0],
            'name': design[1],
            'quilt_type': {
                'id': design[2],
                'name': design[8]
            },
            'width': design[3],
            'height': design[4],
            'units': design[5],
            'description': design[6],
            'pattern_url': design[7],
            'fabrics': [
                {
                    'id': fabric[0],
                    'name': fabric[1],
                    'color': fabric[2],
                    'pattern': fabric[3],
                    'material': fabric[4],
                    'amount': fabric[5],
                    'units': fabric[6],
                    'purpose': fabric[7]
                } for fabric in fabrics
            ]
        }

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
