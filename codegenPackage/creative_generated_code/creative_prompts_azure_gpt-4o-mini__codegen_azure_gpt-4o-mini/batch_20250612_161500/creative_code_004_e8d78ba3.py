"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Illustrate how to use a database to store patient testimonials and feedback, similar to the testimonials section found on the Heroes Dental website.
Generated: DETERMINISTIC_e8d78ba34bb679e5
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create a testimonials table
def create_table(conn):
    """ Create the testimonials table in the database """
    try:
        sql_create_testimonials_table = """
        CREATE TABLE IF NOT EXISTS testimonials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            feedback TEXT NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_testimonials_table)
        print("Testimonials table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to insert a new testimonial
def insert_testimonial(conn, testimonial):
    """ Insert a new testimonial into the testimonials table """
    sql = ''' INSERT INTO testimonials(patient_name, feedback, rating)
              VALUES(?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, testimonial)
        conn.commit()
        print("Testimonial added successfully.")
        return cursor.lastrowid
    except Error as e:
        print(f"Error inserting testimonial: {e}")

# Function to fetch all testimonials
def fetch_testimonials(conn):
    """ Fetch all testimonials from the testimonials table """
    sql = 'SELECT * FROM testimonials ORDER BY created_at DESC'
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching testimonials: {e}")
        return []

# Example usage
if __name__ == '__main__':
    # Define the database file
    database = "patient_testimonials.db"

    # Create a database connection
    conn = create_connection(database)

    # Create testimonials table
    if conn:
        create_table(conn)

        # Example testimonial data
        testimonial_data = ("John Doe", "Great experience at Heroes Dental!", 5)
        
        # Insert a new testimonial
        insert_testimonial(conn, testimonial_data)

        # Fetch and display all testimonials
        testimonials = fetch_testimonials(conn)
        print("Testimonials:")
        for testimonial in testimonials:
            print(f"ID: {testimonial[0]}, Name: {testimonial[1]}, Feedback: {testimonial[2]}, Rating: {testimonial[3]}, Date: {testimonial[4]}")

        # Close the database connection
        conn.close()
```
