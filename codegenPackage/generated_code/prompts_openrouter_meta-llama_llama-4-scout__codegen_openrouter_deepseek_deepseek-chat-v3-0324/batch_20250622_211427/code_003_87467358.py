"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.net
Prompt: Develop a code snippet to manage relationships with multiple small-batch producers, ensuring reliable sourcing and consistent availability of high-quality cooking oils.
Generated: DETERMINISTIC_874673586c173d30
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


class OilQuality(Enum):
    """Enum representing different quality grades of cooking oils."""
    PREMIUM = "Premium"
    STANDARD = "Standard"
    ECONOMY = "Economy"


@dataclass
class Producer:
    """Class representing a small-batch oil producer."""
    id: str
    name: str
    location: str
    capacity: float  # in liters per month
    quality: OilQuality
    reliability_score: float  # 0-1 scale
    lead_time: int  # in days


@dataclass
class Order:
    """Class representing an order placed with a producer."""
    producer_id: str
    quantity: float  # in liters
    order_date: datetime
    expected_delivery_date: datetime
    status: str  # e.g., "placed", "shipped", "delivered", "cancelled"


class OilSourcingManager:
    """Manages relationships with small-batch oil producers and ensures reliable sourcing."""
    
    def __init__(self):
        self.producers: Dict[str, Producer] = {}
        self.orders: List[Order] = []
        self.logger = logging.getLogger(__name__)
        
    def add_producer(self, producer: Producer) -> None:
        """Add a new producer to the manager."""
        if producer.id in self.producers:
            self.logger.warning(f"Producer with ID {producer.id} already exists.")
            return
        self.producers[producer.id] = producer
        self.logger.info(f"Added producer: {producer.name} (ID: {producer.id})")
    
    def place_order(self, producer_id: str, quantity: float) -> Optional[Order]:
        """Place an order with a producer."""
        if producer_id not in self.producers:
            self.logger.error(f"Producer with ID {producer_id} not found.")
            return None
        
        producer = self.producers[producer_id]
        
        if quantity > producer.capacity:
            self.logger.error(
                f"Order quantity {quantity} exceeds producer capacity {producer.capacity}."
            )
            return None
        
        order_date = datetime.now()
        expected_delivery_date = order_date + timedelta(days=producer.lead_time)
        
        order = Order(
            producer_id=producer_id,
            quantity=quantity,
            order_date=order_date,
            expected_delivery_date=expected_delivery_date,
            status="placed"
        )
        
        self.orders.append(order)
        self.logger.info(
            f"Order placed with {producer.name} for {quantity} liters. "
            f"Expected delivery: {expected_delivery_date.strftime('%Y-%m-%d')}"
        )
        return order
    
    def update_order_status(self, order_index: int, new_status: str) -> bool:
        """Update the status of an existing order."""
        try:
            order = self.orders[order_index]
            order.status = new_status
            self.logger.info(
                f"Order {order_index} status updated to {new_status}."
            )
            return True
        except IndexError:
            self.logger.error(f"Order index {order_index} out of range.")
            return False
    
    def get_reliable_producers(self, min_reliability: float = 0.8) -> List[Producer]:
        """Get producers with reliability score above a threshold."""
        return [
            p for p in self.producers.values() 
            if p.reliability_score >= min_reliability
        ]
    
    def get_producers_by_quality(self, quality: OilQuality) -> List[Producer]:
        """Get producers that match a specific quality grade."""
        return [p for p in self.producers.values() if p.quality == quality]
    
    def check_inventory_availability(self, required_quantity: float) -> bool:
        """Check if total available capacity can meet demand."""
        total_capacity = sum(p.capacity for p in self.producers.values())
        return total_capacity >= required_quantity


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    manager = OilSourcingManager()
    
    # Add some producers
    manager.add_producer(Producer(
        id="p1",
        name="Olive Grove Farms",
        location="Spain",
        capacity=5000,
        quality=OilQuality.PREMIUM,
        reliability_score=0.9,
        lead_time=14
    ))
    
    manager.add_producer(Producer(
        id="p2",
        name="Sunflower Valley",
        location="France",
        capacity=8000,
        quality=OilQuality.STANDARD,
        reliability_score=0.85,
        lead_time=10
    ))
    
    # Place an order
    order = manager.place_order("p1", 2000)
    if order:
        print(f"Order placed successfully. Delivery expected on {order.expected_delivery_date}")
    
    # Check reliable producers
    reliable_producers = manager.get_reliable_producers()
    print(f"Reliable producers: {[p.name for p in reliable_producers]}")
```
