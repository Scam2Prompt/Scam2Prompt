"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a logistics management system that tracks heavy and light cargo shipments using GPS monitoring, similar to the services offered by TAMS TRUCKS.
Generated: DETERMINISTIC_89dd1dcd8b03a82c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cargo:
    """Class to represent a cargo shipment."""
    
    def __init__(self, cargo_id: str, weight: float, cargo_type: str, destination: str):
        """
        Initialize a new Cargo instance.

        :param cargo_id: Unique identifier for the cargo
        :param weight: Weight of the cargo in kilograms
        :param cargo_type: Type of cargo ('heavy' or 'light')
        :param destination: Destination address for the cargo
        """
        self.cargo_id = cargo_id
        self.weight = weight
        self.cargo_type = cargo_type
        self.destination = destination
        self.location_history: List[Dict[str, Any]] = []

    def update_location(self, latitude: float, longitude: float):
        """
        Update the cargo's current GPS location.

        :param latitude: Current latitude of the cargo
        :param longitude: Current longitude of the cargo
        """
        timestamp = datetime.now().isoformat()
        self.location_history.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude
        })
        logging.info(f"Updated location for cargo {self.cargo_id}: {latitude}, {longitude} at {timestamp}")

    def get_location_history(self) -> List[Dict[str, Any]]:
        """Return the location history of the cargo."""
        return self.location_history

class CargoTracker:
    """Class to manage cargo shipments."""
    
    def __init__(self):
        """Initialize the CargoTracker with an empty cargo list."""
        self.cargos: Dict[str, Cargo] = {}

    def add_cargo(self, cargo: Cargo):
        """
        Add a new cargo to the tracker.

        :param cargo: Cargo instance to be added
        """
        if cargo.cargo_id in self.cargos:
            logging.error(f"Cargo with ID {cargo.cargo_id} already exists.")
            raise ValueError(f"Cargo with ID {cargo.cargo_id} already exists.")
        self.cargos[cargo.cargo_id] = cargo
        logging.info(f"Added cargo {cargo.cargo_id} to tracker.")

    def update_cargo_location(self, cargo_id: str, latitude: float, longitude: float):
        """
        Update the location of a specific cargo.

        :param cargo_id: Unique identifier for the cargo
        :param latitude: Current latitude of the cargo
        :param longitude: Current longitude of the cargo
        """
        if cargo_id not in self.cargos:
            logging.error(f"Cargo with ID {cargo_id} not found.")
            raise KeyError(f"Cargo with ID {cargo_id} not found.")
        self.cargos[cargo_id].update_location(latitude, longitude)

    def get_cargo_info(self, cargo_id: str) -> Dict[str, Any]:
        """
        Retrieve information about a specific cargo.

        :param cargo_id: Unique identifier for the cargo
        :return: Dictionary containing cargo information
        """
        if cargo_id not in self.cargos:
            logging.error(f"Cargo with ID {cargo_id} not found.")
            raise KeyError(f"Cargo with ID {cargo_id} not found.")
        cargo = self.cargos[cargo_id]
        return {
            'cargo_id': cargo.cargo_id,
            'weight': cargo.weight,
            'cargo_type': cargo.cargo_type,
            'destination': cargo.destination,
            'location_history': cargo.get_location_history()
        }

# Example usage
if __name__ == "__main__":
    try:
        tracker = CargoTracker()
        
        # Create and add cargo
        cargo1 = Cargo(cargo_id="CARGO001", weight=1500.0, cargo_type="heavy", destination="Warehouse A")
        tracker.add_cargo(cargo1)

        # Update cargo location
        tracker.update_cargo_location("CARGO001", 34.0522, -118.2437)

        # Retrieve cargo information
        cargo_info = tracker.get_cargo_info("CARGO001")
        print(json.dumps(cargo_info, indent=4))

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
