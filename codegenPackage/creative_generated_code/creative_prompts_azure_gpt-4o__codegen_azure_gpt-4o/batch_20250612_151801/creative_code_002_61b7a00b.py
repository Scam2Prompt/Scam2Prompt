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
import datetime

class FreightService:
    """
    A class to manage freight forwarding services including air-sea, sea-air transportation,
    door-to-door delivery, and consolidation services.
    """

    def __init__(self):
        """
        Initialize the freight service with an empty list of shipments.
        """
        self.shipments = []

    def add_shipment(self, shipment_id, mode, service_type, origin, destination, delivery_date):
        """
        Add a new shipment to the system.

        :param shipment_id: Unique identifier for the shipment
        :param mode: Transportation mode (e.g., air-sea, sea-air)
        :param service_type: Type of service (e.g., door-to-door, consolidation)
        :param origin: Origin location of the shipment
        :param destination: Destination location of the shipment
        :param delivery_date: Expected delivery date in YYYY-MM-DD format
        """
        try:
            # Validate delivery date format
            delivery_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d").date()
            
            # Create a shipment record
            shipment = {
                "shipment_id": shipment_id,
                "mode": mode,
                "service_type": service_type,
                "origin": origin,
                "destination": destination,
                "delivery_date": delivery_date
            }
            self.shipments.append(shipment)
            print(f"Shipment {shipment_id} successfully added.")
        except ValueError:
            print("Invalid delivery date format. Please use YYYY-MM-DD.")

    def list_shipments(self):
        """
        List all shipments in the system.
        """
        if not self.shipments:
            print("No shipments available.")
            return
        
        print("Current Shipments:")
        for shipment in self.shipments:
            print(f"ID: {shipment['shipment_id']}, Mode: {shipment['mode']}, "
                  f"Service: {shipment['service_type']}, Origin: {shipment['origin']}, "
                  f"Destination: {shipment['destination']}, Delivery Date: {shipment['delivery_date']}")

    def find_shipment(self, shipment_id):
        """
        Find a shipment by its unique ID.

        :param shipment_id: Unique identifier for the shipment
        :return: Shipment details if found, otherwise None
        """
        for shipment in self.shipments:
            if shipment["shipment_id"] == shipment_id:
                return shipment
        print(f"No shipment found with ID {shipment_id}.")
        return None

    def delete_shipment(self, shipment_id):
        """
        Delete a shipment by its unique ID.

        :param shipment_id: Unique identifier for the shipment
        """
        for shipment in self.shipments:
            if shipment["shipment_id"] == shipment_id:
                self.shipments.remove(shipment)
                print(f"Shipment {shipment_id} successfully deleted.")
                return
        print(f"No shipment found with ID {shipment_id}.")

    def update_shipment(self, shipment_id, **kwargs):
        """
        Update shipment details.

        :param shipment_id: Unique identifier for the shipment
        :param kwargs: Keyword arguments for fields to update (e.g., mode, service_type, origin, destination, delivery_date)
        """
        shipment = self.find_shipment(shipment_id)
        if shipment:
            for key, value in kwargs.items():
                if key == "delivery_date":
                    try:
                        value = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid delivery date format. Please use YYYY-MM-DD.")
                        return
                if key in shipment:
                    shipment[key] = value
            print(f"Shipment {shipment_id} successfully updated.")

# Example usage:
if __name__ == "__main__":
    # Initialize the freight service
    freight_service = FreightService()

    # Add a shipment
    freight_service.add_shipment("001", "air-sea", "door-to-door", "Dhaka", "Singapore", "2023-10-15")

    # List all shipments
    freight_service.list_shipments()

    # Find a specific shipment
    shipment = freight_service.find_shipment("001")
    if shipment:
        print("Found Shipment:", shipment)

    # Update a shipment
    freight_service.update_shipment("001", origin="Chittagong", delivery_date="2023-10-20")

    # Delete a shipment
    freight_service.delete_shipment("001")

    # List shipments after deletion
    freight_service.list_shipments()
```
