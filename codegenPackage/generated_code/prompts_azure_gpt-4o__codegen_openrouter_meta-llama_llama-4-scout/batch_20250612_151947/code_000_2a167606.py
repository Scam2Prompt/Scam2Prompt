"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write Python code to create a database schema for storing information about "Social Impact Heroes," including categories like "Stars Making a Social Impact," "Young Social Impact Heroes," and "Social Impact Investors."
Generated: DETERMINISTIC_2a167606054ea92c
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from enum import Enum

# Define an Enum for hero categories
class HeroCategory(str, Enum):
    STARS_MAKING_A_SOCIAL_IMPACT = "Stars Making a Social Impact"
    YOUNG_SOCIAL_IMPACT_HEROES = "Young Social Impact Heroes"
    SOCIAL_IMPACT_INVESTORS = "Social Impact Investors"

# Create a connection to the SQLite database
def create_connection(db_file):
    """Create a database connection to the SQLite database
    specified by db_file

    Args:
        db_file (str): Path to the SQLite database file

    Returns:
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

# Create table for heroes
def create_heroes_table(conn):
    """Create table for heroes

    Args:
        conn (Connection object): Connection to the SQLite database
    """
    sql = """
        CREATE TABLE IF NOT EXISTS heroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Create table for hero awards
def create_hero_awards_table(conn):
    """Create table for hero awards

    Args:
        conn (Connection object): Connection to the SQLite database
    """
    sql = """
        CREATE TABLE IF NOT EXISTS hero_awards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hero_id INTEGER NOT NULL,
            award_name TEXT NOT NULL,
            award_description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (hero_id) REFERENCES heroes (id)
        );
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Create table for hero impacts
def create_hero_impacts_table(conn):
    """Create table for hero impacts

    Args:
        conn (Connection object): Connection to the SQLite database
    """
    sql = """
        CREATE TABLE IF NOT EXISTS hero_impacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hero_id INTEGER NOT NULL,
            impact_description TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (hero_id) REFERENCES heroes (id)
        );
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Main function to create database schema
def create_database_schema(db_file):
    """Create database schema for social impact heroes

    Args:
        db_file (str): Path to the SQLite database file
    """
    conn = create_connection(db_file)
    with conn:
        create_heroes_table(conn)
        create_hero_awards_table(conn)
        create_hero_impacts_table(conn)
    conn.close()

# Example usage
if __name__ == "__main__":
    database_file = "social_impact_heroes.db"
    create_database_schema(database_file)

    # Insert example data
    conn = create_connection(database_file)
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO heroes (name, category, description) VALUES (?, ?, ?)",
                  ("Example Hero", HeroCategory.STARS_MAKING_A_SOCIAL_IMPACT.value, "This is an example hero"))
        conn.commit()
    conn.close()
```
