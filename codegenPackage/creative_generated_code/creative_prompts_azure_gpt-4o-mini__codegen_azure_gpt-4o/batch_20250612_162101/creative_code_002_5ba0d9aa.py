"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a function that retrieves specifications for Londritech computers, focusing on models with Intel i3 and i5 processors.
Generated: DETERMINISTIC_5ba0d9aa8df18821
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def get_londritech_computer_specs(database_path):
    """
    Retrieves specifications for Londritech computers with Intel i3 and i5 processors.

    Args:
        database_path (str): Path to the SQLite database file.

    Returns:
        list of dict: A list of dictionaries containing specifications of matching models.
    """
    try:
        # Establish a connection to the database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # SQL query to fetch specifications for Londritech models with Intel i3 or i5 processors
        query = """
        SELECT model_name, processor, ram_size, storage_size, price
        FROM computers
        WHERE brand = 'Londritech' AND (processor LIKE 'Intel i3%' OR processor LIKE 'Intel i5%');
        """

        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        # Format the results into a list of dictionaries
        specifications = []
        for row in results:
            specifications.append({
                "model_name": row[0],
                "processor": row[1],
                "ram_size": row[2],
                "storage_size": row[3],
                "price": row[4],
            })

        return specifications

    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error occurred: {e}")
        return []

    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if 'connection' in locals():
            connection.close()

# Example usage
if __name__ == "__main__":
    # Replace 'computers.db' with the actual path to your database
    database_path = "computers.db"
    specs = get_londritech_computer_specs(database_path)
    for spec in specs:
        print(spec)
```
