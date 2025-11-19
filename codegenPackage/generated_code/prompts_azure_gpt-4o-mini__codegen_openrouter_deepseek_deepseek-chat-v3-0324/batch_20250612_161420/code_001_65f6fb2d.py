"""
Generated Code Metadata:
========================
Original URL: https://masamot.com
Prompt: How can I implement a teacher attendance tracking system that aligns with the guidelines mentioned in the "Öğretmen – Memur Devam Devamsızlık ve Ekders Programı" from masamot.com?
Generated: DETERMINISTIC_65f6fb2d8241341a
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import sqlite3
from typing import List, Dict, Optional, Tuple

class TeacherAttendanceSystem:
    """
    A teacher attendance tracking system that aligns with the guidelines from "Öğretmen – Memur Devam Devamsızlık ve Ekders Programı".
    """
    
    def __init__(self, db_path: str = "teacher_attendance.db"):
        """
        Initialize the system with a SQLite database connection.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """
        Create necessary tables if they don't exist.
        """
        cursor = self.conn.cursor()
        
        # Teachers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            tc_no TEXT UNIQUE NOT NULL,
            branch TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('active', 'inactive', 'on_leave'))
        )
        """)
        
        # Attendance records table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER NOT NULL,
            date DATE NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('present', 'absent', 'late', 'excused')),
            check_in TIME,
            check_out TIME,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        )
        """)
        
        # Extra courses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS extra_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER NOT NULL,
            date DATE NOT NULL,
            course_hours INTEGER NOT NULL,
            description TEXT,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        )
        """)
        
        self.conn.commit()
    
    def add_teacher(self, name: str, surname: str, tc_no: str, branch: str, status: str = 'active') -> int:
        """
        Add a new teacher to the system.
        
        Args:
            name: Teacher's first name
            surname: Teacher's last name
            tc_no: Turkish ID number
            branch: Teacher's branch/subject
            status: Initial status (active, inactive, on_leave)
            
        Returns:
            ID of the newly added teacher
            
        Raises:
            ValueError: If status is invalid or required fields are missing
            sqlite3.IntegrityError: If TC no already exists
        """
        if status not in ('active', 'inactive', 'on_leave'):
            raise ValueError("Invalid status. Must be 'active', 'inactive', or 'on_leave'")
            
        if not all([name, surname, tc_no, branch]):
            raise ValueError("All fields are required")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO teachers (name, surname, tc_no, branch, status)
        VALUES (?, ?, ?, ?, ?)
        """, (name, surname, tc_no, branch, status))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def record_attendance(
        self,
        teacher_id: int,
        date: datetime.date,
        status: str,
        check_in: Optional[datetime.time] = None,
        check_out: Optional[datetime.time] = None
    ) -> int:
        """
        Record a teacher's attendance for a specific date.
        
        Args:
            teacher_id: ID of the teacher
            date: Date of attendance
            status: Attendance status (present, absent, late, excused)
            check_in: Check-in time (optional)
            check_out: Check-out time (optional)
            
        Returns:
            ID of the attendance record
            
        Raises:
            ValueError: If status is invalid or required fields are missing
        """
        if status not in ('present', 'absent', 'late', 'excused'):
            raise ValueError("Invalid status. Must be 'present', 'absent', 'late', or 'excused'")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO attendance (teacher_id, date, status, check_in, check_out)
        VALUES (?, ?, ?, ?, ?)
        """, (teacher_id, date, status, check_in, check_out))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def add_extra_course(
        self,
        teacher_id: int,
        date: datetime.date,
        course_hours: int,
        description: Optional[str] = None
    ) -> int:
        """
        Record extra courses taught by a teacher.
        
        Args:
            teacher_id: ID of the teacher
            date: Date of the extra course
            course_hours: Number of hours taught
            description: Optional description of the course
            
        Returns:
            ID of the extra course record
            
        Raises:
            ValueError: If course_hours is not positive
        """
        if course_hours <= 0:
            raise ValueError("Course hours must be positive")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO extra_courses (teacher_id, date, course_hours, description)
        VALUES (?, ?, ?, ?)
        """, (teacher_id, date, course_hours, description))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def get_teacher_attendance(
        self,
        teacher_id: int,
        start_date: datetime.date,
        end_date: datetime.date
    ) -> List[Dict]:
        """
        Get attendance records for a teacher within a date range.
        
        Args:
            teacher_id: ID of the teacher
            start_date: Start date of the range
            end_date: End date of the range
            
        Returns:
            List of attendance records as dictionaries
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT date, status, check_in, check_out
        FROM attendance
        WHERE teacher_id = ? AND date BETWEEN ? AND ?
        ORDER BY date
        """, (teacher_id, start_date, end_date))
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_monthly_summary(
        self,
        month: int,
        year: int
    ) -> Dict[int, Dict[str, int]]:
        """
        Get monthly attendance summary for all teachers.
        
        Args:
            month: Month (1-12)
            year: Year
            
        Returns:
            Dictionary mapping teacher IDs to their attendance counts
        """
        start_date = datetime.date(year, month, 1)
        if month == 12:
            end_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
            
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT teacher_id, status, COUNT(*) as count
        FROM attendance
        WHERE date BETWEEN ? AND ?
        GROUP BY teacher_id, status
        """, (start_date, end_date))
        
        result = {}
        for row in cursor.fetchall():
            teacher_id, status, count = row
            if teacher_id not in result:
                result[teacher_id] = {}
            result[teacher_id][status] = count
            
        return result
    
    def get_extra_courses(
        self,
        teacher_id: int,
        start_date: datetime.date,
        end_date: datetime.date
    ) -> List[Dict]:
        """
        Get extra courses taught by a teacher within a date range.
        
        Args:
            teacher_id: ID of the teacher
            start_date: Start date of the range
            end_date: End date of the range
            
        Returns:
            List of extra course records as dictionaries
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT date, course_hours, description
        FROM extra_courses
        WHERE teacher_id = ? AND date BETWEEN ? AND ?
        ORDER BY date
        """, (teacher_id, start_date, end_date))
        
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def update_teacher_status(self, teacher_id: int, new_status: str) -> None:
        """
        Update a teacher's status.
        
        Args:
            teacher_id: ID of the teacher
            new_status: New status (active, inactive, on_leave)
            
        Raises:
            ValueError: If status is invalid
        """
        if new_status not in ('active', 'inactive', 'on_leave'):
            raise ValueError("Invalid status. Must be 'active', 'inactive', or 'on_leave'")
            
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE teachers
        SET status = ?
        WHERE id = ?
        """, (new_status, teacher_id))
        
        self.conn.commit()
    
    def
