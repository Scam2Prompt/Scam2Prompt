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

class ServiceDatabase:
    """
    A class to interact with the service database for aérogommage and parquet installation.
    """

    def __init__(self, db_path):
        """
        Initializes the ServiceDatabase instance.
        
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def connect_to_db(self):
        """
        Establishes a connection to the SQLite database.

        :return: SQLite connection object.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def get_service_details(self, service_type):
        """
        Retrieves service details for a given service type.

        :param service_type: Type of service to retrieve (e.g., 'aérogommage', 'parquet installation').
        :return: List of dictionaries containing service details.
        """
        result = []
        try:
            conn = self.connect_to_db()
            cursor = conn.cursor()

            # Query to fetch service details
            query = """
            SELECT service_id, name, description, price
            FROM services
            WHERE category = ?
            """

            cursor.execute(query, (service_type,))
            rows = cursor.fetchall()

            # Convert rows into a list of dictionaries
            for row in rows:
                result.append({
                    "service_id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "price": row[3]
                })

        except sqlite3.Error as e:
            print(f"Error retrieving service details: {e}")
        finally:
            if conn:
                conn.close()

        return result


# Example usage
if __name__ == "__main__":
    # Replace 'services.db' with the path to your actual database file
    db = ServiceDatabase('services.db')

    # Retrieve aérogommage service details
    aerogommage_services = db.get_service_details('aérogommage')
    print("Aérogommage Services:")
    for service in aerogommage_services:
        print(service)

    # Retrieve parquet installation service details
    parquet_services = db.get_service_details('parquet installation')
    print("\nParquet Installation Services:")
    for service in parquet_services:
        print(service)
```

**Note:** Ensure the `services` table in your database contains columns `service_id`, `name`, `description`, `price`, and `category` for this code to work as intended.
