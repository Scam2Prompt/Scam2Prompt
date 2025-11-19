"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Develop a basic data model and database schema to manage exhibitor information, products, and visitor interactions for the Pro Integration Future Asia event.
Generated: DETERMINISTIC_87638c681f59f81b
Batch ID: 20250622_212850
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
    """ Create tables for exhibitors, products, and visitor interactions """
    try:
        cursor = conn.cursor()
        
        # Create Exhibitors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exhibitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_email TEXT NOT NULL UNIQUE,
                phone_number TEXT,
                booth_number TEXT
            );
        ''')
        
        # Create Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                exhibitor_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                description TEXT,
                price REAL,
                FOREIGN KEY (exhibitor_id) REFERENCES exhibitors (id) ON DELETE CASCADE
            );
        ''')
        
        # Create Visitor Interactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitor_interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visitor_name TEXT NOT NULL,
                exhibitor_id INTEGER NOT NULL,
                interaction_date TEXT NOT NULL,
                notes TEXT,
                FOREIGN KEY (exhibitor_id) REFERENCES exhibitors (id) ON DELETE CASCADE
            );
        ''')
        
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Define a function to insert an exhibitor
def insert_exhibitor(conn, exhibitor):
    """ Insert a new exhibitor into the exhibitors table """
    sql = ''' INSERT INTO exhibitors(name, contact_email, phone_number, booth_number)
              VALUES(?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, exhibitor)
        conn.commit()
        print(f"Exhibitor {exhibitor[0]} added successfully.")
    except Error as e:
        print(f"Error inserting exhibitor: {e}")

# Define a function to insert a product
def insert_product(conn, product):
    """ Insert a new product into the products table """
    sql = ''' INSERT INTO products(exhibitor_id, product_name, description, price)
              VALUES(?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
        print(f"Product {product[1]} added successfully.")
    except Error as e:
        print(f"Error inserting product: {e}")

# Define a function to insert a visitor interaction
def insert_visitor_interaction(conn, interaction):
    """ Insert a new visitor interaction into the visitor_interactions table """
    sql = ''' INSERT INTO visitor_interactions(visitor_name, exhibitor_id, interaction_date, notes)
              VALUES(?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, interaction)
        conn.commit()
        print(f"Visitor interaction for {interaction[0]} added successfully.")
    except Error as e:
        print(f"Error inserting visitor interaction: {e}")

# Main function to run the application
def main():
    database = "exhibitor_management.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example data to insert
        exhibitor = ('Tech Innovations', 'contact@techinnovations.com', '123-456-7890', 'A1')
        insert_exhibitor(conn, exhibitor)
        
        product = (1, 'Smart Widget', 'A widget that does smart things', 99.99)
        insert_product(conn, product)
        
        interaction = ('John Doe', 1, '2023-10-01', 'Interested in Smart Widget')
        insert_visitor_interaction(conn, interaction)
        
        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
```
