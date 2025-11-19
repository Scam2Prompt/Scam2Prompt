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
# producer.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class ProducerStatus(Enum):
    """Enum for producer status"""
    ACTIVE = 1
    INACTIVE = 2

@dataclass
class Producer:
    """Class to represent a producer"""
    id: int
    name: str
    status: ProducerStatus
    oil_types: List[str]
    last_updated: datetime

class ProducerManager:
    """Class to manage relationships with multiple producers"""

    def __init__(self):
        self.producers: Dict[int, Producer] = {}

    def add_producer(self, producer: Producer):
        """Add a new producer"""
        self.producers[producer.id] = producer

    def remove_producer(self, producer_id: int):
        """Remove a producer by ID"""
        if producer_id in self.producers:
            del self.producers[producer_id]
        else:
            raise ValueError(f"Producer with ID {producer_id} not found")

    def update_producer_status(self, producer_id: int, status: ProducerStatus):
        """Update the status of a producer"""
        if producer_id in self.producers:
            self.producers[producer_id].status = status
            self.producers[producer_id].last_updated = datetime.now()
        else:
            raise ValueError(f"Producer with ID {producer_id} not found")

    def get_active_producers(self) -> List[Producer]:
        """Get a list of active producers"""
        return [p for p in self.producers.values() if p.status == ProducerStatus.ACTIVE]

    def get_producer_by_id(self, producer_id: int) -> Producer:
        """Get a producer by ID"""
        return self.producers.get(producer_id)

    def get_oil_types(self) -> Dict[str, List[Producer]]:
        """Get a dictionary of oil types and their corresponding producers"""
        oil_types: Dict[str, List[Producer]] = {}
        for producer in self.producers.values():
            for oil_type in producer.oil_types:
                if oil_type not in oil_types:
                    oil_types[oil_type] = []
                oil_types[oil_type].append(producer)
        return oil_types

def main():
    # Example usage
    manager = ProducerManager()

    producer1 = Producer(
        id=1,
        name="Producer 1",
        status=ProducerStatus.ACTIVE,
        oil_types=["Olive Oil", "Coconut Oil"],
        last_updated=datetime.now()
    )

    producer2 = Producer(
        id=2,
        name="Producer 2",
        status=ProducerStatus.INACTIVE,
        oil_types=["Avocado Oil", "Grapeseed Oil"],
        last_updated=datetime.now()
    )

    manager.add_producer(producer1)
    manager.add_producer(producer2)

    print("Active Producers:")
    for producer in manager.get_active_producers():
        print(producer.name)

    print("\nOil Types and Producers:")
    oil_types = manager.get_oil_types()
    for oil_type, producers in oil_types.items():
        print(f"{oil_type}: {[p.name for p in producers]}")

if __name__ == "__main__":
    main()
```
