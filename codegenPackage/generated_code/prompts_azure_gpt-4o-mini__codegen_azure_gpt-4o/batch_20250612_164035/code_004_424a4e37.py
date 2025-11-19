"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Write a sample code to connect to a plumbing service database and retrieve information about licensed plumbers specializing in slab leak detection in Graham, TX.
Generated: DETERMINISTIC_424a4e370b8a0301
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

def connect_to_database(db_path):
    """
    Establishes a connection to the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        sqlite3.Connection: Database connection object.
    """
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_licensed_plumbers(connection, specialization, city):
    """
    Retrieves information about licensed plumbers based on specialization and city.

    Args:
        connection (sqlite3.Connection): Database connection object.
        specialization (str): Specialization to filter plumbers (e.g., 'slab leak detection').
        city (str): City to filter plumbers (e.g., 'Graham, TX').

    Returns:
        list: List of dictionaries containing plumber information.
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT name, license_number, phone, email, specialization, city
        FROM plumbers
        WHERE specialization = ? AND city = ?
        """
        cursor.execute(query, (specialization, city))
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries for better readability
        plumbers = [
            {
                "name": row[0],
                "license_number": row[1],
                "phone": row[2],
                "email": row[3],
                "specialization": row[4],
                "city": row[5],
            }
            for row in rows
        ]
        return plumbers
    except sqlite3.Error as e:
        print(f"Error fetching plumbers: {e}")
        return []

def main():
    """
    Main function to connect to the database and retrieve plumber information.
    """
    # Path to the plumbing service database
    database_path = "plumbing_service.db"

    # Connect to the database
    connection = connect_to_database(database_path)
    if not connection:
        print("Failed to connect to the database. Exiting.")
        return

    # Define search criteria
    specialization = "slab leak detection"
    city = "Graham, TX"

    # Fetch licensed plumbers
    plumbers = fetch_licensed_plumbers(connection, specialization, city)

    # Display the results
    if plumbers:
        print("Licensed plumbers specializing in slab leak detection in Graham, TX:")
        for plumber in plumbers:
            print(f"Name: {plumber['name']}, License: {plumber['license_number']}, "
                  f"Phone: {plumber['phone']}, Email: {plumber['email']}")
    else:
        print("No plumbers found matching the criteria.")

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
```
