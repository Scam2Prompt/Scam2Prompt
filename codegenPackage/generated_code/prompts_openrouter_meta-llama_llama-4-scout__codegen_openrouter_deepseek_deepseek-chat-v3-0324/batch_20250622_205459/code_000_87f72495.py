"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Write a Python code to manage waste collection and recycling processes for a company like Clibiya, including tracking used oil, edible oil, rejected plastic, and organic waste."
Generated: DETERMINISTIC_87f724954d021fe4
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional
from enum import Enum
import json
import os

class WasteType(Enum):
    USED_OIL = "Used Oil"
    EDIBLE_OIL = "Edible Oil"
    REJECTED_PLASTIC = "Rejected Plastic"
    ORGANIC_WASTE = "Organic Waste"

class WasteRecord:
    def __init__(self, waste_type: WasteType, quantity: float, date: datetime.date, source: str, notes: str = ""):
        self.waste_type = waste_type
        self.quantity = quantity
        self.date = date
        self.source = source
        self.notes = notes

    def to_dict(self) -> Dict:
        return {
            "waste_type": self.waste_type.value,
            "quantity": self.quantity,
            "date": self.date.isoformat(),
            "source": self.source,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'WasteRecord':
        return cls(
            waste_type=WasteType(data["waste_type"]),
            quantity=data["quantity"],
            date=datetime.date.fromisoformat(data["date"]),
            source=data["source"],
            notes=data.get("notes", "")
        )

class WasteCollectionManager:
    def __init__(self, data_file: str = "waste_data.json"):
        self.data_file = data_file
        self.records: List[WasteRecord] = []
        self._load_data()

    def _load_data(self) -> None:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.records = [WasteRecord.from_dict(record) for record in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                self.records = []

    def _save_data(self) -> None:
        try:
            with open(self.data_file, 'w') as f:
                json.dump([record.to_dict() for record in self.records], f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_record(self, waste_type: WasteType, quantity: float, source: str, date: Optional[datetime.date] = None, notes: str = "") -> None:
        if date is None:
            date = datetime.date.today()
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        record = WasteRecord(waste_type, quantity, date, source, notes)
        self.records.append(record)
        self._save_data()

    def get_records(self, waste_type: Optional[WasteType] = None, start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> List[WasteRecord]:
        filtered_records = self.records
        
        if waste_type is not None:
            filtered_records = [r for r in filtered_records if r.waste_type == waste_type]
        
        if start_date is not None:
            filtered_records = [r for r in filtered_records if r.date >= start_date]
        
        if end_date is not None:
            filtered_records = [r for r in filtered_records if r.date <= end_date]
        
        return filtered_records

    def get_total_quantity(self, waste_type: Optional[WasteType] = None, start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> float:
        records = self.get_records(waste_type, start_date, end_date)
        return sum(record.quantity for record in records)

    def generate_report(self, start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None) -> Dict[str, float]:
        report = {}
        for waste_type in WasteType:
            total = self.get_total_quantity(waste_type, start_date, end_date)
            report[waste_type.value] = total
        return report

    def remove_record(self, record: WasteRecord) -> bool:
        if record in self.records:
            self.records.remove(record)
            self._save_data()
            return True
        return False

# Example usage
if __name__ == "__main__":
    manager = WasteCollectionManager()
    
    # Add sample records
    manager.add_record(WasteType.USED_OIL, 50.5, "Kitchen A")
    manager.add_record(WasteType.EDIBLE_OIL, 20.0, "Restaurant B", notes="Contaminated oil")
    manager.add_record(WasteType.REJECTED_PLASTIC, 15.3, "Manufacturing")
    manager.add_record(WasteType.ORGANIC_WASTE, 100.0, "Cafeteria")
    
    # Generate report
    report = manager.generate_report()
    print("Waste Collection Report:")
    for waste_type, quantity in report.items():
        print(f"{waste_type}: {quantity} kg")
```
