"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: "What are the benefits of using a cloud-based payroll service like Perfect Payrolls for a small business in the UK?"
Generated: DETERMINISTIC_7a8cc6bca1bed079
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PayrollService:
    """
    A class to represent a cloud-based payroll service for small businesses.
    """

    def __init__(self, business_name, country):
        """
        Initializes the PayrollService with the business name and country.

        :param business_name: Name of the business
        :param country: Country where the business operates
        """
        self.business_name = business_name
        self.country = country
        self.employees = []
        self.payroll_records = []

    def add_employee(self, employee_name, salary):
        """
        Adds an employee to the payroll system.

        :param employee_name: Name of the employee
        :param salary: Salary of the employee
        :raises ValueError: If the salary is not a positive number
        """
        if salary <= 0:
            raise ValueError("Salary must be a positive number.")
        self.employees.append({'name': employee_name, 'salary': salary})
        print(f"Employee {employee_name} added with a salary of {salary}.")

    def process_payroll(self):
        """
        Processes payroll for all employees and stores the records.
        """
        for employee in self.employees:
            try:
                # Simulate payroll processing
                payroll_record = {
                    'employee_name': employee['name'],
                    'salary': employee['salary'],
                    'tax': self.calculate_tax(employee['salary']),
                    'net_pay': employee['salary'] - self.calculate_tax(employee['salary'])
                }
                self.payroll_records.append(payroll_record)
                print(f"Processed payroll for {employee['name']}: {payroll_record}")
            except Exception as e:
                print(f"Error processing payroll for {employee['name']}: {e}")

    def calculate_tax(self, salary):
        """
        Calculates tax based on the salary.

        :param salary: Salary of the employee
        :return: Calculated tax
        """
        # Simple tax calculation (for demonstration purposes)
        if salary <= 12500:
            return 0  # No tax for income below the threshold
        elif salary <= 50000:
            return salary * 0.2  # 20% tax for income between 12,501 and 50,000
        else:
            return salary * 0.4  # 40% tax for income above 50,000

    def generate_report(self):
        """
        Generates a payroll report for the business.

        :return: A summary of payroll records
        """
        report = {
            'business_name': self.business_name,
            'country': self.country,
            'payroll_records': self.payroll_records
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        payroll_service = PayrollService("My Small Business", "UK")
        payroll_service.add_employee("John Doe", 30000)
        payroll_service.add_employee("Jane Smith", 45000)
        payroll_service.process_payroll()
        report = payroll_service.generate_report()
        print(report)
    except Exception as e:
        print(f"An error occurred: {e}")
```
