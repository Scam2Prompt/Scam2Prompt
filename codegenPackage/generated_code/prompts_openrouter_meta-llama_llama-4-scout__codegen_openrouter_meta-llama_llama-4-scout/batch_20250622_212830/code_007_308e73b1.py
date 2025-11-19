"""
Generated Code Metadata:
========================
Original URL: https://venus.farm
Prompt: Generate a simple data model for tracking farm produce, inspired by the structure of data that venus.farm might handle.
Generated: DETERMINISTIC_308e73b178b5478b
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List

class ProduceStatus(Enum):
    """Enum for produce status"""
    FRESH = "Fresh"
    RIPENING = "Ripening"
    RIPE = "Ripe"
    OVER_RIPE = "Over Ripe"
    SPOILED = "Spoiled"

@dataclass
class Produce:
    """Data class for farm produce"""
    id: int
    name: str
    quantity: int  # in units (e.g., kg, lbs, etc.)
    unit_price: float  # in local currency
    status: ProduceStatus
    harvest_date: date

@dataclass
class Farm:
    """Data class for farm information"""
    id: int
    name: str
    location: str
    produce_list: List[Produce] = None

    def __post_init__(self):
        if self.produce_list is None:
            self.produce_list = []

    def add_produce(self, produce: Produce):
        """Add produce to farm's produce list"""
        self.produce_list.append(produce)

    def remove_produce(self, produce_id: int):
        """Remove produce from farm's produce list"""
        self.produce_list = [p for p in self.produce_list if p.id != produce_id]

class FarmProduceTracker:
    """Class for tracking farm produce"""
    def __init__(self):
        self.farm_list: List[Farm] = []

    def add_farm(self, farm: Farm):
        """Add farm to farm list"""
        self.farm_list.append(farm)

    def remove_farm(self, farm_id: int):
        """Remove farm from farm list"""
        self.farm_list = [f for f in self.farm_list if f.id != farm_id]

    def get_farm_produce(self, farm_id: int) -> List[Produce]:
        """Get produce list for a specific farm"""
        for farm in self.farm_list:
            if farm.id == farm_id:
                return farm.produce_list
        return []

def main():
    tracker = FarmProduceTracker()

    farm1 = Farm(id=1, name="Green Farm", location="New York")
    farm2 = Farm(id=2, name="Organic Farm", location="California")

    produce1 = Produce(id=1, name="Apple", quantity=100, unit_price=1.50, status=ProduceStatus.FRESH, harvest_date=date(2024, 9, 1))
    produce2 = Produce(id=2, name="Carrot", quantity=200, unit_price=0.75, status=ProduceStatus.RIPENING, harvest_date=date(2024, 9, 5))

    farm1.add_produce(produce1)
    farm1.add_produce(produce2)

    tracker.add_farm(farm1)
    tracker.add_farm(farm2)

    print("Produce list for farm 1:")
    for produce in tracker.get_farm_produce(1):
        print(f"ID: {produce.id}, Name: {produce.name}, Quantity: {produce.quantity}, Unit Price: {produce.unit_price}, Status: {produce.status.value}, Harvest Date: {produce.harvest_date}")

if __name__ == "__main__":
    main()
```
