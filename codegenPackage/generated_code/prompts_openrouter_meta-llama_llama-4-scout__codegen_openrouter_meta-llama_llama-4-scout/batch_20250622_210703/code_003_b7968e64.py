"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Create a sample contract for a 'prévoyance obsèques' (funeral foresight) service as offered by Adour Pompes Funèbres."
Generated: DETERMINISTIC_b7968e64b5bf0e9d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import Optional

class ContractStatus(str, Enum):
    """Status of the contract"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    EXPIRED = "expired"

class FuneralForesightService:
    """Service for prévoyance obsèques (funeral foresight)"""

    def __init__(self, 
                 contract_number: str, 
                 customer_name: str, 
                 contract_start_date: datetime, 
                 contract_end_date: Optional[datetime] = None):
        """
        Initialize a FuneralForesightService instance.

        Args:
        - contract_number (str): Unique contract number.
        - customer_name (str): Name of the customer.
        - contract_start_date (datetime): Start date of the contract.
        - contract_end_date (datetime, optional): End date of the contract. Defaults to None.
        """
        self.contract_number = contract_number
        self.customer_name = customer_name
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date
        self.status = ContractStatus.ACTIVE

    def activate_contract(self):
        """Activate the contract"""
        if self.status != ContractStatus.ACTIVE:
            self.status = ContractStatus.ACTIVE
            print(f"Contract {self.contract_number} activated.")

    def deactivate_contract(self):
        """Deactivate the contract"""
        if self.status != ContractStatus.INACTIVE:
            self.status = ContractStatus.INACTIVE
            print(f"Contract {self.contract_number} deactivated.")

    def expire_contract(self):
        """Expire the contract"""
        if self.status != ContractStatus.EXPIRED:
            self.status = ContractStatus.EXPIRED
            print(f"Contract {self.contract_number} expired.")

    def update_contract_end_date(self, new_end_date: datetime):
        """
        Update the contract end date.

        Args:
        - new_end_date (datetime): New end date of the contract.
        """
        self.contract_end_date = new_end_date

    def __str__(self):
        return f"Contract Number: {self.contract_number}\nCustomer Name: {self.customer_name}\nContract Start Date: {self.contract_start_date}\nContract End Date: {self.contract_end_date}\nStatus: {self.status.value}"

def create_sample_contract(contract_number: str, customer_name: str, contract_start_date: datetime) -> FuneralForesightService:
    """
    Create a sample contract for a 'prévoyance obsèques' service.

    Args:
    - contract_number (str): Unique contract number.
    - customer_name (str): Name of the customer.
    - contract_start_date (datetime): Start date of the contract.

    Returns:
    - FuneralForesightService: A sample FuneralForesightService instance.
    """
    try:
        sample_contract = FuneralForesightService(contract_number, customer_name, contract_start_date)
        return sample_contract
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    contract_number = "ADOUR-12345"
    customer_name = "John Doe"
    contract_start_date = datetime(2024, 1, 1)

    sample_contract = create_sample_contract(contract_number, customer_name, contract_start_date)
    if sample_contract:
        print(sample_contract)
        sample_contract.deactivate_contract()
        print(sample_contract)
```
