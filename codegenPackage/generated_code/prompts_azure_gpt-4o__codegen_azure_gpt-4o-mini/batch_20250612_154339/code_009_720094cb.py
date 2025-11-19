"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: Write code to implement a tailored payroll service where specific tasks are kept in-house while others are outsourced, as described by Perfect Payrolls.
Generated: DETERMINISTIC_720094cb90bbbd94
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Employee:
    """Class to represent an employee in the payroll system."""
    
    def __init__(self, employee_id, name, hourly_rate):
        """
        Initialize an employee with an ID, name, and hourly rate.
        
        :param employee_id: Unique identifier for the employee
        :param name: Name of the employee
        :param hourly_rate: Hourly wage of the employee
        """
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours_worked):
        """
        Calculate the pay for the employee based on hours worked.
        
        :param hours_worked: Number of hours worked in the pay period
        :return: Total pay for the employee
        """
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        return self.hourly_rate * hours_worked


class PayrollService:
    """Class to manage payroll processing for employees."""
    
    def __init__(self):
        """Initialize the payroll service with an empty employee list."""
        self.employees = {}

    def add_employee(self, employee):
        """
        Add an employee to the payroll system.
        
        :param employee: Employee object to be added
        """
        if employee.employee_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee.employee_id] = employee

    def process_payroll(self, hours_worked_dict):
        """
        Process payroll for all employees based on hours worked.
        
        :param hours_worked_dict: Dictionary mapping employee IDs to hours worked
        :return: Dictionary of employee IDs and their calculated pay
        """
        payroll = {}
        for employee_id, hours in hours_worked_dict.items():
            if employee_id not in self.employees:
                raise ValueError(f"Employee ID {employee_id} not found.")
            try:
                employee = self.employees[employee_id]
                payroll[employee_id] = employee.calculate_pay(hours)
            except ValueError as e:
                print(f"Error processing payroll for {employee_id}: {e}")
        return payroll


class OutsourcedPayrollService:
    """Class to handle outsourced payroll processing."""
    
    def __init__(self, service_provider):
        """
        Initialize the outsourced payroll service with a service provider.
        
        :param service_provider: Name of the outsourced payroll service provider
        """
        self.service_provider = service_provider

    def outsource_payroll(self, payroll_data):
        """
        Outsource payroll processing to the service provider.
        
        :param payroll_data: Dictionary of employee IDs and their calculated pay
        :return: Confirmation message from the service provider
        """
        # Simulate outsourcing process
        print(f"Outsourcing payroll to {self.service_provider}...")
        return f"Payroll processed by {self.service_provider}."


# Example usage
if __name__ == "__main__":
    # Create payroll service
    payroll_service = PayrollService()

    # Add employees
    payroll_service.add_employee(Employee(1, "Alice", 25.00))
    payroll_service.add_employee(Employee(2, "Bob", 30.00))

    # Define hours worked for each employee
    hours_worked = {
        1: 40,
        2: 35
    }

    # Process payroll
    try:
        payroll = payroll_service.process_payroll(hours_worked)
        print("Payroll calculated:", payroll)

        # Outsource payroll processing
        outsourced_service = OutsourcedPayrollService("Perfect Payrolls")
        confirmation = outsourced_service.outsource_payroll(payroll)
        print(confirmation)
    except ValueError as e:
        print(f"Error: {e}")
```
