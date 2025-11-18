"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Provide a solution using Python and a database (e.g., PostgreSQL) to manage customer data, shipment tracking, and fleet availability for a logistics company operating nationwide.
Generated: DETERMINISTIC_89d2546ada3350e5
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import psycopg2
from psycopg2 import sql, extras
import logging
from contextlib import contextmanager

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection configuration
DB_CONFIG = {
    'dbname': 'logistics_db',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

@contextmanager
def db_connection():
    """Context manager for database connection."""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        yield conn
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        raise
    finally:
        if conn is not None:
            conn.close()

def create_tables():
    """Create the necessary tables in the database."""
    with db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    address TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS shipments (
                    shipment_id SERIAL PRIMARY KEY,
                    customer_id INT REFERENCES customers(customer_id),
                    tracking_number VARCHAR(50) NOT NULL UNIQUE,
                    status VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS fleet (
                    vehicle_id SERIAL PRIMARY KEY,
                    vehicle_type VARCHAR(50) NOT NULL,
                    availability BOOLEAN DEFAULT TRUE
                );
            """)
            conn.commit()
            logging.info("Tables created successfully.")

def add_customer(name, email, address):
    """Add a new customer to the database."""
    with db_connection() as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO customers (name, email, address)
                    VALUES (%s, %s, %s) RETURNING customer_id;
                """, (name, email, address))
                customer_id = cursor.fetchone()[0]
                conn.commit()
                logging.info(f"Customer added with ID: {customer_id}")
                return customer_id
            except psycopg2.IntegrityError:
                conn.rollback()
                logging.error("Error adding customer: Email must be unique.")
                raise

def track_shipment(tracking_number):
    """Retrieve shipment status by tracking number."""
    with db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT shipments.status FROM shipments
                WHERE tracking_number = %s;
            """, (tracking_number,))
            result = cursor.fetchone()
            if result:
                logging.info(f"Shipment status for {tracking_number}: {result[0]}")
                return result[0]
            else:
                logging.warning("Tracking number not found.")
                raise ValueError("Tracking number not found.")

def update_fleet_availability(vehicle_id, availability):
    """Update the availability status of a vehicle in the fleet."""
    with db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE fleet SET availability = %s
                WHERE vehicle_id = %s;
            """, (availability, vehicle_id))
            conn.commit()
            logging.info(f"Fleet availability updated for vehicle ID: {vehicle_id}")

if __name__ == "__main__":
    # Example usage
    create_tables()
    customer_id = add_customer("John Doe", "john.doe@example.com", "123 Elm St.")
    tracking_status = track_shipment("TRK123456")
    update_fleet_availability(1, False)
```
