"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Create a basic Python script to track and manage successful real estate ventures, similar to Alghanim Capital's experience in identifying and executing high-potential opportunities."
Generated: DETERMINISTIC_b96b5b41e4ba85e9
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Real Estate Venture Tracker
A script to track and manage successful real estate ventures with features to:
- Add new ventures
- Update venture status
- Generate reports
- Calculate ROI
"""

import csv
import datetime
import os
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Venture:
    """Class representing a real estate venture."""
    name: str
    location: str
    acquisition_date: str
    acquisition_cost: float
    current_value: float
    status: str = "Active"  # Active, Sold, Under Review
    sale_date: Optional[str] = None
    sale_price: Optional[float] = None
    notes: List[str] = field(default_factory=list)

    def roi(self) -> float:
        """Calculate Return on Investment."""
        if self.sale_price:
            return ((self.sale_price - self.acquisition_cost) / self.acquisition_cost) * 100
        return ((self.current_value - self.acquisition_cost) / self.acquisition_cost) * 100

    def days_held(self) -> int:
        """Calculate number of days the property has been held."""
        if self.sale_date:
            end_date = datetime.datetime.strptime(self.sale_date, "%Y-%m-%d").date()
        else:
            end_date = datetime.date.today()
        
        start_date = datetime.datetime.strptime(self.acquisition_date, "%Y-%m-%d").date()
        return (end_date - start_date).days


class VentureTracker:
    """Main class to manage real estate ventures."""
    
    def __init__(self, data_file: str = "ventures.csv"):
        self.data_file = data_file
        self.ventures: List[Venture] = []
        self._load_data()

    def _load_data(self) -> None:
        """Load venture data from CSV file."""
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.ventures.append(Venture(
                    name=row['name'],
                    location=row['location'],
                    acquisition_date=row['acquisition_date'],
                    acquisition_cost=float(row['acquisition_cost']),
                    current_value=float(row['current_value']),
                    status=row['status'],
                    sale_date=row['sale_date'] if row['sale_date'] else None,
                    sale_price=float(row['sale_price']) if row['sale_price'] else None,
                    notes=row['notes'].split('|') if row['notes'] else []
                ))

    def _save_data(self) -> None:
        """Save venture data to CSV file."""
        with open(self.data_file, mode='w', newline='') as file:
            fieldnames = [
                'name', 'location', 'acquisition_date', 'acquisition_cost',
                'current_value', 'status', 'sale_date', 'sale_price', 'notes'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for venture in self.ventures:
                writer.writerow({
                    'name': venture.name,
                    'location': venture.location,
                    'acquisition_date': venture.acquisition_date,
                    'acquisition_cost': venture.acquisition_cost,
                    'current_value': venture.current_value,
                    'status': venture.status,
                    'sale_date': venture.sale_date if venture.sale_date else '',
                    'sale_price': venture.sale_price if venture.sale_price else '',
                    'notes': '|'.join(venture.notes) if venture.notes else ''
                })

    def add_venture(self, venture: Venture) -> None:
        """Add a new venture to the tracker."""
        self.ventures.append(venture)
        self._save_data()

    def update_venture(self, name: str, **kwargs) -> None:
        """Update an existing venture's properties."""
        for venture in self.ventures:
            if venture.name == name:
                for key, value in kwargs.items():
                    if hasattr(venture, key):
                        setattr(venture, key, value)
                self._save_data()
                return
        raise ValueError(f"Venture '{name}' not found")

    def get_venture(self, name: str) -> Venture:
        """Get a venture by name."""
        for venture in self.ventures:
            if venture.name == name:
                return venture
        raise ValueError(f"Venture '{name}' not found")

    def generate_report(self) -> str:
        """Generate a summary report of all ventures."""
        report = []
        report.append("Real Estate Ventures Report")
        report.append("=" * 40)
        report.append(f"Total Ventures: {len(self.ventures)}")
        
        active = sum(1 for v in self.ventures if v.status == "Active")
        sold = sum(1 for v in self.ventures if v.status == "Sold")
        
        report.append(f"Active: {active} | Sold: {sold}")
        report.append("\nTop Performing Ventures:")
        
        # Sort by ROI descending
        sorted_ventures = sorted(
            self.ventures,
            key=lambda v: v.roi(),
            reverse=True
        )
        
        for venture in sorted_ventures[:5]:
            report.append(
                f"{venture.name}: ROI {venture.roi():.2f}% | "
                f"Days Held: {venture.days_held()}"
            )
            
        return "\n".join(report)

    def add_note(self, venture_name: str, note: str) -> None:
        """Add a note to a venture."""
        venture = self.get_venture(venture_name)
        venture.notes.append(f"{datetime.date.today()}: {note}")
        self._save_data()


def main():
    """Main function to demonstrate the VentureTracker."""
    tracker = VentureTracker()
    
    while True:
        print("\nReal Estate Venture Tracker")
        print("1. Add New Venture")
        print("2. Update Venture")
        print("3. View Venture Details")
        print("4. Generate Report")
        print("5. Add Note to Venture")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                print("\nAdd New Venture")
                name = input("Venture Name: ")
                location = input("Location: ")
                acquisition_date = input("Acquisition Date (YYYY-MM-DD): ")
                acquisition_cost = float(input("Acquisition Cost: "))
                current_value = float(input("Current Value: "))
                
                venture = Venture(
                    name=name,
                    location=location,
                    acquisition_date=acquisition_date,
                    acquisition_cost=acquisition_cost,
                    current_value=current_value
                )
                tracker.add_venture(venture)
                print("Venture added successfully!")
                
            elif choice == "2":
                name = input("Enter venture name to update: ")
                print("Leave blank to keep current value")
                
                updates = {}
                location = input(f"New Location [{tracker.get_venture(name).location}]: ")
                if location: updates['location'] = location
                
                current_value = input(f"New Current Value [{tracker.get_venture(name).current_value}]: ")
                if current_value: updates['current_value'] = float(current_value)
                
                status = input(f"New Status [{tracker.get_venture(name).status}]: ")
                if status: updates['status'] = status
                
                if status == "Sold":
                    sale_date = input("Sale Date (YYYY-MM-DD): ")
                    sale_price = input("Sale Price: ")
                    if sale_date: updates['sale_date'] = sale_date
                    if sale_price: updates['sale_price'] = float(sale_price)
                
                if updates:
                    tracker.update_venture(name, **updates)
                    print("Venture updated successfully!")
                else:
                    print("No updates made.")
                    
            elif choice == "3":
                name = input("Enter venture name to view: ")
                venture = tracker.get_venture(name)
                print("\nVenture Details:")
                print(f"Name: {venture.name}")
                print(f"Location: {venture.location}")
                print(f"Acquisition Date: {venture.acquisition_date}")
                print(f"Acquisition Cost: ${venture.acquisition_cost:,.2f}")
                print(f"Current Value: ${venture.current_value:,.2f}")
                print(f"ROI: {venture.roi():.2f}%")
                print(f"Days Held: {venture.days_held()}")
                print(f"Status: {venture.status}")
                if venture.sale_date:
                    print(f"Sale Date: {venture.sale_date}")
                    print(f"Sale Price: ${venture.sale_price:,.2f}")
                print("Notes:")
                for note in venture.notes:
                    print(f"- {note}")
                    
            elif choice == "4":
                print(tracker.generate_report())
                
            elif choice == "5":
                name = input("Enter venture name to add note: ")
                note = input("Enter note: ")
                tracker.add_note(name, note)
