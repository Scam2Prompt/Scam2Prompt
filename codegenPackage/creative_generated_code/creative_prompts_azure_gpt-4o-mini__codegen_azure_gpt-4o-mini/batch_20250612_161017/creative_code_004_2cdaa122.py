"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: How can I use a database to store customer testimonials for a carpet service, inspired by the testimonials section of Perfect Melbourne Carpet's site?
Generated: DETERMINISTIC_2cdaa1220ef043c1
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    """ Establish a database connection to the SQLite database specified by db_file. """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database successful.")
    except Error as e:
        print(f"Error occurred while connecting to database: {e}")
    return conn

# Function to create a table for testimonials
def create_testimonials_table(conn):
    """ Create a table for storing customer testimonials. """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS testimonials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        testimonial TEXT NOT NULL,
        service_date TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Testimonials table created successfully.")
    except Error as e:
        print(f"Error occurred while creating table: {e}")

# Function to insert a new testimonial
def insert_testimonial(conn, customer_name, testimonial, service_date):
    """ Insert a new testimonial into the testimonials table. """
    insert_sql = """
    INSERT INTO testimonials (customer_name, testimonial, service_date)
    VALUES (?, ?, ?);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, (customer_name, testimonial, service_date))
        conn.commit()
        print("Testimonial added successfully.")
    except Error as e:
        print(f"Error occurred while inserting testimonial: {e}")

# Function to fetch all testimonials
def fetch_testimonials(conn):
    """ Fetch all testimonials from the testimonials table. """
    select_sql = "SELECT * FROM testimonials;"
    try:
        cursor = conn.cursor()
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error occurred while fetching testimonials: {e}")
        return []

# Main execution flow
if __name__ == '__main__':
    # Specify the database file
    database = "testimonials.db"

    # Create a database connection
    conn = create_connection(database)

    # Create testimonials table
    if conn is not None:
        create_testimonials_table(conn)

        # Insert sample testimonials
        insert_testimonial(conn, "John Doe", "Great service and quality carpets!", "2023-10-01")
        insert_testimonial(conn, "Jane Smith", "I'm very happy with my new carpet. Highly recommend!", "2023-10-02")

        # Fetch and display all testimonials
        testimonials = fetch_testimonials(conn)
        print("Customer Testimonials:")
        for testimonial in testimonials:
            print(f"{testimonial[1]}: {testimonial[2]} (Date: {testimonial[3]})")

        # Close the connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")
```
