"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write a script to manage rental contracts for refrigerated vans, including features for tracking vehicle usage and ensuring timely delivery, inspired by the services on RefrigeratorTransport.com.
Generated: DETERMINISTIC_b39b5662837c2fa7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class RentalContractManager:
    """
    A class to manage rental contracts for refrigerated vans.
    Handles contract creation, tracking, and delivery management.
    """
    
    def __init__(self, storage_file: str = "rental_contracts.json"):
        """
        Initialize the RentalContractManager.
        
        Args:
            storage_file: Path to the JSON file for storing contract data.
        """
        self.storage_file = storage_file
        self.contracts = self._load_contracts()
        
    def _load_contracts(self) -> Dict[str, Dict]:
        """
        Load contracts from the storage file.
        
        Returns:
            Dictionary of contracts with contract IDs as keys.
        """
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading contracts: {e}")
            return {}
    
    def _save_contracts(self) -> bool:
        """
        Save contracts to the storage file.
        
        Returns:
            True if save was successful, False otherwise.
        """
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.contracts, f, indent=4)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving contracts: {e}")
            return False
    
    def create_contract(
        self,
        customer_name: str,
        van_id: str,
        start_date: str,
        end_date: str,
        delivery_address: str,
        temperature_range: Tuple[float, float],
        usage_limit_hours: Optional[int] = None
    ) -> Optional[str]:
        """
        Create a new rental contract.
        
        Args:
            customer_name: Name of the customer.
            van_id: ID of the refrigerated van.
            start_date: Contract start date (YYYY-MM-DD).
            end_date: Contract end date (YYYY-MM-DD).
            delivery_address: Delivery address for the van.
            temperature_range: Tuple of (min_temp, max_temp) in Celsius.
            usage_limit_hours: Optional maximum usage hours for the contract.
            
        Returns:
            Contract ID if successful, None otherwise.
        """
        try:
            contract_id = f"CON-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Validate dates
            start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            
            if end_dt <= start_dt:
                raise ValueError("End date must be after start date")
            
            contract = {
                "contract_id": contract_id,
                "customer_name": customer_name,
                "van_id": van_id,
                "start_date": start_date,
                "end_date": end_date,
                "delivery_address": delivery_address,
                "temperature_range": temperature_range,
                "usage_limit_hours": usage_limit_hours,
                "usage_hours": 0,
                "delivery_status": "pending",
                "created_at": datetime.datetime.now().isoformat(),
                "last_updated": datetime.datetime.now().isoformat()
            }
            
            self.contracts[contract_id] = contract
            if self._save_contracts():
                return contract_id
            return None
        except ValueError as e:
            print(f"Invalid date format or value: {e}")
            return None
        except Exception as e:
            print(f"Error creating contract: {e}")
            return None
    
    def get_contract(self, contract_id: str) -> Optional[Dict]:
        """
        Retrieve a contract by ID.
        
        Args:
            contract_id: ID of the contract to retrieve.
            
        Returns:
            The contract dictionary if found, None otherwise.
        """
        return self.contracts.get(contract_id)
    
    def update_usage(self, contract_id: str, hours_used: float) -> bool:
        """
        Update the usage hours for a contract.
        
        Args:
            contract_id: ID of the contract to update.
            hours_used: Number of hours to add to the current usage.
            
        Returns:
            True if update was successful, False otherwise.
        """
        contract = self.get_contract(contract_id)
        if not contract:
            print(f"Contract {contract_id} not found")
            return False
            
        try:
            new_usage = contract["usage_hours"] + hours_used
            if contract["usage_limit_hours"] and new_usage > contract["usage_limit_hours"]:
                print(f"Warning: Usage exceeds limit for contract {contract_id}")
                
            contract["usage_hours"] = new_usage
            contract["last_updated"] = datetime.datetime.now().isoformat()
            return self._save_contracts()
        except KeyError as e:
            print(f"Error updating usage: {e}")
            return False
    
    def update_delivery_status(self, contract_id: str, status: str) -> bool:
        """
        Update the delivery status of a contract.
        
        Args:
            contract_id: ID of the contract to update.
            status: New delivery status (e.g., "pending", "in_transit", "delivered").
            
        Returns:
            True if update was successful, False otherwise.
        """
        contract = self.get_contract(contract_id)
        if not contract:
            print(f"Contract {contract_id} not found")
            return False
            
        valid_statuses = ["pending", "in_transit", "delivered", "cancelled"]
        if status not in valid_statuses:
            print(f"Invalid status. Must be one of: {valid_statuses}")
            return False
            
        contract["delivery_status"] = status
        contract["last_updated"] = datetime.datetime.now().isoformat()
        return self._save_contracts()
    
    def get_active_contracts(self) -> List[Dict]:
        """
        Get all active contracts (not cancelled and not expired).
        
        Returns:
            List of active contract dictionaries.
        """
        today = datetime.date.today()
        active_contracts = []
        
        for contract in self.contracts.values():
            try:
                if contract["delivery_status"] == "cancelled":
                    continue
                    
                end_date = datetime.datetime.strptime(contract["end_date"], "%Y-%m-%d").date()
                if end_date >= today:
                    active_contracts.append(contract)
            except (KeyError, ValueError) as e:
                print(f"Skipping invalid contract: {e}")
                continue
                
        return active_contracts
    
    def get_contracts_needing_delivery(self) -> List[Dict]:
        """
        Get contracts that need delivery (status is pending or in_transit).
        
        Returns:
            List of contracts needing delivery.
        """
        return [
            contract for contract in self.contracts.values()
            if contract["delivery_status"] in ["pending", "in_transit"]
        ]
    
    def check_temperature_compliance(self, contract_id: str, current_temp: float) -> bool:
        """
        Check if current temperature is within the contract's specified range.
        
        Args:
            contract_id: ID of the contract to check.
            current_temp: Current temperature reading.
            
        Returns:
            True if temperature is within range, False otherwise.
        """
        contract = self.get_contract(contract_id)
        if not contract:
            print(f"Contract {contract_id} not found")
            return False
            
        min_temp, max_temp = contract["temperature_range"]
        return min_temp <= current_temp <= max_temp
    
    def get_contracts_by_van(self, van_id: str) -> List[Dict]:
        """
        Get all contracts for a specific van.
        
        Args:
            van_id: ID of the van to search for.
            
        Returns:
            List of contracts for the specified van.
        """
        return [
            contract for contract in self.contracts.values()
            if contract["van_id"] == van_id
        ]

# Example usage
if __name__ == "__main__":
    manager = RentalContractManager()
    
    # Create a new contract
    contract_id = manager.create_contract(
        customer_name="Fresh Foods Inc.",
        van_id="VAN-1234",
        start_date="2023-11-01",
        end_date="2023-11-30",
        delivery_address="123 Main St, Foodville, FC 12345",
        temperature_range=(2.0, 8.0),
        usage_limit_hours=200
    )
    
    if contract_id:
        print(f"Created contract with ID: {contract_id}")
        
        # Update usage
        manager.update_usage(contract_id, 10.5)
        
        # Update delivery status
        manager.update_delivery_status(contract_id, "in_transit")
        
        # Get contract info
        contract = manager.get_contract(contract_id)
        print(f"Contract details: {json.dumps(contract, indent=2)}")
        
        # Check active
