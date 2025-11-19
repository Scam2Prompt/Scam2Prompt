"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orgairways.top
Prompt: Write a Python function that retrieves and displays the details of specific track cycling components, like "144BCD Chainsets" or "Track Helmets," from an online shop database.
Generated: DETERMINISTIC_1fbce02d501a5868
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

def fetch_cycling_component_details(component_name: str) -> List[Tuple]:
    """
    Fetches details of the specified track cycling component from the online shop database.

    Args:
        component_name (str): Name of the cycling component to search for (e.g., "144BCD Chainsets").

    Returns:
        List[Tuple]: A list of tuples containing the details of the matching component(s).
                     Each tuple represents a row from the database.
                     Returns an empty list if no results are found.
                     
    Raises:
        ValueError: If the component_name is empty or invalid.
    """
    # Validate that the component_name is not empty
    if not component_name.strip():
        raise ValueError("Component name must not be empty.")

    # Path to the SQLite database file
    database_path = 'online_shop.db'  # Update this path according to your setup

    # SQL query to fetch details for the specified component
    query = """
    SELECT *
    FROM track_cycling_components
    WHERE component_name = ?
    """

    try:
        # Establish a connection to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Execute the query with parameterized input to prevent SQL injection
        cursor.execute(query, (component_name,))
        
        # Fetch all matching rows
        results = cursor.fetchall()

    except sqlite3.Error as e:
        # Log or handle database errors
        print(f"Database error: {e}")
        results = []
        
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
        results = []

    finally:
        # Ensure the database connection is closed
        if 'conn' in locals():
            conn.close()

    return results

# Example usage:
if __name__ == "__main__":
    try:
        component_name = "144BCD Chainsets"  # Replace with desired component name
        details = fetch_cycling_component_details(component_name)
        
        if details:
            print("Component Details:")
            for row in details:
                print(row)
        else:
            print(f"No details found for component: {component_name}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as ex:
        print(f"Error: {ex}")
```
