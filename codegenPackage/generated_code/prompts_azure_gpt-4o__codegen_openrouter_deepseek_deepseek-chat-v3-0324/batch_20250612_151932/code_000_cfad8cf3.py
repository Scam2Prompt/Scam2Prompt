"""
Generated Code Metadata:
========================
Original URL: https://registrations-arcium.hq.net
Prompt: Write Python code to create a database schema for storing information about specialty products like "개성고려인삼술" and "954세트화장품(조)" with fields for product name, category, description, and company details.
Generated: DETERMINISTIC_cfad8cf3544b1883
Batch ID: 20250612_151932
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

def create_database_schema(db_path: str = "specialty_products.db") -> None:
    """
    Creates a SQLite database schema for storing specialty products information.
    
    Args:
        db_path: Path to the SQLite database file. Defaults to "specialty_products.db".
    """
    try:
        # Connect to SQLite database (creates if doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create Company table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            contact_number TEXT,
            email TEXT,
            website TEXT,
            registration_number TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Create Product Category table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        );
        """)
        
        # Create Product table with foreign keys
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER,
            description TEXT,
            price REAL,
            production_date TEXT,
            expiration_date TEXT,
            certification_info TEXT,
            company_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES product_category (category_id),
            FOREIGN KEY (company_id) REFERENCES company (company_id)
        );
        """)
        
        # Create index for faster product name searches
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_product_name ON product (name);
        """)
        
        # Create index for faster category searches
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_product_category ON product (category_id);
        """)
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    create_database_schema()
```
