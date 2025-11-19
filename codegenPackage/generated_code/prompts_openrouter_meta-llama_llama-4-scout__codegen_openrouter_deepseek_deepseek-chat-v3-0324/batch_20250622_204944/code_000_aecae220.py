"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a Python script to manage appointments for a mobile windscreen repair service in Melbourne, considering factors like customer location and technician availability.
Generated: DETERMINISTIC_aecae2205a047dfe
Batch ID: 20250622_204944
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
import logging
import pytz

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MELBOURNE_TIMEZONE = pytz.timezone('Australia/Melbourne')
WORKING_HOURS = (8, 17)  # 8 AM to 5 PM
APPOINTMENT_DURATION = timedelta(hours=1)
MAX_TECHNICIANS = 5
DB_NAME = "windscreen_repair.db"

class AppointmentManager:
    def __init__(self):
        self.conn = self._create_connection()
        self._initialize_db()

    def _create_connection(self) -> sqlite3.Connection:
        """Create a database connection."""
        try:
            conn = sqlite3.connect(DB_NAME)
            return conn
        except sqlite3.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise

    def _initialize_db(self):
        """Initialize database tables if they don't exist."""
        try:
            cursor = self.conn.cursor()
            
            # Create customers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT,
                    address TEXT NOT NULL,
                    suburb TEXT NOT NULL,
                    postcode TEXT NOT NULL
                )
            ''')
            
            # Create technicians table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS technicians (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    is_available BOOLEAN DEFAULT 1
                )
            ''')
            
            # Create appointments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER NOT NULL,
                    technician_id INTEGER NOT NULL,
                    appointment_time DATETIME NOT NULL,
                    status TEXT DEFAULT 'scheduled',
                    notes TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customers (id),
                    FOREIGN KEY (technician_id) REFERENCES technicians (id)
                )
            ''')
            
            self.conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error initializing database: {e}")
            raise

    def add_customer(self, name: str, phone: str, address: str, suburb: str, postcode: str, email: str = None) -> int:
        """Add a new customer to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO customers (name, phone, email, address, suburb, postcode)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, phone, email, address, suburb, postcode))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error adding customer: {e}")
            raise

    def add_technician(self, name: str, phone: str, email: str) -> int:
        """Add a new technician to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO technicians (name, phone, email)
                VALUES (?, ?, ?)
            ''', (name, phone, email))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error adding technician: {e}")
            raise

    def get_available_technicians(self, date_time: datetime) -> List[Dict]:
        """Get available technicians for a given datetime."""
        try:
            # Convert to Melbourne timezone
            melbourne_time = date_time.astimezone(MELBOURNE_TIMEZONE)
            
            # Check if within working hours
            if not (WORKING_HOURS[0] <= melbourne_time.hour < WORKING_HOURS[1]):
                return []
            
            cursor = self.conn.cursor()
            
            # Find technicians not already booked at this time
            cursor.execute('''
                SELECT t.id, t.name, t.phone, t.email
                FROM technicians t
                WHERE t.is_available = 1
                AND t.id NOT IN (
                    SELECT a.technician_id
                    FROM appointments a
                    WHERE a.appointment_time = ?
                    AND a.status != 'cancelled'
                )
            ''', (melbourne_time.strftime('%Y-%m-%d %H:%M:%S'),))
            
            available_techs = []
            for row in cursor.fetchall():
                available_techs.append({
                    'id': row[0],
                    'name': row[1],
                    'phone': row[2],
                    'email': row[3]
                })
            
            return available_techs
        except sqlite3.Error as e:
            logger.error(f"Error getting available technicians: {e}")
            raise

    def schedule_appointment(self, customer_id: int, preferred_time: datetime, notes: str = None) -> Optional[int]:
        """Schedule an appointment for a customer."""
        try:
            available_techs = self.get_available_technicians(preferred_time)
            if not available_techs:
                logger.warning("No available technicians at the preferred time")
                return None
            
            # For simplicity, pick the first available technician
            # In production, you might want to consider technician proximity to customer
            technician_id = available_techs[0]['id']
            
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO appointments (customer_id, technician_id, appointment_time, notes)
                VALUES (?, ?, ?, ?)
            ''', (customer_id, technician_id, preferred_time.strftime('%Y-%m-%d %H:%M:%S'), notes))
            
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error scheduling appointment: {e}")
            raise

    def get_customer_appointments(self, customer_id: int) -> List[Dict]:
        """Get all appointments for a customer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT a.id, a.appointment_time, a.status, a.notes, 
                       t.name as technician_name, t.phone as technician_phone
                FROM appointments a
                JOIN technicians t ON a.technician_id = t.id
                WHERE a.customer_id = ?
                ORDER BY a.appointment_time DESC
            ''', (customer_id,))
            
            appointments = []
            for row in cursor.fetchall():
                appointments.append({
                    'id': row[0],
                    'appointment_time': datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'),
                    'status': row[2],
                    'notes': row[3],
                    'technician_name': row[4],
                    'technician_phone': row[5]
                })
            
            return appointments
        except sqlite3.Error as e:
            logger.error(f"Error getting customer appointments: {e}")
            raise

    def cancel_appointment(self, appointment_id: int) -> bool:
        """Cancel an appointment."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE appointments
                SET status = 'cancelled'
                WHERE id = ?
            ''', (appointment_id,))
            
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Error cancelling appointment: {e}")
            raise

    def reschedule_appointment(self, appointment_id: int, new_time: datetime) -> bool:
        """Reschedule an appointment to a new time."""
        try:
            # First check if the new time is available
            available_techs = self.get_available_technicians(new_time)
            if not available_techs:
                logger.warning("No available technicians at the new time")
                return False
            
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE appointments
                SET appointment_time = ?, status = 'rescheduled'
                WHERE id = ?
            ''', (new_time.strftime('%Y-%m-%d %H:%M:%S'), appointment_id))
            
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            logger.error(f"Error rescheduling appointment: {e}")
            raise

    def get_technician_schedule(self, technician_id: int, date: datetime) -> List[Dict]:
        """Get a technician's schedule for a specific date."""
        try:
            start_date = datetime(date.year, date.month, date.day, 0, 0, 0)
            end_date = datetime(date.year, date.month, date.day, 23, 59, 59)
            
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT a.id, a.appointment
