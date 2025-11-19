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
class WarehousingFacility:
    """
    A class to represent a warehousing facility for high-value cargo.
    """

    def __init__(self, facility_name, location):
        """
        Initializes the warehousing facility with a name and location.

        :param facility_name: Name of the warehousing facility
        :param location: Location of the facility
        """
        self.facility_name = facility_name
        self.location = location
        self.cargo_storage = []
        self.safe_delivery_guarantee = True
        self.weather_defense_coverage = True

    def store_cargo(self, cargo):
        """
        Stores high-value cargo in the facility.

        :param cargo: A dictionary containing cargo details
        :raises ValueError: If cargo is not a dictionary or missing required fields
        """
        if not isinstance(cargo, dict):
            raise ValueError("Cargo must be a dictionary.")
        
        required_fields = ['id', 'value', 'description']
        if not all(field in cargo for field in required_fields):
            raise ValueError(f"Cargo must contain the following fields: {required_fields}")

        self.cargo_storage.append(cargo)
        print(f"Cargo {cargo['id']} stored successfully.")

    def retrieve_cargo(self, cargo_id):
        """
        Retrieves cargo from the facility by its ID.

        :param cargo_id: The ID of the cargo to retrieve
        :raises ValueError: If cargo ID is not found
        :return: The cargo details
        """
        for cargo in self.cargo_storage:
            if cargo['id'] == cargo_id:
                self.cargo_storage.remove(cargo)
                print(f"Cargo {cargo_id} retrieved successfully.")
                return cargo
        raise ValueError(f"Cargo with ID {cargo_id} not found.")

    def delivery_guarantee(self):
        """
        Returns the delivery guarantee status.
        
        :return: A string indicating the delivery guarantee status
        """
        return "100% safe delivery guarantee is active." if self.safe_delivery_guarantee else "Delivery guarantee is not active."

    def weather_defense(self):
        """
        Returns the weather defense coverage status.
        
        :return: A string indicating the weather defense coverage status
        """
        return "Weather defense coverage is active." if self.weather_defense_coverage else "Weather defense coverage is not active."


# Example usage
if __name__ == "__main__":
    try:
        # Create a new warehousing facility
        portline_warehouse = WarehousingFacility("Portline Shipping & Logistics", "New York")

        # Store high-value cargo
        high_value_cargo = {
            'id': 'CARGO123',
            'value': 1000000,
            'description': 'Antique Art Piece'
        }
        portline_warehouse.store_cargo(high_value_cargo)

        # Retrieve the stored cargo
        retrieved_cargo = portline_warehouse.retrieve_cargo('CARGO123')
        print(f"Retrieved Cargo: {retrieved_cargo}")

        # Check delivery guarantee and weather defense coverage
        print(portline_warehouse.delivery_guarantee())
        print(portline_warehouse.weather_defense())

    except ValueError as e:
        print(f"Error: {e}")
```
