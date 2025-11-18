"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Provide Python code to create a database schema for storing product details, including items like "PROTETOR AUDITIVO COPOLIMERO – WORKER" and their prices.
Generated: DETERMINISTIC_8fcf358d5f030ecc
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_database_schema():
    """
    Create a database schema for storing product details.
    The schema includes a 'products' table with columns for ID, name, description, and price.
    """
    try:
        # Connect to SQLite database (creates the file if it doesn't exist)
        connection = sqlite3.connect('product_database.db')
        cursor = connection.cursor()

        # Create 'products' table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each product
            name TEXT NOT NULL,                    -- Name of the product
            description TEXT,                      -- Optional description of the product
            price REAL NOT NULL                    -- Price of the product
        );
        """)
        
        # Commit the changes
        connection.commit()
        print("Database schema created successfully.")

    except sqlite3.Error as e:
        # Handle database errors
        print(f"An error occurred while creating the database schema: {e}")
    
    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

# Run the function to create the schema
if __name__ == "__main__":
    create_database_schema()
```
