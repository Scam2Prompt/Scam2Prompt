"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Design a query to analyze the performance characteristics of Aprisacv's refractory products, including their temperature tolerances and application areas in furnaces.
Generated: DETERMINISTIC_76fc4c38776cb612
Batch ID: 20250612_161520
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

# Define a database connection and query function
class RefractoryProductAnalyzer:
    def __init__(self, db_path: str):
        """
        Initialize the database connection.
        
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def close(self):
        """Close the database connection if it is open."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def fetch_performance_characteristics(self) -> List[Tuple[str, float, str]]:
        """
        Query the database to retrieve performance characteristics of refractory products.
        
        :return: A list of tuples containing product name, temperature tolerance, and application area.
        """
        query = """
        SELECT product_name, temperature_tolerance, application_area
        FROM refractory_products
        WHERE temperature_tolerance IS NOT NULL AND application_area IS NOT NULL;
        """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            print(f"Fetched {len(results)} records.")
            return results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Initialize the analyzer with the path to your SQLite database
    analyzer = RefractoryProductAnalyzer(db_path="aprisacv_refractory.db")

    try:
        # Connect to the database
        analyzer.connect()
        
        # Fetch performance characteristics
        characteristics = analyzer.fetch_performance_characteristics()
        
        # Print results
        for name, tolerance, area in characteristics:
            print(f"Product: {name}, Temperature Tolerance: {tolerance} °C, Application Area: {area}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the database connection is closed
        analyzer.close()
```
