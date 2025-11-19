"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Generate a cost estimation template for a custom pipeline construction project in Africa, including factors such as materials, labor, and equipment costs."
Generated: DETERMINISTIC_a6c2b6b883a010da
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import datetime

class CostCategory(Enum):
    MATERIALS = "Materials"
    LABOR = "Labor"
    EQUIPMENT = "Equipment"
    TRANSPORT = "Transport"
    PERMITS = "Permits"
    CONTINGENCY = "Contingency"
    OTHER = "Other"

@dataclass
class CostItem:
    name: str
    category: CostCategory
    unit: str
    quantity: float
    unit_cost: float
    notes: Optional[str] = None

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost

@dataclass
class PipelineProject:
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    currency: str = "USD"
    cost_items: List[CostItem] = field(default_factory=list)
    exchange_rate: float = 1.0  # Default to 1 for USD

    def add_cost_item(self, item: CostItem) -> None:
        self.cost_items.append(item)

    def remove_cost_item(self, item_name: str) -> bool:
        for i, item in enumerate(self.cost_items):
            if item.name == item_name:
                self.cost_items.pop(i)
                return True
        return False

    def calculate_total_cost(self) -> float:
        return sum(item.total_cost for item in self.cost_items) * self.exchange_rate

    def calculate_cost_by_category(self) -> Dict[CostCategory, float]:
        category_totals = {category: 0.0 for category in CostCategory}
        for item in self.cost_items:
            category_totals[item.category] += item.total_cost
        return {k: v * self.exchange_rate for k, v in category_totals.items()}

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "currency": self.currency,
            "exchange_rate": self.exchange_rate,
            "cost_items": [
                {
                    "name": item.name,
                    "category": item.category.value,
                    "unit": item.unit,
                    "quantity": item.quantity,
                    "unit_cost": item.unit_cost,
                    "notes": item.notes,
                    "total_cost": item.total_cost
                }
                for item in self.cost_items
            ],
            "total_cost": self.calculate_total_cost(),
            "cost_by_category": {
                category.value: amount
                for category, amount in self.calculate_cost_by_category().items()
            }
        }

    def save_to_file(self, filename: str) -> None:
        try:
            with open(filename, "w") as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise Exception(f"Failed to save project: {str(e)}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'PipelineProject':
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            
            project = cls(
                name=data["name"],
                location=data["location"],
                start_date=datetime.date.fromisoformat(data["start_date"]),
                end_date=datetime.date.fromisoformat(data["end_date"]),
                currency=data.get("currency", "USD"),
                exchange_rate=data.get("exchange_rate", 1.0)
            )
            
            for item_data in data["cost_items"]:
                project.add_cost_item(
                    CostItem(
                        name=item_data["name"],
                        category=CostCategory(item_data["category"]),
                        unit=item_data["unit"],
                        quantity=item_data["quantity"],
                        unit_cost=item_data["unit_cost"],
                        notes=item_data.get("notes")
                    )
                )
            
            return project
        except (IOError, KeyError, ValueError) as e:
            raise Exception(f"Failed to load project: {str(e)}")

def main():
    # Example usage
    project = PipelineProject(
        name="Nigeria Pipeline Project",
        location="Lagos, Nigeria",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 12, 31),
        currency="NGN",
        exchange_rate=0.0024  # Example rate: 1 NGN = 0.0024 USD
    )

    # Add cost items
    project.add_cost_item(
        CostItem(
            name="Steel Pipes",
            category=CostCategory.MATERIALS,
            unit="meter",
            quantity=5000,
            unit_cost=150,
            notes="High-grade steel pipes"
        )
    )

    project.add_cost_item(
        CostItem(
            name="Excavation Labor",
            category=CostCategory.LABOR,
            unit="hour",
            quantity=2000,
            unit_cost=25,
            notes="Local labor costs"
        )
    )

    project.add_cost_item(
        CostItem(
            name="Excavator Rental",
            category=CostCategory.EQUIPMENT,
            unit="day",
            quantity=90,
            unit_cost=500,
            notes="Includes operator"
        )
    )

    # Save and load example
    try:
        project.save_to_file("pipeline_project.json")
        loaded_project = PipelineProject.load_from_file("pipeline_project.json")
        
        print(f"Project: {loaded_project.name}")
        print(f"Total Cost: {loaded_project.currency} {loaded_project.calculate_total_cost():,.2f}")
        print("\nCost Breakdown by Category:")
        for category, amount in loaded_project.calculate_cost_by_category().items():
            print(f"{category.value}: {loaded_project.currency} {amount:,.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
