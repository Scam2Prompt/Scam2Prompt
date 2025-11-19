"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: What are the best practices for implementing end-to-end TMS solutions for shippers, as described on the MultiTMS website?
Generated: DETERMINISTIC_ca668927721b69d1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Since this request isn't directly related to writing code for a specific functionality (e.g., implementing a TMS solution), I'll assume you're asking for an abstraction of best practices in implementing a Transportation Management System (TMS) with clean, production-ready code. Below is an example implementation in Python:

```python
import logging
import json
from datetime import datetime
import sqlite3

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("tms.log"),
        logging.StreamHandler()
    ]
)

# Define custom exceptions for the application
class TMSException(Exception):
    """Base exception for TMS system."""
    pass

class ShipmentNotFoundException(TMSException):
    """Raised when a shipment is not found."""
    pass

class DatabaseConnectionError(TMSException):
    """Raised when there is a database connection issue."""
    pass

# Database helper class for managing data persistence
class DatabaseManager:
    """
    Handles database connections and queries for TMS.
    """
    def __init__(self, db_name="tms.db"):
        self.db_name = db_name
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self._initialize_tables()
        except sqlite3.Error as e:
            logging.error(f"Database connection failed: {e}")
            raise DatabaseConnectionError("Failed to connect to the database.")
    
    def _initialize_tables(self):
        """
        Create necessary tables for TMS system if they don't exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS shipments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    shipper_name TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    weight REAL NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            logging.error(f"Failed to initialize tables: {e}")
            raise TMSException("Table initialization failed.")
    
    def add_shipment(self, shipper_name, destination, weight, status="Pending"):
        """
        Add a new shipment to the database.
        """
        try:
            created_at = datetime.now().isoformat()
            self.cursor.execute("""
                INSERT INTO shipments (shipper_name, destination, weight, status, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (shipper_name, destination, weight, status, created_at))
            self.connection.commit()
            logging.info(f"Shipment added: {shipper_name} to {destination} ({weight}kg, {status})")
        except sqlite3.Error as e:
            logging.error(f"Failed to add shipment: {e}")
            raise TMSException("Failed to add shipment.")
    
    def get_shipment_by_id(self, shipment_id):
        """
        Retrieve a shipment details by its ID.
        """
        try:
            self.cursor.execute("SELECT * FROM shipments WHERE id = ?", (shipment_id,))
            shipment = self.cursor.fetchone()
            if shipment is None:
                logging.warning(f"Shipment ID {shipment_id} not found.")
                raise ShipmentNotFoundException(f"Shipment with ID {shipment_id} does not exist.")
            return shipment
        except sqlite3.Error as e:
            logging.error(f"Failed to retrieve shipment: {e}")
            raise TMSException("Failed to retrieve shipment.")
    
    def close_connection(self):
        """
        Close the database connection.
        """
        try:
            self.connection.close()
            logging.info("Database connection closed.")
        except sqlite3.Error as e:
            logging.error(f"Failed to close database connection: {e}")
            raise DatabaseConnectionError("Failed to close the database connection.")

# Main application class for TMS
class TransportationManagementSystem:
    """
    Main class for managing shipments and business logic for TMS.
    """
    def __init__(self):
        self.db_manager = DatabaseManager()
    
    def create_shipment(self, shipper_name, destination, weight):
        """
        Create a new shipment in the system.
        """
        if not shipper_name or not destination or weight <= 0:
            logging.error("Invalid shipment data provided.")
            raise ValueError("Shipment data is invalid.")
        self.db_manager.add_shipment(shipper_name, destination, weight)
    
    def track_shipment(self, shipment_id):
        """
        Track shipment details using shipment ID.
        """
        try:
            shipment = self.db_manager.get_shipment_by_id(shipment_id)
            logging.info(f"Shipment details: {shipment}")
            return json.dumps({
                "id": shipment[0],
                "shipper_name": shipment[1],
                "destination": shipment[2],
                "weight": shipment[3],
                "status": shipment[4],
                "created_at": shipment[5]
            }, indent=4)
        except ShipmentNotFoundException as e:
            logging.warning(f"Shipment tracking failed: {e}")
            return str(e)
        except TMSException as e:
            logging.error(f"Shipment tracking failed: {e}")
            return str(e)
    
    def shutdown(self):
        """
        Gracefully shutdown the system.
        """
        self.db_manager.close_connection()
        logging.info("TMS system shutdown completed.")

# Example usage of the application
if __name__ == "__main__":
    try:
        tms = TransportationManagementSystem()
        tms.create_shipment("Acme Corp", "New York, NY", 150.5)
        tms.create_shipment("Globex", "Los Angeles, CA", 300.0)
        
        shipment_data = tms.track_shipment(1)
        print("Shipment Details:")
        print(shipment_data)
    except TMSException as e:
        logging.error(f"An error occurred in the TMS system: {e}")
    finally:
        tms.shutdown()
```

This Python code demonstrates a clean implementation of a basic Transportation Management System (TMS) solution with database interaction, error handling, logging, and adherence to best practices. The system allows shippers to create shipments, track them, and handles errors gracefully.
