"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: What are the best practices for drafting contracts that comply with Spanish immigration law when hiring foreign employees?
Generated: DETERMINISTIC_39c91030a8079823
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ContractDrafting:
    """
    A class to handle the drafting of contracts that comply with Spanish immigration law
    when hiring foreign employees.
    """

    def __init__(self, employee_name, employee_nationality, job_title, salary):
        """
        Initializes the contract drafting with employee details.

        :param employee_name: str - Name of the employee
        :param employee_nationality: str - Nationality of the employee
        :param job_title: str - Job title for the employee
        :param salary: float - Salary offered to the employee
        """
        self.employee_name = employee_name
        self.employee_nationality = employee_nationality
        self.job_title = job_title
        self.salary = salary

    def validate_employee_details(self):
        """
        Validates the employee details to ensure they meet the required format.

        :raises ValueError: If any of the employee details are invalid.
        """
        if not isinstance(self.employee_name, str) or not self.employee_name:
            raise ValueError("Invalid employee name.")
        if not isinstance(self.employee_nationality, str) or not self.employee_nationality:
            raise ValueError("Invalid employee nationality.")
        if not isinstance(self.job_title, str) or not self.job_title:
            raise ValueError("Invalid job title.")
        if not isinstance(self.salary, (int, float)) or self.salary <= 0:
            raise ValueError("Invalid salary amount.")

    def draft_contract(self):
        """
        Drafts a contract based on the employee details.

        :return: str - The drafted contract.
        """
        self.validate_employee_details()

        contract_template = f"""
        Contract of Employment

        This contract is made between the employer and the employee.

        Employee Name: {self.employee_name}
        Nationality: {self.employee_nationality}
        Job Title: {self.job_title}
        Salary: €{self.salary:.2f}

        Terms and Conditions:
        1. The employee must comply with Spanish immigration laws.
        2. The employer will assist the employee in obtaining the necessary work visa.
        3. The employee must provide all required documentation for visa application.

        Signed,
        [Employer's Name]
        [Date]
        """

        return contract_template.strip()

def main():
    """
    Main function to execute the contract drafting process.
    """
    try:
        # Example employee details
        employee_name = "John Doe"
        employee_nationality = "USA"
        job_title = "Software Engineer"
        salary = 50000.00

        # Create a contract drafting instance
        contract_drafter = ContractDrafting(employee_name, employee_nationality, job_title, salary)

        # Draft the contract
        contract = contract_drafter.draft_contract()
        print(contract)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
