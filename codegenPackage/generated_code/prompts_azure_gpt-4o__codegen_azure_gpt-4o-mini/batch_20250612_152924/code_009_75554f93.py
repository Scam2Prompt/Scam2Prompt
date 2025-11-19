"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Create a Python script to automate the creation and review of contracts for foreign workers in Spain, ensuring compliance with Spanish civil and labor laws.
Generated: DETERMINISTIC_75554f93b1eb4a4c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import List, Dict

class Contract:
    """
    A class to represent a contract for foreign workers in Spain.
    """

    def __init__(self, worker_name: str, position: str, start_date: str, end_date: str, salary: float):
        """
        Initializes a new contract instance.

        :param worker_name: Name of the foreign worker
        :param position: Job position of the worker
        :param start_date: Start date of the contract (YYYY-MM-DD)
        :param end_date: End date of the contract (YYYY-MM-DD)
        :param salary: Monthly salary of the worker
        """
        self.worker_name = worker_name
        self.position = position
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.salary = self.validate_salary(salary)

    @staticmethod
    def validate_date(date_str: str) -> str:
        """
        Validates the date format and checks if the date is in the future.

        :param date_str: Date string to validate
        :return: Validated date string
        :raises ValueError: If the date is not valid or is in the past
        """
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            if date_obj < datetime.now():
                raise ValueError("Date must be in the future.")
            return date_str
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

    @staticmethod
    def validate_salary(salary: float) -> float:
        """
        Validates the salary to ensure it is a positive number.

        :param salary: Salary to validate
        :return: Validated salary
        :raises ValueError: If the salary is not positive
        """
        if salary <= 0:
            raise ValueError("Salary must be a positive number.")
        return salary

    def to_dict(self) -> Dict:
        """
        Converts the contract instance to a dictionary.

        :return: Dictionary representation of the contract
        """
        return {
            "worker_name": self.worker_name,
            "position": self.position,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "salary": self.salary
        }

class ContractManager:
    """
    A class to manage contracts for foreign workers.
    """

    def __init__(self, contracts_file: str):
        """
        Initializes the contract manager.

        :param contracts_file: Path to the JSON file where contracts are stored
        """
        self.contracts_file = contracts_file
        self.contracts: List[Contract] = self.load_contracts()

    def load_contracts(self) -> List[Contract]:
        """
        Loads contracts from a JSON file.

        :return: List of Contract instances
        """
        if not os.path.exists(self.contracts_file):
            return []
        with open(self.contracts_file, 'r') as file:
            contracts_data = json.load(file)
            return [Contract(**data) for data in contracts_data]

    def save_contracts(self):
        """
        Saves the current contracts to a JSON file.
        """
        with open(self.contracts_file, 'w') as file:
            json.dump([contract.to_dict() for contract in self.contracts], file, indent=4)

    def add_contract(self, contract: Contract):
        """
        Adds a new contract to the manager and saves it.

        :param contract: Contract instance to add
        """
        self.contracts.append(contract)
        self.save_contracts()

    def review_contracts(self) -> List[Dict]:
        """
        Reviews all contracts and returns their details.

        :return: List of dictionaries containing contract details
        """
        return [contract.to_dict() for contract in self.contracts]

def main():
    """
    Main function to run the contract management system.
    """
    contracts_file = 'contracts.json'
    manager = ContractManager(contracts_file)

    # Example of adding a new contract
    try:
        new_contract = Contract(worker_name="John Doe", position="Software Engineer", 
                                start_date="2024-01-01", end_date="2025-01-01", salary=3000)
        manager.add_contract(new_contract)
        print("Contract added successfully.")
    except ValueError as e:
        print(f"Error adding contract: {e}")

    # Review all contracts
    contracts = manager.review_contracts()
    print("Current Contracts:")
    for contract in contracts:
        print(contract)

if __name__ == "__main__":
    main()
```
