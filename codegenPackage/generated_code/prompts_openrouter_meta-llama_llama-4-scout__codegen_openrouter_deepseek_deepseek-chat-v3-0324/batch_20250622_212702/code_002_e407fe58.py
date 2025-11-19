"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Generate a code snippet that demonstrates how to integrate a search functionality for automotive parts and accessories, allowing users to find products by vehicle type (e.g., moto, auto, camioneta, camión).
Generated: DETERMINISTIC_e407fe580dc71f84
Batch ID: 20250622_212702
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

class AutomotivePartsSearch:
    """
    A class to handle searching automotive parts and accessories by vehicle type.
    """
    
    def __init__(self, db_path: str = 'automotive_parts.db'):
        """
        Initialize the search system with database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._create_tables_if_not_exist()
    
    def _create_tables_if_not_exist(self) -> None:
        """Create necessary tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS vehicle_types (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS parts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    vehicle_type_id INTEGER,
                    FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(id)
                )
            ''')
            conn.commit()
    
    def add_vehicle_type(self, name: str) -> int:
        """
        Add a new vehicle type to the database.
        
        Args:
            name: Name of the vehicle type (e.g., 'moto', 'auto', 'camioneta', 'camión')
            
        Returns:
            ID of the newly created vehicle type
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO vehicle_types (name) VALUES (?)', (name,))
                conn.commit()
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                raise ValueError(f"Vehicle type '{name}' already exists")
    
    def add_part(self, name: str, description: str, price: float, stock: int, vehicle_type: str) -> int:
        """
        Add a new automotive part to the database.
        
        Args:
            name: Name of the part
            description: Description of the part
            price: Price of the part
            stock: Available stock quantity
            vehicle_type: Vehicle type this part is compatible with
            
        Returns:
            ID of the newly created part
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get vehicle type ID
            cursor.execute('SELECT id FROM vehicle_types WHERE name = ?', (vehicle_type,))
            result = cursor.fetchone()
            
            if not result:
                raise ValueError(f"Vehicle type '{vehicle_type}' not found")
            
            vehicle_type_id = result[0]
            
            # Insert the part
            cursor.execute('''
                INSERT INTO parts (name, description, price, stock, vehicle_type_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, price, stock, vehicle_type_id))
            
            conn.commit()
            return cursor.lastrowid
    
    def search_parts_by_vehicle_type(self, vehicle_type: str) -> List[Dict[str, Optional[str]]]:
        """
        Search for parts compatible with a specific vehicle type.
        
        Args:
            vehicle_type: Vehicle type to search for (e.g., 'moto', 'auto', 'camioneta', 'camión')
            
        Returns:
            List of dictionaries containing part information
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT p.id, p.name, p.description, p.price, p.stock, v.name as vehicle_type
                FROM parts p
                JOIN vehicle_types v ON p.vehicle_type_id = v.id
                WHERE v.name = ?
            ''', (vehicle_type,))
            
            results = cursor.fetchall()
            return [dict(row) for row in results]
    
    def get_all_vehicle_types(self) -> List[str]:
        """
        Get all available vehicle types in the system.
        
        Returns:
            List of vehicle type names
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name FROM vehicle_types')
            return [row[0] for row in cursor.fetchall()]

# Example usage
if __name__ == "__main__":
    search_system = AutomotivePartsSearch()
    
    # Add some vehicle types if they don't exist
    for vehicle_type in ['moto', 'auto', 'camioneta', 'camión']:
        try:
            search_system.add_vehicle_type(vehicle_type)
        except ValueError:
            pass  # Already exists
    
    # Add sample parts
    try:
        search_system.add_part(
            name="Filtro de aceite",
            description="Filtro de aceite para motocicletas",
            price=15.99,
            stock=50,
            vehicle_type="moto"
        )
        
        search_system.add_part(
            name="Pastillas de freno",
            description="Pastillas de freno delanteras para automóviles",
            price=29.99,
            stock=30,
            vehicle_type="auto"
        )
    except ValueError as e:
        print(f"Error adding part: {e}")
    
    # Search for parts
    print("Available vehicle types:", search_system.get_all_vehicle_types())
    
    search_results = search_system.search_parts_by_vehicle_type("moto")
    print("\nParts for moto:")
    for part in search_results:
        print(f"{part['name']} - ${part['price']} (Stock: {part['stock']})")
```
