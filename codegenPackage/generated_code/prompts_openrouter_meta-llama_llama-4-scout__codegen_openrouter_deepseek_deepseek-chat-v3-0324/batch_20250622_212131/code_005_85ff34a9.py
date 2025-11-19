"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "Create a simple time tracking application recommendation for small businesses."
Generated: DETERMINISTIC_85ff34a9d1067355
Batch ID: 20250622_212131
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
from typing import Optional, List, Tuple

class TimeTracker:
    """
    A simple time tracking application for small businesses.
    Allows employees to clock in/out and managers to view reports.
    """
    
    def __init__(self, db_name: str = "time_tracker.db"):
        """
        Initialize the time tracker with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create employees table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT,
                    is_active BOOLEAN DEFAULT 1
                )
            """)
            
            # Create time_entries table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS time_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    clock_in TIMESTAMP NOT NULL,
                    clock_out TIMESTAMP,
                    notes TEXT,
                    FOREIGN KEY (employee_id) REFERENCES employees(id)
                )
            """)
            
            conn.commit()
    
    def add_employee(self, name: str, position: str) -> int:
        """
        Add a new employee to the system.
        
        Args:
            name: Employee's full name
            position: Employee's position/job title
            
        Returns:
            ID of the newly created employee
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (name, position) VALUES (?, ?)",
                (name, position)
            )
            conn.commit()
            return cursor.lastrowid
    
    def clock_in(self, employee_id: int, notes: str = "") -> int:
        """
        Record a clock-in event for an employee.
        
        Args:
            employee_id: ID of the employee
            notes: Optional notes about the shift
            
        Returns:
            ID of the time entry
            
        Raises:
            ValueError: If employee doesn't exist or is already clocked in
        """
        if not self._is_employee_active(employee_id):
            raise ValueError("Employee does not exist or is inactive")
            
        if self._is_clocked_in(employee_id):
            raise ValueError("Employee is already clocked in")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO time_entries 
                   (employee_id, clock_in, notes) 
                   VALUES (?, ?, ?)""",
                (employee_id, datetime.now(), notes)
            )
            conn.commit()
            return cursor.lastrowid
    
    def clock_out(self, employee_id: int, notes: str = "") -> None:
        """
        Record a clock-out event for an employee.
        
        Args:
            employee_id: ID of the employee
            notes: Optional notes about the shift
            
        Raises:
            ValueError: If employee isn't clocked in
        """
        if not self._is_clocked_in(employee_id):
            raise ValueError("Employee is not clocked in")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE time_entries 
                   SET clock_out = ?, notes = ?
                   WHERE employee_id = ? AND clock_out IS NULL""",
                (datetime.now(), notes, employee_id)
            )
            conn.commit()
    
    def _is_employee_active(self, employee_id: int) -> bool:
        """Check if employee exists and is active."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM employees WHERE id = ? AND is_active = 1",
                (employee_id,)
            )
            return cursor.fetchone() is not None
    
    def _is_clocked_in(self, employee_id: int) -> bool:
        """Check if employee is currently clocked in."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT id FROM time_entries 
                   WHERE employee_id = ? AND clock_out IS NULL""",
                (employee_id,)
            )
            return cursor.fetchone() is not None
    
    def get_employee_time_entries(
        self, 
        employee_id: int, 
        start_date: Optional[datetime] = None, 
        end_date: Optional[datetime] = None
    ) -> List[Tuple]:
        """
        Get time entries for a specific employee.
        
        Args:
            employee_id: ID of the employee
            start_date: Optional start date filter
            end_date: Optional end date filter
            
        Returns:
            List of time entries as tuples (id, clock_in, clock_out, notes)
        """
        query = """
            SELECT id, clock_in, clock_out, notes 
            FROM time_entries 
            WHERE employee_id = ?
        """
        params = [employee_id]
        
        if start_date:
            query += " AND clock_in >= ?"
            params.append(start_date)
        if end_date:
            query += " AND clock_in <= ?"
            params.append(end_date)
            
        query += " ORDER BY clock_in DESC"
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    
    def get_all_time_entries(
        self, 
        start_date: Optional[datetime] = None, 
        end_date: Optional[datetime] = None
    ) -> List[Tuple]:
        """
        Get all time entries across all employees.
        
        Args:
            start_date: Optional start date filter
            end_date: Optional end date filter
            
        Returns:
            List of time entries with employee info as tuples
            (entry_id, employee_id, name, position, clock_in, clock_out, notes)
        """
        query = """
            SELECT t.id, e.id, e.name, e.position, t.clock_in, t.clock_out, t.notes
            FROM time_entries t
            JOIN employees e ON t.employee_id = e.id
            WHERE e.is_active = 1
        """
        params = []
        
        if start_date:
            query += " AND t.clock_in >= ?"
            params.append(start_date)
        if end_date:
            query += " AND t.clock_in <= ?"
            params.append(end_date)
            
        query += " ORDER BY t.clock_in DESC"
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    
    def generate_hours_report(
        self, 
        start_date: Optional[datetime] = None, 
        end_date: Optional[datetime] = None
    ) -> List[Tuple]:
        """
        Generate a report of hours worked per employee.
        
        Args:
            start_date: Optional start date filter
            end_date: Optional end date filter
            
        Returns:
            List of tuples (employee_id, name, total_hours)
        """
        query = """
            SELECT e.id, e.name, 
                   SUM(ROUND((JULIANDAY(t.clock_out) - JULIANDAY(t.clock_in)) * 24, 2)) as hours
            FROM time_entries t
            JOIN employees e ON t.employee_id = e.id
            WHERE t.clock_out IS NOT NULL
            AND e.is_active = 1
        """
        params = []
        
        if start_date:
            query += " AND t.clock_in >= ?"
            params.append(start_date)
        if end_date:
            query += " AND t.clock_in <= ?"
            params.append(end_date)
            
        query += " GROUP BY e.id, e.name ORDER BY e.name"
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
```
