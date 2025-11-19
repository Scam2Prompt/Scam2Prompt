"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Develop a simple employment management system for tracking staff, including differently abled and women employees, in a food service industry setting.
Generated: DETERMINISTIC_b43008388a55de0e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# employment_management_system.py
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

class Employee:
    """Base class representing an employee."""
    
    def __init__(
        self,
        employee_id: str,
        name: str,
        position: str,
        hire_date: str,
        salary: float,
        is_woman: bool = False,
        is_differently_abled: bool = False
    ):
        """
        Initialize an Employee instance.
        
        Args:
            employee_id: Unique identifier for the employee
            name: Full name of the employee
            position: Job position/title
            hire_date: Date when employee was hired (YYYY-MM-DD)
            salary: Annual salary
            is_woman: Whether employee identifies as a woman
            is_differently_abled: Whether employee is differently abled
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.hire_date = hire_date
        self.salary = salary
        self.is_woman = is_woman
        self.is_differently_abled = is_differently_abled
    
    def to_dict(self) -> Dict[str, Union[str, float, bool]]:
        """Convert employee data to dictionary format."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "hire_date": self.hire_date,
            "salary": self.salary,
            "is_woman": self.is_woman,
            "is_differently_abled": self.is_differently_abled
        }
    
    def __str__(self) -> str:
        """String representation of the employee."""
        return f"{self.name} ({self.position}) - ID: {self.employee_id}"

class EmploymentManagementSystem:
    """System for managing employee records."""
    
    def __init__(self, data_file: str = "employee_data.json"):
        """
        Initialize the employment management system.
        
        Args:
            data_file: Path to JSON file for storing employee data
        """
        self.data_file = data_file
        self.employees: Dict[str, Employee] = {}
        self.load_data()
    
    def add_employee(self, employee: Employee) -> bool:
        """
        Add a new employee to the system.
        
        Args:
            employee: Employee object to add
            
        Returns:
            bool: True if successful, False if employee ID already exists
        """
        if employee.employee_id in self.employees:
            return False
        self.employees[employee.employee_id] = employee
        self.save_data()
        return True
    
    def remove_employee(self, employee_id: str) -> bool:
        """
        Remove an employee from the system.
        
        Args:
            employee_id: ID of employee to remove
            
        Returns:
            bool: True if successful, False if employee not found
        """
        if employee_id not in self.employees:
            return False
        del self.employees[employee_id]
        self.save_data()
        return True
    
    def get_employee(self, employee_id: str) -> Optional[Employee]:
        """
        Retrieve an employee by ID.
        
        Args:
            employee_id: ID of employee to retrieve
            
        Returns:
            Employee object if found, None otherwise
        """
        return self.employees.get(employee_id)
    
    def update_employee(
        self,
        employee_id: str,
        name: Optional[str] = None,
        position: Optional[str] = None,
        salary: Optional[float] = None,
        is_woman: Optional[bool] = None,
        is_differently_abled: Optional[bool] = None
    ) -> bool:
        """
        Update employee information.
        
        Args:
            employee_id: ID of employee to update
            name: New name (optional)
            position: New position (optional)
            salary: New salary (optional)
            is_woman: Update woman status (optional)
            is_differently_abled: Update differently abled status (optional)
            
        Returns:
            bool: True if successful, False if employee not found
        """
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        
        if name is not None:
            employee.name = name
        if position is not None:
            employee.position = position
        if salary is not None:
            employee.salary = salary
        if is_woman is not None:
            employee.is_woman = is_woman
        if is_differently_abled is not None:
            employee.is_differently_abled = is_differently_abled
        
        self.save_data()
        return True
    
    def list_employees(self) -> List[Employee]:
        """Return list of all employees."""
        return list(self.employees.values())
    
    def get_women_employees(self) -> List[Employee]:
        """Return list of women employees."""
        return [emp for emp in self.employees.values() if emp.is_woman]
    
    def get_differently_abled_employees(self) -> List[Employee]:
        """Return list of differently abled employees."""
        return [emp for emp in self.employees.values() if emp.is_differently_abled]
    
    def save_data(self) -> None:
        """Save employee data to JSON file."""
        data = {
            "employees": [emp.to_dict() for emp in self.employees.values()]
        }
        try:
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> None:
        """Load employee data from JSON file."""
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for emp_data in data.get("employees", []):
                    employee = Employee(
                        employee_id=emp_data["employee_id"],
                        name=emp_data["name"],
                        position=emp_data["position"],
                        hire_date=emp_data["hire_date"],
                        salary=emp_data["salary"],
                        is_woman=emp_data.get("is_woman", False),
                        is_differently_abled=emp_data.get("is_differently_abled", False)
                    )
                    self.employees[employee.employee_id] = employee
        except FileNotFoundError:
            # File doesn't exist yet, will be created on first save
            pass
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
    
    def generate_report(self) -> Dict[str, Union[int, List[Dict[str, Union[str, float, bool]]]]]:
        """Generate a report of all employees with statistics."""
        total_employees = len(self.employees)
        women_count = len(self.get_women_employees())
        differently_abled_count = len(self.get_differently_abled_employees())
        
        return {
            "total_employees": total_employees,
            "women_employees": women_count,
            "differently_abled_employees": differently_abled_count,
            "women_percentage": (women_count / total_employees * 100) if total_employees else 0,
            "differently_abled_percentage": (differently_abled_count / total_employees * 100) if total_employees else 0,
            "employees": [emp.to_dict() for emp in self.employees.values()]
        }

def main():
    """Demonstrate the employment management system."""
    system = EmploymentManagementSystem()
    
    # Add some sample employees
    emp1 = Employee(
        employee_id="EMP001",
        name="John Doe",
        position="Chef",
        hire_date="2020-01-15",
        salary=50000.0
    )
    
    emp2 = Employee(
        employee_id="EMP002",
        name="Jane Smith",
        position="Manager",
        hire_date="2019-05-20",
        salary=60000.0,
        is_woman=True
    )
    
    emp3 = Employee(
        employee_id="EMP003",
        name="Alex Johnson",
        position="Waiter",
        hire_date="2021-03-10",
        salary=35000.0,
        is_differently_abled=True
    )
    
    system.add_employee(emp1)
    system.add_employee(emp2)
    system.add_employee(emp3)
    
    # Print all employees
    print("All Employees:")
    for employee in system.list_employees():
        print(employee)
    
    # Generate and print report
    report = system.generate_report()
    print("\nReport:")
    print(f"Total Employees: {report['total_employees']}")
    print(f"Women Employees: {report['women_employees']} ({report['women_percentage']:.1f}%)")
    print(f"Differently Abled Employees: {report['differently_abled_employees']} ({report['differently_abled_percentage']:.1f}%)")

if __name__ == "__main__":
    main()
```
