"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write Python code to filter automotive parts by vehicle type, brand, model, and year, as described on the "autopecasbrazz" website.
Generated: DETERMINISTIC_5e2102260d612c66
Batch ID: 20250612_152000
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

class AutoPartsFilter:
    """
    A class to filter automotive parts based on vehicle type, brand, model, and year.
    """
    
    def __init__(self, db_path: str = 'autoparts.db'):
        """
        Initialize the AutoPartsFilter with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file. Defaults to 'autoparts.db'.
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self):
        """Establish a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise Exception(f"Database connection error: {e}")
            
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            
    def create_tables(self):
        """
        Create necessary tables if they don't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehicle_types (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS brands (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    vehicle_type_id INTEGER,
                    FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(id)
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS models (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    brand_id INTEGER,
                    FOREIGN KEY (brand_id) REFERENCES brands(id),
                    UNIQUE(name, brand_id)
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS years (
                    id INTEGER PRIMARY KEY,
                    year INTEGER NOT NULL,
                    model_id INTEGER,
                    FOREIGN KEY (model_id) REFERENCES models(id),
                    UNIQUE(year, model_id)
                )
            """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS parts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    part_number TEXT,
                    description TEXT,
                    price REAL,
                    year_id INTEGER,
                    FOREIGN KEY (year_id) REFERENCES years(id)
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error creating tables: {e}")
            
    def get_vehicle_types(self) -> List[Dict[str, str]]:
        """
        Retrieve all vehicle types from the database.
        
        Returns:
            List[Dict[str, str]]: List of vehicle types with their IDs and names.
        """
        try:
            self.cursor.execute("SELECT id, name FROM vehicle_types")
            return [{'id': row[0], 'name': row[1]} for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error fetching vehicle types: {e}")
            
    def get_brands(self, vehicle_type_id: int) -> List[Dict[str, str]]:
        """
        Retrieve brands for a specific vehicle type.
        
        Args:
            vehicle_type_id (int): ID of the vehicle type.
            
        Returns:
            List[Dict[str, str]]: List of brands with their IDs and names.
        """
        try:
            self.cursor.execute(
                "SELECT id, name FROM brands WHERE vehicle_type_id = ?",
                (vehicle_type_id,)
            )
            return [{'id': row[0], 'name': row[1]} for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error fetching brands: {e}")
            
    def get_models(self, brand_id: int) -> List[Dict[str, str]]:
        """
        Retrieve models for a specific brand.
        
        Args:
            brand_id (int): ID of the brand.
            
        Returns:
            List[Dict[str, str]]: List of models with their IDs and names.
        """
        try:
            self.cursor.execute(
                "SELECT id, name FROM models WHERE brand_id = ?",
                (brand_id,)
            )
            return [{'id': row[0], 'name': row[1]} for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error fetching models: {e}")
            
    def get_years(self, model_id: int) -> List[Dict[str, int]]:
        """
        Retrieve years for a specific model.
        
        Args:
            model_id (int): ID of the model.
            
        Returns:
            List[Dict[str, int]]: List of years with their IDs and year values.
        """
        try:
            self.cursor.execute(
                "SELECT id, year FROM years WHERE model_id = ?",
                (model_id,)
            )
            return [{'id': row[0], 'year': row[1]} for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error fetching years: {e}")
            
    def get_parts(
        self,
        vehicle_type_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        model_id: Optional[int] = None,
        year_id: Optional[int] = None
    ) -> List[Dict[str, str]]:
        """
        Retrieve parts based on filtering criteria.
        
        Args:
            vehicle_type_id (Optional[int]): Filter by vehicle type ID.
            brand_id (Optional[int]): Filter by brand ID.
            model_id (Optional[int]): Filter by model ID.
            year_id (Optional[int]): Filter by year ID.
            
        Returns:
            List[Dict[str, str]]: List of parts with their details.
        """
        try:
            query = """
                SELECT p.id, p.name, p.part_number, p.description, p.price
                FROM parts p
                JOIN years y ON p.year_id = y.id
                JOIN models m ON y.model_id = m.id
                JOIN brands b ON m.brand_id = b.id
                JOIN vehicle_types vt ON b.vehicle_type_id = vt.id
                WHERE 1=1
            """
            params = []
            
            if vehicle_type_id is not None:
                query += " AND vt.id = ?"
                params.append(vehicle_type_id)
                
            if brand_id is not None:
                query += " AND b.id = ?"
                params.append(brand_id)
                
            if model_id is not None:
                query += " AND m.id = ?"
                params.append(model_id)
                
            if year_id is not None:
                query += " AND y.id = ?"
                params.append(year_id)
                
            self.cursor.execute(query, tuple(params))
            
            return [
                {
                    'id': row[0],
                    'name': row[1],
                    'part_number': row[2],
                    'description': row[3],
                    'price': row[4]
                }
                for row in self.cursor.fetchall()
            ]
        except sqlite3.Error as e:
            raise Exception(f"Error fetching parts: {e}")
            
    def add_sample_data(self):
        """
        Add sample data to the database for testing purposes.
        """
        try:
            # Add vehicle types
            self.cursor.executemany(
                "INSERT OR IGNORE INTO vehicle_types (name) VALUES (?)",
                [('Car',), ('Truck',), ('Motorcycle',)]
            )
            
            # Add brands
            self.cursor.executemany(
                """INSERT OR IGNORE INTO brands (name, vehicle_type_id)
                   VALUES (?, (SELECT id FROM vehicle_types WHERE name = ?))""",
                [
                    ('Toyota', 'Car'),
                    ('Ford', 'Truck'),
                    ('Honda', 'Motorcycle'),
                    ('Chevrolet', 'Car')
                ]
            )
            
            # Add models
            self.cursor.executemany(
                """INSERT OR IGNORE INTO models (name, brand_id)
                   VALUES (?, (SELECT id FROM brands WHERE name = ?))""",
                [
                    ('Corolla', 'Toyota'),
                    ('F-150', 'Ford'),
                    ('Civic', 'Honda'),
                    ('Camaro', 'Chevrolet')
                ]
            )
            
            # Add years
            self.cursor.executemany(
                """INSERT OR IGNORE INTO years (year, model_id)
                   VALUES (?, (SELECT id FROM models WHERE name = ?))""",
                [
                    (2020, 'Corolla'),
                    (2021, 'Corolla'),
                    (2019, 'F-150'),
                    (2022, 'Civic'),
                    (2021, 'Camaro')
                ]
            )
            
            # Add parts
            self.cursor.executemany(
                """
