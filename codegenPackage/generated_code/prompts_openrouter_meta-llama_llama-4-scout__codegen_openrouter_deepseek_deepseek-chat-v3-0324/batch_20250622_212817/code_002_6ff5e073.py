"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Generate code for a car maintenance tracker that includes features like rust removal, engine coil cover replacement, and other services mentioned for this customized Cobalt SS/TC.
Generated: DETERMINISTIC_6ff5e073ba55b1e8
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional

class MaintenanceType(Enum):
    RUST_REMOVAL = "Rust Removal"
    ENGINE_COIL_COVER_REPLACEMENT = "Engine Coil Cover Replacement"
    OIL_CHANGE = "Oil Change"
    TIRE_ROTATION = "Tire Rotation"
    BRAKE_PAD_REPLACEMENT = "Brake Pad Replacement"
    OTHER = "Other"

class MaintenanceRecord:
    def __init__(self, 
                 maintenance_type: MaintenanceType, 
                 date: datetime.date, 
                 mileage: int, 
                 cost: float, 
                 notes: Optional[str] = None):
        self.maintenance_type = maintenance_type
        self.date = date
        self.mileage = mileage
        self.cost = cost
        self.notes = notes

    def __str__(self):
        return (f"{self.maintenance_type.value} on {self.date.strftime('%Y-%m-%d')} "
                f"at {self.mileage} miles. Cost: ${self.cost:.2f}. "
                f"Notes: {self.notes if self.notes else 'N/A'}")

class CarMaintenanceTracker:
    def __init__(self, car_model: str = "Cobalt SS/TC"):
        self.car_model = car_model
        self.records: List[MaintenanceRecord] = []
    
    def add_record(self, record: MaintenanceRecord) -> None:
        """Add a maintenance record to the tracker."""
        self.records.append(record)
    
    def get_records_by_type(self, maintenance_type: MaintenanceType) -> List[MaintenanceRecord]:
        """Get all records of a specific maintenance type."""
        return [record for record in self.records if record.maintenance_type == maintenance_type]
    
    def get_records_by_date_range(self, start_date: datetime.date, end_date: datetime.date) -> List[MaintenanceRecord]:
        """Get all records within a date range."""
        return [record for record in self.records if start_date <= record.date <= end_date]
    
    def get_records_by_mileage_range(self, min_mileage: int, max_mileage: int) -> List[MaintenanceRecord]:
        """Get all records within a mileage range."""
        return [record for record in self.records if min_mileage <= record.mileage <= max_mileage]
    
    def get_total_spent(self) -> float:
        """Calculate total amount spent on maintenance."""
        return sum(record.cost for record in self.records)
    
    def get_maintenance_summary(self) -> Dict[MaintenanceType, int]:
        """Get count of each maintenance type performed."""
        summary = {}
        for record in self.records:
            summary[record.maintenance_type] = summary.get(record.maintenance_type, 0) + 1
        return summary
    
    def print_all_records(self) -> None:
        """Print all maintenance records."""
        print(f"Maintenance Records for {self.car_model}:")
        for record in self.records:
            print(record)
    
    def save_to_file(self, filename: str) -> None:
        """Save maintenance records to a file."""
        try:
            with open(filename, 'w') as f:
                f.write(f"Car Model: {self.car_model}\n")
                for record in self.records:
                    f.write(f"{record.maintenance_type.value},{record.date},{record.mileage},{record.cost},{record.notes or ''}\n")
        except IOError as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load maintenance records from a file."""
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                if not lines:
                    return
                
                # First line contains car model
                self.car_model = lines[0].split(": ")[1].strip()
                
                # Process remaining lines
                self.records = []
                for line in lines[1:]:
                    parts = line.strip().split(',')
                    if len(parts) >= 4:
                        maintenance_type = MaintenanceType(parts[0])
                        date = datetime.datetime.strptime(parts[1], "%Y-%m-%d").date()
                        mileage = int(parts[2])
                        cost = float(parts[3])
                        notes = parts[4] if len(parts) > 4 and parts[4] else None
                        self.records.append(MaintenanceRecord(maintenance_type, date, mileage, cost, notes))
        except (IOError, ValueError, IndexError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = CarMaintenanceTracker()
    
    # Add some sample records
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=30)
    
    tracker.add_record(MaintenanceRecord(
        MaintenanceType.RUST_REMOVAL,
        last_month,
        45000,
        150.00,
        "Removed rust from undercarriage and wheel wells"
    ))
    
    tracker.add_record(MaintenanceRecord(
        MaintenanceType.ENGINE_COIL_COVER_REPLACEMENT,
        today,
        45500,
        75.50,
        "Replaced cracked engine coil cover"
    ))
    
    tracker.add_record(MaintenanceRecord(
        MaintenanceType.OIL_CHANGE,
        today,
        45500,
        45.00,
        "Full synthetic oil change"
    ))
    
    # Print all records
    tracker.print_all_records()
    
    # Save to file
    tracker.save_to_file("cobalt_maintenance.txt")
    
    # Load from file
    new_tracker = CarMaintenanceTracker()
    new_tracker.load_from_file("cobalt_maintenance.txt")
    new_tracker.print_all_records()
```
