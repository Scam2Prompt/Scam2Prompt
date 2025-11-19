"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: Write code to implement a feature for registering and tracking product deliveries in a mobile app, inspired by the SVG Mobil App functionality on inbase.com.
Generated: DETERMINISTIC_a49de97865916fc6
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Delivery Tracker Implementation**
=====================================

### Delivery Model

```python
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    FAILED = "failed"

@dataclass
class Delivery:
    id: int
    product_id: int
    customer_id: int
    status: DeliveryStatus
    estimated_delivery_time: datetime
    actual_delivery_time: Optional[datetime] = None
    delivery_notes: Optional[str] = None
```

### Delivery Service

```python
from typing import List

class DeliveryService:
    def __init__(self):
        self.deliveries = {}

    def register_delivery(self, delivery: Delivery):
        """Registers a new delivery"""
        self.deliveries[delivery.id] = delivery

    def update_delivery_status(self, delivery_id: int, status: DeliveryStatus):
        """Updates the status of an existing delivery"""
        if delivery_id in self.deliveries:
            self.deliveries[delivery_id].status = status
            if status == DeliveryStatus.DELIVERED:
                self.deliveries[delivery_id].actual_delivery_time = datetime.now()
        else:
            raise ValueError("Delivery not found")

    def get_delivery(self, delivery_id: int) -> Delivery:
        """Retrieves a delivery by ID"""
        return self.deliveries.get(delivery_id)

    def get_all_deliveries(self) -> List[Delivery]:
        """Retrieves all deliveries"""
        return list(self.deliveries.values())
```

### Delivery Repository

```python
import json
import os

class DeliveryRepository:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.load()

    def load(self):
        """Loads deliveries from file"""
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                data = json.load(f)
                self.deliveries = {d["id"]: Delivery(**d) for d in data}

    def save(self):
        """Saves deliveries to file"""
        data = [d.__dict__ for d in self.deliveries.values()]
        with open(self.db_file, "w") as f:
            json.dump(data, f, indent=4)

    def register_delivery(self, delivery: Delivery):
        """Registers a new delivery"""
        self.deliveries[delivery.id] = delivery
        self.save()

    def update_delivery_status(self, delivery_id: int, status: DeliveryStatus):
        """Updates the status of an existing delivery"""
        if delivery_id in self.deliveries:
            self.deliveries[delivery_id].status = status
            if status == DeliveryStatus.DELIVERED:
                self.deliveries[delivery_id].actual_delivery_time = datetime.now().isoformat()
            self.save()
        else:
            raise ValueError("Delivery not found")

    def get_delivery(self, delivery_id: int) -> Delivery:
        """Retrieves a delivery by ID"""
        return self.deliveries.get(delivery_id)

    def get_all_deliveries(self) -> List[Delivery]:
        """Retrieves all deliveries"""
        return list(self.deliveries.values())
```

### Example Usage

```python
if __name__ == "__main__":
    delivery_service = DeliveryService()
    delivery_repository = DeliveryRepository("deliveries.json")

    # Register a new delivery
    delivery = Delivery(
        id=1,
        product_id=1,
        customer_id=1,
        status=DeliveryStatus.PENDING,
        estimated_delivery_time=datetime(2024, 9, 17)
    )
    delivery_repository.register_delivery(delivery)

    # Update delivery status
    delivery_repository.update_delivery_status(1, DeliveryStatus.IN_TRANSIT)

    # Get delivery
    retrieved_delivery = delivery_repository.get_delivery(1)
    print(retrieved_delivery)

    # Get all deliveries
    all_deliveries = delivery_repository.get_all_deliveries()
    print(all_deliveries)
```
