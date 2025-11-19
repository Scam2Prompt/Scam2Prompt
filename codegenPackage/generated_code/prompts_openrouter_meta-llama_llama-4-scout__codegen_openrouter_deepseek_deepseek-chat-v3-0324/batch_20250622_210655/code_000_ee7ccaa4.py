"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a Python script to manage a cleaning services company, including scheduling appointments and tracking customer information, inspired by the services offered by شركة إنجاز.
Generated: DETERMINISTIC_ee7ccaa42be157f3
Batch ID: 20250622_210655
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

class CleaningServiceManager:
    """A class to manage cleaning service appointments and customer information."""
    
    def __init__(self, db_name: str = "cleaning_service.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables in the database."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT NOT NULL,
                registration_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                duration_minutes INTEGER NOT NULL
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                status TEXT DEFAULT 'scheduled',
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
                FOREIGN KEY (service_id) REFERENCES services (service_id)
            )
        """)
        
        self.conn.commit()
    
    def add_customer(self, name: str, phone: str, address: str, email: str = None) -> int:
        """Add a new customer to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO customers (name, phone, email, address) VALUES (?, ?, ?, ?)",
                (name, phone, email, address)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding customer: {e}")
            return -1
    
    def add_service(self, name: str, price: float, duration_minutes: int, description: str = None) -> int:
        """Add a new service to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO services (name, description, price, duration_minutes) VALUES (?, ?, ?, ?)",
                (name, description, price, duration_minutes)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding service: {e}")
            return -1
    
    def schedule_appointment(self, customer_id: int, service_id: int, appointment_date: str, notes: str = None) -> int:
        """Schedule a new appointment."""
        try:
            # Validate the appointment date is in the future
            appointment_datetime = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
            if appointment_datetime < datetime.now():
                print("Error: Appointment date must be in the future")
                return -1
            
            self.cursor.execute(
                "INSERT INTO appointments (customer_id, service_id, appointment_date, notes) VALUES (?, ?, ?, ?)",
                (customer_id, service_id, appointment_date, notes)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD HH:MM")
            return -1
        except sqlite3.Error as e:
            print(f"Error scheduling appointment: {e}")
            return -1
    
    def get_customer_appointments(self, customer_id: int) -> List[Dict]:
        """Get all appointments for a specific customer."""
        try:
            self.cursor.execute("""
                SELECT a.appointment_id, s.name as service_name, a.appointment_date, a.status, a.notes
                FROM appointments a
                JOIN services s ON a.service_id = s.service_id
                WHERE a.customer_id = ?
                ORDER BY a.appointment_date
            """, (customer_id,))
            
            appointments = []
            for row in self.cursor.fetchall():
                appointments.append({
                    "appointment_id": row[0],
                    "service_name": row[1],
                    "appointment_date": row[2],
                    "status": row[3],
                    "notes": row[4]
                })
            return appointments
        except sqlite3.Error as e:
            print(f"Error retrieving appointments: {e}")
            return []
    
    def get_available_time_slots(self, date: str, service_id: int) -> List[str]:
        """Get available time slots for a specific date and service."""
        try:
            # Get service duration
            self.cursor.execute(
                "SELECT duration_minutes FROM services WHERE service_id = ?",
                (service_id,)
            )
            duration = self.cursor.fetchone()[0]
            
            # Get existing appointments for the date
            date_start = f"{date} 00:00:00"
            date_end = f"{date} 23:59:59"
            self.cursor.execute("""
                SELECT appointment_date FROM appointments
                WHERE date(appointment_date) = date(?)
                AND status != 'cancelled'
            """, (date,))
            
            booked_slots = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in self.cursor.fetchall()]
            
            # Generate all possible slots
            start_time = datetime.strptime(f"{date} 08:00", "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(f"{date} 18:00", "%Y-%m-%d %H:%M")
            slot_duration = timedelta(minutes=duration)
            
            available_slots = []
            current_slot = start_time
            
            while current_slot + slot_duration <= end_time:
                slot_available = True
                for booked in booked_slots:
                    if (current_slot < booked + timedelta(minutes=duration) and 
                        current_slot + slot_duration > booked):
                        slot_available = False
                        break
                
                if slot_available:
                    available_slots.append(current_slot.strftime("%H:%M"))
                
                current_slot += timedelta(minutes=30)  # Next slot starts every 30 minutes
            
            return available_slots
        except sqlite3.Error as e:
            print(f"Error retrieving available slots: {e}")
            return []
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD")
            return []
    
    def update_appointment_status(self, appointment_id: int, status: str) -> bool:
        """Update the status of an appointment."""
        valid_statuses = ['scheduled', 'completed', 'cancelled']
        if status not in valid_statuses:
            print(f"Error: Invalid status. Must be one of {valid_statuses}")
            return False
        
        try:
            self.cursor.execute(
                "UPDATE appointments SET status = ? WHERE appointment_id = ?",
                (status, appointment_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating appointment status: {e}")
            return False
    
    def get_customer_by_phone(self, phone: str) -> Optional[Dict]:
        """Retrieve customer information by phone number."""
        try:
            self.cursor.execute(
                "SELECT * FROM customers WHERE phone = ?",
                (phone,)
            )
            row = self.cursor.fetchone()
            if row:
                return {
                    "customer_id": row[0],
                    "name": row[1],
                    "phone": row[2],
                    "email": row[3],
                    "address": row[4],
                    "registration_date": row[5]
                }
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving customer: {e}")
            return None
    
    def get_all_services(self) -> List[Dict]:
        """Retrieve all available services."""
        try:
            self.cursor.execute("SELECT * FROM services")
            services = []
            for row in self.cursor.fetchall():
                services.append({
                    "service_id": row[0],
                    "name": row[1],
                    "description": row[2],
                    "price": row[3],
                    "duration_minutes": row[4]
                })
            return services
        except sqlite3.Error as e:
            print(f"Error retrieving services: {e}")
            return []
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# Example usage
if __name__ == "__main__":
    with CleaningServiceManager() as manager:
        # Add sample data
        customer_id = manager.add_customer(
            name="Ahmed Mohammed",
            phone="
