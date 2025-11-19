"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Build a hostel management system for schools that tracks room assignments and student details, similar to the Hostel module in Him Saral's ERP.
Generated: DETERMINISTIC_106fa0df8b1dc7d0
Batch ID: 20250612_153224
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
from typing import List, Dict, Optional

class HostelManagementSystem:
    """
    Hostel Management System for schools to track room assignments and student details.
    """
    
    def __init__(self, db_name: str = "hostel_management.db"):
        """
        Initialize the system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        # Students table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_number TEXT UNIQUE NOT NULL,
                gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
                contact_number TEXT,
                email TEXT,
                address TEXT,
                guardian_name TEXT,
                guardian_contact TEXT,
                date_of_birth TEXT,
                date_of_admission TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Hostels table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS hostels (
                hostel_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                total_rooms INTEGER NOT NULL,
                warden_name TEXT,
                warden_contact TEXT,
                description TEXT
            )
        """)
        
        # Rooms table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hostel_id INTEGER NOT NULL,
                room_number TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                current_occupancy INTEGER DEFAULT 0,
                room_type TEXT CHECK(room_type IN ('Single', 'Double', 'Dormitory')),
                FOREIGN KEY (hostel_id) REFERENCES hostels (hostel_id)
            )
        """)
        
        # Assignments table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                room_id INTEGER NOT NULL,
                date_assigned TEXT DEFAULT CURRENT_TIMESTAMP,
                date_vacated TEXT,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (room_id) REFERENCES rooms (room_id)
            )
        """)
        
        # Fees table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fees (
                fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                payment_date TEXT DEFAULT CURRENT_TIMESTAMP,
                due_date TEXT NOT NULL,
                status TEXT CHECK(status IN ('Paid', 'Unpaid', 'Partial')) DEFAULT 'Unpaid',
                description TEXT,
                FOREIGN KEY (student_id) REFERENCES students (student_id)
            )
        """)
        
        self.conn.commit()
    
    def add_student(self, name: str, roll_number: str, gender: str, 
                   contact_number: str = None, email: str = None, 
                   address: str = None, guardian_name: str = None, 
                   guardian_contact: str = None, date_of_birth: str = None) -> int:
        """
        Add a new student to the system.
        
        Args:
            name: Full name of the student
            roll_number: Unique roll number
            gender: Gender (Male/Female/Other)
            contact_number: Student's contact number
            email: Student's email
            address: Student's address
            guardian_name: Guardian's name
            guardian_contact: Guardian's contact number
            date_of_birth: Date of birth (YYYY-MM-DD)
            
        Returns:
            ID of the newly added student
        """
        try:
            self.cursor.execute("""
                INSERT INTO students (
                    name, roll_number, gender, contact_number, email, 
                    address, guardian_name, guardian_contact, date_of_birth
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, roll_number, gender, contact_number, email, 
                 address, guardian_name, guardian_contact, date_of_birth))
            
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Student with roll number {roll_number} already exists")
    
    def add_hostel(self, name: str, total_rooms: int, address: str = None, 
                  warden_name: str = None, warden_contact: str = None, 
                  description: str = None) -> int:
        """
        Add a new hostel to the system.
        
        Args:
            name: Name of the hostel
            total_rooms: Total number of rooms in the hostel
            address: Hostel address
            warden_name: Name of the warden
            warden_contact: Contact number of the warden
            description: Description of the hostel
            
        Returns:
            ID of the newly added hostel
        """
        self.cursor.execute("""
            INSERT INTO hostels (
                name, address, total_rooms, warden_name, 
                warden_contact, description
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (name, address, total_rooms, warden_name, 
             warden_contact, description))
        
        self.conn.commit()
        return self.cursor.lastrowid
    
    def add_room(self, hostel_id: int, room_number: str, capacity: int, 
                room_type: str = "Dormitory") -> int:
        """
        Add a new room to a hostel.
        
        Args:
            hostel_id: ID of the hostel
            room_number: Room number/identifier
            capacity: Maximum capacity of the room
            room_type: Type of room (Single/Double/Dormitory)
            
        Returns:
            ID of the newly added room
            
        Raises:
            ValueError: If hostel doesn't exist or capacity is invalid
        """
        # Check if hostel exists
        self.cursor.execute("SELECT 1 FROM hostels WHERE hostel_id = ?", (hostel_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Hostel with ID {hostel_id} does not exist")
        
        if capacity <= 0:
            raise ValueError("Room capacity must be positive")
        
        self.cursor.execute("""
            INSERT INTO rooms (
                hostel_id, room_number, capacity, room_type
            ) VALUES (?, ?, ?, ?)
        """, (hostel_id, room_number, capacity, room_type))
        
        self.conn.commit()
        return self.cursor.lastrowid
    
    def assign_student_to_room(self, student_id: int, room_id: int) -> int:
        """
        Assign a student to a room.
        
        Args:
            student_id: ID of the student
            room_id: ID of the room
            
        Returns:
            ID of the assignment record
            
        Raises:
            ValueError: If student or room doesn't exist, or room is full
        """
        # Check if student exists
        self.cursor.execute("SELECT 1 FROM students WHERE student_id = ?", (student_id,))
        if not self.cursor.fetchone():
            raise ValueError(f"Student with ID {student_id} does not exist")
        
        # Check if room exists and has capacity
        self.cursor.execute("""
            SELECT capacity, current_occupancy 
            FROM rooms 
            WHERE room_id = ?
        """, (room_id,))
        
        result = self.cursor.fetchone()
        if not result:
            raise ValueError(f"Room with ID {room_id} does not exist")
        
        capacity, occupancy = result
        if occupancy >= capacity:
            raise ValueError(f"Room {room_id} is already at full capacity")
        
        # Check if student already has an active assignment
        self.cursor.execute("""
            SELECT 1 
            FROM assignments 
            WHERE student_id = ? AND date_vacated IS NULL
        """, (student_id,))
        
        if self.cursor.fetchone():
            raise ValueError(f"Student {student_id} already has an active room assignment")
        
        # Create assignment
        self.cursor.execute("""
            INSERT INTO assignments (student_id, room_id)
            VALUES (?, ?)
        """, (student_id, room_id))
        
        # Update room occupancy
        self.cursor.execute("""
            UPDATE rooms 
            SET current_occupancy = current_occupancy + 1 
            WHERE room_id = ?
        """, (room_id,))
        
        self.conn.commit()
        return self.cursor.lastrowid
    
    def vacate_room(self, assignment_id: int) -> None:
        """
        Mark a room assignment as vacated.
        
        Args:
            assignment_id: ID of the assignment record
            
        Raises:
            ValueError: If assignment doesn't exist or is already vacated
        """
        # Check if assignment exists and is active
        self.cursor.execute("""
            SELECT 1 
            FROM assignments 
            WHERE assignment_id = ? AND date_vacated IS NULL
        """, (assignment_id
