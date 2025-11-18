"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Write code to implement a tailored payroll service where specific tasks are kept in-house while others are outsourced, as described by Perfect Payrolls.
Generated: DETERMINISTIC_720094cb90bbbd94
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payroll_service.py

import logging
from datetime import datetime

# Set up logging to capture issues and operational details
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PayrollService:
    """
    A tailored payroll service where specific tasks are handled in-house 
    while others are outsourced. This service includes basic employee management 
    and payroll processing.
    """
    
    def __init__(self):
        self.employees = []
        logging.info("Initialized PayrollService")

    def add_employee(self, name, hourly_rate, is_outsourced):
        """
        Adds an employee to the payroll system.

        Args:
        name (str): Name of the employee.
        hourly_rate (float): Hourly rate for the employee.
        is_outsourced (bool): True if the employee's payroll is outsourced, else False.
        """
        try:
            employee = {
                'id': len(self.employees) + 1,
                'name': name,
                'hourly_rate': hourly_rate,
                'is_outsourced': is_outsourced
            }
            self.employees.append(employee)
            logging.info(f"Employee added: {employee}")
        except Exception as e:
            logging.error(f"Error adding employee: {str(e)}")
            raise

    def calculate_in_house_payroll(self):
        """
        Calculates the total payroll for in-house employees.

        Returns:
        float: Total payroll amount for in-house employees.
        """
        try:
            in_house_employees = [
                emp for emp in self.employees if not emp['is_outsourced']
            ]
            total_payroll = sum(emp['hourly_rate'] * 40 for emp in in_house_employees)  # Assuming 40 hours/week
            logging.info(f"In-house payroll calculated: ${total_payroll:.2f}")
            return total_payroll
        except Exception as e:
            logging.error(f"Error calculating in-house payroll: {str(e)}")
            raise

    def get_outsourced_employees(self):
        """
        Retrieves the list of outsourced employees.

        Returns:
        list: List of outsourced employees.
        """
        try:
            outsourced_employees = [
                emp for emp in self.employees if emp['is_outsourced']
            ]
            logging.info(f"Outsourced employees retrieved: {outsourced_employees}")
            return outsourced_employees
        except Exception as e:
            logging.error(f"Error retrieving outsourced employees: {str(e)}")
            raise

    def generate_pay_report(self):
        """
        Generates a payroll report for both in-house and outsourced employees.

        Returns:
        dict: Summary report of payroll data.
        """
        try:
            report = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'in_house_payroll': f"${self.calculate_in_house_payroll():.2f}",
                'outsourced_employees': len(self.get_outsourced_employees()),
                'total_employees': len(self.employees)
            }
            logging.info(f"Payroll report generated: {report}")
            return report
        except Exception as e:
            logging.error(f"Error generating payroll report: {str(e)}")
            raise


# Example usage (uncomment and run as needed):
# payroll_service = PayrollService()
# payroll_service.add_employee("Alice", 25.0, False)
# payroll_service.add_employee("Bob", 30.0, True)
# payroll_service.add_employee("Charlie", 20.0, False)
# print(payroll_service.generate_pay_report())
```
