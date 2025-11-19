"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Implement a system to track and analyze payroll benefits, inspired by the "Beneficios Sociales" course demo available on AulaContable.
Generated: DETERMINISTIC_f7547bb1d64da928
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Payroll Benefits Tracking System

This system allows tracking and analyzing employee payroll benefits such as:
- Social security contributions
- Bonuses
- Allowances
- Other benefits

The system provides functionality to:
- Add/update employee benefits
- Calculate total benefits per employee
- Generate reports
- Analyze benefit distributions
"""

import csv
from datetime import datetime
from typing import List, Dict, Optional, Union
import json
import os


class Benefit:
    """Represents a single benefit entry for an employee"""
    
    def __init__(self, name: str, amount: float, category: str, date: str, description: str = ""):
        """
        Initialize a benefit instance
        
        Args:
            name: Name of the benefit
            amount: Monetary value of the benefit
            category: Benefit category (e.g., 'health', 'bonus')
            date: Date when benefit was applied (YYYY-MM-DD)
            description: Optional description of the benefit
        """
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        
    def to_dict(self) -> Dict:
        """Convert benefit to dictionary for serialization"""
        return {
            'name': self.name,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Benefit':
        """Create Benefit instance from dictionary"""
        return cls(
            name=data['name'],
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data.get('description', '')
        )


class EmployeeBenefits:
    """Manages benefits for a single employee"""
    
    def __init__(self, employee_id: str, name: str):
        """
        Initialize employee benefits tracker
        
        Args:
            employee_id: Unique identifier for employee
            name: Employee full name
        """
        self.employee_id = employee_id
        self.name = name
        self.benefits: List[Benefit] = []
        
    def add_benefit(self, benefit: Benefit) -> None:
        """Add a new benefit to the employee's record"""
        self.benefits.append(benefit)
        
    def remove_benefit(self, index: int) -> None:
        """Remove a benefit by its index"""
        if 0 <= index < len(self.benefits):
            self.benefits.pop(index)
            
    def total_benefits(self) -> float:
        """Calculate total value of all benefits"""
        return sum(benefit.amount for benefit in self.benefits)
    
    def benefits_by_category(self) -> Dict[str, float]:
        """Group benefits by category and sum amounts"""
        categories = {}
        for benefit in self.benefits:
            if benefit.category not in categories:
                categories[benefit.category] = 0
            categories[benefit.category] += benefit.amount
        return categories
    
    def to_dict(self) -> Dict:
        """Convert employee benefits to dictionary for serialization"""
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'benefits': [benefit.to_dict() for benefit in self.benefits]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EmployeeBenefits':
        """Create EmployeeBenefits instance from dictionary"""
        employee = cls(data['employee_id'], data['name'])
        employee.benefits = [Benefit.from_dict(b) for b in data['benefits']]
        return employee


class PayrollBenefitsSystem:
    """Main system for managing payroll benefits across all employees"""
    
    def __init__(self):
        """Initialize the system with empty employee records"""
        self.employees: Dict[str, EmployeeBenefits] = {}
        
    def add_employee(self, employee_id: str, name: str) -> None:
        """Add a new employee to the system"""
        if employee_id not in self.employees:
            self.employees[employee_id] = EmployeeBenefits(employee_id, name)
            
    def get_employee(self, employee_id: str) -> Optional[EmployeeBenefits]:
        """Retrieve employee benefits by ID"""
        return self.employees.get(employee_id)
    
    def add_benefit(self, employee_id: str, benefit: Benefit) -> bool:
        """Add benefit to an employee's record"""
        employee = self.get_employee(employee_id)
        if employee:
            employee.add_benefit(benefit)
            return True
        return False
    
    def remove_employee(self, employee_id: str) -> bool:
        """Remove an employee from the system"""
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False
    
    def total_company_benefits(self) -> float:
        """Calculate total benefits cost across all employees"""
        return sum(employee.total_benefits() for employee in self.employees.values())
    
    def benefits_distribution(self) -> Dict[str, float]:
        """Calculate benefit distribution by category across all employees"""
        distribution = {}
        for employee in self.employees.values():
            categories = employee.benefits_by_category()
            for category, amount in categories.items():
                if category not in distribution:
                    distribution[category] = 0
                distribution[category] += amount
        return distribution
    
    def generate_report(self, filename: str, report_type: str = 'json') -> None:
        """
        Generate a report of all benefits
        
        Args:
            filename: Output file name
            report_type: Type of report ('json', 'csv')
        """
        if report_type == 'json':
            self._generate_json_report(filename)
        elif report_type == 'csv':
            self._generate_csv_report(filename)
        else:
            raise ValueError(f"Unsupported report type: {report_type}")
    
    def _generate_json_report(self, filename: str) -> None:
        """Generate JSON report"""
        data = {
            'employees': [employee.to_dict() for employee in self.employees.values()],
            'total_benefits': self.total_company_benefits(),
            'benefits_distribution': self.benefits_distribution(),
            'generated_at': datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _generate_csv_report(self, filename: str) -> None:
        """Generate CSV report"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Employee ID', 'Employee Name', 'Benefit Name', 
                            'Category', 'Amount', 'Date', 'Description'])
            
            for employee in self.employees.values():
                for benefit in employee.benefits:
                    writer.writerow([
                        employee.employee_id,
                        employee.name,
                        benefit.name,
                        benefit.category,
                        benefit.amount,
                        benefit.date,
                        benefit.description
                    ])
    
    def save_to_file(self, filename: str) -> None:
        """Save the entire system state to a file"""
        data = {
            'employees': [employee.to_dict() for employee in self.employees.values()],
            'version': '1.0',
            'saved_at': datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'PayrollBenefitsSystem':
        """Load system state from a file"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
            
        with open(filename, 'r') as f:
            data = json.load(f)
            
        system = cls()
        for employee_data in data['employees']:
            employee = EmployeeBenefits.from_dict(employee_data)
            system.employees[employee.employee_id] = employee
            
        return system


# Example usage
if __name__ == "__main__":
    # Create system instance
    system = PayrollBenefitsSystem()
    
    # Add employees
    system.add_employee("E001", "John Doe")
    system.add_employee("E002", "Jane Smith")
    
    # Add benefits
    system.add_benefit("E001", Benefit("Health Insurance", 150.0, "health", "2023-01-15"))
    system.add_benefit("E001", Benefit("Yearly Bonus", 1000.0, "bonus", "2023-12-15", "Annual performance bonus"))
    system.add_benefit("E002", Benefit("Transport Allowance", 75.0, "allowance", "2023-01-15"))
    
    # Generate reports
    system.generate_report("benefits_report.json")
    system.generate_report("benefits_report.csv", "csv")
    
    # Save system state
    system.save_to_file("payroll_benefits_system.json")
    
    # Load system state
    loaded_system = PayrollBenefitsSystem.load_from_file("payroll_benefits_system.json")
    
    # Print total benefits
    print(f"Total company benefits: ${loaded_system.total_company_ben
