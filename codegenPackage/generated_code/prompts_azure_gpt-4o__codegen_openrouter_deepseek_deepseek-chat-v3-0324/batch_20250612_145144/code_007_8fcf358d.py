"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Provide Python code to create a database schema for storing product details, including items like "PROTETOR AUDITIVO COPOLIMERO – WORKER" and their prices.
Generated: DETERMINISTIC_8fcf358d5f030ecc
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional

def create_database_schema(db_path: str = "products.db") -> None:
    """
    Creates a SQLite database with a schema for storing product details.
    
    Args:
        db_path: Path to the SQLite database file. Defaults to "products.db".
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Create index for faster lookups
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_product_name ON products (name)
        """)
        
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    finally:
        if conn:
            conn.close()

def insert_sample_data(db_path: str = "products.db") -> None:
    """
    Inserts sample product data into the database.
    
    Args:
        db_path: Path to the SQLite database file. Defaults to "products.db".
    """
    sample_products = [
        ("PROTETOR AUDITIVO COPOLIMERO – WORKER", "High-quality hearing protection", 25.99, "Safety Equipment"),
        ("LUVAS DE SEGURANÇA", "Durable safety gloves", 12.50, "Safety Equipment"),
        ("ÓCULOS DE PROTEÇÃO", "Anti-fog safety goggles", 15.75, "Safety Equipment")
    ]
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.executemany("""
        INSERT INTO products (name, description, price, category)
        VALUES (?, ?, ?, ?)
        """, sample_products)
        
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database_schema()
    insert_sample_data()
    print("Database schema created and sample data inserted successfully.")
```
