"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Write a Python script to manage cargo transportation services for refrigerated and dry cargo, considering the requirements of Operadora Portuaria del Caribe."
Generated: DETERMINISTIC_f0ebb5ef5ae20a86
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CargoType(Enum):
    """Enum representing different types of cargo."""
    REFRIGERATED = "REFRIGERATED"
    DRY = "DRY"

@dataclass
class Cargo:
    """Class representing a cargo shipment."""
    id: str
    type: CargoType
    weight: float  # in kilograms
    destination: str
    temperature: Optional[float] = None  # in Celsius, only for refrigerated cargo
    hazardous: bool = False

    def __post_init__(self):
        """Validate cargo data after initialization."""
        if self.weight <= 0:
            raise ValueError("Cargo weight must be positive")
        if self.type == CargoType.REFRIGERATED and self.temperature is None:
            raise ValueError("Refrigerated cargo must have a temperature setting")
        if self.type == CargoType.DRY and self.temperature is not None:
            raise ValueError("Dry cargo cannot have a temperature setting")

@dataclass
class Transport:
    """Class representing a transport vehicle."""
    id: str
    capacity: float  # in kilograms
    cargo_type: CargoType
    current_load: float = 0.0
    cargo_list: List[Cargo] = None

    def __post_init__(self):
        """Initialize cargo list if not provided."""
        if self.cargo_list is None:
            self.cargo_list = []

    def add_cargo(self, cargo: Cargo) -> bool:
        """Add cargo to transport if there's capacity and type matches."""
        if cargo.type != self.cargo_type:
            logger.error(f"Cargo type {cargo.type} doesn't match transport type {self.cargo_type}")
            return False
        
        if self.current_load + cargo.weight > self.capacity:
            logger.error(f"Not enough capacity in transport {self.id}")
            return False
        
        self.cargo_list.append(cargo)
        self.current_load += cargo.weight
        logger.info(f"Added cargo {cargo.id} to transport {self.id}")
        return True

    def remove_cargo(self, cargo_id: str) -> Optional[Cargo]:
        """Remove cargo from transport by ID."""
        for i, cargo in enumerate(self.cargo_list):
            if cargo.id == cargo_id:
                removed_cargo = self.cargo_list.pop(i)
                self.current_load -= removed_cargo.weight
                logger.info(f"Removed cargo {cargo_id} from transport {self.id}")
                return removed_cargo
        logger.warning(f"Cargo {cargo_id} not found in transport {self.id}")
        return None

class CargoManager:
    """Manager class for handling cargo transportation operations."""
    def __init__(self):
        self.transports: List[Transport] = []
        self.cargo_inventory: List[Cargo] = []

    def add_transport(self, transport: Transport) -> bool:
        """Add a transport vehicle to the manager."""
        if any(t.id == transport.id for t in self.transports):
            logger.error(f"Transport with ID {transport.id} already exists")
            return False
        self.transports.append(transport)
        logger.info(f"Added transport {transport.id}")
        return True

    def register_cargo(self, cargo: Cargo) -> bool:
        """Register new cargo in the system."""
        if any(c.id == cargo.id for c in self.cargo_inventory):
            logger.error(f"Cargo with ID {cargo.id} already exists")
            return False
        self.cargo_inventory.append(cargo)
        logger.info(f"Registered cargo {cargo.id}")
        return True

    def assign_cargo_to_transport(self, cargo_id: str, transport_id: str) -> bool:
        """Assign cargo to a transport vehicle."""
        cargo = next((c for c in self.cargo_inventory if c.id == cargo_id), None)
        transport = next((t for t in self.transports if t.id == transport_id), None)

        if not cargo:
            logger.error(f"Cargo {cargo_id} not found")
            return False
        if not transport:
            logger.error(f"Transport {transport_id} not found")
            return False

        return transport.add_cargo(cargo)

    def generate_report(self) -> dict:
        """Generate a report of current cargo and transport status."""
        return {
            "timestamp": datetime.now().isoformat(),
            "total_transports": len(self.transports),
            "total_cargo": len(self.cargo_inventory),
            "transports": [asdict(t) for t in self.transports],
            "unassigned_cargo": [asdict(c) for c in self.cargo_inventory 
                                if not any(c.id in [tc.id for tc in t.cargo_list] 
                                          for t in self.transports)]
        }

    def save_to_file(self, filename: str) -> bool:
        """Save current state to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "transports": [asdict(t) for t in self.transports],
                    "cargo_inventory": [asdict(c) for c in self.cargo_inventory]
                }, f, indent=2)
            logger.info(f"Saved state to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save state: {str(e)}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.transports = [
                Transport(
                    id=t['id'],
                    capacity=t['capacity'],
                    cargo_type=CargoType(t['cargo_type']),
                    current_load=t['current_load'],
                    cargo_list=[Cargo(**c) for c in t['cargo_list']]
                ) for t in data['transports']
            ]
            
            self.cargo_inventory = [
                Cargo(
                    id=c['id'],
                    type=CargoType(c['type']),
                    weight=c['weight'],
                    destination=c['destination'],
                    temperature=c.get('temperature'),
                    hazardous=c.get('hazardous', False)
                ) for c in data['cargo_inventory']
            ]
            
            logger.info(f"Loaded state from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load state: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    manager = CargoManager()
    
    # Create transports
    refrigerated_transport = Transport(
        id="TR-001",
        capacity=20000,
        cargo_type=CargoType.REFRIGERATED
    )
    
    dry_transport = Transport(
        id="TR-002",
        capacity=30000,
        cargo_type=CargoType.DRY
    )
    
    manager.add_transport(refrigerated_transport)
    manager.add_transport(dry_transport)
    
    # Register cargo
    refrigerated_cargo = Cargo(
        id="CRG-001",
        type=CargoType.REFRIGERATED,
        weight=5000,
        destination="Cartagena",
        temperature=-18.0
    )
    
    dry_cargo = Cargo(
        id="CRG-002",
        type=CargoType.DRY,
        weight=10000,
        destination="Barranquilla",
        hazardous=True
    )
    
    manager.register_cargo(refrigerated_cargo)
    manager.register_cargo(dry_cargo)
    
    # Assign cargo to transports
    manager.assign_cargo_to_transport("CRG-001", "TR-001")
    manager.assign_cargo_to_transport("CRG-002", "TR-002")
    
    # Generate and print report
    report = manager.generate_report()
    print(json.dumps(report, indent=2))
    
    # Save state
    manager.save_to_file("cargo_state.json")
```
