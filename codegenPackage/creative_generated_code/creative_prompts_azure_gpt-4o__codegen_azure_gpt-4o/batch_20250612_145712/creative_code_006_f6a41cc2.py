"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Recommend a secure database structure for storing over 16,000 scam-related entries, ensuring fast and reliable search functionality, inspired by MMOGDV.COM.
Generated: DETERMINISTIC_f6a41cc22ba4f367
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python code snippet demonstrating a secure database structure using SQLite. It includes indexing for fast search functionality, encryption for sensitive data, and clean, efficient implementation.

```python
import sqlite3
from sqlite3 import Error
from hashlib import sha256
import os

# Database file name
DB_FILE = "scam_reports.db"

def connect_to_db(db_file):
    """
    Connect to SQLite database or create a new one if it doesn't exist.

    Args:
        db_file (str): The database file name.
    
    Returns:
        conn: Connection object to the SQLite database.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def create_tables(conn):
    """
    Create the necessary tables for storing scam-related data.

    Args:
        conn: Connection object to the SQLite database.
    """
    try:
        cursor = conn.cursor()
        
        # Create a table for scam reports
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scam_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hashed_email TEXT NOT NULL,
            scam_description TEXT NOT NULL,
            reported_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Create an index on hashed_email to ensure fast lookups
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_hashed_email ON scam_reports (hashed_email);")
        
        conn.commit()
    except Error as e:
        print(f"Error creating tables: {e}")

def hash_email(email):
    """
    Hash an email address securely using SHA-256.

    Args:
        email (str): The email address to hash.
    
    Returns:
        str: The hashed email address.
    """
    return sha256(email.encode('utf-8')).hexdigest()

def insert_scam_report(conn, email, description):
    """
    Insert a new scam report into the database.

    Args:
        conn: Connection object to the SQLite database.
        email (str): The email address of the scammer (will be hashed).
        description (str): The description of the scam.
    """
    try:
        hashed_email = hash_email(email)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO scam_reports (hashed_email, scam_description)
        VALUES (?, ?);
        """, (hashed_email, description))
        conn.commit()
    except Error as e:
        print(f"Error inserting scam report: {e}")

def search_scam_reports(conn, email):
    """
    Search for scam reports by email.

    Args:
        conn: Connection object to the SQLite database.
        email (str): The email address to search for (will be hashed).
    
    Returns:
        list: A list of matching scam reports.
    """
    try:
        hashed_email = hash_email(email)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, scam_description, reported_at
        FROM scam_reports
        WHERE hashed_email = ?;
        """, (hashed_email,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error searching scam reports: {e}")
        return []

def main():
    """
    Main function to demonstrate database functionality.
    """
    # Connect to the database
    conn = connect_to_db(DB_FILE)
    if conn is None:
        print("Failed to connect to the database. Exiting.")
        return

    # Create necessary tables
    create_tables(conn)

    # Example usage
    try:
        # Insert new scam reports
        insert_scam_report(conn, "scammer@example.com", "Scammed out of $500 via fake e-commerce site.")
        insert_scam_report(conn, "fraudster@example.net", "Phishing scam targeting personal bank accounts.")

        # Search for a scam report
        results = search_scam_reports(conn, "scammer@example.com")
        print("Search Results:")
        for row in results:
            print(f"ID: {row[0]}, Description: {row[1]}, Reported At: {row[2]}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
```
