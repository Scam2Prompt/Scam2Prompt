"""
Generated Code Metadata:
========================
Original URL: https://hajj.free.nf
Prompt: "Design a database schema for storing and managing Hajj pilgrimage information, including pilgrim details and travel itineraries."
Generated: DETERMINISTIC_eb32c4fff4283af0
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime
from typing import Optional

# Database connection and setup
def get_db_connection():
    conn = sqlite3.connect('hajj_pilgrimage.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database tables
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create pilgrims table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pilgrims (
        pilgrim_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        passport_number TEXT UNIQUE NOT NULL,
        nationality TEXT NOT NULL,
        gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
        date_of_birth DATE NOT NULL,
        phone_number TEXT NOT NULL,
        email TEXT,
        emergency_contact_name TEXT NOT NULL,
        emergency_contact_number TEXT NOT NULL,
        medical_conditions TEXT,
        special_requirements TEXT,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT CHECK(status IN ('Registered', 'Approved', 'Rejected', 'Completed')) DEFAULT 'Registered'
    )
    ''')

    # Create travel_itineraries table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS travel_itineraries (
        itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pilgrim_id INTEGER NOT NULL,
        departure_city TEXT NOT NULL,
        departure_date DATE NOT NULL,
        arrival_city TEXT NOT NULL,
        arrival_date DATE NOT NULL,
        airline TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        accommodation_makkah TEXT NOT NULL,
        accommodation_madinah TEXT,
        package_type TEXT CHECK(package_type IN ('Standard', 'Premium', 'VIP')) NOT NULL,
        FOREIGN KEY (pilgrim_id) REFERENCES pilgrims (pilgrim_id) ON DELETE CASCADE
    )
    ''')

    # Create payments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pilgrim_id INTEGER NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        payment_method TEXT CHECK(payment_method IN ('Credit Card', 'Bank Transfer', 'Cash')) NOT NULL,
        transaction_reference TEXT,
        status TEXT CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')) DEFAULT 'Pending',
        FOREIGN KEY (pilgrim_id) REFERENCES pilgrims (pilgrim_id) ON DELETE CASCADE
    )
    ''')

    # Create documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        document_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pilgrim_id INTEGER NOT NULL,
        document_type TEXT CHECK(document_type IN ('Passport', 'Visa', 'Vaccination', 'Other')) NOT NULL,
        document_number TEXT NOT NULL,
        issue_date DATE,
        expiry_date DATE,
        file_path TEXT NOT NULL,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (pilgrim_id) REFERENCES pilgrims (pilgrim_id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()

# Sample CRUD operations
class PilgrimManager:
    @staticmethod
    def add_pilgrim(
        full_name: str,
        passport_number: str,
        nationality: str,
        gender: str,
        date_of_birth: str,
        phone_number: str,
        emergency_contact_name: str,
        emergency_contact_number: str,
        email: Optional[str] = None,
        medical_conditions: Optional[str] = None,
        special_requirements: Optional[str] = None
    ) -> int:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pilgrims (
                    full_name, passport_number, nationality, gender, date_of_birth,
                    phone_number, email, emergency_contact_name, emergency_contact_number,
                    medical_conditions, special_requirements
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                full_name, passport_number, nationality, gender, date_of_birth,
                phone_number, email, emergency_contact_name, emergency_contact_number,
                medical_conditions, special_requirements
            ))
            pilgrim_id = cursor.lastrowid
            conn.commit()
            return pilgrim_id
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @staticmethod
    def get_pilgrim(pilgrim_id: int) -> Optional[dict]:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM pilgrims WHERE pilgrim_id = ?', (pilgrim_id,))
            pilgrim = cursor.fetchone()
            return dict(pilgrim) if pilgrim else None
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

class ItineraryManager:
    @staticmethod
    def add_itinerary(
        pilgrim_id: int,
        departure_city: str,
        departure_date: str,
        arrival_city: str,
        arrival_date: str,
        airline: str,
        flight_number: str,
        accommodation_makkah: str,
        package_type: str,
        accommodation_madinah: Optional[str] = None
    ) -> int:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO travel_itineraries (
                    pilgrim_id, departure_city, departure_date, arrival_city, arrival_date,
                    airline, flight_number, accommodation_makkah, accommodation_madinah, package_type
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                pilgrim_id, departure_city, departure_date, arrival_city, arrival_date,
                airline, flight_number, accommodation_makkah, accommodation_madinah, package_type
            ))
            itinerary_id = cursor.lastrowid
            conn.commit()
            return itinerary_id
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

# Initialize the database when this module is imported
init_db()
```
