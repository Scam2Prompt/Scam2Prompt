"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a sample code to connect to a plumbing service database and retrieve information about licensed plumbers specializing in slab leak detection in Graham, TX.
Generated: DETERMINISTIC_424a4e370b8a0301
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def get_specialized_plumbers(city, specialization):
    """
    Function to connect to the plumbing service database and retrieve information
    about licensed plumbers specializing in a specific service for a given city.

    :param city: The city where plumbers are being searched (str).
    :param specialization: The specialization to filter plumbers by (str).
    :return: List of plumbers matching the criteria.
    """
    # Database file path (update as needed for production)
    database_path = "plumbing_service.db"
    
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # SQL query to find plumbers based on location and specialization
        query = """
        SELECT name, license_number, phone_number, email
        FROM plumbers
        WHERE city = ? AND specialization = ? AND is_licensed = 1
        """
        
        # Execute query with parameters to prevent SQL injection
        cursor.execute(query, (city, specialization))
        
        # Fetch all matching rows
        plumbers = cursor.fetchall()
        
        # Return results
        return plumbers

    except sqlite3.Error as e:
        # Log and handle any database errors
        print(f"Database error occurred: {e}")
        return []
    finally:
        # Ensure the database connection is always closed
        if connection:
            connection.close()


if __name__ == "__main__":
    # Sample usage
    city = "Graham, TX"
    specialization = "Slab Leak Detection"

    print(f"Retrieving plumbers specializing in '{specialization}' in {city}...\n")
    
    # Fetch plumbers
    licensed_plumbers = get_specialized_plumbers(city, specialization)
    
    if licensed_plumbers:
        print("Licensed Plumbers Found:")
        for plumber in licensed_plumbers:
            name, license_number, phone_number, email = plumber
            print(f"Name: {name}, License: {license_number}, Phone: {phone_number}, Email: {email}")
    else:
        print("No plumbers found matching the criteria.")
```
