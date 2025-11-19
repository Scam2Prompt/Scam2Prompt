"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a Python script to create a scheduling system for refuse and recycling collection, including features for tracking collection dates and locations specific to the City of York.
Generated: DETERMINISTIC_8d8f549c7a76ef3b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import csv
import os
from enum import Enum

class CollectionType(Enum):
    REFUSE = "Refuse"
    RECYCLING = "Recycling"
    GARDEN_WASTE = "Garden Waste"

@dataclass
class CollectionSchedule:
    location: str
    collection_type: CollectionType
    next_collection_date: datetime.date
    frequency_days: int

    def to_dict(self) -> Dict:
        return {
            "location": self.location,
            "collection_type": self.collection_type.value,
            "next_collection_date": self.next_collection_date.isoformat(),
            "frequency_days": self.frequency_days
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CollectionSchedule':
        return cls(
            location=data["location"],
            collection_type=CollectionType(data["collection_type"]),
            next_collection_date=datetime.date.fromisoformat(data["next_collection_date"]),
            frequency_days=data["frequency_days"]
        )

class CollectionScheduler:
    def __init__(self, data_file: str = "collection_schedules.json"):
        self.data_file = data_file
        self.schedules: List[CollectionSchedule] = []
        self._load_data()

    def _load_data(self) -> None:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.schedules = [CollectionSchedule.from_dict(item) for item in data]
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Failed to load data: {e}")

    def _save_data(self) -> None:
        try:
            with open(self.data_file, "w") as f:
                json.dump([schedule.to_dict() for schedule in self.schedules], f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def add_schedule(self, schedule: CollectionSchedule) -> None:
        self.schedules.append(schedule)
        self._save_data()

    def update_schedule(self, location: str, collection_type: CollectionType, new_date: datetime.date) -> None:
        for schedule in self.schedules:
            if schedule.location == location and schedule.collection_type == collection_type:
                schedule.next_collection_date = new_date
                self._save_data()
                return
        raise ValueError(f"No schedule found for {collection_type.value} at {location}")

    def get_upcoming_collections(self, days_ahead: int = 7) -> List[CollectionSchedule]:
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        return [
            schedule for schedule in self.schedules
            if today <= schedule.next_collection_date <= end_date
        ]

    def import_from_csv(self, csv_file: str) -> None:
        try:
            with open(csv_file, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        schedule = CollectionSchedule(
                            location=row["location"],
                            collection_type=CollectionType(row["collection_type"]),
                            next_collection_date=datetime.date.fromisoformat(row["next_collection_date"]),
                            frequency_days=int(row["frequency_days"])
                        )
                        self.add_schedule(schedule)
                    except (KeyError, ValueError) as e:
                        print(f"Skipping invalid row: {row}. Error: {e}")
        except IOError as e:
            raise RuntimeError(f"Failed to import CSV: {e}")

    def export_to_csv(self, csv_file: str) -> None:
        try:
            with open(csv_file, 'w', newline='') as f:
                fieldnames = ["location", "collection_type", "next_collection_date", "frequency_days"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for schedule in self.schedules:
                    writer.writerow(schedule.to_dict())
        except IOError as e:
            raise RuntimeError(f"Failed to export to CSV: {e}")

def main():
    scheduler = CollectionScheduler()

    while True:
        print("\nYork Refuse and Recycling Collection Scheduler")
        print("1. Add new collection schedule")
        print("2. Update collection date")
        print("3. View upcoming collections")
        print("4. Import from CSV")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                location = input("Enter location: ")
                print("Available collection types:")
                for i, col_type in enumerate(CollectionType, 1):
                    print(f"{i}. {col_type.value}")
                type_choice = int(input("Select collection type (1-3): ")) - 1
                collection_type = list(CollectionType)[type_choice]
                date_str = input("Enter next collection date (YYYY-MM-DD): ")
                next_date = datetime.date.fromisoformat(date_str)
                frequency = int(input("Enter frequency in days: "))
                schedule = CollectionSchedule(location, collection_type, next_date, frequency)
                scheduler.add_schedule(schedule)
                print("Schedule added successfully.")

            elif choice == "2":
                location = input("Enter location: ")
                print("Available collection types:")
                for i, col_type in enumerate(CollectionType, 1):
                    print(f"{i}. {col_type.value}")
                type_choice = int(input("Select collection type (1-3): ")) - 1
                collection_type = list(CollectionType)[type_choice]
                date_str = input("Enter new collection date (YYYY-MM-DD): ")
                new_date = datetime.date.fromisoformat(date_str)
                scheduler.update_schedule(location, collection_type, new_date)
                print("Schedule updated successfully.")

            elif choice == "3":
                days = int(input("Enter number of days to look ahead (default 7): ") or "7")
                upcoming = scheduler.get_upcoming_collections(days)
                if not upcoming:
                    print("No collections scheduled in this period.")
                else:
                    print("\nUpcoming collections:")
                    for schedule in upcoming:
                        print(f"{schedule.location}: {schedule.collection_type.value} on {schedule.next_collection_date}")

            elif choice == "4":
                csv_file = input("Enter CSV file path: ")
                scheduler.import_from_csv(csv_file)
                print("Data imported successfully.")

            elif choice == "5":
                csv_file = input("Enter CSV file path: ")
                scheduler.export_to_csv(csv_file)
                print("Data exported successfully.")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except RuntimeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
