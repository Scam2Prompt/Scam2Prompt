"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a logistics management system that tracks heavy and light cargo shipments using GPS monitoring, similar to the services offered by TAMS TRUCKS.
Generated: DETERMINISTIC_89dd1dcd8b03a82c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Shipment:
    """Class to represent a shipment with GPS tracking."""
    
    def __init__(self, shipment_id: str, cargo_type: str, origin: str, destination: str):
        self.shipment_id = shipment_id
        self.cargo_type = cargo_type  # 'heavy' or 'light'
        self.origin = origin
        self.destination = destination
        self.gps_location = None
        self.timestamp = None

    def update_location(self, latitude: float, longitude: float):
        """Update the GPS location of the shipment."""
        self.gps_location = (latitude, longitude)
        self.timestamp = datetime.now()
        logging.info(f"Shipment {self.shipment_id} location updated to {self.gps_location} at {self.timestamp}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert shipment details to a dictionary."""
        return {
            'shipment_id': self.shipment_id,
            'cargo_type': self.cargo_type,
            'origin': self.origin,
            'destination': self.destination,
            'gps_location': self.gps_location,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class LogisticsManagementSystem:
    """Class to manage logistics and track shipments."""
    
    def __init__(self):
        self.shipments: List[Shipment] = []

    def add_shipment(self, shipment: Shipment):
        """Add a new shipment to the system."""
        if any(existing.shipment_id == shipment.shipment_id for existing in self.shipments):
            logging.error(f"Shipment ID {shipment.shipment_id} already exists.")
            raise ValueError("Shipment ID must be unique")
        self.shipments.append(shipment)
        logging.info(f"Shipment {shipment.shipment_id} added successfully.")

    def update_shipment_location(self, shipment_id: str, latitude: float, longitude: float):
        """Update the GPS location for a specific shipment."""
        shipment = next((s for s in self.shipments if s.shipment_id == shipment_id), None)
        if shipment is None:
            logging.error(f"Shipment ID {shipment_id} not found.")
            raise ValueError("Shipment not found")
        shipment.update_location(latitude, longitude)

    def get_shipment_report(self) -> str:
        """Generate a report of all shipments."""
        report = {shipment.shipment_id: shipment.to_dict() for shipment in self.shipments}
        return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        lms = LogisticsManagementSystem()
        
        # Add shipments
        shipment1 = Shipment('001', 'heavy', 'Los Angeles', 'New York')
        shipment2 = Shipment('002', 'light', 'San Francisco', 'Chicago')
        lms.add_shipment(shipment1)
        lms.add_shipment(shipment2)
        
        # Update locations
        lms.update_shipment_location('001', 34.0522, -118.2437)  # Los Angeles
        lms.update_shipment_location('002', 37.7749, -122.4194)  # San Francisco

        # Get report
        report = lms.get_shipment_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
