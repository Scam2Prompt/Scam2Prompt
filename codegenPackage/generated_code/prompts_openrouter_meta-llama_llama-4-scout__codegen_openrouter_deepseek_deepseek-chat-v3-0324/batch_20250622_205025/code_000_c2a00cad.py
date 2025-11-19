"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Write a Python script to manage client appointments for a men's grooming salon like MEN'S GROOM, including features for booking, rescheduling, and canceling appointments."
Generated: DETERMINISTIC_c2a00cade6e70103
Batch ID: 20250622_205025
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
import pytz

class AppointmentManager:
    """A class to manage client appointments for a men's grooming salon."""
    
    def __init__(self, db_name='salon_appointments.db'):
        """Initialize the appointment manager with a database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary database tables if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                service_type TEXT NOT NULL,
                appointment_time DATETIME NOT NULL,
                status TEXT DEFAULT 'booked',
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        ''')
        self.conn.commit()
    
    def add_client(self, name, phone, email=None):
        """Add a new client to the database."""
        if not name or not phone:
            raise ValueError("Name and phone are required fields")
        
        try:
            self.cursor.execute('''
                INSERT INTO clients (name, phone, email)
                VALUES (?, ?, ?)
            ''', (name, phone, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            raise Exception(f"Error adding client: {str(e)}")
    
    def book_appointment(self, client_id, service_type, appointment_time):
        """Book a new appointment for a client."""
        if not self._validate_client_id(client_id):
            raise ValueError("Invalid client ID")
        
        if not service_type:
            raise ValueError("Service type is required")
        
        try:
            appointment_time = self._parse_datetime(appointment_time)
            if not self._is_valid_appointment_time(appointment_time):
                raise ValueError("Appointment time must be during business hours")
            
            if self._is_time_slot_available(appointment_time):
                self.cursor.execute('''
                    INSERT INTO appointments (client_id, service_type, appointment_time, status)
                    VALUES (?, ?, ?, 'booked')
                ''', (client_id, service_type, appointment_time))
                self.conn.commit()
                return self.cursor.lastrowid
            else:
                raise ValueError("Time slot is not available")
        except sqlite3.Error as e:
            raise Exception(f"Error booking appointment: {str(e)}")
    
    def reschedule_appointment(self, appointment_id, new_time):
        """Reschedule an existing appointment."""
        if not self._validate_appointment_id(appointment_id):
            raise ValueError("Invalid appointment ID")
        
        try:
            new_time = self._parse_datetime(new_time)
            if not self._is_valid_appointment_time(new_time):
                raise ValueError("New appointment time must be during business hours")
            
            if self._is_time_slot_available(new_time, exclude_appointment_id=appointment_id):
                self.cursor.execute('''
                    UPDATE appointments
                    SET appointment_time = ?
                    WHERE appointment_id = ?
                ''', (new_time, appointment_id))
                self.conn.commit()
                return True
            else:
                raise ValueError("New time slot is not available")
        except sqlite3.Error as e:
            raise Exception(f"Error rescheduling appointment: {str(e)}")
    
    def cancel_appointment(self, appointment_id):
        """Cancel an existing appointment."""
        if not self._validate_appointment_id(appointment_id):
            raise ValueError("Invalid appointment ID")
        
        try:
            self.cursor.execute('''
                UPDATE appointments
                SET status = 'cancelled'
                WHERE appointment_id = ?
            ''', (appointment_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            raise Exception(f"Error cancelling appointment: {str(e)}")
    
    def get_client_appointments(self, client_id):
        """Get all appointments for a specific client."""
        if not self._validate_client_id(client_id):
            raise ValueError("Invalid client ID")
        
        try:
            self.cursor.execute('''
                SELECT a.appointment_id, a.service_type, a.appointment_time, a.status
                FROM appointments a
                WHERE a.client_id = ?
                ORDER BY a.appointment_time
            ''', (client_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Error retrieving appointments: {str(e)}")
    
    def get_available_time_slots(self, date):
        """Get available time slots for a given date."""
        try:
            date = self._parse_date(date)
            start_time = datetime.combine(date, datetime.strptime('09:00', '%H:%M').time())
            end_time = datetime.combine(date, datetime.strptime('18:00', '%H:%M').time())
            
            # Get all booked appointments for the day
            self.cursor.execute('''
                SELECT appointment_time
                FROM appointments
                WHERE date(appointment_time) = date(?)
                AND status = 'booked'
            ''', (date,))
            booked_times = [row[0] for row in self.cursor.fetchall()]
            
            # Generate all possible 30-minute slots
            time_slots = []
            current_time = start_time
            while current_time < end_time:
                time_slots.append(current_time)
                current_time += timedelta(minutes=30)
            
            # Filter out booked times
            available_slots = [
                slot for slot in time_slots 
                if not any(
                    abs((slot - self._parse_datetime(booked_time)).total_seconds()) < 1800
                    for booked_time in booked_times
                )
            ]
            
            return available_slots
        except sqlite3.Error as e:
            raise Exception(f"Error retrieving available time slots: {str(e)}")
    
    def _validate_client_id(self, client_id):
        """Check if a client ID exists in the database."""
        self.cursor.execute('SELECT 1 FROM clients WHERE client_id = ?', (client_id,))
        return self.cursor.fetchone() is not None
    
    def _validate_appointment_id(self, appointment_id):
        """Check if an appointment ID exists in the database."""
        self.cursor.execute('SELECT 1 FROM appointments WHERE appointment_id = ?', (appointment_id,))
        return self.cursor.fetchone() is not None
    
    def _is_time_slot_available(self, appointment_time, exclude_appointment_id=None):
        """Check if a time slot is available."""
        query = '''
            SELECT 1 FROM appointments
            WHERE status = 'booked'
            AND abs(strftime('%s', appointment_time) - strftime('%s', ?)) < 1800
        '''
        params = [appointment_time]
        
        if exclude_appointment_id:
            query += ' AND appointment_id != ?'
            params.append(exclude_appointment_id)
        
        self.cursor.execute(query, params)
        return self.cursor.fetchone() is None
    
    def _is_valid_appointment_time(self, appointment_time):
        """Check if the appointment time is during business hours."""
        timezone = pytz.timezone('America/New_York')  # Example timezone
        localized_time = timezone.localize(appointment_time)
        
        # Business hours: 9AM to 6PM, Monday through Saturday
        if localized_time.weekday() >= 6:  # Sunday is 6
            return False
        
        opening_time = localized_time.replace(hour=9, minute=0, second=0)
        closing_time = localized_time.replace(hour=18, minute=0, second=0)
        
        return opening_time <= localized_time < closing_time
    
    def _parse_datetime(self, datetime_str):
        """Parse a datetime string into a datetime object."""
        if isinstance(datetime_str, datetime):
            return datetime_str
            
        try:
            return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        except ValueError:
            try:
                return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                raise ValueError("Invalid datetime format. Use 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DDTHH:MM'")
    
    def _parse_date(self, date_str):
        """Parse a date string into a date object."""
        if isinstance(date_str, datetime):
            return date_str.date()
            
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    def close(self):
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


#
