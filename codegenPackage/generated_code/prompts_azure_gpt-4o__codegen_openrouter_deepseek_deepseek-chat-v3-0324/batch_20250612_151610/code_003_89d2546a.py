"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Provide a solution using Python and a database (e.g., PostgreSQL) to manage customer data, shipment tracking, and fleet availability for a logistics company operating nationwide.
Generated: DETERMINISTIC_89d2546ada3350e5
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple

# Database configuration
DB_CONFIG = {
    'dbname': 'logistics_db',
    'user': 'logistics_user',
    'password': os.getenv('DB_PASSWORD', 'secure_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}

class DatabaseConnection:
    """Handles database connections with context management."""
    
    def __init__(self, config: Dict):
        self.config = config
        self.connection = None
    
    def __enter__(self):
        try:
            self.connection = psycopg2.connect(**self.config)
            self.connection.autocommit = False
            return self.connection
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to connect to database: {e}")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

class DatabaseError(Exception):
    """Custom exception for database operations."""
    pass

class LogisticsManager:
    """Main class for managing logistics operations."""
    
    @staticmethod
    def initialize_database():
        """Initialize the database schema."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    # Create tables
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS customers (
                            customer_id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            email VARCHAR(100) UNIQUE NOT NULL,
                            phone VARCHAR(20),
                            address TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS vehicles (
                            vehicle_id SERIAL PRIMARY KEY,
                            registration_number VARCHAR(20) UNIQUE NOT NULL,
                            vehicle_type VARCHAR(50) NOT NULL,
                            capacity_kg DECIMAL(10, 2) NOT NULL,
                            status VARCHAR(20) NOT NULL CHECK (
                                status IN ('available', 'in_maintenance', 'on_route')
                            ),
                            last_maintenance_date DATE,
                            next_maintenance_date DATE
                        );
                    """)
                    
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS shipments (
                            shipment_id SERIAL PRIMARY KEY,
                            customer_id INTEGER REFERENCES customers(customer_id),
                            origin TEXT NOT NULL,
                            destination TEXT NOT NULL,
                            weight_kg DECIMAL(10, 2) NOT NULL,
                            status VARCHAR(20) NOT NULL CHECK (
                                status IN ('pending', 'in_transit', 'delivered', 'cancelled')
                            ),
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            estimated_delivery_date TIMESTAMP,
                            actual_delivery_date TIMESTAMP,
                            vehicle_id INTEGER REFERENCES vehicles(vehicle_id)
                        );
                    """)
                    
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tracking (
                            tracking_id SERIAL PRIMARY KEY,
                            shipment_id INTEGER REFERENCES shipments(shipment_id),
                            location TEXT NOT NULL,
                            status_update VARCHAR(100) NOT NULL,
                            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)
                    
        except psycopg2.Error as e:
            raise DatabaseError(f"Database initialization failed: {e}")
    
    # Customer operations
    @staticmethod
    def add_customer(name: str, email: str, phone: str, address: str) -> int:
        """Add a new customer to the database."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO customers (name, email, phone, address)
                        VALUES (%s, %s, %s, %s)
                        RETURNING customer_id;
                    """, (name, email, phone, address))
                    customer_id = cursor.fetchone()[0]
                    return customer_id
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to add customer: {e}")
    
    @staticmethod
    def get_customer(customer_id: int) -> Optional[Dict]:
        """Retrieve customer details by ID."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute("""
                        SELECT * FROM customers WHERE customer_id = %s;
                    """, (customer_id,))
                    return cursor.fetchone()
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to get customer: {e}")
    
    # Vehicle operations
    @staticmethod
    def add_vehicle(registration_number: str, vehicle_type: str, capacity_kg: float) -> int:
        """Add a new vehicle to the fleet."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO vehicles (
                            registration_number, 
                            vehicle_type, 
                            capacity_kg, 
                            status
                        ) VALUES (%s, %s, %s, 'available')
                        RETURNING vehicle_id;
                    """, (registration_number, vehicle_type, capacity_kg))
                    vehicle_id = cursor.fetchone()[0]
                    return vehicle_id
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to add vehicle: {e}")
    
    @staticmethod
    def get_available_vehicles(min_capacity: float = 0) -> List[Dict]:
        """Retrieve available vehicles with optional minimum capacity."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute("""
                        SELECT * FROM vehicles 
                        WHERE status = 'available' 
                        AND capacity_kg >= %s;
                    """, (min_capacity,))
                    return cursor.fetchall()
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to get available vehicles: {e}")
    
    @staticmethod
    def update_vehicle_status(vehicle_id: int, status: str) -> bool:
        """Update vehicle status."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        UPDATE vehicles 
                        SET status = %s 
                        WHERE vehicle_id = %s;
                    """, (status, vehicle_id))
                    return cursor.rowcount > 0
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to update vehicle status: {e}")
    
    # Shipment operations
    @staticmethod
    def create_shipment(
        customer_id: int,
        origin: str,
        destination: str,
        weight_kg: float,
        estimated_delivery_date: datetime
    ) -> int:
        """Create a new shipment."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO shipments (
                            customer_id, 
                            origin, 
                            destination, 
                            weight_kg, 
                            status,
                            estimated_delivery_date
                        ) VALUES (%s, %s, %s, %s, 'pending', %s)
                        RETURNING shipment_id;
                    """, (customer_id, origin, destination, weight_kg, estimated_delivery_date))
                    shipment_id = cursor.fetchone()[0]
                    return shipment_id
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to create shipment: {e}")
    
    @staticmethod
    def assign_vehicle_to_shipment(shipment_id: int, vehicle_id: int) -> bool:
        """Assign a vehicle to a shipment and update statuses."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor() as cursor:
                    # Start transaction
                    cursor.execute("""
                        UPDATE shipments 
                        SET vehicle_id = %s, 
                            status = 'in_transit' 
                        WHERE shipment_id = %s;
                    """, (vehicle_id, shipment_id))
                    
                    cursor.execute("""
                        UPDATE vehicles 
                        SET status = 'on_route' 
                        WHERE vehicle_id = %s;
                    """, (vehicle_id,))
                    
                    return cursor.rowcount > 0
        except psycopg2.Error as e:
            raise DatabaseError(f"Failed to assign vehicle: {e}")
    
    @staticmethod
    def get_shipment_status(shipment_id: int) -> Optional[Dict]:
        """Get current status and tracking info for a shipment."""
        try:
            with DatabaseConnection(DB_CONFIG) as conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute("""
                        SELECT s.*, c.name as customer_name, 
                               v.registration_number as vehicle_reg
                        FROM shipments s
                        LEFT JOIN customers c ON s.customer_id = c.customer_id
                        LEFT JOIN vehicles v ON s.vehicle_id = v.vehicle
