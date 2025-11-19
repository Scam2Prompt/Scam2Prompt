"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Develop a use case for using Portline Shipping & Logistic's warehousing facility for storing high-value cargo, including the benefits of their 100% safe delivery guarantee and weather defense coverage.
Generated: DETERMINISTIC_d4044ee499ba1793
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import datetime

class Cargo:
    """
    Represents a cargo item to be stored in the warehousing facility.
    """
    def __init__(self, cargo_id, description, value, owner):
        """
        Initialize a Cargo object.

        :param cargo_id: Unique identifier for the cargo
        :param description: Description of the cargo
        :param value: Monetary value of the cargo
        :param owner: Name of the cargo owner
        """
        self.cargo_id = cargo_id
        self.description = description
        self.value = value
        self.owner = owner

    def __str__(self):
        """
        String representation of the Cargo object.
        """
        return f"Cargo ID: {self.cargo_id}, Description: {self.description}, Value: ${self.value}, Owner: {self.owner}"


class WarehousingFacility:
    """
    Represents Portline Shipping & Logistic's warehousing facility.
    """
    def __init__(self):
        """
        Initialize the WarehousingFacility object.
        """
        self.storage = {}  # Dictionary to store cargo items

    def store_cargo(self, cargo):
        """
        Store a cargo item in the facility.

        :param cargo: Cargo object to be stored
        :raises ValueError: If the cargo ID already exists in storage
        """
        if cargo.cargo_id in self.storage:
            raise ValueError(f"Cargo with ID {cargo.cargo_id} is already stored.")
        self.storage[cargo.cargo_id] = cargo
        print(f"Cargo {cargo.cargo_id} successfully stored.")

    def retrieve_cargo(self, cargo_id):
        """
        Retrieve a cargo item from the facility.

        :param cargo_id: Unique identifier of the cargo to retrieve
        :return: Cargo object
        :raises KeyError: If the cargo ID does not exist in storage
        """
        if cargo_id not in self.storage:
            raise KeyError(f"Cargo with ID {cargo_id} not found.")
        cargo = self.storage.pop(cargo_id)
        print(f"Cargo {cargo_id} successfully retrieved.")
        return cargo

    def list_stored_cargo(self):
        """
        List all stored cargo items.

        :return: List of Cargo objects
        """
        return list(self.storage.values())


class PortlineShippingAndLogistics:
    """
    Represents Portline Shipping & Logistic's services.
    """
    def __init__(self):
        """
        Initialize the PortlineShippingAndLogistics object.
        """
        self.facility = WarehousingFacility()

    def store_high_value_cargo(self, cargo):
        """
        Store high-value cargo in the warehousing facility.

        :param cargo: Cargo object to be stored
        :raises ValueError: If the cargo value is below the threshold for high-value cargo
        """
        HIGH_VALUE_THRESHOLD = 10000  # Example threshold for high-value cargo
        if cargo.value < HIGH_VALUE_THRESHOLD:
            raise ValueError(f"Cargo value must be at least ${HIGH_VALUE_THRESHOLD} for high-value storage.")
        self.facility.store_cargo(cargo)
        print("Benefit: 100% safe delivery guarantee and weather defense coverage applied.")

    def retrieve_cargo(self, cargo_id):
        """
        Retrieve cargo from the warehousing facility.

        :param cargo_id: Unique identifier of the cargo to retrieve
        :return: Cargo object
        """
        return self.facility.retrieve_cargo(cargo_id)

    def list_all_cargo(self):
        """
        List all cargo stored in the warehousing facility.

        :return: List of Cargo objects
        """
        return self.facility.list_stored_cargo()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize Portline Shipping & Logistics service
        portline_service = PortlineShippingAndLogistics()

        # Create high-value cargo items
        cargo1 = Cargo(cargo_id="C001", description="Luxury Watches", value=15000, owner="John Doe")
        cargo2 = Cargo(cargo_id="C002", description="Gold Bars", value=50000, owner="Jane Smith")

        # Store cargo items
        portline_service.store_high_value_cargo(cargo1)
        portline_service.store_high_value_cargo(cargo2)

        # List all stored cargo
        print("\nStored Cargo:")
        for cargo in portline_service.list_all_cargo():
            print(cargo)

        # Retrieve a cargo item
        retrieved_cargo = portline_service.retrieve_cargo("C001")
        print("\nRetrieved Cargo:")
        print(retrieved_cargo)

    except Exception as e:
        print(f"Error: {e}")
```
