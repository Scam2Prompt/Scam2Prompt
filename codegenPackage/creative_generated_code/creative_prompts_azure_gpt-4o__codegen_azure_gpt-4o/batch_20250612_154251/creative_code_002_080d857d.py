"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clinicaidet.com.ve
Prompt: Generate code for querying a database of medical specialties and services offered by Grupo Clínico IDET, including filtering by location (e.g., Caracas or Barquisimeto).
Generated: DETERMINISTIC_080d857d4b2be0e5
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def query_medical_services(location):
    """
    Queries the database for medical specialties and services offered by Grupo Clínico IDET
    filtered by location (e.g., Caracas or Barquisimeto).

    Args:
        location (str): The location to filter services by (e.g., 'Caracas', 'Barquisimeto').

    Returns:
        list of tuple: A list of tuples containing the specialties and services offered in the given location.
    """
    # Validate location input
    if not location or not isinstance(location, str):
        raise ValueError("Invalid location. Please provide a valid string.")

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect('grupo_clinico_idet.db')  # Ensure the database file is correctly named and exists
        cursor = conn.cursor()

        # Prepare the SQL query
        query = """
        SELECT specialty, service, location 
        FROM medical_services 
        WHERE location = ?
        """
        
        # Execute the query with parameterized input to prevent SQL injection
        cursor.execute(query, (location,))
        
        # Fetch all results
        results = cursor.fetchall()
        
        return results

    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error occurred: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


# Example usage:
if __name__ == "__main__":
    try:
        location_to_filter = "Caracas"  # Change to desired location (e.g., 'Barquisimeto')
        services = query_medical_services(location_to_filter)

        if services:
            print(f"Medical specialties and services in {location_to_filter}:")
            for specialty, service, loc in services:
                print(f"Specialty: {specialty}, Service: {service}, Location: {loc}")
        else:
            print(f"No services found for location: {location_to_filter}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```

### Notes:
- Make sure you have a SQLite database named `grupo_clinico_idet.db` with a table named `medical_services` that includes columns `specialty`, `service`, and `location`.
- Update the database path and schema accordingly to match your setup.
