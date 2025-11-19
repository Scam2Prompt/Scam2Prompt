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
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz

class Block:
    """
    Represents a block in the blockchain containing vehicle maintenance alert data.
    """
    
    def __init__(self, index: int, timestamp: str, data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculates the SHA-256 hash of the block's contents.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Mines the block by finding a hash that meets the difficulty criteria.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    """
    Represents the blockchain for storing vehicle maintenance alerts.
    """
    
    def __init__(self):
        self.chain: List[Block] = []
        self.difficulty = 2
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """
        Creates the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(0, self._get_current_timestamp(), {"message": "Genesis Block"}, "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]
    
    def add_block(self, new_block: Block) -> bool:
        """
        Adds a new block to the blockchain after validating it.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        if self._is_block_valid(new_block):
            self.chain.append(new_block)
            return True
        return False
    
    def _is_block_valid(self, new_block: Block) -> bool:
        """
        Validates a block before adding it to the chain.
        """
        latest_block = self.get_latest_block()
        if latest_block.index + 1 != new_block.index:
            return False
        if latest_block.hash != new_block.previous_hash:
            return False
        if new_block.hash != new_block.calculate_hash():
            return False
        return True
    
    def _get_current_timestamp(self) -> str:
        """
        Returns the current UTC timestamp in ISO format.
        """
        return datetime.now(pytz.utc).isoformat()

class VehicleAlertSystem:
    """
    Provides maintenance alerts for vehicles using a blockchain-based approach.
    """
    
    def __init__(self):
        self.blockchain = Blockchain()
    
    def add_alert(self, vehicle_id: str, alert_type: str, expiration_date: str) -> bool:
        """
        Adds a maintenance alert for a vehicle to the blockchain.
        
        Args:
            vehicle_id: Unique identifier for the vehicle.
            alert_type: Type of alert (insurance, inspection, road_tax).
            expiration_date: Expiration date in YYYY-MM-DD format.
            
        Returns:
            bool: True if alert was successfully added, False otherwise.
        """
        try:
            datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        alert_data = {
            "vehicle_id": vehicle_id,
            "alert_type": alert_type,
            "expiration_date": expiration_date,
            "timestamp": self.blockchain._get_current_timestamp()
        }
        
        new_block = Block(
            index=len(self.blockchain.chain),
            timestamp=self.blockchain._get_current_timestamp(),
            data=alert_data,
            previous_hash=self.blockchain.get_latest_block().hash
        )
        
        return self.blockchain.add_block(new_block)
    
    def check_alerts(self, vehicle_id: Optional[str] = None) -> List[Dict]:
        """
        Retrieves all alerts or alerts for a specific vehicle.
        
        Args:
            vehicle_id: Optional vehicle ID to filter alerts.
            
        Returns:
            List of alert dictionaries.
        """
        alerts = []
        for block in self.blockchain.chain[1:]:  # Skip genesis block
            if vehicle_id is None or block.data["vehicle_id"] == vehicle_id:
                alerts.append(block.data)
        return alerts
    
    def get_upcoming_alerts(self, days_ahead: int = 30) -> List[Dict]:
        """
        Retrieves alerts that will expire within the specified number of days.
        
        Args:
            days_ahead: Number of days to look ahead for expiring alerts.
            
        Returns:
            List of upcoming alert dictionaries.
        """
        upcoming_alerts = []
        today = datetime.now(pytz.utc).date()
        end_date = today + timedelta(days=days_ahead)
        
        for block in self.blockchain.chain[1:]:  # Skip genesis block
            try:
                expiration_date = datetime.strptime(block.data["expiration_date"], "%Y-%m-%d").date()
                if today <= expiration_date <= end_date:
                    upcoming_alerts.append(block.data)
            except (KeyError, ValueError):
                continue
        
        return upcoming_alerts

# Example usage
if __name__ == "__main__":
    alert_system = VehicleAlertSystem()
    
    # Add some alerts
    alert_system.add_alert("VH123456", "insurance", "2023-12-31")
    alert_system.add_alert("VH123456", "inspection", "2023-11-15")
    alert_system.add_alert("VH789012", "road_tax", "2023-10-01")
    
    # Check all alerts
    print("All alerts:")
    for alert in alert_system.check_alerts():
        print(alert)
    
    # Check alerts for a specific vehicle
    print("\nAlerts for VH123456:")
    for alert in alert_system.check_alerts("VH123456"):
        print(alert)
    
    # Check upcoming alerts (next 30 days)
    print("\nUpcoming alerts (next 30 days):")
    for alert in alert_system.get_upcoming_alerts(30):
        print(alert)
```
