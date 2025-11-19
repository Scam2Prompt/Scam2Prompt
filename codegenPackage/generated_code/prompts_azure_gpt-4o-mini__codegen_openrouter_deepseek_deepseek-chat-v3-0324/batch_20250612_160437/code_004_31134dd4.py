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
from typing import Dict, List, Optional

class ServiceDatabase:
    """
    A class to interact with the database and retrieve service details.
    """

    def __init__(self, db_path: str = "services.db"):
        """
        Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()

    def connect(self):
        """Establish a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_service_details(self, service_type: str) -> List[Dict[str, str]]:
        """
        Retrieve details for a specific service type.
        
        Args:
            service_type: The type of service to query (e.g., 'aérogommage', 'parquet').
            
        Returns:
            A list of dictionaries containing service details.
            
        Raises:
            ValueError: If service_type is empty or None.
            sqlite3.Error: If there's a database error.
        """
        if not service_type:
            raise ValueError("Service type cannot be empty or None.")

        query = """
        SELECT id, name, description, price_range, duration 
        FROM services 
        WHERE service_type = ?
        """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (service_type.lower(),))
            services = [dict(row) for row in cursor.fetchall()]
            return services
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database error occurred: {e}")

    def initialize_database(self):
        """
        Initialize the database with sample data if it doesn't exist.
        """
        try:
            cursor = self.conn.cursor()
            
            # Create services table if it doesn't exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_type TEXT NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price_range TEXT NOT NULL,
                duration TEXT NOT NULL
            )
            """)
            
            # Insert sample data if table is empty
            cursor.execute("SELECT COUNT(*) FROM services")
            if cursor.fetchone()[0] == 0:
                sample_data = [
                    ('aérogommage', 'Basic Aérogommage', 
                     'Gentle cleaning without damaging surfaces', 
                     '€50-€100', '2-4 hours'),
                    ('aérogommage', 'Advanced Aérogommage', 
                     'Deep cleaning with protective coating', 
                     '€100-€200', '4-6 hours'),
                    ('parquet', 'Parquet Installation', 
                     'Professional installation of hardwood floors', 
                     '€30-€50 per m²', '1-3 days'),
                    ('parquet', 'Parquet Restoration', 
                     'Restoring old parquet to original condition', 
                     '€40-€70 per m²', '2-5 days')
                ]
                
                cursor.executemany("""
                INSERT INTO services (service_type, name, description, price_range, duration)
                VALUES (?, ?, ?, ?, ?)
                """, sample_data)
                self.conn.commit()
                
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Failed to initialize database: {e}")

def main():
    """
    Example usage of the ServiceDatabase class.
    """
    try:
        with ServiceDatabase() as db:
            db.initialize_database()
            
            # Get aérogommage services
            aerogommage_services = db.get_service_details('aérogommage')
            print("Aérogommage Services:")
            for service in aerogommage_services:
                print(f"{service['name']}: {service['description']} ({service['price_range']})")
            
            # Get parquet services
            parquet_services = db.get_service_details('parquet')
            print("\nParquet Services:")
            for service in parquet_services:
                print(f"{service['name']}: {service['description']} ({service['price_range']})")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
