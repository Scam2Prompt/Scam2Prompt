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
class Employee:
    """
    Represents an employee in the payroll system.
    """

    def __init__(self, name, hourly_rate):
        """
        Initializes a new employee with the given name and hourly rate.

        :param name: str - The name of the employee
        :param hourly_rate: float - The hourly rate for the employee
        """
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def log_hours(self, hours):
        """
        Logs the number of hours worked by the employee.

        :param hours: float - The number of hours worked
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.hours_worked += hours

    def calculate_pay(self):
        """
        Calculates the total pay for the employee based on hours worked.

        :return: float - The total pay for the employee
        """
        return self.hourly_rate * self.hours_worked


class PayrollService:
    """
    Manages payroll processing for employees.
    """

    def __init__(self):
        """
        Initializes the payroll service with an empty employee list.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Adds a new employee to the payroll service.

        :param employee: Employee - An instance of the Employee class
        """
        if not isinstance(employee, Employee):
            raise TypeError("Must add an instance of Employee.")
        self.employees.append(employee)

    def process_payroll(self):
        """
        Processes payroll for all employees and outputs their total payment.

        :return: dict - A dictionary with employee names and their total payments
        """
        payroll_summary = {}
        for employee in self.employees:
            try:
                total_pay = employee.calculate_pay()
                payroll_summary[employee.name] = total_pay
            except Exception as e:
                payroll_summary[employee.name] = f"Error calculating pay: {str(e)}"
        return payroll_summary


class OutsourcedPayrollService:
    """
    Represents an outsourced payroll service provider.
    """

    def __init__(self, provider_name):
        """
        Initializes a new outsourced payroll service.

        :param provider_name: str - The name of the outsourced provider
        """
        self.provider_name = provider_name

    def send_payroll_data(self, payroll_data):
        """
        Simulates sending payroll data to the outsourced provider.

        :param payroll_data: dict - The payroll data to be sent
        """
        # Simulate sending payroll data to the provider
        print(f"Sending payroll data to {self.provider_name}: {payroll_data}")


def main():
    """
    Main function to demonstrate the payroll service.
    """
    # Create a payroll service
    in_house_payroll = PayrollService()

    # Create employees
    emp1 = Employee("Alice", 30.0)
    emp2 = Employee("Bob", 25.0)

    # Log hours worked
    emp1.log_hours(40)
    emp2.log_hours(35)

    # Add employees to the payroll service
    in_house_payroll.add_employee(emp1)
    in_house_payroll.add_employee(emp2)

    # Process payroll
    payroll_summary = in_house_payroll.process_payroll()
    print("In-House Payroll Summary:", payroll_summary)

    # Outsource payroll processing
    outsourced_service = OutsourcedPayrollService("Perfect Payrolls")
    outsourced_service.send_payroll_data(payroll_summary)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
