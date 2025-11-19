"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to manage a handyman service business, including services like osmosis inversa installation, electrodomestic repair, and fontanería maintenance in Murcia.
Generated: DETERMINISTIC_5c5e9f99e744a0ab
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
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class HandymanService:
    """Class to manage handyman services in Murcia."""

    def __init__(self, db_name: str = "handyman_service.db"):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        """Create necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                duration_minutes INTEGER NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                service_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                status TEXT DEFAULT 'scheduled',
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (service_id) REFERENCES services (id)
            )
        """)
        self.conn.commit()

    def add_service(self, name: str, price: float, duration_minutes: int, description: str = "") -> int:
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

    def add_customer(self, name: str, phone: str, address: str, email: str = "") -> int:
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

    def schedule_appointment(self, customer_id: int, service_id: int, appointment_date: datetime, notes: str = "") -> int:
        """Schedule a new appointment."""
        try:
            self.cursor.execute(
                "INSERT INTO appointments (customer_id, service_id, appointment_date, notes) VALUES (?, ?, ?, ?)",
                (customer_id, service_id, appointment_date.isoformat(), notes)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error scheduling appointment: {e}")
            return -1

    def get_services(self) -> List[Dict]:
        """Get all available services."""
        try:
            self.cursor.execute("SELECT id, name, description, price, duration_minutes FROM services")
            return [dict(zip(['id', 'name', 'description', 'price', 'duration'], row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting services: {e}")
            return []

    def get_customers(self) -> List[Dict]:
        """Get all customers."""
        try:
            self.cursor.execute("SELECT id, name, phone, email, address FROM customers")
            return [dict(zip(['id', 'name', 'phone', 'email', 'address'], row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting customers: {e}")
            return []

    def get_appointments(self, date: Optional[datetime] = None) -> List[Dict]:
        """Get all appointments or appointments for a specific date."""
        try:
            if date:
                self.cursor.execute(
                    "SELECT a.id, c.name as customer_name, s.name as service_name, "
                    "a.appointment_date, a.status, a.notes "
                    "FROM appointments a "
                    "JOIN customers c ON a.customer_id = c.id "
                    "JOIN services s ON a.service_id = s.id "
                    "WHERE date(a.appointment_date) = date(?)",
                    (date.isoformat(),)
                )
            else:
                self.cursor.execute(
                    "SELECT a.id, c.name as customer_name, s.name as service_name, "
                    "a.appointment_date, a.status, a.notes "
                    "FROM appointments a "
                    "JOIN customers c ON a.customer_id = c.id "
                    "JOIN services s ON a.service_id = s.id"
                )
            return [dict(zip(['id', 'customer', 'service', 'date', 'status', 'notes'], row)) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error getting appointments: {e}")
            return []

    def update_appointment_status(self, appointment_id: int, status: str) -> bool:
        """Update the status of an appointment."""
        try:
            self.cursor.execute(
                "UPDATE appointments SET status = ? WHERE id = ?",
                (status, appointment_id)
            )
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating appointment status: {e}")
            return False

    def delete_appointment(self, appointment_id: int) -> bool:
        """Delete an appointment."""
        try:
            self.cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error deleting appointment: {e}")
            return False

    def close(self) -> None:
        """Close the database connection."""
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

def initialize_sample_data(service: HandymanService) -> None:
    """Initialize sample data for demonstration."""
    # Add sample services
    services = [
        ("Osmosis Inversa Installation", 150.0, 120, "Professional reverse osmosis system installation"),
        ("Electrodomestic Repair", 75.0, 60, "Repair of household appliances"),
        ("Fontanería Maintenance", 90.0, 90, "Plumbing maintenance and repairs")
    ]
    
    for name, price, duration, desc in services:
        service.add_service(name, price, duration, desc)

    # Add sample customers
    customers = [
        ("Juan Pérez", "123456789", "juan@example.com", "Calle Mayor 123, Murcia"),
        ("María García", "987654321", "maria@example.com", "Avenida Libertad 45, Murcia")
    ]
    
    for name, phone, email, address in customers:
        service.add_customer(name, phone, address, email)

if __name__ == "__main__":
    with HandymanService() as service:
        initialize_sample_data(service)
        
        # Example usage
        print("Available Services:")
        for svc in service.get_services():
            print(f"{svc['id']}: {svc['name']} - €{svc['price']} ({svc['duration']} mins)")
        
        print("\nCustomers:")
        for cust in service.get_customers():
            print(f"{cust['id']}: {cust['name']} - {cust['phone']}")
```
