"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: "Write a Python script to simulate a rental property search in Bucaramanga using the Dominguez Parra database."
Generated: DETERMINISTIC_6181092f820c7bef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import sys

# Database connection setup
DB_NAME = "dominguez_parra.db"

def connect_to_database(db_name):
    """
    Establishes a connection to the SQLite database.
    :param db_name: Name of the database file.
    :return: Connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def search_properties(conn, location, min_price, max_price, bedrooms):
    """
    Searches for rental properties in the database based on user criteria.
    :param conn: SQLite connection object.
    :param location: Desired location for the property.
    :param min_price: Minimum price for the property.
    :param max_price: Maximum price for the property.
    :param bedrooms: Minimum number of bedrooms required.
    :return: List of matching properties.
    """
    try:
        cursor = conn.cursor()
        query = """
        SELECT * FROM properties
        WHERE location = ?
        AND price BETWEEN ? AND ?
        AND bedrooms >= ?
        """
        cursor.execute(query, (location, min_price, max_price, bedrooms))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return []

def display_properties(properties):
    """
    Displays the list of properties in a user-friendly format.
    :param properties: List of properties to display.
    """
    if not properties:
        print("No properties found matching your criteria.")
        return

    print("Matching Properties:")
    print("-" * 50)
    for property in properties:
        property_id, location, price, bedrooms, description = property
        print(f"ID: {property_id}")
        print(f"Location: {location}")
        print(f"Price: ${price}")
        print(f"Bedrooms: {bedrooms}")
        print(f"Description: {description}")
        print("-" * 50)

def main():
    """
    Main function to simulate the rental property search.
    """
    print("Welcome to the Bucaramanga Rental Property Search!")
    
    # Get user input for search criteria
    location = input("Enter the desired location: ").strip()
    try:
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        bedrooms = int(input("Enter the minimum number of bedrooms: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for price and bedrooms.")
        sys.exit(1)

    # Connect to the database
    conn = connect_to_database(DB_NAME)

    # Search for properties
    properties = search_properties(conn, location, min_price, max_price, bedrooms)

    # Display the results
    display_properties(properties)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
```
