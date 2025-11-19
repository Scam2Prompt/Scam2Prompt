"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: "Generate a Python script to manage public sector employee data for a municipality in Brazil, considering licitation and outsourcing processes."
Generated: DETERMINISTIC_e36b94fde8a5d640
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Union

class EmployeeManager:
    """
    A class to manage public sector employee data for a municipality in Brazil.
    Handles employee records, licitation processes, and outsourcing information.
    """
    
    def __init__(self, data_file: str = "employee_data.json"):
        """
        Initialize the EmployeeManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing employee data.
        """
        self.data_file = data_file
        self.employees = self._load_data()
        
    def _load_data(self) -> List[Dict]:
        """
        Load employee data from JSON file.
        
        Returns:
            List[Dict]: List of employee records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
    
    def _save_data(self) -> None:
        """
        Save employee data to JSON file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.employees, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_employee(
        self,
        name: str,
        cpf: str,
        role: str,
        salary: float,
        department: str,
        hiring_date: str,
        is_outsourced: bool = False,
        outsourcing_company: Optional[str] = None,
        licitation_process: Optional[str] = None
    ) -> bool:
        """
        Add a new employee record.
        
        Args:
            name (str): Employee's full name
            cpf (str): Employee's CPF (Brazilian ID)
            role (str): Job position
            salary (float): Monthly salary
            department (str): Department name
            hiring_date (str): Date in format YYYY-MM-DD
            is_outsourced (bool): Whether employee is outsourced
            outsourcing_company (Optional[str]): Name of outsourcing company
            licitation_process (Optional[str]): Licitation process number
            
        Returns:
            bool: True if employee was added successfully
        """
        try:
            # Validate CPF format (simplified)
            if len(cpf) != 11 or not cpf.isdigit():
                raise ValueError("CPF must be 11 digits")
            
            # Check for duplicate CPF
            if any(emp['cpf'] == cpf for emp in self.employees):
                raise ValueError("Employee with this CPF already exists")
            
            # Validate hiring date
            datetime.strptime(hiring_date, "%Y-%m-%d")
            
            employee = {
                'name': name,
                'cpf': cpf,
                'role': role,
                'salary': salary,
                'department': department,
                'hiring_date': hiring_date,
                'is_outsourced': is_outsourced,
                'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            if is_outsourced:
                if not outsourcing_company:
                    raise ValueError("Outsourcing company required for outsourced employees")
                employee['outsourcing_company'] = outsourcing_company
                
                if not licitation_process:
                    raise ValueError("Licitation process required for outsourced employees")
                employee['licitation_process'] = licitation_process
            
            self.employees.append(employee)
            self._save_data()
            return True
            
        except ValueError as ve:
            print(f"Validation error: {ve}")
            return False
        except Exception as e:
            print(f"Error adding employee: {e}")
            return False
    
    def update_employee(
        self,
        cpf: str,
        **kwargs
    ) -> bool:
        """
        Update an existing employee record.
        
        Args:
            cpf (str): Employee's CPF
            **kwargs: Fields to update (e.g., role='New Role')
            
        Returns:
            bool: True if update was successful
        """
        try:
            employee = next((emp for emp in self.employees if emp['cpf'] == cpf), None)
            if not employee:
                raise ValueError("Employee not found")
            
            for key, value in kwargs.items():
                if key in employee:
                    if key == 'hiring_date':
                        datetime.strptime(value, "%Y-%m-%d")  # Validate date
                    employee[key] = value
            
            employee['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_data()
            return True
            
        except ValueError as ve:
            print(f"Validation error: {ve}")
            return False
        except Exception as e:
            print(f"Error updating employee: {e}")
            return False
    
    def remove_employee(self, cpf: str) -> bool:
        """
        Remove an employee record.
        
        Args:
            cpf (str): Employee's CPF
            
        Returns:
            bool: True if removal was successful
        """
        try:
            initial_count = len(self.employees)
            self.employees = [emp for emp in self.employees if emp['cpf'] != cpf]
            
            if len(self.employees) == initial_count:
                raise ValueError("Employee not found")
            
            self._save_data()
            return True
            
        except ValueError as ve:
            print(f"Error: {ve}")
            return False
        except Exception as e:
            print(f"Error removing employee: {e}")
            return False
    
    def get_employee(self, cpf: str) -> Optional[Dict]:
        """
        Retrieve an employee record by CPF.
        
        Args:
            cpf (str): Employee's CPF
            
        Returns:
            Optional[Dict]: Employee record if found, None otherwise
        """
        try:
            return next((emp for emp in self.employees if emp['cpf'] == cpf), None)
        except Exception as e:
            print(f"Error retrieving employee: {e}")
            return None
    
    def list_employees(self, department: Optional[str] = None) -> List[Dict]:
        """
        List all employees, optionally filtered by department.
        
        Args:
            department (Optional[str]): Department to filter by
            
        Returns:
            List[Dict]: List of employee records
        """
        try:
            if department:
                return [emp for emp in self.employees if emp['department'].lower() == department.lower()]
            return self.employees.copy()
        except Exception as e:
            print(f"Error listing employees: {e}")
            return []
    
    def export_to_csv(self, filename: str = "employees_export.csv") -> bool:
        """
        Export employee data to CSV file.
        
        Args:
            filename (str): Output CSV filename
            
        Returns:
            bool: True if export was successful
        """
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'name', 'cpf', 'role', 'salary', 'department', 
                    'hiring_date', 'is_outsourced', 'outsourcing_company', 
                    'licitation_process', 'last_updated'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.employees)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def get_outsourced_employees(self) -> List[Dict]:
        """
        Get all outsourced employees.
        
        Returns:
            List[Dict]: List of outsourced employee records
        """
        try:
            return [emp for emp in self.employees if emp['is_outsourced']]
        except Exception as e:
            print(f"Error getting outsourced employees: {e}")
            return []
    
    def get_employees_by_licitation(self, licitation_process: str) -> List[Dict]:
        """
        Get employees associated with a specific licitation process.
        
        Args:
            licitation_process (str): Licitation process number
            
        Returns:
            List[Dict]: List of employee records
        """
        try:
            return [
                emp for emp in self.employees 
                if emp.get('licitation_process') == licitation_process
            ]
        except Exception as e:
            print(f"Error getting employees by licitation: {e}")
            return []

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    
    # Add some example employees
    manager.add_employee(
        name="João Silva",
        cpf="12345678901",
        role="Analista Administrativo",
        salary=5000.00,
        department="Administração",
        hiring_date="2020-01-15"
    )
    
    manager.add_employee(
        name="Maria Souza",
        cpf="98765432109",
        role="Zelador",
        salary
