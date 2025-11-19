"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Write a Python script to manage bus routes and schedules for a transportation company like Autocares Cosme, including features for tracking punctuality and vehicle maintenance.
Generated: DETERMINISTIC_ab53557aecbc07f7
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

class BusRouteManager:
    """
    A class to manage bus routes, schedules, punctuality tracking, and vehicle maintenance.
    """
    
    def __init__(self, db_name: str = "bus_management.db"):
        """
        Initialize the database connection and create tables if they don't exist.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables in the database if they don't exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS buses (
                bus_id INTEGER PRIMARY KEY AUTOINCREMENT,
                license_plate TEXT UNIQUE NOT NULL,
                capacity INTEGER NOT NULL,
                manufacturer TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                last_maintenance_date TEXT
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS routes (
                route_id INTEGER PRIMARY KEY AUTOINCREMENT,
                route_name TEXT UNIQUE NOT NULL,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                distance_km REAL NOT NULL,
                estimated_duration_min INTEGER NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedules (
                schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                route_id INTEGER NOT NULL,
                bus_id INTEGER NOT NULL,
                departure_time TEXT NOT NULL,
                arrival_time TEXT NOT NULL,
                driver_name TEXT NOT NULL,
                FOREIGN KEY (route_id) REFERENCES routes (route_id),
                FOREIGN KEY (bus_id) REFERENCES buses (bus_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS punctuality (
                punctuality_id INTEGER PRIMARY KEY AUTOINCREMENT,
                schedule_id INTEGER NOT NULL,
                actual_departure_time TEXT,
                actual_arrival_time TEXT,
                delay_minutes INTEGER DEFAULT 0,
                notes TEXT,
                FOREIGN KEY (schedule_id) REFERENCES schedules (schedule_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS maintenance (
                maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bus_id INTEGER NOT NULL,
                maintenance_date TEXT NOT NULL,
                maintenance_type TEXT NOT NULL,
                description TEXT,
                cost REAL NOT NULL,
                FOREIGN KEY (bus_id) REFERENCES buses (bus_id)
            )
        """)
        
        self.conn.commit()
    
    def add_bus(self, license_plate: str, capacity: int, manufacturer: str, 
                model: str, year: int) -> int:
        """
        Add a new bus to the database.
        Returns the bus_id of the newly added bus.
        """
        try:
            self.cursor.execute("""
                INSERT INTO buses (license_plate, capacity, manufacturer, model, year)
                VALUES (?, ?, ?, ?, ?)
            """, (license_plate, capacity, manufacturer, model, year))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Bus with this license plate already exists")
    
    def add_route(self, route_name: str, origin: str, destination: str, 
                  distance_km: float, estimated_duration_min: int) -> int:
        """
        Add a new route to the database.
        Returns the route_id of the newly added route.
        """
        try:
            self.cursor.execute("""
                INSERT INTO routes (route_name, origin, destination, distance_km, estimated_duration_min)
                VALUES (?, ?, ?, ?, ?)
            """, (route_name, origin, destination, distance_km, estimated_duration_min))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Route with this name already exists")
    
    def add_schedule(self, route_id: int, bus_id: int, departure_time: str, 
                     arrival_time: str, driver_name: str) -> int:
        """
        Add a new schedule to the database.
        Returns the schedule_id of the newly added schedule.
        """
        try:
            self.cursor.execute("""
                INSERT INTO schedules (route_id, bus_id, departure_time, arrival_time, driver_name)
                VALUES (?, ?, ?, ?, ?)
            """, (route_id, bus_id, departure_time, arrival_time, driver_name))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Error adding schedule: {str(e)}")
    
    def record_punctuality(self, schedule_id: int, actual_departure_time: str, 
                          actual_arrival_time: str, notes: str = "") -> int:
        """
        Record punctuality data for a schedule.
        Returns the punctuality_id of the new record.
        """
        # Get scheduled times
        self.cursor.execute("""
            SELECT departure_time, arrival_time 
            FROM schedules 
            WHERE schedule_id = ?
        """, (schedule_id,))
        scheduled_departure, scheduled_arrival = self.cursor.fetchone()
        
        # Calculate delays
        scheduled_departure_dt = datetime.strptime(scheduled_departure, "%Y-%m-%d %H:%M:%S")
        scheduled_arrival_dt = datetime.strptime(scheduled_arrival, "%Y-%m-%d %H:%M:%S")
        actual_departure_dt = datetime.strptime(actual_departure_time, "%Y-%m-%d %H:%M:%S")
        actual_arrival_dt = datetime.strptime(actual_arrival_time, "%Y-%m-%d %H:%M:%S")
        
        departure_delay = (actual_departure_dt - scheduled_departure_dt).total_seconds() / 60
        arrival_delay = (actual_arrival_dt - scheduled_arrival_dt).total_seconds() / 60
        
        # Record punctuality data
        self.cursor.execute("""
            INSERT INTO punctuality (
                schedule_id, actual_departure_time, actual_arrival_time, 
                delay_minutes, notes
            )
            VALUES (?, ?, ?, ?, ?)
        """, (schedule_id, actual_departure_time, actual_arrival_time, 
              max(departure_delay, arrival_delay), notes))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_maintenance(self, bus_id: int, maintenance_date: str, 
                       maintenance_type: str, description: str, cost: float) -> int:
        """
        Add a maintenance record for a bus.
        Returns the maintenance_id of the new record.
        """
        try:
            self.cursor.execute("""
                INSERT INTO maintenance (bus_id, maintenance_date, maintenance_type, description, cost)
                VALUES (?, ?, ?, ?, ?)
            """, (bus_id, maintenance_date, maintenance_type, description, cost))
            
            # Update last maintenance date for the bus
            self.cursor.execute("""
                UPDATE buses 
                SET last_maintenance_date = ?
                WHERE bus_id = ?
            """, (maintenance_date, bus_id))
            
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Error adding maintenance record: {str(e)}")
    
    def get_buses_needing_maintenance(self, days_threshold: int = 180) -> List[Dict]:
        """
        Get buses that haven't had maintenance in more than days_threshold days.
        """
        self.cursor.execute("""
            SELECT b.bus_id, b.license_plate, b.last_maintenance_date,
                   julianday('now') - julianday(b.last_maintenance_date) as days_since_maintenance
            FROM buses b
            WHERE b.last_maintenance_date IS NULL OR 
                  julianday('now') - julianday(b.last_maintenance_date) > ?
        """, (days_threshold,))
        
        buses = []
        for row in self.cursor.fetchall():
            buses.append({
                "bus_id": row[0],
                "license_plate": row[1],
                "last_maintenance_date": row[2],
                "days_since_maintenance": row[3]
            })
        return buses
    
    def get_route_punctuality_stats(self, route_id: int, days: int = 30) -> Dict:
        """
        Get punctuality statistics for a route over the last 'days' days.
        """
        # Get all schedules for this route in the time period
        cutoff_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        
        self.cursor.execute("""
            SELECT s.schedule_id, s.departure_time, p.delay_minutes
            FROM schedules s
            LEFT JOIN punctuality p ON s.schedule_id = p.schedule_id
            WHERE s.route_id = ? AND s.d
