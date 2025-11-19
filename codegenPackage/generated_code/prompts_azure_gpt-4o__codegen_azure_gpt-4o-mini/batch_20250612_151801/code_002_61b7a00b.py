"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Create a program to manage freight forwarding services that include air-sea and sea-air transportation, incorporating features like door-to-door delivery and consolidation services as highlighted by Daimon Logistics BD.
Generated: DETERMINISTIC_61b7a00b28541c26
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreightForwardingService:
    def __init__(self):
        """Initialize the freight forwarding service with an empty list of shipments."""
        self.shipments: List[Dict] = []

    def add_shipment(self, shipment: Dict) -> None:
        """
        Add a new shipment to the service.

        Args:
            shipment (Dict): A dictionary containing shipment details.
        """
        try:
            if not self.validate_shipment(shipment):
                raise ValueError("Invalid shipment data.")
            self.shipments.append(shipment)
            logging.info(f"Shipment added: {shipment}")
        except Exception as e:
            logging.error(f"Error adding shipment: {e}")

    def validate_shipment(self, shipment: Dict) -> bool:
        """
        Validate the shipment data.

        Args:
            shipment (Dict): A dictionary containing shipment details.

        Returns:
            bool: True if valid, False otherwise.
        """
        required_fields = ['origin', 'destination', 'weight', 'service_type']
        return all(field in shipment for field in required_fields)

    def get_shipments(self) -> List[Dict]:
        """Return the list of all shipments."""
        return self.shipments

    def consolidate_shipments(self) -> List[Dict]:
        """
        Consolidate shipments for cost-effective transportation.

        Returns:
            List[Dict]: A list of consolidated shipments.
        """
        # This is a placeholder for consolidation logic
        consolidated = []
        if self.shipments:
            consolidated.append({
                'origin': self.shipments[0]['origin'],
                'destination': self.shipments[0]['destination'],
                'total_weight': sum(shipment['weight'] for shipment in self.shipments),
                'service_type': 'Consolidated'
            })
            logging.info("Shipments consolidated.")
        return consolidated

    def door_to_door_service(self, shipment_id: int) -> Optional[Dict]:
        """
        Provide door-to-door delivery service for a specific shipment.

        Args:
            shipment_id (int): The ID of the shipment to deliver.

        Returns:
            Optional[Dict]: The shipment details if found, None otherwise.
        """
        try:
            shipment = self.shipments[shipment_id]
            logging.info(f"Door-to-door service initiated for shipment: {shipment}")
            return shipment
        except IndexError:
            logging.error("Shipment ID not found.")
            return None

# Example usage
if __name__ == "__main__":
    service = FreightForwardingService()
    
    # Adding sample shipments
    service.add_shipment({'origin': 'New York', 'destination': 'London', 'weight': 100, 'service_type': 'Air-Sea'})
    service.add_shipment({'origin': 'Tokyo', 'destination': 'Los Angeles', 'weight': 200, 'service_type': 'Sea-Air'})
    
    # Retrieve all shipments
    all_shipments = service.get_shipments()
    logging.info(f"All shipments: {all_shipments}")
    
    # Consolidate shipments
    consolidated_shipments = service.consolidate_shipments()
    logging.info(f"Consolidated shipments: {consolidated_shipments}")
    
    # Door-to-door service
    door_to_door = service.door_to_door_service(0)
    logging.info(f"Door-to-door service result: {door_to_door}")
```
