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
from psycopg2 import sql
from datetime import datetime


class LogisticsManager:
    """
    A class to manage customer data, shipment tracking, and fleet availability for a logistics company.
    """

    def __init__(self, db_config):
        """
        Initialize the database connection.
        
        :param db_config: Dictionary containing database connection parameters.
        """
        try:
            self.conn = psycopg2.connect(
                dbname=db_config["dbname"],
                user=db_config["user"],
                password=db_config["password"],
                host=db_config["host"],
                port=db_config["port"]
            )
            self.cursor = self.conn.cursor()
            self._initialize_tables()
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            raise

    def _initialize_tables(self):
        """
        Create required tables if they do not exist in the database.
        """
        try:
            # Create customers table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    phone VARCHAR(15),
                    address TEXT
                );
            """)

            # Create shipments table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS shipments (
                    shipment_id SERIAL PRIMARY KEY,
                    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
                    origin VARCHAR(100) NOT NULL,
                    destination VARCHAR(100) NOT NULL,
                    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'In Transit', 'Delivered')),
                    estimated_delivery_date DATE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Create fleet table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS fleet (
                    vehicle_id SERIAL PRIMARY KEY,
                    vehicle_type VARCHAR(50),
                    availability BOOLEAN DEFAULT TRUE,
                    location VARCHAR(100)
                );
            """)

            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error initializing tables: {e}")
            raise

    def add_customer(self, name, email, phone=None, address=None):
        """
        Add a new customer to the database.

        :param name: Customer's name.
        :param email: Customer's email (must be unique).
        :param phone: Customer's phone number (optional).
        :param address: Customer's address (optional).
        """
        try:
            self.cursor.execute("""
                INSERT INTO customers (name, email, phone, address)
                VALUES (%s, %s, %s, %s);
            """, (name, email, phone, address))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error adding customer: {e}")
            raise

    def add_shipment(self, customer_id, origin, destination, status='Pending', estimated_delivery_date=None):
        """
        Add a new shipment to the database.

        :param customer_id: ID of the customer associated with the shipment.
        :param origin: Shipment origin location.
        :param destination: Shipment destination location.
        :param status: Shipment status (default is 'Pending').
        :param estimated_delivery_date: Estimated delivery date (optional).
        """
        try:
            self.cursor.execute("""
                INSERT INTO shipments (customer_id, origin, destination, status, estimated_delivery_date)
                VALUES (%s, %s, %s, %s, %s);
            """, (customer_id, origin, destination, status, estimated_delivery_date))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error adding shipment: {e}")
            raise

    def update_shipment_status(self, shipment_id, new_status):
        """
        Update the status of an existing shipment.

        :param shipment_id: ID of the shipment to update.
        :param new_status: New status for the shipment ('Pending', 'In Transit', or 'Delivered').
        """
        try:
            self.cursor.execute("""
                UPDATE shipments
                SET status = %s
                WHERE shipment_id = %s;
            """, (new_status, shipment_id))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error updating shipment status: {e}")
            raise

    def add_vehicle(self, vehicle_type, location, availability=True):
        """
        Add a new vehicle to the fleet.

        :param vehicle_type: Type of the vehicle (e.g., truck, van).
        :param location: Current location of the vehicle.
        :param availability: Availability status of the vehicle (default is True).
        """
        try:
            self.cursor.execute("""
                INSERT INTO fleet (vehicle_type, location, availability)
                VALUES (%s, %s, %s);
            """, (vehicle_type, location, availability))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error adding vehicle: {e}")
            raise

    def update_vehicle_availability(self, vehicle_id, availability):
        """
        Update the availability of a vehicle in the fleet.

        :param vehicle_id: ID of the vehicle to update.
        :param availability: New availability status (True or False).
        """
        try:
            self.cursor.execute("""
                UPDATE fleet
                SET availability = %s
                WHERE vehicle_id = %s;
            """, (availability, vehicle_id))
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error updating vehicle availability: {e}")
            raise

    def close_connection(self):
        """
        Close the database connection.
        """
        try:
            self.cursor.close()
            self.conn.close()
        except psycopg2.Error as e:
            print(f"Error closing connection: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Database connection configuration
    db_config = {
        "dbname": "logistics_db",
        "user": "postgres",
        "password": "your_password",
        "host": "localhost",
        "port": 5432
    }

    # Initialize the LogisticsManager
    manager = LogisticsManager(db_config)

    # Add a customer
    manager.add_customer(name="John Doe", email="john@example.com", phone="123-456-7890", address="123 Main St")

    # Add a shipment
    manager.add_shipment(customer_id=1, origin="New York", destination="Los Angeles", estimated_delivery_date=datetime(2023, 11, 1))

    # Update shipment status
    manager.update_shipment_status(shipment_id=1, new_status="In Transit")

    # Add a vehicle to the fleet
    manager.add_vehicle(vehicle_type="Truck", location="Chicago")

    # Update vehicle availability
    manager.update_vehicle_availability(vehicle_id=1, availability=False)

    # Close database connection
    manager.close_connection()
```
