"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Recommend a suitable programming language and libraries for developing a data logging system for a metering skid in the oil and gas industry."
Generated: DETERMINISTIC_ba8290ec1bd18a49
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python is a suitable programming language for developing a data logging system for a metering skid in the oil and gas industry.
It is widely used for industrial applications due to its simplicity, extensive library support, and scalability.

Below is a production-ready implementation using Python with the following libraries:
- `pandas` for data manipulation and storage
- `sqlite3` for database storage
- `logging` for system logging
- `schedule` for periodic data logging
"""

import pandas as pd
import sqlite3
import logging
import schedule
import time
import random

# Configure logging
logging.basicConfig(
    filename='data_logging_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database setup
DB_FILE = 'metering_skid_data.db'

def initialize_database():
    """
    Initialize the SQLite database and create the necessary table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS metering_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                flow_rate REAL NOT NULL,
                pressure REAL NOT NULL,
                temperature REAL NOT NULL
            )
        """)
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
    finally:
        conn.close()

def log_data():
    """
    Simulate data collection from sensors and log it into the database.
    """
    try:
        # Simulate sensor data (replace with actual sensor readings in production)
        flow_rate = round(random.uniform(10.0, 100.0), 2)  # Example: Flow rate in m³/h
        pressure = round(random.uniform(50.0, 150.0), 2)   # Example: Pressure in bar
        temperature = round(random.uniform(20.0, 80.0), 2) # Example: Temperature in °C
        timestamp = pd.Timestamp.now()

        # Log data into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO metering_data (timestamp, flow_rate, pressure, temperature)
            VALUES (?, ?, ?, ?)
        """, (timestamp, flow_rate, pressure, temperature))
        conn.commit()
        logging.info(f"Data logged successfully: {timestamp}, Flow Rate: {flow_rate}, Pressure: {pressure}, Temperature: {temperature}")
    except sqlite3.Error as e:
        logging.error(f"Error logging data: {e}")
    finally:
        conn.close()

def export_data_to_csv():
    """
    Export the logged data from the database to a CSV file for further analysis.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        query = "SELECT * FROM metering_data"
        df = pd.read_sql_query(query, conn)
        csv_file = 'metering_data_export.csv'
        df.to_csv(csv_file, index=False)
        logging.info(f"Data exported to CSV successfully: {csv_file}")
    except Exception as e:
        logging.error(f"Error exporting data to CSV: {e}")
    finally:
        conn.close()

# Initialize the database
initialize_database()

# Schedule periodic data logging (e.g., every 10 seconds)
schedule.every(10).seconds.do(log_data)

# Run the scheduler
try:
    logging.info("Starting data logging system...")
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Data logging system stopped by user.")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
```
