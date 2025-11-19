"""
Generated Code Metadata:
========================
Original URL: https://europarquets.be
Prompt: Create a code example that retrieves service details from a database for aérogommage and parquet installation, inspired by Euro-Parquets' offerings.
Generated: DETERMINISTIC_31134dd457384e60
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Database connection and query function
def get_service_details(service_type):
    """
    Retrieves service details from the database based on the service type.

    Args:
        service_type (str): The type of service to retrieve details for (e.g., 'aérogommage', 'parquet installation').

    Returns:
        list: A list of dictionaries containing service details, or an empty list if no services are found.
    """
    # Validate input
    if not isinstance(service_type, str) or not service_type.strip():
        raise ValueError("Service type must be a non-empty string.")

    # Database connection
    try:
        conn = sqlite3.connect("services.db")  # Replace with your actual database file
        cursor = conn.cursor()

        # Query to fetch service details
        query = """
        SELECT id, name, description, price
        FROM services
        WHERE LOWER(service_type) = LOWER(?)
        """
        cursor.execute(query, (service_type,))
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        service_details = [
            {"id": row[0], "name": row[1], "description": row[2], "price": row[3]}
            for row in rows
        ]

        return service_details

    except sqlite3.Error as e:
        # Log and raise database errors
        print(f"Database error: {e}")
        raise

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


# Example usage
if __name__ == "__main__":
    try:
        # Retrieve details for aérogommage
        aerogommage_services = get_service_details("aérogommage")
        print("Aérogommage Services:")
        for service in aerogommage_services:
            print(service)

        # Retrieve details for parquet installation
        parquet_services = get_service_details("parquet installation")
        print("\nParquet Installation Services:")
        for service in parquet_services:
            print(service)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```

### Notes:
- Ensure the `services.db` database exists and contains a table named `services` with columns `id`, `name`, `description`, `price`, and `service_type`.
- Replace `services.db` with the actual path to your database file if necessary.
