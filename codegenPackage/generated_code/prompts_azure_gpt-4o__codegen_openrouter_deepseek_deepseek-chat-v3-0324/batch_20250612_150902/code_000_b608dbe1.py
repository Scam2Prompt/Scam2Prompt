"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: Write Python code to simulate a waste management system based on Clibiya's "black and white" model, including collection, recycling, and sales of renewable/recycled products like used oil, edible fats, and rejected plastic.
Generated: DETERMINISTIC_b608dbe113567815
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta

class WasteType(Enum):
    USED_OIL = "Used Oil"
    EDIBLE_FATS = "Edible Fats"
    REJECTED_PLASTIC = "Rejected Plastic"

class CollectionStatus(Enum):
    PENDING = "Pending"
    COLLECTED = "Collected"
    PROCESSED = "Processed"
    RECYCLED = "Recycled"
    SOLD = "Sold"

@dataclass
class WasteItem:
    id: str
    type: WasteType
    quantity: float  # in kilograms
    collection_date: datetime
    status: CollectionStatus = CollectionStatus.PENDING
    processing_cost: float = 0.0
    revenue: float = 0.0

class WasteManagementSystem:
    def __init__(self):
        self.waste_items: List[WasteItem] = []
        self.recycling_rates: Dict[WasteType, float] = {
            WasteType.USED_OIL: 0.85,  # 85% recycling rate
            WasteType.EDIBLE_FATS: 0.75,
            WasteType.REJECTED_PLASTIC: 0.65
        }
        self.sale_prices: Dict[WasteType, float] = {
            WasteType.USED_OIL: 2.50,  # price per kg
            WasteType.EDIBLE_FATS: 1.80,
            WasteType.REJECTED_PLASTIC: 0.75
        }
        self.processing_costs: Dict[WasteType, float] = {
            WasteType.USED_OIL: 0.50,  # cost per kg
            WasteType.EDIBLE_FATS: 0.40,
            WasteType.REJECTED_PLASTIC: 0.30
        }

    def generate_waste(self, days: int = 30) -> None:
        """Simulate waste generation over a period of days."""
        current_date = datetime.now()
        for day in range(days):
            date = current_date - timedelta(days=day)
            for _ in range(random.randint(1, 5)):
                waste_type = random.choice(list(WasteType))
                quantity = random.uniform(10.0, 100.0)
                self.waste_items.append(
                    WasteItem(
                        id=f"WI-{date.strftime('%Y%m%d')}-{random.randint(1000, 9999)}",
                        type=waste_type,
                        quantity=quantity,
                        collection_date=date
                    )
                )

    def collect_waste(self) -> None:
        """Collect pending waste items."""
        for item in self.waste_items:
            if item.status == CollectionStatus.PENDING:
                item.status = CollectionStatus.COLLECTED

    def process_waste(self) -> None:
        """Process collected waste items."""
        for item in self.waste_items:
            if item.status == CollectionStatus.COLLECTED:
                item.status = CollectionStatus.PROCESSED
                item.processing_cost = item.quantity * self.processing_costs[item.type]

    def recycle_waste(self) -> None:
        """Recycle processed waste items based on recycling rates."""
        for item in self.waste_items:
            if item.status == CollectionStatus.PROCESSED:
                item.status = CollectionStatus.RECYCLED
                recycled_quantity = item.quantity * self.recycling_rates[item.type]
                item.revenue = recycled_quantity * self.sale_prices[item.type]

    def sell_recycled_products(self) -> None:
        """Mark recycled items as sold."""
        for item in self.waste_items:
            if item.status == CollectionStatus.RECYCLED:
                item.status = CollectionStatus.SOLD

    def get_total_revenue(self) -> float:
        """Calculate total revenue from sold items."""
        return sum(item.revenue for item in self.waste_items if item.status == CollectionStatus.SOLD)

    def get_total_processing_cost(self) -> float:
        """Calculate total processing costs."""
        return sum(item.processing_cost for item in self.waste_items if item.status != CollectionStatus.PENDING)

    def get_net_profit(self) -> float:
        """Calculate net profit (revenue - processing costs)."""
        return self.get_total_revenue() - self.get_total_processing_cost()

    def get_waste_summary(self) -> Dict[WasteType, Dict[str, float]]:
        """Generate summary statistics by waste type."""
        summary = {}
        for waste_type in WasteType:
            items = [item for item in self.waste_items if item.type == waste_type]
            total_quantity = sum(item.quantity for item in items)
            recycled_quantity = sum(
                item.quantity * self.recycling_rates[waste_type] 
                for item in items 
                if item.status in [CollectionStatus.RECYCLED, CollectionStatus.SOLD]
            )
            summary[waste_type] = {
                "total_quantity": total_quantity,
                "recycled_quantity": recycled_quantity,
                "recycling_rate": recycled_quantity / total_quantity if total_quantity > 0 else 0.0,
                "revenue": sum(item.revenue for item in items if item.status == CollectionStatus.SOLD),
                "processing_cost": sum(item.processing_cost for item in items if item.status != CollectionStatus.PENDING)
            }
        return summary

    def run_simulation(self, days: int = 30) -> None:
        """Run complete simulation for given number of days."""
        self.generate_waste(days)
        self.collect_waste()
        self.process_waste()
        self.recycle_waste()
        self.sell_recycled_products()

# Example usage
if __name__ == "__main__":
    system = WasteManagementSystem()
    system.run_simulation(60)
    
    print(f"Total Revenue: ${system.get_total_revenue():.2f}")
    print(f"Total Processing Cost: ${system.get_total_processing_cost():.2f}")
    print(f"Net Profit: ${system.get_net_profit():.2f}")
    
    print("\nWaste Summary:")
    for waste_type, stats in system.get_waste_summary().items():
        print(f"\n{waste_type.value}:")
        print(f"  Total Quantity: {stats['total_quantity']:.2f} kg")
        print(f"  Recycled Quantity: {stats['recycled_quantity']:.2f} kg")
        print(f"  Recycling Rate: {stats['recycling_rate']:.2%}")
        print(f"  Revenue: ${stats['revenue']:.2f}")
        print(f"  Processing Cost: ${stats['processing_cost']:.2f}")
```
