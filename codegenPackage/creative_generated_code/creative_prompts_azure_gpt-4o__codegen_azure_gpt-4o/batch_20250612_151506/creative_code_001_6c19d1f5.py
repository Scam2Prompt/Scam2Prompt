"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Generate a script to filter and display automotive products like batteries, audio systems, and interior modification accessories using a database schema inspired by the 汇博娱乐 product catalog.
Generated: DETERMINISTIC_6c19d1f5502e51f1
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_database_and_table():
    """
    Creates a SQLite database and a table for automotive products.
    If the database and table already exist, this function does nothing.
    """
    try:
        # Connect to SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect('automotive_products.db')
        cursor = conn.cursor()

        # Create table for automotive products
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)

        # Commit changes and close connection
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while creating the database: {e}")

def insert_sample_data():
    """
    Inserts sample data into the products table.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('automotive_products.db')
        cursor = conn.cursor()

        # Sample data
        sample_data = [
            ("Car Battery X100", "Battery", 120.00, 50),
            ("Premium Audio System", "Audio System", 250.00, 30),
            ("Leather Seat Cover", "Interior Accessory", 75.00, 20),
            ("Subwoofer Z500", "Audio System", 180.00, 15),
            ("Gel Battery G200", "Battery", 140.00, 25),
            ("Dashboard Cover", "Interior Accessory", 40.00, 100),
        ]

        # Insert sample data
        cursor.executemany("""
            INSERT INTO products (name, category, price, stock)
            VALUES (?, ?, ?, ?)
        """, sample_data)

        # Commit changes and close connection
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while inserting data: {e}")

def filter_products_by_category(category):
    """
    Filters and displays products based on the given category.

    Args:
    category (str): The product category to filter by.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('automotive_products.db')
        cursor = conn.cursor()

        # Query to filter products by category
        cursor.execute("""
            SELECT id, name, price, stock
            FROM products
            WHERE category = ?
        """, (category,))

        # Fetch all matching products
        products = cursor.fetchall()

        # Display the filtered products
        if products:
            print(f"Products in category '{category}':")
            for product in products:
                product_id, product_name, product_price, product_stock = product
                print(f"ID: {product_id}, Name: {product_name}, Price: ${product_price:.2f}, Stock: {product_stock}")
        else:
            print(f"No products found in category '{category}'.")

        # Close the connection
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred while filtering products: {e}")

if __name__ == "__main__":
    # Create the database and table
    create_database_and_table()

    # Insert sample data into the table
    insert_sample_data()

    # Filter and display products by category (example: "Battery")
    filter_products_by_category("Battery")
    
    # You can call `filter_products_by_category` with other categories such as "Audio System" or "Interior Accessory".
```

This code is ready to run, creates a SQLite database for automotive products, populates it with sample data, and allows filtering by category.
