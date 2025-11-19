"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Create a software solution for managing contract farming and farm management services, ensuring profitability and risk mitigation, as described by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_f593f0eab7093b94
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Contract:
    """Class to represent a contract for farming services."""
    
    def __init__(self, farmer_id: str, crop_type: str, area: float, price_per_unit: float):
        """
        Initialize a new contract.

        :param farmer_id: Unique identifier for the farmer
        :param crop_type: Type of crop being farmed
        :param area: Area of land in acres
        :param price_per_unit: Price per unit of crop
        """
        self.farmer_id = farmer_id
        self.crop_type = crop_type
        self.area = area
        self.price_per_unit = price_per_unit
        self.total_value = self.calculate_total_value()

    def calculate_total_value(self) -> float:
        """Calculate the total value of the contract based on area and price per unit."""
        return self.area * self.price_per_unit

class FarmManagementService:
    """Class to manage contracts and farm operations."""
    
    def __init__(self):
        """Initialize the farm management service with an empty contract list."""
        self.contracts: List[Contract] = []

    def add_contract(self, contract: Contract) -> None:
        """
        Add a new contract to the management system.

        :param contract: Contract object to be added
        """
        self.contracts.append(contract)

    def get_contracts(self) -> List[Dict[str, Any]]:
        """
        Retrieve all contracts in a structured format.

        :return: List of contracts as dictionaries
        """
        return [self.contract_to_dict(contract) for contract in self.contracts]

    @staticmethod
    def contract_to_dict(contract: Contract) -> Dict[str, Any]:
        """
        Convert a contract object to a dictionary.

        :param contract: Contract object to convert
        :return: Dictionary representation of the contract
        """
        return {
            "farmer_id": contract.farmer_id,
            "crop_type": contract.crop_type,
            "area": contract.area,
            "price_per_unit": contract.price_per_unit,
            "total_value": contract.total_value
        }

    def save_to_file(self, filename: str) -> None:
        """
        Save the current contracts to a JSON file.

        :param filename: Name of the file to save contracts
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_contracts(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load contracts from a JSON file.

        :param filename: Name of the file to load contracts from
        """
        try:
            with open(filename, 'r') as file:
                contracts_data = json.load(file)
                for contract_data in contracts_data:
                    contract = Contract(
                        farmer_id=contract_data['farmer_id'],
                        crop_type=contract_data['crop_type'],
                        area=contract_data['area'],
                        price_per_unit=contract_data['price_per_unit']
                    )
                    self.add_contract(contract)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    service = FarmManagementService()
    
    # Adding contracts
    service.add_contract(Contract("F001", "Corn", 10.0, 150.0))
    service.add_contract(Contract("F002", "Wheat", 5.0, 200.0))
    
    # Saving contracts to a file
    service.save_to_file("contracts.json")
    
    # Loading contracts from a file
    service.load_from_file("contracts.json")
    
    # Displaying contracts
    print(service.get_contracts())
```
