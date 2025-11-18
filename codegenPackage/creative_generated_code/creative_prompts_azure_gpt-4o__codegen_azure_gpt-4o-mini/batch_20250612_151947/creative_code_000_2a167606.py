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
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to SQLite DB successful: {db_file}")
    except Error as e:
        print(f"Error while connecting to SQLite: {e}")
    return conn

# Function to execute a single SQL statement
def execute_sql(conn, sql):
    """Execute a single SQL statement."""
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("SQL executed successfully.")
    except Error as e:
        print(f"Error executing SQL: {e}")

# SQL statements to create tables
def create_tables():
    """Create tables for Social Impact Heroes database."""
    create_heroes_table = """
    CREATE TABLE IF NOT EXISTS heroes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL CHECK(category IN ('Stars Making a Social Impact', 'Young Social Impact Heroes', 'Social Impact Investors')),
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hero_id INTEGER NOT NULL,
        project_name TEXT NOT NULL,
        impact_description TEXT,
        funding_amount REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE
    );
    """
    
    return [create_heroes_table, create_projects_table]

def main():
    # Database file path
    database = "social_impact_heroes.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create tables
        for sql in create_tables():
            execute_sql(conn, sql)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
