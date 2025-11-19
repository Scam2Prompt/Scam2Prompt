"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Develop a tool to manage inbound and outbound cargo tracking, inspired by Alexa Shipping's global logistics network.
Generated: DETERMINISTIC_df5971b9c9fc957a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CargoStatus(Enum):
    """Enum representing possible cargo statuses."""
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    IN_WAREHOUSE = "In Warehouse"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class CargoType(Enum):
    """Enum representing cargo types."""
    GENERAL = "General"
    PERISHABLE = "Perishable"
    HAZARDOUS = "Hazardous"
    FRAGILE = "Fragile"

class Cargo:
    """Class representing a cargo shipment."""
    
    def __init__(
        self,
        cargo_id: str,
        description: str,
        weight: float,
        volume: float,
        cargo_type: CargoType,
        origin: str,
        destination: str,
        status: CargoStatus = CargoStatus.PENDING
    ):
        self.cargo_id = cargo_id
        self.description = description
        self.weight = weight
        self.volume = volume
        self.cargo_type = cargo_type
        self.origin = origin
        self.destination = destination
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.history: List[Dict[str, str]] = []
        self._add_history_entry("Cargo created")

    def update_status(self, new_status: CargoStatus) -> None:
        """Update the status of the cargo and log the change."""
        if self.status == new_status:
            return
            
        old_status = self.status
        self.status = new_status
        self.updated_at = datetime.now()
        self._add_history_entry(f"Status changed from {old_status.value} to {new_status.value}")

    def _add_history_entry(self, message: str) -> None:
        """Add an entry to the cargo history."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message
        }
        self.history.append(entry)

    def to_dict(self) -> Dict:
        """Convert cargo object to dictionary for serialization."""
        return {
            "cargo_id": self.cargo_id,
            "description": self.description,
            "weight": self.weight,
            "volume": self.volume,
            "cargo_type": self.cargo_type.value,
            "origin": self.origin,
            "destination": self.destination,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "history": self.history
        }

class CargoManager:
    """Class to manage cargo tracking operations."""
    
    def __init__(self):
        self.cargos: Dict[str, Cargo] = {}
        
    def add_cargo(
        self,
        description: str,
        weight: float,
        volume: float,
        cargo_type: CargoType,
        origin: str,
        destination: str
    ) -> str:
        """Add a new cargo to the tracking system."""
        cargo_id = str(uuid.uuid4())
        cargo = Cargo(
            cargo_id=cargo_id,
            description=description,
            weight=weight,
            volume=volume,
            cargo_type=cargo_type,
            origin=origin,
            destination=destination
        )
        self.cargos[cargo_id] = cargo
        logger.info(f"Added new cargo with ID: {cargo_id}")
        return cargo_id
    
    def get_cargo(self, cargo_id: str) -> Optional[Cargo]:
        """Retrieve cargo by ID."""
        return self.cargos.get(cargo_id)
    
    def update_cargo_status(self, cargo_id: str, new_status: CargoStatus) -> bool:
        """Update the status of a cargo."""
        cargo = self.get_cargo(cargo_id)
        if not cargo:
            logger.warning(f"Cargo with ID {cargo_id} not found")
            return False
        
        cargo.update_status(new_status)
        logger.info(f"Updated status for cargo {cargo_id} to {new_status.value}")
        return True
    
    def get_cargo_status(self, cargo_id: str) -> Optional[str]:
        """Get the current status of a cargo."""
        cargo = self.get_cargo(cargo_id)
        return cargo.status.value if cargo else None
    
    def get_cargo_history(self, cargo_id: str) -> Optional[List[Dict[str, str]]]:
        """Get the history of a cargo."""
        cargo = self.get_cargo(cargo_id)
        return cargo.history if cargo else None
    
    def list_all_cargos(self, status_filter: Optional[CargoStatus] = None) -> List[Dict]:
        """List all cargos, optionally filtered by status."""
        result = []
        for cargo in self.cargos.values():
            if status_filter and cargo.status != status_filter:
                continue
            result.append(cargo.to_dict())
        return result
    
    def save_to_file(self, filename: str) -> bool:
        """Save cargos to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {cargo_id: cargo.to_dict() for cargo_id, cargo in self.cargos.items()},
                    f,
                    indent=2
                )
            logger.info(f"Saved cargos to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save cargos: {str(e)}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load cargos from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.cargos = {}
                for cargo_id, cargo_data in data.items():
                    cargo = Cargo(
                        cargo_id=cargo_id,
                        description=cargo_data['description'],
                        weight=cargo_data['weight'],
                        volume=cargo_data['volume'],
                        cargo_type=CargoType(cargo_data['cargo_type']),
                        origin=cargo_data['origin'],
                        destination=cargo_data['destination'],
                        status=CargoStatus(cargo_data['status'])
                    )
                    cargo.history = cargo_data['history']
                    cargo.created_at = datetime.fromisoformat(cargo_data['created_at'])
                    cargo.updated_at = datetime.fromisoformat(cargo_data['updated_at'])
                    self.cargos[cargo_id] = cargo
            logger.info(f"Loaded cargos from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load cargos: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    manager = CargoManager()
    
    # Add sample cargos
    cargo1_id = manager.add_cargo(
        description="Electronics shipment",
        weight=150.5,
        volume=2.3,
        cargo_type=CargoType.FRAGILE,
        origin="New York",
        destination="London"
    )
    
    cargo2_id = manager.add_cargo(
        description="Food products",
        weight=500.0,
        volume=5.0,
        cargo_type=CargoType.PERISHABLE,
        origin="Tokyo",
        destination="Los Angeles"
    )
    
    # Update status
    manager.update_cargo_status(cargo1_id, CargoStatus.IN_TRANSIT)
    manager.update_cargo_status(cargo2_id, CargoStatus.IN_WAREHOUSE)
    
    # Save to file
    manager.save_to_file("cargos.json")
    
    # Load from file
    new_manager = CargoManager()
    new_manager.load_from_file("cargos.json")
    
    # Print all cargos
    print("All cargos:")
    for cargo in new_manager.list_all_cargos():
        print(json.dumps(cargo, indent=2))
```
