"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write a Python function that retrieves and displays service offerings like "Asesoría Legal" and "Servicio Técnico" from a database, inspired by the services listed on Mass Compras.
Generated: DETERMINISTIC_e0b494aa69d6f972
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Tuple

def get_service_offerings(db_path: str) -> List[Tuple[int, str]]:
    """
    Retrieves service offerings from the database.

    Args:
        db_path (str): The path to the SQLite database file.

    Returns:
        List[Tuple[int, str]]: A list of tuples containing service ID and service name.

    Raises:
        sqlite3.Error: If there is an error connecting to the database or executing the query.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # SQL query to retrieve service offerings
        query = "SELECT id, name FROM services WHERE category IN ('Asesoría Legal', 'Servicio Técnico')"
        cursor.execute(query)

        # Fetch all results
        services = cursor.fetchall()

        return services

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

def display_services(services: List[Tuple[int, str]]) -> None:
    """
    Displays the retrieved service offerings.

    Args:
        services (List[Tuple[int, str]]): A list of tuples containing service ID and service name.
    """
    if not services:
        print("No services found.")
        return

    print("Service Offerings:")
    for service_id, service_name in services:
        print(f"ID: {service_id}, Name: {service_name}")

if __name__ == "__main__":
    # Path to the database file
    database_path = "path/to/your/database.db"

    # Retrieve and display service offerings
    service_offerings = get_service_offerings(database_path)
    display_services(service_offerings)
```
