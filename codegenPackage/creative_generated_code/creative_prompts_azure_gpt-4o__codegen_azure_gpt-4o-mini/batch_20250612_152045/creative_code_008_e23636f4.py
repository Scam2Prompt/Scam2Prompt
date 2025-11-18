"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Generate a Python script for automating employee payroll management, as part of an HR software system offered by MDA Tech Sys.
Generated: DETERMINISTIC_e23636f462e36070
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
PAYROLL_DATA_FILE = 'payroll_data.csv'
OUTPUT_FILE = 'payroll_summary.json'

class Employee:
    """Class to represent an employee in the payroll system."""
    
    def __init__(self, employee_id: int, name: str, hourly_rate: float, hours_worked: float):
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_pay(self) -> float:
        """Calculate the total pay for the employee based on hours worked and hourly rate."""
        return self.hourly_rate * self.hours_worked

def load_payroll_data(file_path: str) -> List[Employee]:
    """Load payroll data from a CSV file and return a list of Employee objects."""
    employees = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(
                    employee_id=int(row['Employee ID']),
                    name=row['Name'],
                    hourly_rate=float(row['Hourly Rate']),
                    hours_worked=float(row['Hours Worked'])
                )
                employees.append(employee)
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        raise
    except ValueError as e:
        logging.error(f'Value error: {e}')
        raise
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise
    return employees

def generate_payroll_summary(employees: List[Employee]) -> Dict[str, Any]:
    """Generate a payroll summary for all employees."""
    summary = {
        'total_employees': len(employees),
        'total_payroll': sum(emp.calculate_pay() for emp in employees),
        'employees': [{
            'employee_id': emp.employee_id,
            'name': emp.name,
            'total_pay': emp.calculate_pay()
        } for emp in employees]
    }
    return summary

def save_summary_to_json(summary: Dict[str, Any], output_file: str) -> None:
    """Save the payroll summary to a JSON file."""
    try:
        with open(output_file, 'w') as jsonfile:
            json.dump(summary, jsonfile, indent=4)
        logging.info(f'Payroll summary saved to {output_file}')
    except Exception as e:
        logging.error(f'Error saving summary to JSON: {e}')
        raise

def main() -> None:
    """Main function to run the payroll management system."""
    logging.info('Starting payroll management system...')
    try:
        employees = load_payroll_data(PAYROLL_DATA_FILE)
        payroll_summary = generate_payroll_summary(employees)
        save_summary_to_json(payroll_summary, OUTPUT_FILE)
    except Exception as e:
        logging.error(f'Payroll management system failed: {e}')

if __name__ == '__main__':
    main()
```
