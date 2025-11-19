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
import hashlib
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Vehicle:
    def __init__(self, vin: str, owner: str):
        """
        Initialize a new vehicle with a VIN and owner.
        
        :param vin: Vehicle Identification Number
        :param owner: Owner of the vehicle
        """
        self.vin = vin
        self.owner = owner
        self.alerts = []

    def add_alert(self, alert: Dict[str, Any]):
        """
        Add an alert to the vehicle's alert list.
        
        :param alert: A dictionary containing alert details
        """
        self.alerts.append(alert)

    def get_alerts(self) -> List[Dict[str, Any]]:
        """
        Retrieve all alerts for the vehicle.
        
        :return: List of alerts
        """
        return self.alerts


class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block in the blockchain.
        
        :param proof: Proof of work
        :param previous_hash: Hash of the previous block
        :return: New block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, transaction: Dict[str, Any]) -> int:
        """
        Add a transaction to the list of transactions.
        
        :param transaction: A dictionary containing transaction details
        :return: The index of the block that will hold this transaction
        """
        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Return the last block in the chain.
        
        :return: Last block
        """
        return self.chain[-1]

    def hash(self, block: Dict[str, Any]) -> str:
        """
        Create a SHA-256 hash of a block.
        
        :param block: Block to hash
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class MaintenanceAlertSystem:
    def __init__(self):
        """
        Initialize the maintenance alert system with a blockchain and a vehicle registry.
        """
        self.blockchain = Blockchain()
        self.vehicles: Dict[str, Vehicle] = {}

    def register_vehicle(self, vin: str, owner: str):
        """
        Register a new vehicle in the system.
        
        :param vin: Vehicle Identification Number
        :param owner: Owner of the vehicle
        """
        if vin in self.vehicles:
            raise ValueError("Vehicle already registered.")
        self.vehicles[vin] = Vehicle(vin, owner)

    def add_alert(self, vin: str, alert_type: str, expiration_date: str):
        """
        Add a maintenance alert for a vehicle.
        
        :param vin: Vehicle Identification Number
        :param alert_type: Type of alert (insurance, inspection, road tax)
        :param expiration_date: Expiration date of the alert
        """
        if vin not in self.vehicles:
            raise ValueError("Vehicle not found.")
        
        alert = {
            'type': alert_type,
            'expiration_date': expiration_date,
            'created_at': str(datetime.now())
        }
        self.vehicles[vin].add_alert(alert)
        self.blockchain.add_transaction({
            'vin': vin,
            'alert': alert
        })

    def get_vehicle_alerts(self, vin: str) -> List[Dict[str, Any]]:
        """
        Retrieve alerts for a specific vehicle.
        
        :param vin: Vehicle Identification Number
        :return: List of alerts for the vehicle
        """
        if vin not in self.vehicles:
            raise ValueError("Vehicle not found.")
        return self.vehicles[vin].get_alerts()


# Example usage
if __name__ == "__main__":
    try:
        alert_system = MaintenanceAlertSystem()
        alert_system.register_vehicle("1HGCM82633A123456", "John Doe")
        alert_system.add_alert("1HGCM82633A123456", "insurance", (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'))
        alerts = alert_system.get_vehicle_alerts("1HGCM82633A123456")
        print(alerts)
    except Exception as e:
        print(f"Error: {e}")
```
