"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a-step.site
Prompt: Can you provide a code snippet to track earnings from an automated online system similar to the one mentioned on A-Step?
Generated: DETERMINISTIC_97fab997b94e0a22
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Define the database connection and cursor
DATABASE_NAME = 'earnings_tracker.db'

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the earnings table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS earnings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        source TEXT NOT NULL,
        date TEXT NOT NULL
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def log_earning(conn, amount, source):
    """Log a new earning entry."""
    sql = '''INSERT INTO earnings (amount, source, date) VALUES (?, ?, ?)'''
    date = datetime.now().isoformat()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (amount, source, date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error logging earning: {e}")

def fetch_earnings(conn):
    """Fetch all earnings logged in the database."""
    sql = '''SELECT * FROM earnings'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching earnings: {e}")
        return []

def main():
    """Main function to run the earnings tracking system."""
    conn = create_connection()
    
    if conn is not None:
        create_table(conn)

        # Example usage: log some earnings
        log_earning(conn, 150.0, 'Affiliate Marketing')
        log_earning(conn, 75.50, 'Online Course Sales')

        # Fetch and display all earnings
        earnings = fetch_earnings(conn)
        for earning in earnings:
            print(f"Earning ID: {earning[0]}, Amount: {earning[1]}, Source: {earning[2]}, Date: {earning[3]}")

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
