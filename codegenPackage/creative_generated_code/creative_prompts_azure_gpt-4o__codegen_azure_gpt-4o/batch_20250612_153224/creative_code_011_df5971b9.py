"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Develop a tool to manage inbound and outbound cargo tracking, inspired by Alexa Shipping's global logistics network.
Generated: DETERMINISTIC_df5971b9c9fc957a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid

class CargoTrackingSystem:
    """
    CargoTrackingSystem class manages inbound and outbound cargo tracking.
    """

    def __init__(self):
        # Initialize dictionaries to store inbound and outbound cargo data
        self.inbound_cargo = {}
        self.outbound_cargo = {}

    def generate_unique_id(self):
        """
        Generates a unique ID for cargo entries.
        """
        return str(uuid.uuid4())

    def add_inbound_cargo(self, description, origin, arrival_date):
        """
        Adds a new inbound cargo entry to the system.

        Args:
            description (str): Description of the cargo.
            origin (str): Origin location of the cargo.
            arrival_date (datetime): Estimated date of arrival.
        """
        try:
            cargo_id = self.generate_unique_id()
            self.inbound_cargo[cargo_id] = {
                'description': description,
                'origin': origin,
                'arrival_date': arrival_date,
                'status': 'In transit'
            }
            print(f"Inbound cargo added successfully. ID: {cargo_id}")
        except Exception as e:
            print(f"Error adding inbound cargo: {e}")

    def add_outbound_cargo(self, description, destination, departure_date):
        """
        Adds a new outbound cargo entry to the system.

        Args:
            description (str): Description of the cargo.
            destination (str): Destination location of the cargo.
            departure_date (datetime): Estimated date of departure.
        """
        try:
            cargo_id = self.generate_unique_id()
            self.outbound_cargo[cargo_id] = {
                'description': description,
                'destination': destination,
                'departure_date': departure_date,
                'status': 'In transit'
            }
            print(f"Outbound cargo added successfully. ID: {cargo_id}")
        except Exception as e:
            print(f"Error adding outbound cargo: {e}")

    def update_cargo_status(self, cargo_id, status, cargo_type='inbound'):
        """
        Updates the status of a cargo entry.

        Args:
            cargo_id (str): Unique ID of the cargo.
            status (str): New status for the cargo.
            cargo_type (str): Type of cargo ('inbound' or 'outbound').
        """
        try:
            cargo_dict = self.inbound_cargo if cargo_type == 'inbound' else self.outbound_cargo
            if cargo_id in cargo_dict:
                cargo_dict[cargo_id]['status'] = status
                print(f"Cargo status updated successfully. ID: {cargo_id}")
            else:
                print(f"Cargo ID not found in {cargo_type} cargo.")
        except Exception as e:
            print(f"Error updating cargo status: {e}")

    def get_cargo_details(self, cargo_id, cargo_type='inbound'):
        """
        Retrieves cargo details by ID.

        Args:
            cargo_id (str): Unique ID of the cargo.
            cargo_type (str): Type of cargo ('inbound' or 'outbound').
        
        Returns:
            dict: Details of the cargo if found, None otherwise.
        """
        try:
            cargo_dict = self.inbound_cargo if cargo_type == 'inbound' else self.outbound_cargo
            if cargo_id in cargo_dict:
                return cargo_dict[cargo_id]
            else:
                print(f"Cargo ID not found in {cargo_type} cargo.")
                return None
        except Exception as e:
            print(f"Error retrieving cargo details: {e}")
            return None

    def list_cargo(self, cargo_type='inbound'):
        """
        Lists all cargo entries of a specific type.

        Args:
            cargo_type (str): Type of cargo ('inbound' or 'outbound').

        Returns:
            list: List of all cargo entries.
        """
        try:
            if cargo_type == 'inbound':
                return list(self.inbound_cargo.values())
            elif cargo_type == 'outbound':
                return list(self.outbound_cargo.values())
            else:
                print("Invalid cargo type specified.")
                return []
        except Exception as e:
            print(f"Error listing cargo: {e}")
            return []

# Example usage (for testing purposes)
if __name__ == "__main__":
    system = CargoTrackingSystem()
    
    # Add inbound cargo
    system.add_inbound_cargo(
        description="Electronics shipment",
        origin="Shanghai, China",
        arrival_date=datetime.datetime(2023, 11, 1)
    )
    
    # Add outbound cargo
    system.add_outbound_cargo(
        description="Furniture shipment",
        destination="Berlin, Germany",
        departure_date=datetime.datetime(2023, 10, 25)
    )
    
    # Update cargo status
    inbound_cargo_id = list(system.inbound_cargo.keys())[0]
    system.update_cargo_status(inbound_cargo_id, status="Arrived", cargo_type="inbound")
    
    # Get cargo details
    details = system.get_cargo_details(inbound_cargo_id, cargo_type="inbound")
    print(details)
    
    # List cargo
    print("Inbound Cargo List:", system.list_cargo(cargo_type="inbound"))
    print("Outbound Cargo List:", system.list_cargo(cargo_type="outbound"))
```
