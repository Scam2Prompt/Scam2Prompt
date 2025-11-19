"""
Generated Code Metadata:
========================
Original URL: https://trait-sniper.pro
Prompt: "Write a basic Python script to create a database for storing and querying user traits, akin to what Trait Sniper might use."
Generated: DETERMINISTIC_1fdfa0a5562f9fe8
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Constants for database and table names
DATABASE_NAME = "user_traits.db"
TABLE_NAME = "traits"

def create_database():
    """
    Creates a SQLite database and a table for storing user traits.
    """
    try:
        # Connect to the SQLite database (creates the file if it doesn't exist)
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Create the traits table if it doesn't already exist
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each record
            username TEXT NOT NULL,               -- Username of the user
            trait_name TEXT NOT NULL,             -- Name of the trait
            trait_value TEXT NOT NULL             -- Value of the trait
        );
        """)

        # Commit changes and close the connection
        connection.commit()
        print(f"Database '{DATABASE_NAME}' and table '{TABLE_NAME}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database or table: {e}")
    finally:
        if connection:
            connection.close()

def insert_trait(username, trait_name, trait_value):
    """
    Inserts a new trait record into the database.

    Args:
        username (str): The username of the user.
        trait_name (str): The name of the trait.
        trait_value (str): The value of the trait.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Insert the trait record into the table
        cursor.execute(f"""
        INSERT INTO {TABLE_NAME} (username, trait_name, trait_value)
        VALUES (?, ?, ?);
        """, (username, trait_name, trait_value))

        # Commit changes and close the connection
        connection.commit()
        print(f"Trait '{trait_name}' for user '{username}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting trait: {e}")
    finally:
        if connection:
            connection.close()

def query_traits_by_username(username):
    """
    Queries and retrieves all traits for a given username.

    Args:
        username (str): The username to query traits for.

    Returns:
        list: A list of tuples containing trait records.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        # Query traits for the given username
        cursor.execute(f"""
        SELECT trait_name, trait_value
        FROM {TABLE_NAME}
        WHERE username = ?;
        """, (username,))

        # Fetch all matching records
        traits = cursor.fetchall()
        return traits
    except sqlite3.Error as e:
        print(f"Error querying traits: {e}")
        return []
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    # Create the database and table
    create_database()

    # Example usage
    insert_trait("john_doe", "intelligence", "high")
    insert_trait("john_doe", "strength", "medium")
    insert_trait("jane_doe", "agility", "low")

    # Query traits for a specific user
    username_to_query = "john_doe"
    traits = query_traits_by_username(username_to_query)
    print(f"Traits for user '{username_to_query}':")
    for trait_name, trait_value in traits:
        print(f"- {trait_name}: {trait_value}")
```
