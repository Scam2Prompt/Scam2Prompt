"""
Generated Code Metadata:
========================
Original URL: https://delivery-services.online
Prompt: How can I generate a tracking system for delivery services using a large language model, and what are some potential use cases?
Generated: DETERMINISTIC_df015da7f2b57fbb
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Delivery:
    """Class to represent a delivery item."""
    
    def __init__(self, recipient: str, address: str, status: str = "Pending"):
        self.id = str(uuid.uuid4())  # Unique identifier for the delivery
        self.recipient = recipient
        self.address = address
        self.status = status
        self.timestamp = datetime.now()  # Timestamp of when the delivery was created

    def update_status(self, new_status: str):
        """Update the status of the delivery."""
        self.status = new_status
        self.timestamp = datetime.now()  # Update timestamp on status change

    def to_dict(self) -> Dict:
        """Convert delivery object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "recipient": self.recipient,
            "address": self.address,
            "status": self.status,
            "timestamp": self.timestamp.isoformat()
        }

class DeliveryService:
    """Class to manage deliveries."""
    
    def __init__(self):
        self.deliveries: List[Delivery] = []  # List to store deliveries

    def create_delivery(self, recipient: str, address: str) -> Delivery:
        """Create a new delivery and add it to the list."""
        delivery = Delivery(recipient, address)
        self.deliveries.append(delivery)
        return delivery

    def update_delivery_status(self, delivery_id: str, new_status: str) -> Optional[Delivery]:
        """Update the status of a delivery by its ID."""
        for delivery in self.deliveries:
            if delivery.id == delivery_id:
                delivery.update_status(new_status)
                return delivery
        raise ValueError(f"Delivery with ID {delivery_id} not found.")

    def get_delivery(self, delivery_id: str) -> Optional[Delivery]:
        """Retrieve a delivery by its ID."""
        for delivery in self.deliveries:
            if delivery.id == delivery_id:
                return delivery
        return None  # Return None if not found

    def get_all_deliveries(self) -> List[Dict]:
        """Get a list of all deliveries in JSON serializable format."""
        return [delivery.to_dict() for delivery in self.deliveries]

def main():
    """Main function to demonstrate the delivery tracking system."""
    service = DeliveryService()
    
    # Create a new delivery
    delivery1 = service.create_delivery("John Doe", "123 Elm St")
    print(f"Created Delivery: {delivery1.to_dict()}")

    # Update delivery status
    try:
        updated_delivery = service.update_delivery_status(delivery1.id, "In Transit")
        print(f"Updated Delivery: {updated_delivery.to_dict()}")
    except ValueError as e:
        print(e)

    # Retrieve all deliveries
    all_deliveries = service.get_all_deliveries()
    print("All Deliveries:", json.dumps(all_deliveries, indent=2))

if __name__ == "__main__":
    main()
```
