"""
Generated Code Metadata:
========================
Original URL: https://www.twincityjacuzzi.com
Prompt: Write a Python script to schedule and track hot tub maintenance, including reminders for water changes every three to four months.
Generated: DETERMINISTIC_6f181070402f5194
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, List, Dict
import json
import os
import sys
from enum import Enum

class MaintenanceType(Enum):
    WATER_CHANGE = "Water Change"
    CHEMICAL_BALANCE = "Chemical Balance"
    FILTER_CLEANING = "Filter Cleaning"
    GENERAL_INSPECTION = "General Inspection"

class MaintenanceRecord:
    def __init__(self, 
                 maintenance_type: MaintenanceType, 
                 date_performed: datetime.date, 
                 notes: str = ""):
        self.maintenance_type = maintenance_type
        self.date_performed = date_performed
        self.notes = notes

    def to_dict(self) -> Dict:
        return {
            "maintenance_type": self.maintenance_type.value,
            "date_performed": self.date_performed.isoformat(),
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'MaintenanceRecord':
        return cls(
            maintenance_type=MaintenanceType(data["maintenance_type"]),
            date_performed=datetime.date.fromisoformat(data["date_performed"]),
            notes=data["notes"]
        )

class HotTubMaintenanceTracker:
    def __init__(self, data_file: str = "hot_tub_maintenance.json"):
        self.data_file = data_file
        self.records: List[MaintenanceRecord] = []
        self._load_data()

    def _load_data(self) -> None:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.records = [MaintenanceRecord.from_dict(record) for record in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}", file=sys.stderr)
                self.records = []

    def _save_data(self) -> None:
        try:
            with open(self.data_file, 'w') as f:
                json.dump([record.to_dict() for record in self.records], f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}", file=sys.stderr)

    def add_record(self, maintenance_type: MaintenanceType, notes: str = "") -> None:
        record = MaintenanceRecord(maintenance_type, datetime.date.today(), notes)
        self.records.append(record)
        self._save_data()

    def get_last_maintenance_date(self, maintenance_type: MaintenanceType) -> Optional[datetime.date]:
        relevant_records = [r for r in self.records if r.maintenance_type == maintenance_type]
        if not relevant_records:
            return None
        return max(r.date_performed for r in relevant_records)

    def check_upcoming_maintenance(self) -> Dict[MaintenanceType, bool]:
        today = datetime.date.today()
        results = {}
        
        water_change_date = self.get_last_maintenance_date(MaintenanceType.WATER_CHANGE)
        if water_change_date:
            three_months = water_change_date + datetime.timedelta(days=90)
            four_months = water_change_date + datetime.timedelta(days=120)
            results[MaintenanceType.WATER_CHANGE] = three_months <= today <= four_months
        
        # Add checks for other maintenance types as needed
        return results

    def list_records(self) -> List[MaintenanceRecord]:
        return sorted(self.records, key=lambda x: x.date_performed, reverse=True)

def main():
    tracker = HotTubMaintenanceTracker()
    
    while True:
        print("\nHot Tub Maintenance Tracker")
        print("1. Add maintenance record")
        print("2. Check upcoming maintenance")
        print("3. View all records")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nSelect maintenance type:")
            for i, mtype in enumerate(MaintenanceType, 1):
                print(f"{i}. {mtype.value}")
            mtype_choice = input("Enter maintenance type number: ")
            
            try:
                selected_type = list(MaintenanceType)[int(mtype_choice)-1]
                notes = input("Enter notes (optional): ")
                tracker.add_record(selected_type, notes)
                print("Record added successfully.")
            except (ValueError, IndexError):
                print("Invalid selection.")
                
        elif choice == "2":
            upcoming = tracker.check_upcoming_maintenance()
            print("\nUpcoming Maintenance:")
            for mtype, due in upcoming.items():
                status = "DUE" if due else "Not due yet"
                last_date = tracker.get_last_maintenance_date(mtype)
                print(f"{mtype.value}: {status} (Last: {last_date})")
                
        elif choice == "3":
            records = tracker.list_records()
            print("\nMaintenance Records:")
            for record in records:
                print(f"{record.date_performed}: {record.maintenance_type.value} - {record.notes}")
                
        elif choice == "4":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
