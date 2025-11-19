"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: Generate a code snippet for an ERP system that includes modules for Human Resources and Payroll, similar to the Helool ERP System mentioned on the Sama Al-Naser Group website.
Generated: DETERMINISTIC_0d2615e62840e94f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ERP System Modules for Human Resources and Payroll
# Inspired by Helool ERP System

import datetime
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

class Department(Enum):
    """Enum representing different departments in the organization"""
    HR = auto()
    FINANCE = auto()
    IT = auto()
    SALES = auto()
    OPERATIONS = auto()

class EmployeeType(Enum):
    """Enum representing different types of employees"""
    FULL_TIME = auto()
    PART_TIME = auto()
    CONTRACT = auto()
    INTERN = auto()

@dataclass
class Employee:
    """Class representing an employee in the HR system"""
    employee_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    department: Department
    employee_type: EmployeeType
    hire_date: datetime.date
    salary: float
    is_active: bool = True

    def full_name(self) -> str:
        """Returns the full name of the employee"""
        return f"{self.first_name} {self.last_name}"

@dataclass
class PayrollRecord:
    """Class representing a payroll record"""
    record_id: str
    employee_id: str
    pay_period_start: datetime.date
    pay_period_end: datetime.date
    gross_pay: float
    deductions: float
    net_pay: float
    payment_date: datetime.date
    is_processed: bool = False

class HRModule:
    """Human Resources module for managing employees"""
    
    def __init__(self):
        self.employees: List[Employee] = []
    
    def add_employee(self, employee: Employee) -> bool:
        """Adds a new employee to the system"""
        if any(e.employee_id == employee.employee_id for e in self.employees):
            raise ValueError(f"Employee with ID {employee.employee_id} already exists")
        self.employees.append(employee)
        return True
    
    def get_employee(self, employee_id: str) -> Optional[Employee]:
        """Retrieves an employee by ID"""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None
    
    def update_employee(self, employee_id: str, **kwargs) -> bool:
        """Updates employee information"""
        employee = self.get_employee(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found")
        
        for key, value in kwargs.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
        return True
    
    def terminate_employee(self, employee_id: str) -> bool:
        """Terminates an employee"""
        employee = self.get_employee(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found")
        employee.is_active = False
        return True
    
    def list_employees(self, department: Optional[Department] = None) -> List[Employee]:
        """Lists all employees, optionally filtered by department"""
        if department:
            return [e for e in self.employees if e.department == department and e.is_active]
        return [e for e in self.employees if e.is_active]

class PayrollModule:
    """Payroll module for processing employee payments"""
    
    def __init__(self, hr_module: HRModule):
        self.hr_module = hr_module
        self.payroll_records: List[PayrollRecord] = []
    
    def calculate_payroll(self, employee_id: str) -> PayrollRecord:
        """Calculates payroll for an employee"""
        employee = self.hr_module.get_employee(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found")
        if not employee.is_active:
            raise ValueError(f"Employee with ID {employee_id} is not active")
        
        # Simple payroll calculation (in a real system this would be more complex)
        today = datetime.date.today()
        start_date = today.replace(day=1)
        end_date = today
        
        # Calculate deductions (simplified)
        deductions = employee.salary * 0.2  # Assuming 20% deductions
        
        record = PayrollRecord(
            record_id=f"PR-{datetime.datetime.now().timestamp()}",
            employee_id=employee_id,
            pay_period_start=start_date,
            pay_period_end=end_date,
            gross_pay=employee.salary,
            deductions=deductions,
            net_pay=employee.salary - deductions,
            payment_date=today
        )
        
        self.payroll_records.append(record)
        return record
    
    def process_payroll(self, employee_id: str) -> bool:
        """Processes payroll for an employee"""
        record = self.calculate_payroll(employee_id)
        record.is_processed = True
        # In a real system, this would interface with bank APIs or generate payment files
        return True
    
    def get_payroll_history(self, employee_id: str) -> List[PayrollRecord]:
        """Retrieves payroll history for an employee"""
        return [r for r in self.payroll_records if r.employee_id == employee_id]

class ERPSystem:
    """Main ERP system class integrating HR and Payroll modules"""
    
    def __init__(self):
        self.hr_module = HRModule()
        self.payroll_module = PayrollModule(self.hr_module)
    
    def generate_monthly_payroll(self) -> bool:
        """Processes payroll for all active employees"""
        employees = self.hr_module.list_employees()
        for employee in employees:
            try:
                self.payroll_module.process_payroll(employee.employee_id)
            except Exception as e:
                print(f"Failed to process payroll for {employee.employee_id}: {str(e)}")
                continue
        return True

# Example usage
if __name__ == "__main__":
    erp = ERPSystem()
    
    # Add employees
    emp1 = Employee(
        employee_id="EMP001",
        first_name="John",
        last_name="Doe",
        email="john.doe@company.com",
        phone="1234567890",
        department=Department.IT,
        employee_type=EmployeeType.FULL_TIME,
        hire_date=datetime.date(2020, 1, 15),
        salary=5000.00
    )
    
    emp2 = Employee(
        employee_id="EMP002",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@company.com",
        phone="9876543210",
        department=Department.HR,
        employee_type=EmployeeType.FULL_TIME,
        hire_date=datetime.date(2019, 5, 10),
        salary=4500.00
    )
    
    erp.hr_module.add_employee(emp1)
    erp.hr_module.add_employee(emp2)
    
    # Process payroll
    erp.generate_monthly_payroll()
    
    # Get payroll history
    history = erp.payroll_module.get_payroll_history("EMP001")
    for record in history:
        print(f"Payroll record for {record.employee_id}: Net pay {record.net_pay}")
```
