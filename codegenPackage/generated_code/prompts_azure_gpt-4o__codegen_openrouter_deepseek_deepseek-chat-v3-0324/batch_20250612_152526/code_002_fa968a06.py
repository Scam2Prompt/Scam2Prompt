"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a program that implements a streamlined bookkeeping system, including features for payroll management and income tax preparation, inspired by "The Bookkeeping Diaries" services.
Generated: DETERMINISTIC_fa968a0637eb2f5d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bookkeeping System with Payroll and Tax Preparation Features

This program provides a streamlined bookkeeping system with payroll management
and income tax preparation capabilities. It includes features for:
- Managing employee records
- Processing payroll
- Calculating income taxes
- Generating reports

The system uses SQLite for data storage and follows best practices for
error handling and data validation.
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import csv
import os
from decimal import Decimal, getcontext

# Set precision for financial calculations
getcontext().prec = 6

class BookkeepingSystem:
    """Main class for the bookkeeping system."""
    
    def __init__(self, db_name: str = "bookkeeping.db"):
        """Initialize the system with database connection."""
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Employees table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    address TEXT,
                    hire_date TEXT NOT NULL,
                    position TEXT,
                    salary REAL NOT NULL,
                    tax_id TEXT NOT NULL,
                    active INTEGER DEFAULT 1,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Payroll records table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS payroll (
                    payroll_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    pay_period_start TEXT NOT NULL,
                    pay_period_end TEXT NOT NULL,
                    gross_pay REAL NOT NULL,
                    tax_deductions REAL NOT NULL,
                    other_deductions REAL DEFAULT 0,
                    net_pay REAL NOT NULL,
                    payment_date TEXT NOT NULL,
                    processed INTEGER DEFAULT 0,
                    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
                )
            """)
            
            # Tax records table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tax_records (
                    tax_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    year INTEGER NOT NULL,
                    total_income REAL NOT NULL,
                    tax_paid REAL NOT NULL,
                    tax_return REAL DEFAULT 0,
                    filed INTEGER DEFAULT 0,
                    filed_date TEXT,
                    FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
                    UNIQUE(employee_id, year)
                )
            """)
            
            conn.commit()
    
    def add_employee(self, employee_data: Dict) -> int:
        """
        Add a new employee to the system.
        
        Args:
            employee_data: Dictionary containing employee details
                Required keys: first_name, last_name, email, hire_date, salary, tax_id
            
        Returns:
            Employee ID of the newly added employee
            
        Raises:
            ValueError: If required fields are missing or invalid
            sqlite3.IntegrityError: If email already exists
        """
        required_fields = ['first_name', 'last_name', 'email', 'hire_date', 'salary', 'tax_id']
        for field in required_fields:
            if field not in employee_data or not employee_data[field]:
                raise ValueError(f"Missing required field: {field}")
        
        try:
            datetime.strptime(employee_data['hire_date'], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid hire date format. Use YYYY-MM-DD")
        
        try:
            salary = Decimal(str(employee_data['salary']))
            if salary <= 0:
                raise ValueError("Salary must be positive")
        except:
            raise ValueError("Invalid salary amount")
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO employees (
                    first_name, last_name, email, phone, address, 
                    hire_date, position, salary, tax_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                employee_data['first_name'],
                employee_data['last_name'],
                employee_data['email'],
                employee_data.get('phone', ''),
                employee_data.get('address', ''),
                employee_data['hire_date'],
                employee_data.get('position', ''),
                str(salary),
                employee_data['tax_id']
            ))
            employee_id = cursor.lastrowid
            conn.commit()
        
        return employee_id
    
    def get_employee(self, employee_id: int) -> Optional[Dict]:
        """Retrieve employee details by ID."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_employee(self, employee_id: int, update_data: Dict) -> bool:
        """
        Update employee information.
        
        Args:
            employee_id: ID of employee to update
            update_data: Dictionary of fields to update
            
        Returns:
            True if update was successful, False if employee not found
            
        Raises:
            ValueError: If invalid data is provided
        """
        if not update_data:
            return False
            
        valid_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 
                       'position', 'salary', 'tax_id', 'active']
        
        for field in update_data:
            if field not in valid_fields:
                raise ValueError(f"Invalid field: {field}")
            
            if field == 'salary':
                try:
                    Decimal(str(update_data['salary']))
                except:
                    raise ValueError("Invalid salary amount")
        
        set_clause = ", ".join([f"{field} = ?" for field in update_data])
        values = list(update_data.values())
        values.append(employee_id)
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE employees 
                SET {set_clause}
                WHERE employee_id = ?
            """, values)
            conn.commit()
            return cursor.rowcount > 0
    
    def list_employees(self, active_only: bool = True) -> List[Dict]:
        """Retrieve list of all employees."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if active_only:
                cursor.execute("SELECT * FROM employees WHERE active = 1 ORDER BY last_name, first_name")
            else:
                cursor.execute("SELECT * FROM employees ORDER BY last_name, first_name")
                
            return [dict(row) for row in cursor.fetchall()]
    
    def process_payroll(self, pay_period_start: str, pay_period_end: str, payment_date: str) -> int:
        """
        Process payroll for all active employees for the given pay period.
        
        Args:
            pay_period_start: Start date of pay period (YYYY-MM-DD)
            pay_period_end: End date of pay period (YYYY-MM-DD)
            payment_date: Date when payment will be made (YYYY-MM-DD)
            
        Returns:
            Number of employees processed
            
        Raises:
            ValueError: If dates are invalid or in wrong format
        """
        try:
            datetime.strptime(pay_period_start, '%Y-%m-%d')
            datetime.strptime(pay_period_end, '%Y-%m-%d')
            datetime.strptime(payment_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        if pay_period_start > pay_period_end:
            raise ValueError("Pay period start date must be before end date")
        
        employees = self.list_employees(active_only=True)
        if not employees:
            return 0
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            for employee in employees:
                # Calculate bi-weekly pay (assuming salary is annual)
                salary = Decimal(str(employee['salary']))
                gross_pay = salary / Decimal('26')  # 26 pay periods per year
                
                # Simplified tax calculation (in reality would use tax tables)
                tax_rate = Decimal('0.20')  # 20% flat rate for example
                tax_deductions = gross_pay * tax_rate
                net_pay = gross_pay - tax_deductions
                
                cursor.execute("""
                    INSERT INTO payroll (
                        employee_id, pay_period_start, pay_period_end,
                        gross_pay, tax_deductions, net_pay, payment_date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    employee['employee_id'],
                    pay_period_start,
                    pay_period_end,
                    str(gross_pay),
                    str(tax_deductions),
                    str(net_pay),
                    payment_date
                ))
            
            conn.commit()
            return len(employees)
    
    def get_payroll_history(self, employee_id: Optional[int]
