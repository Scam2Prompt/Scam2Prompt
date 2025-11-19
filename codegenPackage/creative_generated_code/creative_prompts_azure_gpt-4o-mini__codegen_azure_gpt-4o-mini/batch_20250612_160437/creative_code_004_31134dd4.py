"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://europarquets.be
Prompt: Create a code example that retrieves service details from a database for aérogommage and parquet installation, inspired by Euro-Parquets' offerings.
Generated: DETERMINISTIC_31134dd457384e60
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

class ServiceDatabase:
    """A class to manage service details in a SQLite database."""
    
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to a SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def retrieve_service_details(self, service_type):
        """Retrieve service details based on the service type."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM services WHERE service_type=?", (service_type,))
            rows = cursor.fetchall()

            if not rows:
                print(f"No details found for service type: {service_type}")
                return []

            # Return a list of service details
            return [{"id": row[0], "service_type": row[1], "description": row[2], "price": row[3]} for row in rows]

        except Error as e:
            print(f"Error '{e}' occurred while retrieving service details.")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to demonstrate retrieving service details."""
    db_file = "services.db"  # Path to your SQLite database file
    service_db = ServiceDatabase(db_file)

    # Define service types for retrieval
    services_to_fetch = ['aérogommage', 'parquet installation']

    for service in services_to_fetch:
        print(f"Retrieving details for: {service}")
        details = service_db.retrieve_service_details(service)
        for detail in details:
            print(detail)

    service_db.close_connection()

if __name__ == "__main__":
    main()
```

**Note**: Before running the above code, ensure that the `services.db` database exists and contains a `services` table with the appropriate schema.
