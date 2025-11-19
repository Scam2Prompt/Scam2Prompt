"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Design a database schema to store employee data and implement a system for tracking employee growth and strategizing career aspirations, using a programming language of your choice.
Generated: DETERMINISTIC_b077a20a2af2babf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Define a function to create tables
def create_tables(conn):
    """ Create tables for employee data and career aspirations """
    try:
        cursor = conn.cursor()
        
        # Create Employee table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                department TEXT NOT NULL,
                hire_date DATE NOT NULL,
                performance_rating INTEGER CHECK(performance_rating BETWEEN 1 AND 5)
            );
        ''')
        
        # Create CareerAspiration table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CareerAspiration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER NOT NULL,
                aspiration TEXT NOT NULL,
                target_date DATE,
                FOREIGN KEY (employee_id) REFERENCES Employee (id)
            );
        ''')
        
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Define a function to add an employee
def add_employee(conn, name, position, department, hire_date, performance_rating):
    """ Add a new employee to the Employee table """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Employee (name, position, department, hire_date, performance_rating)
            VALUES (?, ?, ?, ?, ?);
        ''', (name, position, department, hire_date, performance_rating))
        conn.commit()
        print(f"Employee {name} added successfully.")
    except Error as e:
        print(f"Error adding employee: {e}")

# Define a function to add a career aspiration
def add_career_aspiration(conn, employee_id, aspiration, target_date):
    """ Add a career aspiration for an employee """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO CareerAspiration (employee_id, aspiration, target_date)
            VALUES (?, ?, ?);
        ''', (employee_id, aspiration, target_date))
        conn.commit()
        print(f"Career aspiration added for employee ID {employee_id}.")
    except Error as e:
        print(f"Error adding career aspiration: {e}")

# Main function to run the application
def main():
    database = "employee_growth.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example: Add employees and aspirations
        add_employee(conn, "Alice Smith", "Software Engineer", "Development", "2022-01-15", 4)
        add_employee(conn, "Bob Johnson", "Data Analyst", "Analytics", "2021-06-30", 5)
        
        add_career_aspiration(conn, 1, "Senior Software Engineer", "2024-01-15")
        add_career_aspiration(conn, 2, "Lead Data Analyst", "2023-12-30")
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

# Run the main function
if __name__ == '__main__':
    main()
```
