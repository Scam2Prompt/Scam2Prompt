"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Create a program to manage freight forwarding services that include air-sea and sea-air transportation, incorporating features like door-to-door delivery and consolidation services as highlighted by Daimon Logistics BD.
Generated: DETERMINISTIC_61b7a00b28541c26
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Optional

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreightForwardingService:
    def __init__(self, service_type: str, origin: str, destination: str):
        """
        Initialize a FreightForwardingService instance.

        :param service_type: Type of service - either 'air-sea' or 'sea-air'
        :param origin: Origin location for shipment
        :param destination: Destination location for shipment
        """
        self.service_type = service_type
        self.origin = origin
        self.destination = destination
        self.consolidation_list: List[str] = []

        # Validate service type
        if self.service_type not in ['air-sea', 'sea-air']:
            logging.error("Invalid service type provided: %s", service_type)
            raise ValueError("Service type must be 'air-sea' or 'sea-air'")

    def add_consolidation(self, shipment_id: str):
        """
        Add a shipment ID to the consolidation list.

        :param shipment_id: The ID of the shipment to be consolidated
        """
        if shipment_id not in self.consolidation_list:
            self.consolidation_list.append(shipment_id)
            logging.info("Added shipment ID %s to consolidation list", shipment_id)
        else:
            logging.warning("Shipment ID %s is already in the consolidation list", shipment_id)

    def remove_consolidation(self, shipment_id: str):
        """
        Remove a shipment ID from the consolidation list.

        :param shipment_id: The ID of the shipment to be removed
        """
        try:
            self.consolidation_list.remove(shipment_id)
            logging.info("Removed shipment ID %s from consolidation list", shipment_id)
        except ValueError:
            logging.error("Shipment ID %s not found in consolidation list", shipment_id)

    def get_shipment_details(self) -> dict:
        """
        Retrieve shipment details.

        :return: A dictionary containing service details
        """
        return {
            "service_type": self.service_type,
            "origin": self.origin,
            "destination": self.destination,
            "consolidation_list": self.consolidation_list,
        }

    def perform_delivery(self) -> str:
        """
        Simulate the delivery process.

        :return: Status message indicating the delivery status
        """
        if not self.consolidation_list:
            logging.warning("No shipments to deliver.")
            return "No shipments to deliver."
        
        # Simulate processing deliveries
        logging.info("Starting delivery from %s to %s", self.origin, self.destination)
        for shipment_id in self.consolidation_list:
            logging.info("Delivering shipment ID: %s", shipment_id)
        
        # Clear the consolidation list after delivery
        self.consolidation_list.clear()
        logging.info("Delivery completed. Consolidation list has been cleared.")
        return "Delivery completed successfully."

# Example usage
if __name__ == "__main__":
    try:
        service = FreightForwardingService(service_type='air-sea', origin='New York', destination='Tokyo')
        service.add_consolidation("SHIP001")
        service.add_consolidation("SHIP002")
        print(service.get_shipment_details())
        delivery_status = service.perform_delivery()
        print(delivery_status)
    except ValueError as e:
        logging.error("An error occurred: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
