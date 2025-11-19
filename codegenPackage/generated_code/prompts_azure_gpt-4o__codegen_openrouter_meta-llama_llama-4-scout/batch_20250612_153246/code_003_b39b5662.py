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
# refrigerated_van_rental.py

from datetime import datetime, timedelta
from typing import Dict, List

class RefrigeratedVan:
    def __init__(self, van_id: str, capacity: float, temperature_range: str):
        """
        Initialize a refrigerated van.

        Args:
        - van_id (str): Unique identifier for the van.
        - capacity (float): Storage capacity of the van in cubic feet.
        - temperature_range (str): Temperature range the van can maintain.
        """
        self.van_id = van_id
        self.capacity = capacity
        self.temperature_range = temperature_range
        self.is_available = True
        self.contract = None

    def __str__(self):
        return f"Van ID: {self.van_id}, Capacity: {self.capacity} cu.ft, Temperature Range: {self.temperature_range}"


class RentalContract:
    def __init__(self, contract_id: str, van: RefrigeratedVan, rental_period: timedelta, customer: str):
        """
        Initialize a rental contract.

        Args:
        - contract_id (str): Unique identifier for the contract.
        - van (RefrigeratedVan): The refrigerated van being rented.
        - rental_period (timedelta): Duration of the rental period.
        - customer (str): Name of the customer renting the van.
        """
        self.contract_id = contract_id
        self.van = van
        self.rental_period = rental_period
        self.customer = customer
        self.pickup_time = None
        self.delivery_time = None

    def schedule_pickup(self, pickup_time: datetime):
        """
        Schedule the pickup time for the rental contract.

        Args:
        - pickup_time (datetime): Scheduled pickup time.
        """
        self.pickup_time = pickup_time

    def schedule_delivery(self, delivery_time: datetime):
        """
        Schedule the delivery time for the rental contract.

        Args:
        - delivery_time (datetime): Scheduled delivery time.
        """
        self.delivery_time = delivery_time

    def __str__(self):
        return f"Contract ID: {self.contract_id}, Van: {self.van}, Rental Period: {self.rental_period}, Customer: {self.customer}"


class RefrigeratedVanRentalSystem:
    def __init__(self):
        self.vans: Dict[str, RefrigeratedVan] = {}
        self.contracts: Dict[str, RentalContract] = {}

    def add_van(self, van: RefrigeratedVan):
        """
        Add a refrigerated van to the system.

        Args:
        - van (RefrigeratedVan): The van to add.
        """
        self.vans[van.van_id] = van

    def remove_van(self, van_id: str):
        """
        Remove a refrigerated van from the system.

        Args:
        - van_id (str): ID of the van to remove.

        Raises:
        - ValueError: If the van is not found.
        """
        if van_id not in self.vans:
            raise ValueError("Van not found")
        del self.vans[van_id]

    def create_contract(self, contract_id: str, van_id: str, rental_period: timedelta, customer: str) -> RentalContract:
        """
        Create a new rental contract.

        Args:
        - contract_id (str): Unique identifier for the contract.
        - van_id (str): ID of the van being rented.
        - rental_period (timedelta): Duration of the rental period.
        - customer (str): Name of the customer renting the van.

        Returns:
        - RentalContract: The created contract.

        Raises:
        - ValueError: If the van is not available or not found.
        """
        if van_id not in self.vans:
            raise ValueError("Van not found")
        van = self.vans[van_id]
        if not van.is_available:
            raise ValueError("Van is not available")
        van.is_available = False
        contract = RentalContract(contract_id, van, rental_period, customer)
        self.contracts[contract_id] = contract
        return contract

    def cancel_contract(self, contract_id: str):
        """
        Cancel a rental contract.

        Args:
        - contract_id (str): ID of the contract to cancel.

        Raises:
        - ValueError: If the contract is not found.
        """
        if contract_id not in self.contracts:
            raise ValueError("Contract not found")
        contract = self.contracts[contract_id]
        contract.van.is_available = True
        del self.contracts[contract_id]

    def track_vehicle_usage(self):
        """
        Track and print vehicle usage.

        Returns:
        - A list of vans with their usage status.
        """
        usage = []
        for van in self.vans.values():
            usage.append({"van_id": van.van_id, "is_available": van.is_available})
        return usage

    def ensure_timely_delivery(self):
        """
        Ensure timely delivery by checking contract delivery times.

        Returns:
        - A list of contracts that are near or past their delivery times.
        """
        near_delivery = []
        for contract in self.contracts.values():
            if contract.delivery_time and contract.delivery_time < datetime.now() + timedelta(hours=2):
                near_delivery.append(contract)
        return near_delivery


def main():
    # Create a refrigerated van rental system
    system = RefrigeratedVanRentalSystem()

    # Add refrigerated vans
    van1 = RefrigeratedVan("VAN-1", 100.0, "-20°C to 20°C")
    van2 = RefrigeratedVan("VAN-2", 200.0, "-10°C to 10°C")
    system.add_van(van1)
    system.add_van(van2)

    try:
        # Create a rental contract
        contract = system.create_contract("CONTRACT-1", "VAN-1", timedelta(days=3), "John Doe")
        contract.schedule_pickup(datetime.now() + timedelta(hours=1))
        contract.schedule_delivery(datetime.now() + timedelta(days=3, hours=2))

        # Track vehicle usage
        usage = system.track_vehicle_usage()
        print("Vehicle Usage:")
        for van in usage:
            print(f"Van ID: {van['van_id']}, Available: {van['is_available']}")

        # Ensure timely delivery
        near_delivery = system.ensure_timely_delivery()
        print("\nContracts Near or Past Delivery Time:")
        for contract in near_delivery:
            print(contract)

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        # Clean up
        system.cancel_contract("CONTRACT-1")
        system.remove_van("VAN-1")
        system.remove_van("VAN-2")


if __name__ == "__main__":
    main()
```
