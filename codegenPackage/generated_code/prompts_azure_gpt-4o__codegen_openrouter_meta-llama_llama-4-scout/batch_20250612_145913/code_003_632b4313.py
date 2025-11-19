"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Provide an example of how to use a database to store tennis court availability and write a function that retrieves available slots for courts labeled "Center Courts" (Platz 1 & 2).
Generated: DETERMINISTIC_632b4313fbb13cee
Batch ID: 20250612_145913
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
from datetime import datetime, timedelta

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

# Create table for tennis courts
def create_tennis_court_table(conn):
    """Create table for tennis courts

    Args:
        conn (Connection object): Connection to the SQLite database
    """
    sql = """CREATE TABLE IF NOT EXISTS tennis_courts (
                id integer PRIMARY KEY,
                name text NOT NULL
            );"""
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Create table for court availability
def create_availability_table(conn):
    """Create table for court availability

    Args:
        conn (Connection object): Connection to the SQLite database
    """
    sql = """CREATE TABLE IF NOT EXISTS court_availability (
                id integer PRIMARY KEY,
                court_id integer NOT NULL,
                date text NOT NULL,
                start_time text NOT NULL,
                end_time text NOT NULL,
                available integer NOT NULL,
                FOREIGN KEY (court_id) REFERENCES tennis_courts (id)
            );"""
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

# Insert tennis court into database
def insert_tennis_court(conn, court):
    """Insert tennis court into database

    Args:
        conn (Connection object): Connection to the SQLite database
        court (str): Name of the tennis court
    """
    sql = """INSERT INTO tennis_courts(name)
             VALUES(?)"""
    try:
        c = conn.cursor()
        c.execute(sql, (court,))
        conn.commit()
        return c.lastrowid
    except sqlite3.Error as e:
        print(e)

# Insert court availability into database
def insert_availability(conn, court_id, date, start_time, end_time, available):
    """Insert court availability into database

    Args:
        conn (Connection object): Connection to the SQLite database
        court_id (int): ID of the tennis court
        date (str): Date of the court availability
        start_time (str): Start time of the court availability
        end_time (str): End time of the court availability
        available (int): Availability of the court (0/1)
    """
    sql = """INSERT INTO court_availability(court_id, date, start_time, end_time, available)
             VALUES(?,?,?,?,?)"""
    try:
        c = conn.cursor()
        c.execute(sql, (court_id, date, start_time, end_time, available))
        conn.commit()
        return c.lastrowid
    except sqlite3.Error as e:
        print(e)

# Get available slots for Center Courts
def get_available_slots(conn):
    """Get available slots for Center Courts

    Args:
        conn (Connection object): Connection to the SQLite database

    Returns:
        List of available slots
    """
    sql = """SELECT 
                tc.name, 
                ca.date, 
                ca.start_time, 
                ca.end_time
             FROM 
                tennis_courts tc 
             JOIN 
                court_availability ca ON tc.id = ca.court_id
             WHERE 
                tc.name IN ('Platz 1', 'Platz 2') AND 
                ca.available = 1"""
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)

# Main function
def main():
    database = "tennis_court.db"

    # Create a database connection
    conn = create_connection(database)
    with conn:
        # Create tables
        create_tennis_court_table(conn)
        create_availability_table(conn)

        # Insert tennis courts
        court1_id = insert_tennis_court(conn, 'Platz 1')
        court2_id = insert_tennis_court(conn, 'Platz 2')

        # Insert court availability
        insert_availability(conn, court1_id, datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(hours=10)).strftime("%H:%M"), (datetime.now() + timedelta(hours=11)).strftime("%H:%M"), 1)
        insert_availability(conn, court1_id, datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(hours=12)).strftime("%H:%M"), (datetime.now() + timedelta(hours=13)).strftime("%H:%M"), 0)
        insert_availability(conn, court2_id, datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(hours=10)).strftime("%H:%M"), (datetime.now() + timedelta(hours=11)).strftime("%H:%M"), 1)
        insert_availability(conn, court2_id, datetime.now().strftime("%Y-%m-%d"), (datetime.now() + timedelta(hours=14)).strftime("%H:%M"), (datetime.now() + timedelta(hours=15)).strftime("%H:%M"), 1)

        # Get available slots
        available_slots = get_available_slots(conn)
        for row in available_slots:
            print(f"Court: {row[0]}, Date: {row[1]}, Time: {row[2]} - {row[3]}")

if __name__ == '__main__':
    main()
```
