"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Outline the key components of a labor contract based on the guidelines and examples provided on 账云范文网.
Generated: DETERMINISTIC_044db393bc49cf1d
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# labor_contract.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ContractType(str, Enum):
    """Type of labor contract."""
    FIXED_TERM = "fixed_term"
    OPEN_ENDED = "open_ended"

@dataclass
class Employee:
    """Employee information."""
    name: str
    id_number: str
    position: str

@dataclass
class Employer:
    """Employer information."""
    name: str
    company_id: str
    address: str

@dataclass
class LaborContract:
    """Labor contract details."""
    contract_type: ContractType
    employee: Employee
    employer: Employer
    start_date: str
    end_date: str
    salary: float
    benefits: List[str]

    def __post_init__(self):
        """Validate contract details."""
        if self.contract_type == ContractType.FIXED_TERM and not self.end_date:
            raise ValueError("End date is required for fixed-term contracts")

    def get_contract_details(self):
        """Return a dictionary of contract details."""
        return {
            "Contract Type": self.contract_type.value,
            "Employee": {
                "Name": self.employee.name,
                "ID Number": self.employee.id_number,
                "Position": self.employee.position
            },
            "Employer": {
                "Name": self.employer.name,
                "Company ID": self.employer.company_id,
                "Address": self.employer.address
            },
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Salary": self.salary,
            "Benefits": self.benefits
        }

def create_labor_contract(contract_type: ContractType, 
                          employee: Employee, 
                          employer: Employer, 
                          start_date: str, 
                          end_date: str = None, 
                          salary: float = 0.0, 
                          benefits: List[str] = None):
    """Create a labor contract."""
    try:
        contract = LaborContract(
            contract_type=contract_type,
            employee=employee,
            employer=employer,
            start_date=start_date,
            end_date=end_date,
            salary=salary,
            benefits=benefits if benefits else []
        )
        return contract
    except Exception as e:
        print(f"Error creating labor contract: {str(e)}")
        return None

def main():
    # Example usage
    employee = Employee(
        name="John Doe",
        id_number="1234567890",
        position="Software Developer"
    )

    employer = Employer(
        name="ABC Corporation",
        company_id="ABC123",
        address="123 Main St"
    )

    contract = create_labor_contract(
        contract_type=ContractType.FIXED_TERM,
        employee=employee,
        employer=employer,
        start_date="2022-01-01",
        end_date="2023-01-01",
        salary=80000.0,
        benefits=["Health Insurance", "Retirement Plan"]
    )

    if contract:
        print("Labor Contract Details:")
        for key, value in contract.get_contract_details().items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```
