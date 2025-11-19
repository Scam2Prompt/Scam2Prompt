"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Build a transportation management system for schools that tracks bus routes and schedules, as outlined in Him Saral's Transportation module.
Generated: DETERMINISTIC_976ff0f732b2dbef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
School Transportation Management System
This module manages bus routes, schedules, and student transportation details.
"""

from datetime import datetime, time
from typing import List, Dict, Optional
import sqlite3
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Bus:
    """Represents a school bus with its details."""
    bus_id: str
    registration_number: str
    capacity: int
    driver_name: str
    contact_number: str
    is_active: bool = True

@dataclass
class BusStop:
    """Represents a bus stop location."""
    stop_id: str
    name: str
    address: str
    latitude: float
    longitude: float

@dataclass
class Route:
    """Represents a bus route with multiple stops."""
    route_id: str
    name: str
    bus_id: str
    start_time: time
    end_time: time
    is_active: bool = True

@dataclass
class RouteStop:
    """Represents a stop within a route with sequence and timing."""
    route_stop_id: str
    route_id: str
    stop_id: str
    sequence: int
    arrival_time: time
    departure_time: time

@dataclass
class StudentTransport:
    """Represents a student's transportation details."""
    student_id: str
    route_id: str
    stop_id: str
    academic_year: str
    is_active: bool = True

class TransportationDB:
    """Database handler for transportation management system."""
    
    def __init__(self, db_path: str = 'transportation.db'):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
        
    def create_tables(self):
        """Create necessary tables in the database."""
        queries = [
            """CREATE TABLE IF NOT EXISTS buses (
                bus_id TEXT PRIMARY KEY,
                registration_number TEXT UNIQUE NOT NULL,
                capacity INTEGER NOT NULL,
                driver_name TEXT NOT NULL,
                contact_number TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1
            )""",
            """CREATE TABLE IF NOT EXISTS bus_stops (
                stop_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL
            )""",
            """CREATE TABLE IF NOT EXISTS routes (
                route_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                bus_id TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                FOREIGN KEY (bus_id) REFERENCES buses (bus_id)
            )""",
            """CREATE TABLE IF NOT EXISTS route_stops (
                route_stop_id TEXT PRIMARY KEY,
                route_id TEXT NOT NULL,
                stop_id TEXT NOT NULL,
                sequence INTEGER NOT NULL,
                arrival_time TEXT NOT NULL,
                departure_time TEXT NOT NULL,
                FOREIGN KEY (route_id) REFERENCES routes (route_id),
                FOREIGN KEY (stop_id) REFERENCES bus_stops (stop_id),
                UNIQUE (route_id, sequence)
            )""",
            """CREATE TABLE IF NOT EXISTS student_transport (
                student_id TEXT NOT NULL,
                route_id TEXT NOT NULL,
                stop_id TEXT NOT NULL,
                academic_year TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                PRIMARY KEY (student_id, academic_year),
                FOREIGN KEY (route_id) REFERENCES routes (route_id),
                FOREIGN KEY (stop_id) REFERENCES bus_stops (stop_id)
            )"""
        ]
        
        cursor = self.conn.cursor()
        try:
            for query in queries:
                cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating tables: {e}")
            self.conn.rollback()
            raise
        finally:
            cursor.close()
    
    def add_bus(self, bus: Bus) -> bool:
        """Add a new bus to the database."""
        query = """INSERT INTO buses 
                   (bus_id, registration_number, capacity, driver_name, contact_number, is_active)
                   VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (
                bus.bus_id, bus.registration_number, bus.capacity,
                bus.driver_name, bus.contact_number, bus.is_active
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error adding bus: {e}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()
    
    def get_bus(self, bus_id: str) -> Optional[Bus]:
        """Retrieve a bus by its ID."""
        query = "SELECT * FROM buses WHERE bus_id = ?"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (bus_id,))
            row = cursor.fetchone()
            if row:
                return Bus(*row)
            return None
        except sqlite3.Error as e:
            logger.error(f"Error getting bus: {e}")
            return None
        finally:
            cursor.close()
    
    def update_bus(self, bus: Bus) -> bool:
        """Update bus details."""
        query = """UPDATE buses SET 
                   registration_number = ?, capacity = ?, driver_name = ?,
                   contact_number = ?, is_active = ? WHERE bus_id = ?"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (
                bus.registration_number, bus.capacity, bus.driver_name,
                bus.contact_number, bus.is_active, bus.bus_id
            ))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Error updating bus: {e}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()
    
    def add_bus_stop(self, stop: BusStop) -> bool:
        """Add a new bus stop to the database."""
        query = """INSERT INTO bus_stops 
                   (stop_id, name, address, latitude, longitude)
                   VALUES (?, ?, ?, ?, ?)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (
                stop.stop_id, stop.name, stop.address,
                stop.latitude, stop.longitude
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error adding bus stop: {e}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()
    
    def get_bus_stop(self, stop_id: str) -> Optional[BusStop]:
        """Retrieve a bus stop by its ID."""
        query = "SELECT * FROM bus_stops WHERE stop_id = ?"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (stop_id,))
            row = cursor.fetchone()
            if row:
                return BusStop(*row)
            return None
        except sqlite3.Error as e:
            logger.error(f"Error getting bus stop: {e}")
            return None
        finally:
            cursor.close()
    
    def add_route(self, route: Route) -> bool:
        """Add a new route to the database."""
        query = """INSERT INTO routes 
                   (route_id, name, bus_id, start_time, end_time, is_active)
                   VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (
                route.route_id, route.name, route.bus_id,
                route.start_time.strftime('%H:%M'),
                route.end_time.strftime('%H:%M'),
                route.is_active
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error adding route: {e}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()
    
    def get_route(self, route_id: str) -> Optional[Route]:
        """Retrieve a route by its ID."""
        query = "SELECT * FROM routes WHERE route_id = ?"
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (route_id,))
            row = cursor.fetchone()
            if row:
                start_time = datetime.strptime(row[3], '%H:%M').time()
                end_time = datetime.strptime(row[4], '%H:%M').time()
                return Route(row[0], row[1], row[2], start_time, end_time, bool(row[5]))
            return None
        except sqlite3.Error as e:
            logger.error(f"Error getting route: {e}")
            return None
        finally:
            cursor.close()
    
    def add_route_stop(self, route_stop: RouteStop) -> bool:
        """Add a stop to a route."""
        query = """INSERT INTO route_stops
