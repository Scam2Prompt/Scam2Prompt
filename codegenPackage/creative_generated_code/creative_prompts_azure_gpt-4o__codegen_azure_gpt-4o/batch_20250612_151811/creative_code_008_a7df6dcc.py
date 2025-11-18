"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a system for outsourcing drivers, including features for matching drivers to haulage needs, inspired by Kalgate Technology's driver outsourcing services.
Generated: DETERMINISTIC_a7df6dcc1d365acd
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python-based solution for a driver outsourcing system:

```python
import sqlite3
from typing import List, Dict, Optional

# ----- Database Setup -----
DATABASE_NAME = "driver_outsourcing.db"

class Database:
    """Handles database operations."""
    def __init__(self, db_name: str = DATABASE_NAME):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for the system."""
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                city TEXT NOT NULL,
                available BOOLEAN NOT NULL DEFAULT 1
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS haulage_requests (
                request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                pickup_location TEXT NOT NULL,
                dropoff_location TEXT NOT NULL,
                required_city TEXT NOT NULL,
                matched_driver_id INTEGER,
                FOREIGN KEY (matched_driver_id) REFERENCES drivers(driver_id)
            )
            """)

    def execute_query(self, query: str, params: tuple = ()) -> List[Dict]:
        """Execute a query and return results."""
        with self.connection:
            cursor = self.connection.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

# ----- Models -----
class Driver:
    """Represents a driver."""
    def __init__(self, database: Database):
        self.database = database

    def add_driver(self, name: str, phone: str, city: str) -> bool:
        """Add a new driver to the system."""
        try:
            self.database.execute_query(
                "INSERT INTO drivers (name, phone, city) VALUES (?, ?, ?)",
                (name, phone, city)
            )
            return True
        except sqlite3.Error as e:
            print(f"Error adding driver: {e}")
            return False

    def get_available_drivers(self, city: Optional[str] = None) -> List[Dict]:
        """Fetch all available drivers, optionally filtered by city."""
        query = "SELECT * FROM drivers WHERE available = 1"
        params = ()
        if city:
            query += " AND city = ?"
            params = (city,)
        return self.database.execute_query(query, params)

    def mark_unavailable(self, driver_id: int) -> bool:
        """Mark a driver as unavailable."""
        try:
            self.database.execute_query(
                "UPDATE drivers SET available = 0 WHERE driver_id = ?",
                (driver_id,)
            )
            return True
        except sqlite3.Error as e:
            print(f"Error marking driver unavailable: {e}")
            return False

class HaulageRequest:
    """Represents a haulage request."""
    def __init__(self, database: Database):
        self.database = database

    def add_request(self, company_name: str, pickup_location: str, dropoff_location: str, required_city: str) -> bool:
        """Add a new haulage request to the system."""
        try:
            self.database.execute_query(
                "INSERT INTO haulage_requests (company_name, pickup_location, dropoff_location, required_city) VALUES (?, ?, ?, ?)",
                (company_name, pickup_location, dropoff_location, required_city)
            )
            return True
        except sqlite3.Error as e:
            print(f"Error adding haulage request: {e}")
            return False

    def match_driver(self, request_id: int) -> Optional[Dict]:
        """Match an available driver to a haulage request."""
        try:
            # Fetch the request
            request = self.database.execute_query("SELECT * FROM haulage_requests WHERE request_id = ?", (request_id,))
            if not request:
                print(f"No request found with ID {request_id}")
                return None

            required_city = request[0]["required_city"]
            # Fetch available driver
            driver = self.database.execute_query(
                "SELECT * FROM drivers WHERE available = 1 AND city = ? LIMIT 1",
                (required_city,)
            )

            if driver:
                driver_id = driver[0]["driver_id"]
                # Update the haulage request with matched driver
                self.database.execute_query(
                    "UPDATE haulage_requests SET matched_driver_id = ? WHERE request_id = ?",
                    (driver_id, request_id)
                )
                # Mark driver as unavailable
                Driver(self.database).mark_unavailable(driver_id)
                return driver[0]  # Return the matched driver
            else:
                print(f"No available driver found in city {required_city}")
                return None
        except sqlite3.Error as e:
            print(f"Error matching driver: {e}")
            return None

# ----- Application Logic -----
def main():
    """Driver Outsourcing System Main Function."""
    db = Database()
    driver_model = Driver(db)
    haulage_model = HaulageRequest(db)

    # Example: Adding drivers to the system
    driver_model.add_driver("John Doe", "123-456-7890", "New York")
    driver_model.add_driver("Jane Smith", "987-654-3210", "Los Angeles")

    # Example: Adding haulage requests
    haulage_model.add_request("ABC Logistics", "Warehouse A", "Warehouse B", "New York")
    haulage_model.add_request("XYZ Haulage", "Factory C", "Port D", "Los Angeles")

    # Example: Matching a driver for a haulage request
    matched_driver = haulage_model.match_driver(1)
    if matched_driver:
        print(f"Matched Driver: {matched_driver}")
    else:
        print("No driver matched.")

if __name__ == "__main__":
    main()
```

This system uses SQLite as the database and includes features for adding drivers, adding haulage requests, and matching drivers to requests based on city requirements. It includes error handling, comments, and follows best practices.
