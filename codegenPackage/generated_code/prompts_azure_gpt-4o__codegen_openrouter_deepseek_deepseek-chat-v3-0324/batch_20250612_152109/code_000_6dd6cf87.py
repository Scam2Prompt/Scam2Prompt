"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Write Python code to create a scheduling system for car repair appointments, including fields for service type (e.g., engine repair, suspension repair), car brand, and customer details. Use a database to store the appointments.
Generated: DETERMINISTIC_6dd6cf877c2c3ea5
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict

class CarRepairScheduler:
    """A scheduling system for car repair appointments."""
    
    def __init__(self, db_name: str = "car_repair_schedule.db"):
        """Initialize the scheduler with a SQLite database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                car_brand TEXT NOT NULL,
                car_model TEXT NOT NULL,
                service_type TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
            )
        """)
        
        self.conn.commit()
    
    def add_customer(self, name: str, phone: str, email: Optional[str] = None) -> int:
        """Add a new customer to the database.
        
        Args:
            name: Customer's full name
            phone: Customer's phone number
            email: Customer's email address (optional)
            
        Returns:
            The ID of the newly created customer
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def schedule_appointment(
        self,
        customer_id: int,
        car_brand: str,
        car_model: str,
        service_type: str,
        appointment_date: datetime,
        notes: Optional[str] = None
    ) -> int:
        """Schedule a new car repair appointment.
        
        Args:
            customer_id: ID of the customer
            car_brand: Brand of the car (e.g., Toyota, Ford)
            car_model: Model of the car
            service_type: Type of service needed
            appointment_date: Date and time of the appointment
            notes: Additional notes about the appointment (optional)
            
        Returns:
            The ID of the newly created appointment
        """
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO appointments 
            (customer_id, car_brand, car_model, service_type, appointment_date, notes)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (customer_id, car_brand, car_model, service_type, 
             appointment_date.isoformat(), notes)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_appointments_by_date(self, date: datetime) -> List[Dict]:
        """Get all appointments scheduled for a specific date.
        
        Args:
            date: Date to query appointments for
            
        Returns:
            List of appointment dictionaries with customer details
        """
        cursor = self.conn.cursor()
        date_str = date.date().isoformat()
        
        cursor.execute("""
            SELECT a.*, c.name, c.phone, c.email
            FROM appointments a
            JOIN customers c ON a.customer_id = c.customer_id
            WHERE date(a.appointment_date) = ?
            ORDER BY a.appointment_date
        """, (date_str,))
        
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_all_service_types(self) -> List[str]:
        """Get all distinct service types in the system.
        
        Returns:
            List of unique service types
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT service_type FROM appointments")
        return [row[0] for row in cursor.fetchall()]
    
    def cancel_appointment(self, appointment_id: int) -> bool:
        """Cancel an existing appointment.
        
        Args:
            appointment_id: ID of the appointment to cancel
            
        Returns:
            True if the appointment was found and canceled, False otherwise
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM appointments WHERE appointment_id = ?",
            (appointment_id,)
        )
        self.conn.commit()
        return cursor.rowcount > 0
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Enable use as a context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure connection is closed when exiting context."""
        self.close()


# Example usage
if __name__ == "__main__":
    with CarRepairScheduler() as scheduler:
        # Add a customer
        customer_id = scheduler.add_customer(
            name="John Doe",
            phone="555-1234",
            email="john@example.com"
        )
        
        # Schedule an appointment
        appointment_id = scheduler.schedule_appointment(
            customer_id=customer_id,
            car_brand="Toyota",
            car_model="Camry",
            service_type="Engine Repair",
            appointment_date=datetime(2023, 12, 15, 10, 30),
            notes="Check engine light is on"
        )
        
        # Get appointments for a date
        appointments = scheduler.get_appointments_by_date(datetime(2023, 12, 15))
        print("Appointments for Dec 15, 2023:")
        for appt in appointments:
            print(f"{appt['name']} - {appt['car_brand']} {appt['car_model']} - {appt['service_type']}")
```
