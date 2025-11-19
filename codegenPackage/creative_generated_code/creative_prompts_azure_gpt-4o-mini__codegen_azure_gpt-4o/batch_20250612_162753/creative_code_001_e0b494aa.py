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
from typing import List

def get_service_offerings(db_path: str) -> List[str]:
    """
    Retrieves and displays service offerings from the database.

    Args:
        db_path (str): The file path to the SQLite database.

    Returns:
        List[str]: A list of service offerings (e.g., "Asesoría Legal", "Servicio Técnico").
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Query to retrieve service offerings
        query = """
        SELECT service_name
        FROM services
        WHERE active = 1;  -- Only retrieve active services
        """
        
        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        # Extract service names from query results
        service_offerings = [row[0] for row in results]

        return service_offerings

    except sqlite3.Error as e:
        # Log and raise an error if database operation fails
        print(f"Database error occurred: {e}")
        raise

    finally:
        # Ensure the database connection is closed
        if 'connection' in locals():
            connection.close()


# Example usage:
if __name__ == "__main__":
    # Specify the path to your SQLite database
    database_path = "services.db"
    
    try:
        # Retrieve service offerings
        services = get_service_offerings(database_path)
        
        # Display service offerings
        if services:
            print("Available Services:")
            for service in services:
                print(f"- {service}")
        else:
            print("No active services found.")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```

### Notes:
- The code assumes there is a table named `services` in the database with columns `service_name` (string) and `active` (boolean or integer).
- Replace `"services.db"` with the actual path to your SQLite database.
- Ensure the database schema matches the query.
