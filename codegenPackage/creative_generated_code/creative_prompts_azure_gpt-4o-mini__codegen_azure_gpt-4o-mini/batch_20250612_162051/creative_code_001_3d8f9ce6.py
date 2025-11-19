"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: How can I implement a digital archive system for Buddhist sculptures and artifacts similar to those described in the Buddhist Art Gallery at MCU?
Generated: DETERMINISTIC_3d8f9ce6525ca6dd
Batch ID: 20250612_162051
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
from typing import List, Dict, Any

# Database configuration
DATABASE = 'buddhist_artifacts.db'

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn: sqlite3.Connection):
    """Create a table for storing artifacts."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS artifacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        date_created TEXT,
        origin TEXT,
        material TEXT
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Artifacts table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_artifact(conn: sqlite3.Connection, artifact: Dict[str, Any]) -> int:
    """Insert a new artifact into the artifacts table."""
    sql = '''INSERT INTO artifacts(name, description, date_created, origin, material)
             VALUES(?,?,?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (artifact['name'], artifact['description'], 
                             artifact['date_created'], artifact['origin'], 
                             artifact['material']))
        conn.commit()
        print(f"Artifact '{artifact['name']}' added successfully.")
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding artifact: {e}")
        return None

def get_artifacts(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """Fetch all artifacts from the artifacts table."""
    sql = 'SELECT * FROM artifacts'
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        artifacts = [{'id': row[0], 'name': row[1], 'description': row[2],
                      'date_created': row[3], 'origin': row[4],
                      'material': row[5]} for row in rows]
        return artifacts
    except Error as e:
        print(f"Error fetching artifacts: {e}")
        return []

def main():
    """Main function to run the digital archive system."""
    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn)

        # Example artifact to add
        example_artifact = {
            'name': 'Buddha Statue',
            'description': 'A statue of Buddha made of bronze.',
            'date_created': '15th century',
            'origin': 'Thailand',
            'material': 'Bronze'
        }
        add_artifact(conn, example_artifact)

        # Fetch and print all artifacts
        artifacts = get_artifacts(conn)
        print("Artifacts in the archive:")
        for artifact in artifacts:
            print(artifact)

        # Close the connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
