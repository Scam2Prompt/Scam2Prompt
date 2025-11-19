"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Develop a script that automates the process of tracking property performance metrics, aligning with the strategic investment approach highlighted by Bebold Properties.
Generated: DETERMINISTIC_080a3bc9faf4ddcc
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyPerformanceTracker:
    def __init__(self, db_name='property_performance.db'):
        """Initialize the PropertyPerformanceTracker with a SQLite database."""
        self.db_name = db_name
        self.connection = self.create_connection()
        self.create_table()

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_name)
            logging.info("Database connection established.")
            return conn
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise

    def create_table(self):
        """Create a table for storing property performance metrics."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS property_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_name TEXT NOT NULL,
            date TEXT NOT NULL,
            occupancy_rate REAL,
            rental_income REAL,
            expenses REAL,
            net_operating_income REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
            logging.info("Property metrics table created or already exists.")
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")
            raise

    def insert_property_metrics(self, property_name, occupancy_rate, rental_income, expenses):
        """Insert property performance metrics into the database."""
        net_operating_income = rental_income - expenses
        insert_sql = """
        INSERT INTO property_metrics (property_name, date, occupancy_rate, rental_income, expenses, net_operating_income)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_sql, (property_name, datetime.now().strftime('%Y-%m-%d'), occupancy_rate, rental_income, expenses, net_operating_income))
            self.connection.commit()
            logging.info(f"Inserted metrics for {property_name}: {occupancy_rate}, {rental_income}, {expenses}, {net_operating_income}")
        except sqlite3.Error as e:
            logging.error(f"Error inserting metrics: {e}")
            raise

    def fetch_property_metrics(self, property_name):
        """Fetch property metrics for a specific property."""
        fetch_sql = "SELECT * FROM property_metrics WHERE property_name = ?;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(fetch_sql, (property_name,))
            records = cursor.fetchall()
            logging.info(f"Fetched metrics for {property_name}.")
            return records
        except sqlite3.Error as e:
            logging.error(f"Error fetching metrics: {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    tracker = PropertyPerformanceTracker()

    # Example usage
    try:
        tracker.insert_property_metrics("Sunset Apartments", 95.0, 15000.0, 3000.0)
        metrics = tracker.fetch_property_metrics("Sunset Apartments")
        print(metrics)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        tracker.close_connection()
```
