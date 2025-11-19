"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: "What are the advantages of using Perfect Payrolls' online payroll software for a company with multiple payroll types and frequencies, and how can it be customized to meet specific needs?"
Generated: DETERMINISTIC_0ddfd911465c870f
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payroll_system.py
"""
Perfect Payrolls' Online Payroll Software Implementation

This module demonstrates the customization and advantages of using Perfect Payrolls' 
online payroll software for companies with multiple payroll types and frequencies.
"""

from typing import List, Dict, Union
from enum import Enum, auto
import datetime
import json

class PayrollFrequency(Enum):
    """Enumeration for different payroll frequencies."""
    WEEKLY = auto()
    BIWEEKLY = auto()
    SEMIMONTHLY = auto()
    MONTHLY = auto()

class PayrollType(Enum):
    """Enumeration for different payroll types."""
    SALARY = auto()
    HOURLY = auto()
    COMMISSION = auto()
    CONTRACT = auto()

class Employee:
    """Class representing an employee with payroll information."""
    
    def __init__(self, employee_id: str, name: str, payroll_type: PayrollType, 
                 payroll_frequency: PayrollFrequency, custom_fields: Dict = None):
        """
        Initialize an Employee instance.
        
        Args:
            employee_id: Unique identifier for the employee
            name: Employee's full name
            payroll_type: Type of payroll (SALARY, HOURLY, etc.)
            payroll_frequency: Frequency of payroll (WEEKLY, BIWEEKLY, etc.)
            custom_fields: Dictionary of custom fields for additional employee data
        """
        self.employee_id = employee_id
        self.name = name
        self.payroll_type = payroll_type
        self.payroll_frequency = payroll_frequency
        self.custom_fields = custom_fields or {}

    def to_dict(self) -> Dict:
        """Convert Employee object to dictionary for serialization."""
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'payroll_type': self.payroll_type.name,
            'payroll_frequency': self.payroll_frequency.name,
            'custom_fields': self.custom_fields
        }

class PayrollSystem:
    """Main payroll system class handling multiple payroll types and frequencies."""
    
    def __init__(self):
        """Initialize the payroll system with empty employee list."""
        self.employees: List[Employee] = []
        self.custom_rules = {}

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the payroll system.
        
        Args:
            employee: Employee object to add
            
        Raises:
            ValueError: If employee ID already exists
        """
        if any(e.employee_id == employee.employee_id for e in self.employees):
            raise ValueError(f"Employee ID {employee.employee_id} already exists")
        self.employees.append(employee)

    def remove_employee(self, employee_id: str) -> None:
        """Remove an employee from the payroll system.
        
        Args:
            employee_id: ID of employee to remove
            
        Raises:
            ValueError: If employee ID doesn't exist
        """
        employee = next((e for e in self.employees if e.employee_id == employee_id), None)
        if not employee:
            raise ValueError(f"Employee ID {employee_id} not found")
        self.employees.remove(employee)

    def add_custom_rule(self, rule_name: str, rule_function) -> None:
        """Add a custom payroll processing rule.
        
        Args:
            rule_name: Name to identify the rule
            rule_function: Function that implements the rule logic
        """
        self.custom_rules[rule_name] = rule_function

    def process_payroll(self, pay_period: datetime.date) -> Dict[str, Union[float, Dict]]:
        """Process payroll for all employees for a given pay period.
        
        Args:
            pay_period: Date representing the pay period
            
        Returns:
            Dictionary containing payroll results for each employee
            
        Raises:
            ValueError: If no employees are registered
        """
        if not self.employees:
            raise ValueError("No employees registered in the system")
            
        results = {}
        for employee in self.employees:
            # Base calculation based on payroll type
            if employee.payroll_type == PayrollType.SALARY:
                amount = self._calculate_salary(employee)
            elif employee.payroll_type == PayrollType.HOURLY:
                amount = self._calculate_hourly(employee)
            elif employee.payroll_type == PayrollType.COMMISSION:
                amount = self._calculate_commission(employee)
            elif employee.payroll_type == PayrollType.CONTRACT:
                amount = self._calculate_contract(employee)
            else:
                raise ValueError(f"Unknown payroll type: {employee.payroll_type}")
                
            # Apply any custom rules
            for rule_name, rule_func in self.custom_rules.items():
                amount = rule_func(employee, amount, pay_period)
                
            results[employee.employee_id] = {
                'name': employee.name,
                'amount': amount,
                'pay_period': pay_period.strftime('%Y-%m-%d'),
                'payroll_type': employee.payroll_type.name,
                'payroll_frequency': employee.payroll_frequency.name,
                'custom_data': employee.custom_fields
            }
            
        return results

    def _calculate_salary(self, employee: Employee) -> float:
        """Calculate salary payment (simplified example)."""
        # In a real system, this would use the employee's salary data
        return 5000.00  # Example fixed amount

    def _calculate_hourly(self, employee: Employee) -> float:
        """Calculate hourly payment (simplified example)."""
        # In a real system, this would use timesheet data
        hours_worked = 80  # Example hours
        hourly_rate = 25.00  # Example rate
        return hours_worked * hourly_rate

    def _calculate_commission(self, employee: Employee) -> float:
        """Calculate commission payment (simplified example)."""
        # In a real system, this would use sales data
        sales_amount = 10000.00  # Example sales
        commission_rate = 0.10  # 10% commission
        return sales_amount * commission_rate

    def _calculate_contract(self, employee: Employee) -> float:
        """Calculate contract payment (simplified example)."""
        # In a real system, this would use contract terms
        contract_amount = 7500.00  # Example contract amount
        return contract_amount

    def save_to_file(self, filename: str) -> None:
        """Save payroll system data to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        data = {
            'employees': [e.to_dict() for e in self.employees],
            'custom_rules': list(self.custom_rules.keys())
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load payroll system data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.employees = []
            for emp_data in data.get('employees', []):
                payroll_type = PayrollType[emp_data['payroll_type']]
                payroll_freq = PayrollFrequency[emp_data['payroll_frequency']]
                employee = Employee(
                    emp_data['employee_id'],
                    emp_data['name'],
                    payroll_type,
                    payroll_freq,
                    emp_data.get('custom_fields', {})
                )
                self.employees.append(employee)
                
            # Note: Custom rule functions would need to be re-registered
            self.custom_rules = {}
            
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid file format: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create payroll system instance
    payroll = PayrollSystem()
    
    # Add employees with different payroll types and frequencies
    payroll.add_employee(Employee("E001", "John Doe", PayrollType.SALARY, PayrollFrequency.MONTHLY))
    payroll.add_employee(Employee("E002", "Jane Smith", PayrollType.HOURLY, PayrollFrequency.WEEKLY))
    payroll.add_employee(Employee("E003", "Bob Johnson", PayrollType.COMMISSION, PayrollFrequency.BIWEEKLY, 
                                 {"sales_region": "North"}))
    
    # Add a custom rule for bonuses
    def holiday_bonus(employee: Employee, amount: float, pay_period: datetime.date) -> float:
        """Custom rule: Add holiday bonus in December."""
        if pay_period.month == 12:
            return amount + 1000.00
        return amount
    
    payroll.add_custom_rule("holiday_bonus", holiday_bonus)
    
    # Process payroll for a specific period
    try:
        results = payroll.process_payroll(datetime.date(2023,
