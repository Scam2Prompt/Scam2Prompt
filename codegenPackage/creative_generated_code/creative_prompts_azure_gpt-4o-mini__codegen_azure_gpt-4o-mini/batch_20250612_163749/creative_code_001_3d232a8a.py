"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: How can I use the Perfect Payrolls online software to manage payroll for multiple employees with varying payment frequencies and allowances?
Generated: DETERMINISTIC_3d232a8aafb80fe7
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Payroll Management System for Perfect Payrolls

class Employee:
    """
    A class to represent an employee in the payroll system.
    """

    def __init__(self, name, salary, payment_frequency, allowances=None):
        """
        Initializes an employee with their details.

        Args:
            name (str): The name of the employee.
            salary (float): The base salary of the employee.
            payment_frequency (str): The frequency of payment (e.g., 'weekly', 'bi-weekly', 'monthly').
            allowances (dict): Additional allowances for the employee, default is None.
        """
        self.name = name
        self.salary = salary
        self.payment_frequency = payment_frequency
        self.allowances = allowances if allowances else {}

    def calculate_pay(self):
        """
        Calculates the total pay for the employee based on salary, frequency, and allowances.

        Returns:
            float: The total pay for the payment period.
        """
        frequency_mapping = {
            'weekly': 52,
            'bi-weekly': 26,
            'monthly': 12
        }

        # Get the number of payments per year
        try:
            payments_per_year = frequency_mapping[self.payment_frequency]
        except KeyError:
            raise ValueError("Invalid payment frequency. Choose from 'weekly', 'bi-weekly', 'monthly'.")

        # Calculate the base pay for the period
        pay_per_period = self.salary / payments_per_year

        # Add allowances to the pay
        total_allowances = sum(self.allowances.values())
        total_pay = pay_per_period + total_allowances

        return total_pay


class PayrollSystem:
    """
    A class to manage payroll for multiple employees.
    """

    def __init__(self):
        """
        Initializes the payroll system with an empty list of employees.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Adds an employee to the payroll system.

        Args:
            employee (Employee): An instance of the Employee class.
        """
        if not isinstance(employee, Employee):
            raise TypeError("Expected an instance of Employee.")
        self.employees.append(employee)

    def process_payroll(self):
        """
        Processes payroll for all employees and prints their pay details.
        """
        print("Processing Payroll...\n")
        for employee in self.employees:
            try:
                pay = employee.calculate_pay()
                print(f"Employee: {employee.name}, Pay: ${pay:.2f}, Frequency: {employee.payment_frequency}")
            except ValueError as e:
                print(f"Error processing {employee.name}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred for {employee.name}: {e}")


# Example Usage
if __name__ == "__main__":
    payroll_system = PayrollSystem()

    # Adding employees with different salaries, frequencies, and allowances
    emp1 = Employee(name="John Doe", salary=52000, payment_frequency="monthly", allowances={"bonus": 500, "transport": 200})
    emp2 = Employee(name="Jane Smith", salary=120000, payment_frequency="bi-weekly", allowances={"housing": 1000})
    emp3 = Employee(name="Alice Johnson", salary=48000, payment_frequency="weekly", allowances={"meal": 50})

    payroll_system.add_employee(emp1)
    payroll_system.add_employee(emp2)
    payroll_system.add_employee(emp3)

    # Process payroll
    payroll_system.process_payroll()
```
