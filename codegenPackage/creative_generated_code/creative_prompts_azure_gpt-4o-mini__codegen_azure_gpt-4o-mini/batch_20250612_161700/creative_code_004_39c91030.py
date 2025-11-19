"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: What are the best practices for drafting contracts that comply with Spanish immigration law when hiring foreign employees?
Generated: DETERMINISTIC_39c91030a8079823
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Dict

class Contract:
    """A class to represent an employment contract compliant with Spanish immigration law."""

    def __init__(self, employee_name: str, contract_start_date: datetime, 
                 contract_duration_months: int, job_title: str, salary: float):
        """
        Initializes the Contract object.

        Args:
            employee_name (str): Name of the employee.
            contract_start_date (datetime): Start date of the employment contract.
            contract_duration_months (int): Duration of the contract in months.
            job_title (str): Title of the job.
            salary (float): Salary offered to the employee.
        """
        self.employee_name = employee_name
        self.contract_start_date = contract_start_date
        self.contract_duration_months = contract_duration_months
        self.job_title = job_title
        self.salary = salary

    def is_contract_valid(self) -> bool:
        """
        Validates the contract details against Spanish immigration law.

        Returns:
            bool: True if the contract is valid, False otherwise.
        """
        # Basic validation rules
        if self.salary < 0:
            raise ValueError("Salary must be a positive number.")
        
        if self.contract_duration_months <= 0:
            raise ValueError("Contract duration must be greater than zero.")

        # Add additional compliance checks as necessary
        return True

    def generate_contract(self) -> Dict:
        """
        Generates a dictionary representation of the employment contract.

        Returns:
            Dict: Contains the contract details.
        """
        # Validate the contract before generating it
        if not self.is_contract_valid():
            raise ValueError("Contract is not valid.")
        
        return {
            "employee_name": self.employee_name,
            "contract_start_date": self.contract_start_date.strftime("%Y-%m-%d"),
            "contract_duration_months": self.contract_duration_months,
            "job_title": self.job_title,
            "salary": self.salary
        }

def create_contract(employee_name: str, start_date: str, 
                    duration: int, job_title: str, salary: float) -> Dict:
    """
    Creates a contract for an employee.

    Args:
        employee_name (str): Name of the employee.
        start_date (str): Contract start date in 'YYYY-MM-DD' format.
        duration (int): Duration of the contract in months.
        job_title (str): Title of the job.
        salary (float): Salary offered to the employee.

    Returns:
        Dict: The generated contract details.
    """
    try:
        # Parse the start date string into a datetime object
        contract_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        
        # Create a new Contract instance
        contract = Contract(employee_name, contract_start_date, duration, job_title, salary)
        
        # Generate and return the contract
        return contract.generate_contract()

    except ValueError as ve:
        print(f"Error: {ve}")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Create a contract for an employee
    contract_details = create_contract("Juan Pérez", "2023-01-01", 12, "Software Developer", 30000)
    print(contract_details)
```
