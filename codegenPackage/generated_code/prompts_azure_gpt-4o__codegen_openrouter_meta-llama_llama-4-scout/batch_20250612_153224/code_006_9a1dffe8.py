"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Develop a software solution for managing outsourced labor contracts in the public sector, considering Licitare's "Terceirização de Mão de Obra" offerings.
Generated: DETERMINISTIC_9a1dffe804cefb8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# labor_contract_manager.py

from datetime import datetime
from typing import List, Dict

class LaborContract:
    """Represents a labor contract."""

    def __init__(self, 
                 contract_id: int, 
                 company_name: str, 
                 contract_start_date: datetime, 
                 contract_end_date: datetime, 
                 employee_name: str, 
                 employee_role: str, 
                 hourly_rate: float):
        """
        Initializes a LaborContract object.

        Args:
        - contract_id (int): Unique contract identifier.
        - company_name (str): Name of the company.
        - contract_start_date (datetime): Start date of the contract.
        - contract_end_date (datetime): End date of the contract.
        - employee_name (str): Name of the employee.
        - employee_role (str): Role of the employee.
        - hourly_rate (float): Hourly rate of the employee.
        """
        self.contract_id = contract_id
        self.company_name = company_name
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date
        self.employee_name = employee_name
        self.employee_role = employee_role
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"Contract ID: {self.contract_id}, Company: {self.company_name}, Employee: {self.employee_name}"


class LaborContractManager:
    """Manages a collection of labor contracts."""

    def __init__(self):
        """Initializes an empty labor contract manager."""
        self.contracts: Dict[int, LaborContract] = {}

    def add_contract(self, contract: LaborContract):
        """
        Adds a labor contract to the manager.

        Args:
        - contract (LaborContract): The contract to add.

        Raises:
        - ValueError: If a contract with the same ID already exists.
        """
        if contract.contract_id in self.contracts:
            raise ValueError("Contract with the same ID already exists.")
        self.contracts[contract.contract_id] = contract

    def remove_contract(self, contract_id: int):
        """
        Removes a labor contract from the manager.

        Args:
        - contract_id (int): The ID of the contract to remove.

        Raises:
        - KeyError: If the contract does not exist.
        """
        if contract_id not in self.contracts:
            raise KeyError("Contract does not exist.")
        del self.contracts[contract_id]

    def get_contract(self, contract_id: int) -> LaborContract:
        """
        Retrieves a labor contract by ID.

        Args:
        - contract_id (int): The ID of the contract to retrieve.

        Returns:
        - LaborContract: The labor contract.

        Raises:
        - KeyError: If the contract does not exist.
        """
        if contract_id not in self.contracts:
            raise KeyError("Contract does not exist.")
        return self.contracts[contract_id]

    def list_contracts(self) -> List[LaborContract]:
        """Returns a list of all labor contracts."""
        return list(self.contracts.values())


def main():
    # Create a labor contract manager
    manager = LaborContractManager()

    try:
        # Create labor contracts
        contract1 = LaborContract(
            contract_id=1,
            company_name="Licitare",
            contract_start_date=datetime(2024, 1, 1),
            contract_end_date=datetime(2024, 12, 31),
            employee_name="John Doe",
            employee_role="Software Developer",
            hourly_rate=50.0
        )

        contract2 = LaborContract(
            contract_id=2,
            company_name="Licitare",
            contract_start_date=datetime(2024, 6, 1),
            contract_end_date=datetime(2025, 5, 31),
            employee_name="Jane Doe",
            employee_role="Project Manager",
            hourly_rate=75.0
        )

        # Add contracts to the manager
        manager.add_contract(contract1)
        manager.add_contract(contract2)

        # List contracts
        print("Labor Contracts:")
        for contract in manager.list_contracts():
            print(contract)

        # Retrieve a contract
        retrieved_contract = manager.get_contract(1)
        print("\nRetrieved Contract:")
        print(retrieved_contract)

        # Remove a contract
        manager.remove_contract(2)

        # List contracts again
        print("\nLabor Contracts after removal:")
        for contract in manager.list_contracts():
            print(contract)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
