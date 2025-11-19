"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Write a Python script to manage client appointments and loyalty programs for a waxing service like Depilar MG.
Generated: DETERMINISTIC_e90b9c68203968cc
Batch ID: 20250622_210650
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

class WaxingAppointmentManager:
    """A class to manage client appointments and loyalty programs for a waxing service."""
    
    def __init__(self, db_name: str = "waxing_service.db"):
        """Initialize the database connection and create necessary tables."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
        
    def _create_tables(self) -> None:
        """Create database tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT,
                join_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                service_type TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                duration INTEGER NOT NULL,
                price REAL NOT NULL,
                status TEXT DEFAULT 'scheduled',
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS loyalty_program (
                loyalty_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL UNIQUE,
                points INTEGER DEFAULT 0,
                visits INTEGER DEFAULT 0,
                last_visit TEXT,
                FOREIGN KEY (client_id) REFERENCES clients (client_id)
            )
        """)
        self.conn.commit()
    
    def add_client(self, name: str, phone: str, email: Optional[str] = None) -> int:
        """Add a new client to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)",
                (name, phone, email)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("A client with this phone number already exists.")
    
    def schedule_appointment(
        self,
        client_id: int,
        service_type: str,
        appointment_date: str,
        duration: int,
        price: float
    ) -> int:
        """Schedule a new appointment for a client."""
        try:
            self.cursor.execute(
                """INSERT INTO appointments 
                (client_id, service_type, appointment_date, duration, price)
                VALUES (?, ?, ?, ?, ?)""",
                (client_id, service_type, appointment_date, duration, price)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Invalid client ID provided.")
    
    def complete_appointment(self, appointment_id: int) -> None:
        """Mark an appointment as completed and update loyalty program."""
        self.cursor.execute(
            "UPDATE appointments SET status = 'completed' WHERE appointment_id = ?",
            (appointment_id,)
        )
        
        # Get client_id from the appointment
        self.cursor.execute(
            "SELECT client_id FROM appointments WHERE appointment_id = ?",
            (appointment_id,)
        )
        result = self.cursor.fetchone()
        if not result:
            raise ValueError("Appointment not found.")
        
        client_id = result[0]
        self._update_loyalty_program(client_id)
        self.conn.commit()
    
    def _update_loyalty_program(self, client_id: int) -> None:
        """Update loyalty program points and visits for a client."""
        # Check if client exists in loyalty program
        self.cursor.execute(
            "SELECT * FROM loyalty_program WHERE client_id = ?",
            (client_id,)
        )
        result = self.cursor.fetchone()
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        if result:
            # Update existing record
            self.cursor.execute(
                """UPDATE loyalty_program 
                SET points = points + 10, 
                    visits = visits + 1,
                    last_visit = ?
                WHERE client_id = ?""",
                (today, client_id)
            )
        else:
            # Create new record
            self.cursor.execute(
                """INSERT INTO loyalty_program 
                (client_id, points, visits, last_visit)
                VALUES (?, 10, 1, ?)""",
                (client_id, today)
            )
    
    def get_client_appointments(self, client_id: int) -> List[Dict]:
        """Get all appointments for a specific client."""
        self.cursor.execute(
            """SELECT appointment_id, service_type, appointment_date, 
            duration, price, status 
            FROM appointments 
            WHERE client_id = ?""",
            (client_id,)
        )
        appointments = self.cursor.fetchall()
        
        return [{
            "appointment_id": appt[0],
            "service_type": appt[1],
            "appointment_date": appt[2],
            "duration": appt[3],
            "price": appt[4],
            "status": appt[5]
        } for appt in appointments]
    
    def get_upcoming_appointments(self, days: int = 7) -> List[Dict]:
        """Get all appointments scheduled within the next X days."""
        today = datetime.now()
        end_date = (today + timedelta(days=days)).strftime("%Y-%m-%d")
        
        self.cursor.execute(
            """SELECT a.appointment_id, c.name, a.service_type, 
            a.appointment_date, a.duration, a.price, a.status
            FROM appointments a
            JOIN clients c ON a.client_id = c.client_id
            WHERE a.appointment_date BETWEEN date('now') AND ?""",
            (end_date,)
        )
        appointments = self.cursor.fetchall()
        
        return [{
            "appointment_id": appt[0],
            "client_name": appt[1],
            "service_type": appt[2],
            "appointment_date": appt[3],
            "duration": appt[4],
            "price": appt[5],
            "status": appt[6]
        } for appt in appointments]
    
    def get_loyalty_info(self, client_id: int) -> Optional[Dict]:
        """Get loyalty program information for a client."""
        self.cursor.execute(
            """SELECT points, visits, last_visit 
            FROM loyalty_program 
            WHERE client_id = ?""",
            (client_id,)
        )
        result = self.cursor.fetchone()
        
        if result:
            return {
                "points": result[0],
                "visits": result[1],
                "last_visit": result[2]
            }
        return None
    
    def redeem_loyalty_points(self, client_id: int, points: int) -> bool:
        """Redeem loyalty points for a client."""
        self.cursor.execute(
            "SELECT points FROM loyalty_program WHERE client_id = ?",
            (client_id,)
        )
        result = self.cursor.fetchone()
        
        if not result or result[0] < points:
            return False
        
        self.cursor.execute(
            "UPDATE loyalty_program SET points = points - ? WHERE client_id = ?",
            (points, client_id)
        )
        self.conn.commit()
        return True
    
    def cancel_appointment(self, appointment_id: int) -> bool:
        """Cancel an appointment if it hasn't been completed."""
        self.cursor.execute(
            "SELECT status FROM appointments WHERE appointment_id = ?",
            (appointment_id,)
        )
        result = self.cursor.fetchone()
        
        if not result or result[0] != 'scheduled':
            return False
        
        self.cursor.execute(
            "UPDATE appointments SET status = 'cancelled' WHERE appointment_id = ?",
            (appointment_id,)
        )
        self.conn.commit()
        return True
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
```
