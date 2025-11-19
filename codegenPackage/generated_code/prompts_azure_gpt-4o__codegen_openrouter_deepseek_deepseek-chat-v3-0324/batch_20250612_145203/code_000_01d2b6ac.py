"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Write Python code to create a scheduling system for mobile RV repair services within a 100-mile radius of Phoenix, Arizona, incorporating appointment booking and repair status tracking.
Generated: DETERMINISTIC_01d2b6ac90f6b88c
Batch ID: 20250612_145203
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
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass
import math
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
PHOENIX_COORDINATES = (33.4484, -112.0740)  # (latitude, longitude)
EARTH_RADIUS_MILES = 3958.8  # Earth's radius in miles
MAX_SERVICE_RADIUS = 100  # miles

@dataclass
class Customer:
    id: int
    name: str
    phone: str
    email: str
    address: str
    coordinates: Tuple[float, float]  # (latitude, longitude)

@dataclass
class Technician:
    id: int
    name: str
    phone: str
    email: str
    skills: List[str]
    available: bool

@dataclass
class RepairService:
    id: int
    name: str
    description: str
    duration_minutes: int

@dataclass
class Appointment:
    id: int
    customer_id: int
    technician_id: int
    service_id: int
    scheduled_time: datetime
    status: str  # 'scheduled', 'in-progress', 'completed', 'cancelled'
    notes: Optional[str] = None

class RVRepairScheduler:
    def __init__(self, db_path: str = 'rv_repair_scheduler.db'):
        """Initialize the scheduler with database connection."""
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create tables
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    skills TEXT NOT NULL,
                    available BOOLEAN NOT NULL DEFAULT 1
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS repair_services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    duration_minutes INTEGER NOT NULL
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    technician_id INTEGER NOT NULL,
                    service_id INTEGER NOT NULL,
                    scheduled_time DATETIME NOT NULL,
                    status TEXT NOT NULL,
                    notes TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (id),
                    FOREIGN KEY (technician_id) REFERENCES technicians (id),
                    FOREIGN KEY (service_id) REFERENCES repair_services (id)
                )
            ''')
            
            conn.commit()

    def _calculate_distance(self, coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """Calculate distance between two coordinates in miles using Haversine formula."""
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        
        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        # Haversine formula
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = EARTH_RADIUS_MILES * c
        
        return distance

    def is_within_service_area(self, coordinates: Tuple[float, float]) -> bool:
        """Check if given coordinates are within service area."""
        distance = self._calculate_distance(PHOENIX_COORDINATES, coordinates)
        return distance <= MAX_SERVICE_RADIUS

    def add_customer(self, name: str, phone: str, email: str, address: str, coordinates: Tuple[float, float]) -> int:
        """Add a new customer to the system."""
        if not self.is_within_service_area(coordinates):
            raise ValueError("Customer location is outside service area")
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO customers (name, phone, email, address, latitude, longitude)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, phone, email, address, coordinates[0], coordinates[1]))
            conn.commit()
            return cursor.lastrowid

    def add_technician(self, name: str, phone: str, email: str, skills: List[str]) -> int:
        """Add a new technician to the system."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO technicians (name, phone, email, skills, available)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, phone, email, ','.join(skills), True))
            conn.commit()
            return cursor.lastrowid

    def add_service(self, name: str, description: str, duration_minutes: int) -> int:
        """Add a new repair service to the system."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO repair_services (name, description, duration_minutes)
                VALUES (?, ?, ?)
            ''', (name, description, duration_minutes))
            conn.commit()
            return cursor.lastrowid

    def get_available_technicians(self, service_id: int, date: datetime) -> List[Technician]:
        """Get technicians available for a specific service on a given date."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get service duration
            cursor.execute('SELECT duration_minutes FROM repair_services WHERE id = ?', (service_id,))
            service = cursor.fetchone()
            if not service:
                raise ValueError("Service not found")
            duration = service[0]
            
            # Get technicians with matching skills
            cursor.execute('''
                SELECT t.id, t.name, t.phone, t.email, t.skills, t.available
                FROM technicians t
                WHERE t.available = 1 AND t.skills LIKE '%' || (
                    SELECT name FROM repair_services WHERE id = ?
                ) || '%'
            ''', (service_id,))
            
            technicians = []
            for row in cursor.fetchall():
                tech_id, name, phone, email, skills_str, available = row
                skills = skills_str.split(',')
                technicians.append(Technician(tech_id, name, phone, email, skills, available))
            
            # Filter out technicians with conflicting appointments
            available_techs = []
            start_time = date.replace(hour=8, minute=0, second=0)  # Business hours start at 8 AM
            end_time = date.replace(hour=17, minute=0, second=0)   # Business hours end at 5 PM
            
            for tech in technicians:
                cursor.execute('''
                    SELECT scheduled_time, duration_minutes
                    FROM appointments a
                    JOIN repair_services rs ON a.service_id = rs.id
                    WHERE a.technician_id = ? AND DATE(a.scheduled_time) = DATE(?)
                    AND a.status != 'cancelled'
                ''', (tech.id, date))
                
                busy_slots = []
                for row in cursor.fetchall():
                    appt_time, appt_duration = row
                    appt_end = datetime.strptime(appt_time, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=appt_duration)
                    busy_slots.append((datetime.strptime(appt_time, '%Y-%m-%d %H:%M:%S'), appt_end))
                
                # Check for availability in 30-minute increments
                current_time = start_time
                while current_time + timedelta(minutes=duration) <= end_time:
                    slot_end = current_time + timedelta(minutes=duration)
                    conflict = False
                    
                    for busy_start, busy_end in busy_slots:
                        if not (slot_end <= busy_start or
