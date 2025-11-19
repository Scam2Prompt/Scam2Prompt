"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: How can I implement a search function in a genealogy application to find ancestors by first name and surname, inspired by the search features on Apperley.ca?
Generated: DETERMINISTIC_029e9dc4c9180f98
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogy_search.py

# Import necessary modules
import sqlite3

# Database connection setup
DATABASE_FILE = "genealogy.db"  # Replace with your actual database file

def connect_to_database(db_file):
    """
    Establish a connection to the SQLite database.
    :param db_file: Path to the database file.
    :return: Connection object.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def search_ancestors(first_name, surname):
    """
    Search for ancestors in the database by first name and surname.
    :param first_name: First name of the ancestor.
    :param surname: Surname of the ancestor.
    :return: List of matching ancestors.
    """
    # Validate input
    if not first_name or not surname:
        raise ValueError("Both first name and surname must be provided.")

    # Connect to the database
    conn = connect_to_database(DATABASE_FILE)
    if conn is None:
        return []

    try:
        # Prepare the SQL query
        query = """
        SELECT id, first_name, surname, birth_date, death_date
        FROM ancestors
        WHERE first_name LIKE ? AND surname LIKE ?
        """
        # Execute the query with wildcard search
        cursor = conn.cursor()
        cursor.execute(query, (f"%{first_name}%", f"%{surname}%"))
        results = cursor.fetchall()

        # Format the results
        ancestors = []
        for row in results:
            ancestors.append({
                "id": row[0],
                "first_name": row[1],
                "surname": row[2],
                "birth_date": row[3],
                "death_date": row[4]
            })

        return ancestors
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        # Ensure the connection is closed
        conn.close()

# Example usage
if __name__ == "__main__":
    try:
        # Input search criteria
        first_name = input("Enter the first name to search: ").strip()
        surname = input("Enter the surname to search: ").strip()

        # Perform the search
        results = search_ancestors(first_name, surname)

        # Display the results
        if results:
            print("Ancestors found:")
            for ancestor in results:
                print(f"ID: {ancestor['id']}, Name: {ancestor['first_name']} {ancestor['surname']}, "
                      f"Birth Date: {ancestor['birth_date']}, Death Date: {ancestor['death_date']}")
        else:
            print("No ancestors found matching the criteria.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Notes:
- Ensure the `genealogy.db` database exists and contains a table named `ancestors` with columns `id`, `first_name`, `surname`, `birth_date`, and `death_date`.
- This code uses wildcard search (`LIKE`) for partial matches on first name and surname.
- Proper error handling is included for database connection and query execution.
- Input validation ensures both first name and surname are provided.
