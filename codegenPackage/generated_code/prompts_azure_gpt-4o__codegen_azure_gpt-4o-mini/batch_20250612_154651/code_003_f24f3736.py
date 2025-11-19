"""
Generated Code Metadata:
========================
Original URL: https://eigennlayer.com
Prompt: Write code to design a unified platform for e-mobility charge point operations, inspired by Eigen Energy's approach to streamlining EV charging technologies in Asia.
Generated: DETERMINISTIC_f24f373617ee075f
Batch ID: 20250612_154651
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
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChargePoint:
    """Class representing a single charge point for electric vehicles."""
    
    def __init__(self, id: str, location: str, status: str = "available"):
        self.id = id
        self.location = location
        self.status = status

    def update_status(self, new_status: str):
        """Update the status of the charge point."""
        if new_status in ["available", "in_use", "out_of_service"]:
            self.status = new_status
            logging.info(f"Charge point {self.id} status updated to {self.status}.")
        else:
            logging.error(f"Invalid status '{new_status}' for charge point {self.id}.")

class ChargePointManager:
    """Class to manage multiple charge points."""
    
    def __init__(self):
        self.charge_points: Dict[str, ChargePoint] = {}

    def add_charge_point(self, charge_point: ChargePoint):
        """Add a new charge point to the manager."""
        if charge_point.id in self.charge_points:
            logging.error(f"Charge point with ID {charge_point.id} already exists.")
            raise ValueError(f"Charge point with ID {charge_point.id} already exists.")
        self.charge_points[charge_point.id] = charge_point
        logging.info(f"Charge point {charge_point.id} added successfully.")

    def remove_charge_point(self, charge_point_id: str):
        """Remove a charge point from the manager."""
        if charge_point_id in self.charge_points:
            del self.charge_points[charge_point_id]
            logging.info(f"Charge point {charge_point_id} removed successfully.")
        else:
            logging.error(f"Charge point with ID {charge_point_id} does not exist.")
            raise KeyError(f"Charge point with ID {charge_point_id} does not exist.")

    def get_charge_point_status(self, charge_point_id: str) -> str:
        """Get the status of a specific charge point."""
        if charge_point_id in self.charge_points:
            status = self.charge_points[charge_point_id].status
            logging.info(f"Charge point {charge_point_id} status retrieved: {status}.")
            return status
        else:
            logging.error(f"Charge point with ID {charge_point_id} does not exist.")
            raise KeyError(f"Charge point with ID {charge_point_id} does not exist.")

    def list_charge_points(self) -> List[Dict[str, Any]]:
        """List all charge points with their details."""
        return [{"id": cp.id, "location": cp.location, "status": cp.status} for cp in self.charge_points.values()]

def main():
    """Main function to demonstrate the ChargePointManager functionality."""
    try:
        manager = ChargePointManager()
        
        # Adding charge points
        cp1 = ChargePoint(id="CP001", location="Location A")
        cp2 = ChargePoint(id="CP002", location="Location B")
        manager.add_charge_point(cp1)
        manager.add_charge_point(cp2)

        # Listing charge points
        logging.info("Current charge points:")
        logging.info(json.dumps(manager.list_charge_points(), indent=2))

        # Updating status
        cp1.update_status("in_use")
        logging.info(f"Status of CP001: {manager.get_charge_point_status('CP001')}")

        # Removing a charge point
        manager.remove_charge_point("CP002")
        logging.info("Current charge points after removal:")
        logging.info(json.dumps(manager.list_charge_points(), indent=2))

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
