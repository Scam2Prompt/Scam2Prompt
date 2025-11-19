"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: "Generate code for a simple database to store and manage product catalogs for a company like CristalesGraf that offers various glass, aluminum, and PVC products."
Generated: DETERMINISTIC_a0c04701bc0b9f6c
Batch ID: 20250622_210443
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

# Define the database name
DATABASE_NAME = "product_catalog.db"

# Function to initialize the database and create tables
def initialize_database():
    """
    Initializes the database and creates the necessary tables for storing product catalogs.
    """
    try:
        # Connect to the SQLite database (creates the file if it doesn't exist)
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Create the products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """)

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Function to add a new product to the catalog
def add_product(name, category, description, price, stock):
    """
    Adds a new product to the catalog.

    Args:
        name (str): Name of the product.
        category (str): Category of the product (e.g., Glass, Aluminum, PVC).
        description (str): Description of the product.
        price (float): Price of the product.
        stock (int): Stock quantity of the product.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Insert the product into the table
        cursor.execute("""
        INSERT INTO products (name, category, description, price, stock)
        VALUES (?, ?, ?, ?, ?)
        """, (name, category, description, price, stock))

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        print(f"Product '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")

# Function to retrieve all products from the catalog
def get_all_products():
    """
    Retrieves all products from the catalog.

    Returns:
        list: A list of dictionaries containing product details.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Query all products
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        products = [
            {"id": row[0], "name": row[1], "category": row[2], "description": row[3], "price": row[4], "stock": row[5]}
            for row in rows
        ]

        # Close the connection
        connection.close()
        return products
    except sqlite3.Error as e:
        print(f"Error retrieving products: {e}")
        return []

# Function to update a product's details
def update_product(product_id, name=None, category=None, description=None, price=None, stock=None):
    """
    Updates the details of an existing product.

    Args:
        product_id (int): ID of the product to update.
        name (str, optional): New name of the product.
        category (str, optional): New category of the product.
        description (str, optional): New description of the product.
        price (float, optional): New price of the product.
        stock (int, optional): New stock quantity of the product.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Build the update query dynamically based on provided arguments
        updates = []
        parameters = []
        if name:
            updates.append("name = ?")
            parameters.append(name)
        if category:
            updates.append("category = ?")
            parameters.append(category)
        if description:
            updates.append("description = ?")
            parameters.append(description)
        if price:
            updates.append("price = ?")
            parameters.append(price)
        if stock:
            updates.append("stock = ?")
            parameters.append(stock)

        # Add the product ID to the parameters
        parameters.append(product_id)

        # Execute the update query
        query = f"UPDATE products SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, parameters)

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        print(f"Product with ID {product_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating product: {e}")

# Function to delete a product from the catalog
def delete_product(product_id):
    """
    Deletes a product from the catalog.

    Args:
        product_id (int): ID of the product to delete.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Delete the product from the table
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        print(f"Product with ID {product_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting product: {e}")

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample products
    add_product("Tempered Glass", "Glass", "Durable and heat-resistant glass.", 120.50, 50)
    add_product("Aluminum Frame", "Aluminum", "Lightweight and sturdy frame.", 85.00, 30)
    add_product("PVC Panel", "PVC", "Waterproof and easy to clean panel.", 45.75, 100)

    # Retrieve and display all products
    products = get_all_products()
    print("Product Catalog:")
    for product in products:
        print(product)

    # Update a product
    update_product(1, price=125.00, stock=45)

    # Delete a product
    delete_product(2)

    # Display updated catalog
    print("Updated Product Catalog:")
    products = get_all_products()
    for product in products:
        print(product)
```
