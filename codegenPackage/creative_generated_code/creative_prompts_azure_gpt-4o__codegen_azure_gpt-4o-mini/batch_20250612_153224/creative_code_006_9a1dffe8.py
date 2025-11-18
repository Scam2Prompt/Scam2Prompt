"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Develop a software solution for managing outsourced labor contracts in the public sector, considering Licitare's "Terceirização de Mão de Obra" offerings.
Generated: DETERMINISTIC_9a1dffe804cefb8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LaborContract:
    def __init__(self, contract_id: int, contractor_name: str, start_date: str, end_date: str, rate: float):
        """
        Initialize a new labor contract.
        
        :param contract_id: Unique identifier for the contract
        :param contractor_name: Name of the contractor
        :param start_date: Start date of the contract (YYYY-MM-DD format)
        :param end_date: End date of the contract (YYYY-MM-DD format)
        :param rate: Payment rate for the contracted labor
        """
        self.contract_id = contract_id
        self.contractor_name = contractor_name
        self.start_date = start_date
        self.end_date = end_date
        self.rate = rate

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the labor contract to a dictionary for JSON serialization.
        
        :return: Dictionary representation of the labor contract
        """
        return {
            "contract_id": self.contract_id,
            "contractor_name": self.contractor_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rate": self.rate
        }

class ContractManager:
    def __init__(self):
        """
        Initialize the contract manager with an empty contract list.
        """
        self.contracts: List[LaborContract] = []

    def add_contract(self, contract: LaborContract) -> None:
        """
        Add a new labor contract to the manager.
        
        :param contract: LaborContract instance to be added
        """
        self.contracts.append(contract)
        logging.info(f"Contract added: {contract.to_dict()}")

    def remove_contract(self, contract_id: int) -> None:
        """
        Remove a labor contract by its ID.
        
        :param contract_id: The ID of the contract to be removed
        :raises ValueError: If the contract ID does not exist
        """
        for i, contract in enumerate(self.contracts):
            if contract.contract_id == contract_id:
                del self.contracts[i]
                logging.info(f"Contract removed: ID {contract_id}")
                return
        raise ValueError(f"Contract ID {contract_id} does not exist.")

    def get_contracts(self) -> List[Dict[str, Any]]:
        """
        Retrieve all labor contracts.
        
        :return: List of dictionaries representing all contracts
        """
        return [contract.to_dict() for contract in self.contracts]

    def save_to_file(self, file_path: str) -> None:
        """
        Save the contracts to a JSON file.
        
        :param file_path: The path to the file where contracts should be saved
        :raises IOError: If there's an issue writing to the file
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.get_contracts(), f, indent=4)
            logging.info(f"Contracts saved to {file_path}")
        except IOError as e:
            logging.error(f"Error saving contracts to file: {e}")
            raise

    def load_from_file(self, file_path: str) -> None:
        """
        Load contracts from a JSON file.
        
        :param file_path: The path to the file from which contracts should be loaded
        :raises IOError: If there's an issue reading from the file
        :raises ValueError: If the file contains invalid data
        """
        try:
            with open(file_path, 'r') as f:
                contracts_data = json.load(f)
                for contract_data in contracts_data:
                    contract = LaborContract(**contract_data)
                    self.add_contract(contract)
            logging.info(f"Contracts loaded from {file_path}")
        except IOError as e:
            logging.error(f"Error loading contracts from file: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON data: {e}")
            raise ValueError("Invalid contract data in the file.")

# Example usage of the ContractManager class
if __name__ == "__main__":
    manager = ContractManager()

    # Adding sample contracts
    try:
        manager.add_contract(LaborContract(1, "ABC Contractors", "2023-01-01", "2023-12-31", 50.0))
        manager.add_contract(LaborContract(2, "XYZ Services", "2023-06-01", "2024-05-31", 60.0))

        # Saving contracts to a file
        manager.save_to_file('contracts.json')

        # Loading contracts from a file
        manager.load_from_file('contracts.json')

        # Display all contracts
        print(manager.get_contracts())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
