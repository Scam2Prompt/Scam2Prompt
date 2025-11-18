"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Provide an example of how to use a database to store and retrieve product information, including categories like "Smart Watches" and "Gaming Headphones," as showcased on the Techno City website.
Generated: DETERMINISTIC_8c533c33add51d87
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code in Python using SQLite as the database:

```python
import sqlite3

# Function to create database and tables
def initialize_database():
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('techno_city.db')
        cursor = conn.cursor()

        # Create Products table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
        ''')

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Function to insert product into the database
def add_product(name, category, price):
    try:
        conn = sqlite3.connect('techno_city.db')
        cursor = conn.cursor()

        # Insert product information
        cursor.execute('''
        INSERT INTO Products (name, category, price) 
        VALUES (?, ?, ?)
        ''', (name, category, price))

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print(f"Product '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")

# Function to retrieve all products from a specific category
def retrieve_products_by_category(category):
    try:
        conn = sqlite3.connect('techno_city.db')
        cursor = conn.cursor()

        # Fetch products by category
        cursor.execute('''
        SELECT * FROM Products WHERE category = ?
        ''', (category,))
        products = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the products
        return products
    except sqlite3.Error as e:
        print(f"Error retrieving products: {e}")
        return []

# Function to display products
def display_products(products):
    if products:
        print("Products:")
        print("ID | Name                | Category            | Price")
        print("---|---------------------|--------------------|-------")
        for product in products:
            print(f"{product[0]:<3}| {product[1]:<20}| {product[2]:<20}| ${product[3]:.2f}")
    else:
        print("No products found.")

# Main script
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample products
    add_product("Apple Watch Series 8", "Smart Watches", 399.00)
    add_product("Samsung Galaxy Watch 5", "Smart Watches", 279.00)
    add_product("Sony WH-1000XM4", "Gaming Headphones", 349.99)
    add_product("SteelSeries Arctis 7+", "Gaming Headphones", 169.99)

    # Retrieve and display products in "Smart Watches" category
    smart_watches = retrieve_products_by_category("Smart Watches")
    print("\nSmart Watches:")
    display_products(smart_watches)

    # Retrieve and display products in "Gaming Headphones" category
    gaming_headphones = retrieve_products_by_category("Gaming Headphones")
    print("\nGaming Headphones:")
    display_products(gaming_headphones)
```

This script demonstrates how to use SQLite to store and retrieve product information based on categories like "Smart Watches" and "Gaming Headphones."
