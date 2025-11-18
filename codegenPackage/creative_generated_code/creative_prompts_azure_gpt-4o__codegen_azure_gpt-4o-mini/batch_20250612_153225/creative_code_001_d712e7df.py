"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Generate a script that uses the SDS (Safety Data Sheet) information to create a database for tracking chemical properties, hazards, and storage guidelines, referencing Kimia Shimi's emphasis on SDS documentation.
Generated: DETERMINISTIC_d712e7dfc4e9b97f
Batch ID: 20250612_153225
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

# Define the database connection function
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error occurred while connecting to database: {e}")
    return conn

# Define a function to create the SDS table
def create_sds_table(conn):
    """ Create a table for storing SDS information """
    try:
        sql_create_sds_table = """
        CREATE TABLE IF NOT EXISTS sds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chemical_name TEXT NOT NULL,
            properties TEXT NOT NULL,
            hazards TEXT NOT NULL,
            storage_guidelines TEXT NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_sds_table)
        print("SDS table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Define a function to insert SDS data into the table
def insert_sds_data(conn, sds_data):
    """ Insert a new SDS record into the sds table """
    sql_insert_sds = """
    INSERT INTO sds (chemical_name, properties, hazards, storage_guidelines)
    VALUES (?, ?, ?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_sds, sds_data)
        conn.commit()
        print(f"Inserted data for {sds_data[0]} successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")

# Define a function to query all SDS records
def query_sds_data(conn):
    """ Query all rows in the sds table """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sds;")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error querying data: {e}")
        return []

# Main function to execute the script
def main():
    # Database file path
    database = "sds_database.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create the SDS table
        create_sds_table(conn)

        # Example SDS data to insert
        sample_sds_data = [
            ("Acetic Acid", "Colorless liquid, pungent odor.", "Corrosive, flammable.", "Store in a cool, well-ventilated area away from incompatible materials."),
            ("Sodium Chloride", "White crystalline solid.", "Low hazard, irritant.", "Store in a dry place.")
        ]

        # Insert sample SDS data
        for data in sample_sds_data:
            insert_sds_data(conn, data)

        # Query and print all SDS records
        sds_records = query_sds_data(conn)
        print("Current SDS Records:")
        for record in sds_records:
            print(record)

        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create a database connection.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
