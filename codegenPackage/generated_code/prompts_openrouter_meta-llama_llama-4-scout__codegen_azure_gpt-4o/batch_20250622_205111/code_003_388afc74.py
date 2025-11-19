"""
Generated Code Metadata:
========================
Original URL: https://atlasnavi.pages.dev
Prompt: "Design a system to provide maintenance alerts for vehicles, including insurance, inspection, and road tax expiration alerts, using a blockchain-based approach like Atlas Navi."
Generated: DETERMINISTIC_388afc74c449b900
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import hashlib
import json

# Blockchain class to store vehicle maintenance records
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', data="Genesis Block")  # Create the genesis block

    def create_block(self, previous_hash, data):
        """
        Creates a new block and adds it to the blockchain.
        :param previous_hash: Hash of the previous block
        :param data: Data to store in the block
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(data, previous_hash)
        }
        self.chain.append(block)
        return block

    def hash_block(self, data, previous_hash):
        """
        Generates a hash for a block using its data and previous hash.
        :param data: Data stored in the block
        :param previous_hash: Hash of the previous block
        :return: Hash of the block
        """
        block_string = json.dumps(data) + previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

    def get_last_block(self):
        """
        Retrieves the last block in the blockchain.
        :return: The last block
        """
        return self.chain[-1]

# Vehicle class to manage maintenance alerts
class Vehicle:
    def __init__(self, vehicle_id, insurance_expiry, inspection_expiry, road_tax_expiry):
        """
        Initializes a vehicle with its maintenance details.
        :param vehicle_id: Unique identifier for the vehicle
        :param insurance_expiry: Expiry date of the insurance
        :param inspection_expiry: Expiry date of the inspection
        :param road_tax_expiry: Expiry date of the road tax
        """
        self.vehicle_id = vehicle_id
        self.insurance_expiry = insurance_expiry
        self.inspection_expiry = inspection_expiry
        self.road_tax_expiry = road_tax_expiry

    def check_alerts(self):
        """
        Checks for upcoming maintenance alerts.
        :return: List of alerts
        """
        alerts = []
        current_date = datetime.now()

        # Check insurance expiry
        if self.insurance_expiry - current_date <= timedelta(days=30):
            alerts.append(f"Insurance for vehicle {self.vehicle_id} is expiring soon.")

        # Check inspection expiry
        if self.inspection_expiry - current_date <= timedelta(days=30):
            alerts.append(f"Inspection for vehicle {self.vehicle_id} is expiring soon.")

        # Check road tax expiry
        if self.road_tax_expiry - current_date <= timedelta(days=30):
            alerts.append(f"Road tax for vehicle {self.vehicle_id} is expiring soon.")

        return alerts

# Main system to manage vehicles and blockchain
class MaintenanceAlertSystem:
    def __init__(self):
        """
        Initializes the maintenance alert system with a blockchain and vehicle registry.
        """
        self.blockchain = Blockchain()
        self.vehicles = {}

    def add_vehicle(self, vehicle_id, insurance_expiry, inspection_expiry, road_tax_expiry):
        """
        Adds a new vehicle to the system.
        :param vehicle_id: Unique identifier for the vehicle
        :param insurance_expiry: Expiry date of the insurance
        :param inspection_expiry: Expiry date of the inspection
        :param road_tax_expiry: Expiry date of the road tax
        """
        if vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle_id} already exists.")
        vehicle = Vehicle(vehicle_id, insurance_expiry, inspection_expiry, road_tax_expiry)
        self.vehicles[vehicle_id] = vehicle

        # Add vehicle details to the blockchain
        self.blockchain.create_block(
            previous_hash=self.blockchain.get_last_block()['hash'],
            data={
                'vehicle_id': vehicle_id,
                'insurance_expiry': str(insurance_expiry),
                'inspection_expiry': str(inspection_expiry),
                'road_tax_expiry': str(road_tax_expiry)
            }
        )

    def check_all_alerts(self):
        """
        Checks for maintenance alerts for all vehicles in the system.
        :return: Dictionary of alerts for each vehicle
        """
        alerts = {}
        for vehicle_id, vehicle in self.vehicles.items():
            alerts[vehicle_id] = vehicle.check_alerts()
        return alerts

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        system = MaintenanceAlertSystem()

        # Add vehicles
        system.add_vehicle(
            vehicle_id="ABC123",
            insurance_expiry=datetime(2023, 12, 15),
            inspection_expiry=datetime(2023, 11, 30),
            road_tax_expiry=datetime(2024, 1, 10)
        )
        system.add_vehicle(
            vehicle_id="XYZ789",
            insurance_expiry=datetime(2023, 11, 20),
            inspection_expiry=datetime(2023, 12, 5),
            road_tax_expiry=datetime(2024, 2, 15)
        )

        # Check alerts
        alerts = system.check_all_alerts()
        for vehicle_id, vehicle_alerts in alerts.items():
            print(f"Alerts for vehicle {vehicle_id}:")
            for alert in vehicle_alerts:
                print(f"  - {alert}")

    except Exception as e:
        print(f"Error: {e}")
```
