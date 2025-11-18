"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Write Python code to create a database schema for storing information about "Social Impact Heroes," including categories like "Stars Making a Social Impact," "Young Social Impact Heroes," and "Social Impact Investors."
Generated: DETERMINISTIC_2a167606054ea92c
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_database_schema(db_name="social_impact_heroes.db"):
    """
    Creates a database schema for storing information about Social Impact Heroes.
    
    Tables:
    - categories: Stores category information (e.g., "Stars Making a Social Impact").
    - heroes: Stores details about individual heroes.
    """

    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create the 'categories' table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        );
        """)

        # Create the 'heroes' table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS heroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bio TEXT,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
        );
        """)

        # Commit the transaction and close the connection
        conn.commit()
        print("Database schema created successfully.")

    except sqlite3.Error as e:
        print(f"Error occurred while creating database schema: {e}")

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_database_schema()
```
