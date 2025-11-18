"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Generate a Python script to query and filter properties by type, neighborhood, and price range, mimicking the search functionality described in the "Buscar Propietarios Arrendatarios Consignación" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_c71d6570b4187352
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def connect_to_database(db_name):
    """
    Establish a connection to the SQLite database.

    Args:
        db_name (str): Name of the database file.

    Returns:
        sqlite3.Connection: Database connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def create_properties_table(conn):
    """
    Create the properties table if it does not exist.

    Args:
        conn (sqlite3.Connection): Database connection object.
    """
    try:
        query = """
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_type TEXT NOT NULL,
            neighborhood TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
        conn.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating properties table: {e}")


def query_properties(conn, property_type=None, neighborhood=None, price_range=None):
    """
    Query properties based on type, neighborhood, and price range.

    Args:
        conn (sqlite3.Connection): Database connection object.
        property_type (str): Type of the property (e.g., 'House', 'Apartment').
        neighborhood (str): Neighborhood to filter by.
        price_range (tuple): Min and max price range (e.g., (500, 1500)).

    Returns:
        list: List of matching properties.
    """
    try:
        # Base query
        query = "SELECT * FROM properties WHERE 1=1"
        params = []

        # Add filters
        if property_type:
            query += " AND property_type = ?"
            params.append(property_type)
        if neighborhood:
            query += " AND neighborhood = ?"
            params.append(neighborhood)
        if price_range and len(price_range) == 2:
            query += " AND price BETWEEN ? AND ?"
            params.extend(price_range)

        # Execute the query
        cursor = conn.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error querying properties: {e}")
        return []


def add_sample_data(conn):
    """
    Add sample data to the properties table.

    Args:
        conn (sqlite3.Connection): Database connection object.
    """
    try:
        sample_data = [
            ("House", "Downtown", 1200.0),
            ("Apartment", "Suburbs", 800.0),
            ("Apartment", "Downtown", 1500.0),
            ("House", "Suburbs", 950.0),
        ]
        query = "INSERT INTO properties (property_type, neighborhood, price) VALUES (?, ?, ?)"
        conn.executemany(query, sample_data)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error adding sample data: {e}")


def main():
    """
    Main function to test property query functionality.
    """
    # Connect to the database
    db_name = "properties.db"
    conn = connect_to_database(db_name)
    if not conn:
        return

    # Create table and add sample data
    create_properties_table(conn)
    add_sample_data(conn)

    # Query properties
    print("Querying properties...")
    filtered_properties = query_properties(conn, property_type="Apartment", neighborhood="Downtown", price_range=(1000, 2000))
    if filtered_properties:
        print("Filtered Properties:")
        for property in filtered_properties:
            print(property)
    else:
        print("No properties found.")

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
```
