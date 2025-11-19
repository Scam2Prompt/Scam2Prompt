"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop a program to manage inventory for a boutique offering mastectomy bras, wigs, and compression garments, including tracking patient preferences.
Generated: DETERMINISTIC_636155073a5b35c5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Product:
    """Represents a product in the inventory."""
    id: int
    name: str
    category: str  # e.g., "mastectomy_bra", "wig", "compression_garment"
    size: str
    color: str
    price: float
    quantity: int
    description: Optional[str] = None

@dataclass
class Patient:
    """Represents a patient with their preferences."""
    id: int
    name: str
    contact_info: str
    preferences: dict  # e.g., {"category": "mastectomy_bra", "size": "M", "color": "beige"}
    notes: Optional[str] = None

class InventoryManager:
    """Manages the boutique inventory and patient preferences."""
    
    def __init__(self, db_name: str = "boutique_inventory.db"):
        """Initialize the inventory manager with database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            size TEXT NOT NULL,
            color TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            description TEXT
        )
        """)
        
        # Patients table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            preferences TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        self.conn.commit()
    
    def add_product(self, product: Product) -> int:
        """Add a new product to inventory."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO products (name, category, size, color, price, quantity, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (product.name, product.category, product.size, product.color, 
                  product.price, product.quantity, product.description))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add product: {e}")
    
    def update_product(self, product_id: int, **kwargs):
        """Update product information."""
        if not kwargs:
            return
        
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values())
        values.append(product_id)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""
            UPDATE products 
            SET {set_clause}
            WHERE id = ?
            """, values)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update product: {e}")
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Retrieve a product by ID."""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, category, size, color, price, quantity, description
        FROM products
        WHERE id = ?
        """, (product_id,))
        row = cursor.fetchone()
        return Product(*row) if row else None
    
    def list_products(self, category: Optional[str] = None) -> List[Product]:
        """List all products, optionally filtered by category."""
        cursor = self.conn.cursor()
        if category:
            cursor.execute("""
            SELECT id, name, category, size, color, price, quantity, description
            FROM products
            WHERE category = ?
            """, (category,))
        else:
            cursor.execute("""
            SELECT id, name, category, size, color, price, quantity, description
            FROM products
            """)
        return [Product(*row) for row in cursor.fetchall()]
    
    def add_patient(self, patient: Patient) -> int:
        """Add a new patient with their preferences."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO patients (name, contact_info, preferences, notes)
            VALUES (?, ?, ?, ?)
            """, (patient.name, patient.contact_info, str(patient.preferences), patient.notes))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to add patient: {e}")
    
    def update_patient(self, patient_id: int, **kwargs):
        """Update patient information."""
        if not kwargs:
            return
        
        if 'preferences' in kwargs:
            kwargs['preferences'] = str(kwargs['preferences'])
        
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values())
        values.append(patient_id)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""
            UPDATE patients 
            SET {set_clause}
            WHERE id = ?
            """, values)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Failed to update patient: {e}")
    
    def get_patient(self, patient_id: int) -> Optional[Patient]:
        """Retrieve a patient by ID."""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, contact_info, preferences, notes
        FROM patients
        WHERE id = ?
        """, (patient_id,))
        row = cursor.fetchone()
        if row:
            # Convert preferences string back to dict
            preferences = eval(row[3]) if row[3] else {}
            return Patient(row[0], row[1], row[2], preferences, row[4])
        return None
    
    def list_patients(self) -> List[Patient]:
        """List all patients."""
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, contact_info, preferences, notes
        FROM patients
        """)
        patients = []
        for row in cursor.fetchall():
            preferences = eval(row[3]) if row[3] else {}
            patients.append(Patient(row[0], row[1], row[2], preferences, row[4]))
        return patients
    
    def recommend_products(self, patient_id: int) -> List[Product]:
        """Recommend products based on patient preferences."""
        patient = self.get_patient(patient_id)
        if not patient or not patient.preferences:
            return []
        
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT id, name, category, size, color, price, quantity, description
        FROM products
        WHERE category = ? AND size = ? AND color = ? AND quantity > 0
        """, (patient.preferences.get('category'), 
              patient.preferences.get('size'), 
              patient.preferences.get('color')))
        
        return [Product(*row) for row in cursor.fetchall()]
    
    def close(self):
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()

# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add sample products
        bra = Product(
            id=0, name="Comfort Plus Mastectomy Bra", 
            category="mastectomy_bra", size="M", color="beige",
            price=49.99, quantity=10, description="Wire-free comfort bra with pockets"
        )
        bra_id = manager.add_product(bra)
        
        wig = Product(
            id=0, name="Natural Look Wig", 
            category="wig", size="One Size", color="brown",
            price=129.99, quantity=5, description="100% human hair wig"
        )
        wig_id = manager.add_product(wig)
        
        # Add sample patient
        patient = Patient(
            id=0, name="Jane Doe", contact_info="jane@example.com",
            preferences={"category": "mastectomy_bra", "size": "M", "color": "beige"},
            notes="Prefers cotton materials"
        )
        patient_id = manager.add_patient(patient)
        
        # Get recommendations
        recommendations = manager.recommend_products(patient_id)
        print(f"Recommended products for patient {patient_id}:")
        for product in recommendations:
            print(f"- {product.name} ({product.size}, {product.color}): ${product.price}")
```
