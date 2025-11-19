"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Develop a system to manage teacher and employee data, including features for leave management, salary scales, and performance evaluation, tailored to the needs of a Bangladeshi secondary school.
Generated: DETERMINISTIC_30f81d59cbf0593e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Teacher and Employee Management System for Bangladeshi Secondary Schools

Features:
- Teacher/Employee CRUD operations
- Leave management
- Salary scale management
- Performance evaluation
"""

import datetime
from typing import List, Dict, Optional
import sqlite3
from dataclasses import dataclass
import json
from enum import Enum

# Database configuration
DB_NAME = "school_management.db"

class EmployeeType(Enum):
    TEACHER = "teacher"
    STAFF = "staff"
    ADMIN = "admin"

class LeaveStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class PerformanceRating(Enum):
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    BELOW_AVERAGE = 2
    POOR = 1

@dataclass
class Employee:
    id: int
    name: str
    employee_type: EmployeeType
    joining_date: str
    contact_number: str
    email: str
    address: str
    nid: str
    is_active: bool = True

@dataclass
class LeaveApplication:
    id: int
    employee_id: int
    start_date: str
    end_date: str
    reason: str
    status: LeaveStatus = LeaveStatus.PENDING
    approved_by: Optional[int] = None

@dataclass
class SalaryScale:
    id: int
    employee_type: EmployeeType
    grade: int
    basic_salary: float
    house_rent: float
    medical_allowance: float
    conveyance: float

@dataclass
class PerformanceEvaluation:
    id: int
    employee_id: int
    evaluation_date: str
    rating: PerformanceRating
    comments: str
    evaluator_id: int

class SchoolManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self._initialize_db()

    def _initialize_db(self):
        """Initialize database tables if they don't exist"""
        cursor = self.conn.cursor()

        # Employees table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_type TEXT NOT NULL,
            joining_date TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            email TEXT,
            address TEXT,
            nid TEXT NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            UNIQUE(nid)
        )
        """)

        # Leave applications table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leave_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            reason TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            approved_by INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employees(id),
            FOREIGN KEY (approved_by) REFERENCES employees(id)
        )
        """)

        # Salary scales table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS salary_scales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_type TEXT NOT NULL,
            grade INTEGER NOT NULL,
            basic_salary REAL NOT NULL,
            house_rent REAL NOT NULL,
            medical_allowance REAL NOT NULL,
            conveyance REAL NOT NULL,
            UNIQUE(employee_type, grade)
        )
        """)

        # Performance evaluations table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            evaluation_date TEXT NOT NULL,
            rating INTEGER NOT NULL,
            comments TEXT,
            evaluator_id INTEGER NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees(id),
            FOREIGN KEY (evaluator_id) REFERENCES employees(id)
        )
        """)

        self.conn.commit()

    # Employee CRUD operations
    def add_employee(self, employee: Employee) -> int:
        """Add a new employee to the system"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO employees (name, employee_type, joining_date, contact_number, email, address, nid)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                employee.name,
                employee.employee_type.value,
                employee.joining_date,
                employee.contact_number,
                employee.email,
                employee.address,
                employee.nid
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Employee with NID {employee.nid} already exists") from e

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Retrieve an employee by ID"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
        row = cursor.fetchone()
        if row:
            return Employee(
                id=row[0],
                name=row[1],
                employee_type=EmployeeType(row[2]),
                joining_date=row[3],
                contact_number=row[4],
                email=row[5],
                address=row[6],
                nid=row[7],
                is_active=bool(row[8])
            )
        return None

    def update_employee(self, employee: Employee) -> bool:
        """Update employee information"""
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE employees 
        SET name = ?, employee_type = ?, joining_date = ?, contact_number = ?, 
            email = ?, address = ?, nid = ?, is_active = ?
        WHERE id = ?
        """, (
            employee.name,
            employee.employee_type.value,
            employee.joining_date,
            employee.contact_number,
            employee.email,
            employee.address,
            employee.nid,
            employee.is_active,
            employee.id
        ))
        self.conn.commit()
        return cursor.rowcount > 0

    def delete_employee(self, employee_id: int) -> bool:
        """Mark an employee as inactive"""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE employees SET is_active = FALSE WHERE id = ?", (employee_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def list_employees(self, active_only: bool = True) -> List[Employee]:
        """List all employees, optionally filtering by active status"""
        cursor = self.conn.cursor()
        if active_only:
            cursor.execute("SELECT * FROM employees WHERE is_active = TRUE")
        else:
            cursor.execute("SELECT * FROM employees")
        
        employees = []
        for row in cursor.fetchall():
            employees.append(Employee(
                id=row[0],
                name=row[1],
                employee_type=EmployeeType(row[2]),
                joining_date=row[3],
                contact_number=row[4],
                email=row[5],
                address=row[6],
                nid=row[7],
                is_active=bool(row[8])
            ))
        return employees

    # Leave management operations
    def apply_for_leave(self, leave: LeaveApplication) -> int:
        """Submit a new leave application"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO leave_applications (employee_id, start_date, end_date, reason, status)
            VALUES (?, ?, ?, ?, ?)
            """, (
                leave.employee_id,
                leave.start_date,
                leave.end_date,
                leave.reason,
                leave.status.value
            ))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Invalid employee ID: {leave.employee_id}") from e

    def process_leave(self, leave_id: int, status: LeaveStatus, approved_by: int) -> bool:
        """Approve or reject a leave application"""
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE leave_applications 
        SET status = ?, approved_by = ?
        WHERE id = ?
        """, (status.value, approved_by, leave_id))
        self.conn.commit()
        return cursor.rowcount > 0

    def get_leave_applications(self, employee_id: Optional[int] = None) -> List[LeaveApplication]:
        """Get leave applications, optionally filtered by employee"""
        cursor = self.conn.cursor()
        if employee_id:
            cursor.execute("SELECT * FROM leave_applications WHERE employee_id = ?", (employee_id,))
        else:
            cursor.execute("SELECT * FROM leave_applications")
        
        leaves = []
        for row in cursor.fetchall():
            leaves.append(LeaveApplication(
                id=row[0],
                employee_id=row[1],
                start_date=row[2],
                end_date=row[3],
                reason=row[4],
                status=LeaveStatus(row[5]),
                approved_by=row[6]
            ))
        return leaves

    # Salary scale operations
    def add_salary_scale(self, scale: SalaryScale) -> int:
        """Add a new salary scale"""
        try:
            cursor = self.conn.cursor()
            cursor
