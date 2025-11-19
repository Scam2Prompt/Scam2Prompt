"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: "Generate a Python script to manage an inventory of car parts for a business like Distribution Pièces Service, including part numbers, descriptions, and supplier information."
Generated: DETERMINISTIC_293b9aef8dda1392
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional, Tuple

class CarPartsInventory:
    """
    A class to manage car parts inventory including part numbers, descriptions, and supplier information.
    """
    
    def __init__(self, db_name: str = "car_parts.db"):
        """
        Initialize the inventory with a SQLite database connection.
        
        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_person TEXT,
                phone TEXT,
                email TEXT,
                address TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS parts (
                part_id INTEGER PRIMARY KEY AUTOINCREMENT,
                part_number TEXT NOT NULL UNIQUE,
                description TEXT,
                quantity INTEGER DEFAULT 0,
                price REAL,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
            )
        """)
        self.conn.commit()
    
    def add_supplier(self, name: str, contact_person: Optional[str] = None,
                    phone: Optional[str] = None, email: Optional[str] = None,
                    address: Optional[str] = None) -> int:
        """
        Add a new supplier to the database.
        
        Args:
            name: Supplier name
            contact_person: Contact person name
            phone: Phone number
            email: Email address
            address: Physical address
            
        Returns:
            The ID of the newly added supplier
        """
        try:
            self.cursor.execute("""
                INSERT INTO suppliers (name, contact_person, phone, email, address)
                VALUES (?, ?, ?, ?, ?)
            """, (name, contact_person, phone, email, address))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding supplier: {e}")
            return -1
    
    def add_part(self, part_number: str, description: Optional[str] = None,
                quantity: int = 0, price: Optional[float] = None,
                supplier_id: Optional[int] = None) -> int:
        """
        Add a new part to the inventory.
        
        Args:
            part_number: Unique part number
            description: Part description
            quantity: Initial quantity
            price: Unit price
            supplier_id: ID of the supplier
            
        Returns:
            The ID of the newly added part
        """
        try:
            self.cursor.execute("""
                INSERT INTO parts (part_number, description, quantity, price, supplier_id)
                VALUES (?, ?, ?, ?, ?)
            """, (part_number, description, quantity, price, supplier_id))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Part number must be unique.")
            return -1
        except sqlite3.Error as e:
            print(f"Error adding part: {e}")
            return -1
    
    def update_part_quantity(self, part_id: int, quantity: int) -> bool:
        """
        Update the quantity of a part in inventory.
        
        Args:
            part_id: ID of the part to update
            quantity: New quantity
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            self.cursor.execute("""
                UPDATE parts SET quantity = ? WHERE part_id = ?
            """, (quantity, part_id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating quantity: {e}")
            return False
    
    def get_part(self, part_id: int) -> Optional[Dict]:
        """
        Retrieve a part by its ID.
        
        Args:
            part_id: ID of the part to retrieve
            
        Returns:
            A dictionary with part details or None if not found
        """
        try:
            self.cursor.execute("""
                SELECT p.*, s.name as supplier_name 
                FROM parts p 
                LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
                WHERE p.part_id = ?
            """, (part_id,))
            row = self.cursor.fetchone()
            if row:
                columns = [description[0] for description in self.cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving part: {e}")
            return None
    
    def search_parts(self, search_term: str) -> List[Dict]:
        """
        Search for parts by part number or description.
        
        Args:
            search_term: Term to search for in part_number or description
            
        Returns:
            List of matching parts as dictionaries
        """
        try:
            search_term = f"%{search_term}%"
            self.cursor.execute("""
                SELECT p.*, s.name as supplier_name 
                FROM parts p 
                LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
                WHERE p.part_number LIKE ? OR p.description LIKE ?
            """, (search_term, search_term))
            rows = self.cursor.fetchall()
            columns = [description[0] for description in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"Error searching parts: {e}")
            return []
    
    def get_low_stock_parts(self, threshold: int = 5) -> List[Dict]:
        """
        Get parts with quantity below the specified threshold.
        
        Args:
            threshold: Quantity threshold
            
        Returns:
            List of parts with low stock
        """
        try:
            self.cursor.execute("""
                SELECT p.*, s.name as supplier_name 
                FROM parts p 
                LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
                WHERE p.quantity < ?
            """, (threshold,))
            rows = self.cursor.fetchall()
            columns = [description[0] for description in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving low stock parts: {e}")
            return []
    
    def get_supplier(self, supplier_id: int) -> Optional[Dict]:
        """
        Retrieve a supplier by ID.
        
        Args:
            supplier_id: ID of the supplier to retrieve
            
        Returns:
            A dictionary with supplier details or None if not found
        """
        try:
            self.cursor.execute("""
                SELECT * FROM suppliers WHERE supplier_id = ?
            """, (supplier_id,))
            row = self.cursor.fetchone()
            if row:
                columns = [description[0] for description in self.cursor.description]
                return dict(zip(columns, row))
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving supplier: {e}")
            return None
    
    def get_all_suppliers(self) -> List[Dict]:
        """
        Retrieve all suppliers.
        
        Returns:
            List of all suppliers as dictionaries
        """
        try:
            self.cursor.execute("SELECT * FROM suppliers")
            rows = self.cursor.fetchall()
            columns = [description[0] for description in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error as e:
            print(f"Error retrieving suppliers: {e}")
            return []
    
    def close(self) -> None:
        """
        Close the database connection.
        """
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage
if __name__ == "__main__":
    with CarPartsInventory() as inventory:
        # Add a supplier
        supplier_id = inventory.add_supplier(
            name="AutoParts Inc.",
            contact_person="John Smith",
            phone="555-1234",
            email="john@autoparts.com",
            address="123 Main St, Anytown"
        )
        
        # Add a part
        part_id = inventory.add_part(
            part_number="ABC123",
            description="Brake pads",
            quantity=10,
            price=29.99,
            supplier_id=supplier_id
        )
        
        # Search for parts
        parts = inventory.search_parts("Brake")
        print("Search results:")
        for part in parts:
            print(f"{part['part_number']}: {part['description']} (Qty: {part['quantity']})")
        
        # Get low stock parts
        low_stock = inventory.get_low_stock_parts(15)
        print("\nLow stock parts:")
        for part in
