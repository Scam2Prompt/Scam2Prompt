"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write a Python function that retrieves and displays service offerings like "Asesoría Legal" and "Servicio Técnico" from a database, inspired by the services listed on Mass Compras.
Generated: DETERMINISTIC_e0b494aa69d6f972
Batch ID: 20250612_162753
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

def get_service_offerings(db_path: str) -> List[Tuple[int, str]]:
    """
    Retrieves service offerings from the database.

    Args:
        db_path (str): The path to the SQLite database file.

    Returns:
        List[Tuple[int, str]]: A list of tuples containing the service ID and service name.

    Raises:
        sqlite3.Error: If there is an issue connecting to the database or executing the query.
    """
    try:
        # Establish a connection to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to select service offerings
        query = "SELECT id, name FROM services WHERE name IN ('Asesoría Legal', 'Servicio Técnico')"
        cursor.execute(query)

        # Fetch all results
        offerings = cursor.fetchall()

        return offerings

    except sqlite3.Error as e:
        print(f"An error occurred while accessing the database: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

def display_service_offerings(offerings: List[Tuple[int, str]]) -> None:
    """
    Displays the retrieved service offerings.

    Args:
        offerings (List[Tuple[int, str]]): A list of service offerings to display.
    """
    if not offerings:
        print("No service offerings found.")
        return
    
    print("Service Offerings:")
    for service_id, service_name in offerings:
        print(f"ID: {service_id}, Service Name: {service_name}")

if __name__ == "__main__":
    # Path to the SQLite database
    database_path = "path/to/your/database.db"
    
    # Retrieve and display service offerings
    service_offerings = get_service_offerings(database_path)
    display_service_offerings(service_offerings)
```
