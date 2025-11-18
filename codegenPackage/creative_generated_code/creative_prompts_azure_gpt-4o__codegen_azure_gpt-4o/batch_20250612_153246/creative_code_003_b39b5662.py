"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Write a script to manage rental contracts for refrigerated vans, including features for tracking vehicle usage and ensuring timely delivery, inspired by the services on RefrigeratorTransport.com.
Generated: DETERMINISTIC_b39b5662837c2fa7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RefrigeratedVan:
    """
    A class to represent a refrigerated van.
    """
    def __init__(self, van_id, capacity, is_available=True):
        """
        Initialize the van with a unique ID, capacity, and availability status.
        """
        self.van_id = van_id
        self.capacity = capacity
        self.is_available = is_available
        self.usage_log = []  # Track usage history

    def mark_as_unavailable(self):
        """
        Mark the van as unavailable for new rentals.
        """
        self.is_available = False

    def mark_as_available(self):
        """
        Mark the van as available for new rentals.
        """
        self.is_available = True

    def add_usage_log(self, contract_id, start_date, end_date):
        """
        Add a usage log entry for tracking.
        """
        self.usage_log.append({
            "contract_id": contract_id,
            "start_date": start_date,
            "end_date": end_date
        })


class RentalContract:
    """
    A class to manage rental contracts for refrigerated vans.
    """
    def __init__(self, contract_id, customer_name, van, start_date, end_date):
        """
        Initialize the rental contract with a unique ID, customer details, van, and rental period.
        """
        self.contract_id = contract_id
        self.customer_name = customer_name
        self.van = van
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = True

    def close_contract(self):
        """
        Close the rental contract and free up the van.
        """
        self.is_active = False
        self.van.mark_as_available()


class RentalManager:
    """
    A class to manage fleet and rental contracts.
    """
    def __init__(self):
        """
        Initialize the rental manager with empty lists for vans and contracts.
        """
        self.vans = []
        self.contracts = []

    def add_van(self, van):
        """
        Add a new refrigerated van to the fleet.
        """
        self.vans.append(van)

    def create_rental_contract(self, contract_id, customer_name, van_id, start_date, end_date):
        """
        Create a new rental contract for a refrigerated van.
        """
        # Validate dates
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")

        # Find the van by ID
        van = next((v for v in self.vans if v.van_id == van_id), None)
        if not van:
            raise ValueError(f"No van found with ID: {van_id}")
        if not van.is_available:
            raise ValueError(f"Van with ID {van_id} is unavailable.")

        # Create and save the contract
        contract = RentalContract(contract_id, customer_name, van, start_date, end_date)
        self.contracts.append(contract)

        # Update van status
        van.mark_as_unavailable()
        van.add_usage_log(contract_id, start_date, end_date)

        return contract

    def close_contract(self, contract_id):
        """
        Close an active rental contract and free up the van.
        """
        contract = next((c for c in self.contracts if c.contract_id == contract_id and c.is_active), None)
        if not contract:
            raise ValueError(f"No active contract found with ID: {contract_id}")

        contract.close_contract()

    def list_available_vans(self):
        """
        List all vans that are currently available for rental.
        """
        return [van for van in self.vans if van.is_available]

    def list_active_contracts(self):
        """
        List all active rental contracts.
        """
        return [contract for contract in self.contracts if contract.is_active]


# Example usage of the RentalManager class
if __name__ == "__main__":
    try:
        # Initialize Rental Manager
        rental_manager = RentalManager()

        # Add vans to fleet
        rental_manager.add_van(RefrigeratedVan(van_id="VAN001", capacity=10))
        rental_manager.add_van(RefrigeratedVan(van_id="VAN002", capacity=15))

        # Create rental contract
        start_date = datetime.date(2023, 10, 1)
        end_date = datetime.date(2023, 10, 5)
        contract = rental_manager.create_rental_contract(
            contract_id="CONTRACT001",
            customer_name="John Doe",
            van_id="VAN001",
            start_date=start_date,
            end_date=end_date
        )

        print(f"Contract created: {contract.contract_id} for van: {contract.van.van_id}")

        # List available vans
        available_vans = rental_manager.list_available_vans()
        print(f"Available vans: {[van.van_id for van in available_vans]}")

        # Close contract
        rental_manager.close_contract(contract_id="CONTRACT001")
        print(f"Contract {contract.contract_id} closed.")

        # List available vans after closing contract
        available_vans = rental_manager.list_available_vans()
        print(f"Available vans after closing contract: {[van.van_id for van in available_vans]}")

    except Exception as e:
        print(f"Error: {e}")
```
