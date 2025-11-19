"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Develop a manpower management system for a telecommunication company using a suitable programming language, incorporating features from ULTIUOS's manpower management services.
Generated: DETERMINISTIC_13b01b0e8a4cc654
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Manpower Management System for Telecommunication Company
Features inspired by ULTIUOS's services:
- Employee tracking
- Shift scheduling
- Performance monitoring
- Leave management
- Reporting
"""

import datetime
import json
import os
from typing import List, Dict, Optional, Tuple
from enum import Enum

# Database file path
DB_FILE = "manpower_db.json"

class EmployeeRole(Enum):
    TECHNICIAN = "Technician"
    CUSTOMER_SERVICE = "Customer Service"
    NETWORK_ENGINEER = "Network Engineer"
    MANAGER = "Manager"
    OTHER = "Other"

class LeaveStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class PerformanceRating(Enum):
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    BELOW_AVERAGE = 2
    POOR = 1

class Employee:
    def __init__(self, employee_id: str, name: str, role: EmployeeRole, 
                 contact: str, joining_date: str = None):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.contact = contact
        self.joining_date = joining_date or datetime.datetime.now().strftime("%Y-%m-%d")
        self.leaves = []
        self.shifts = []
        self.performance_reviews = []

    def to_dict(self) -> Dict:
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "role": self.role.value,
            "contact": self.contact,
            "joining_date": self.joining_date,
            "leaves": [leave.to_dict() for leave in self.leaves],
            "shifts": [shift.to_dict() for shift in self.shifts],
            "performance_reviews": [review.to_dict() for review in self.performance_reviews]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Employee':
        employee = cls(
            data["employee_id"],
            data["name"],
            EmployeeRole(data["role"]),
            data["contact"],
            data["joining_date"]
        )
        employee.leaves = [Leave.from_dict(leave) for leave in data.get("leaves", [])]
        employee.shifts = [Shift.from_dict(shift) for shift in data.get("shifts", [])]
        employee.performance_reviews = [
            PerformanceReview.from_dict(review) 
            for review in data.get("performance_reviews", [])
        ]
        return employee

class Leave:
    def __init__(self, leave_id: str, start_date: str, end_date: str, 
                 reason: str, status: LeaveStatus = LeaveStatus.PENDING):
        self.leave_id = leave_id
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "leave_id": self.leave_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "reason": self.reason,
            "status": self.status.value
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Leave':
        return cls(
            data["leave_id"],
            data["start_date"],
            data["end_date"],
            data["reason"],
            LeaveStatus(data["status"])
        )

class Shift:
    def __init__(self, shift_id: str, date: str, start_time: str, 
                 end_time: str, location: str):
        self.shift_id = shift_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def to_dict(self) -> Dict:
        return {
            "shift_id": self.shift_id,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Shift':
        return cls(
            data["shift_id"],
            data["date"],
            data["start_time"],
            data["end_time"],
            data["location"]
        )

class PerformanceReview:
    def __init__(self, review_id: str, date: str, reviewer: str, 
                 rating: PerformanceRating, comments: str):
        self.review_id = review_id
        self.date = date
        self.reviewer = reviewer
        self.rating = rating
        self.comments = comments

    def to_dict(self) -> Dict:
        return {
            "review_id": self.review_id,
            "date": self.date,
            "reviewer": self.reviewer,
            "rating": self.rating.value,
            "comments": self.comments
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'PerformanceReview':
        return cls(
            data["review_id"],
            data["date"],
            data["reviewer"],
            PerformanceRating(data["rating"]),
            data["comments"]
        )

class ManpowerSystem:
    def __init__(self):
        self.employees: Dict[str, Employee] = {}
        self.load_data()

    def load_data(self) -> None:
        try:
            if os.path.exists(DB_FILE):
                with open(DB_FILE, "r") as f:
                    data = json.load(f)
                    self.employees = {
                        emp_id: Employee.from_dict(emp_data) 
                        for emp_id, emp_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading data: {e}")
            self.employees = {}

    def save_data(self) -> None:
        try:
            with open(DB_FILE, "w") as f:
                json.dump(
                    {emp_id: emp.to_dict() for emp_id, emp in self.employees.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_employee(self, employee: Employee) -> bool:
        if employee.employee_id in self.employees:
            print(f"Employee ID {employee.employee_id} already exists.")
            return False
        self.employees[employee.employee_id] = employee
        self.save_data()
        return True

    def get_employee(self, employee_id: str) -> Optional[Employee]:
        return self.employees.get(employee_id)

    def update_employee(self, employee_id: str, **kwargs) -> bool:
        if employee_id not in self.employees:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        employee = self.employees[employee_id]
        for key, value in kwargs.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        
        self.save_data()
        return True

    def delete_employee(self, employee_id: str) -> bool:
        if employee_id not in self.employees:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        del self.employees[employee_id]
        self.save_data()
        return True

    def add_leave(self, employee_id: str, leave: Leave) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        employee.leaves.append(leave)
        self.save_data()
        return True

    def approve_leave(self, employee_id: str, leave_id: str) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        for leave in employee.leaves:
            if leave.leave_id == leave_id:
                leave.status = LeaveStatus.APPROVED
                self.save_data()
                return True
        
        print(f"Leave ID {leave_id} not found for employee {employee_id}.")
        return False

    def add_shift(self, employee_id: str, shift: Shift) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        employee.shifts.append(shift)
        self.save_data()
        return True

    def add_performance_review(self, employee_id: str, review: PerformanceReview) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            print(f"Employee ID {employee_id} not found.")
            return False
        
        employee.performance_reviews.append(review)
        self.save_data()
        return True

    def get_employees_by_role(self, role: EmployeeRole) -> List[Employee]:
        return [emp for emp in self.employees.values() if emp.role == role]

    def get_upcoming_shifts(self, days_ahead: int = 7) -> Dict[str, List[Shift]]:
        today = datetime.datetime.now().date()
        end_date = today + datetime.timedelta(days=days_a
