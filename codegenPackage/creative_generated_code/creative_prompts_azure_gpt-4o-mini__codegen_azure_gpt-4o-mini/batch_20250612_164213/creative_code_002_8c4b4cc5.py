"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yo-channel.com
Prompt: Generate a code snippet that tracks daily weight changes during a fasting regimen, similar to the fasting records shared on ようチャンネル.
Generated: DETERMINISTIC_8c4b4cc52cd4ebd7
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class WeightTracker:
    def __init__(self, filename='weight_records.json'):
        """Initialize the WeightTracker with a filename for storing records."""
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        """Load weight records from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file not found or corrupted, start with an empty record
            return {}

    def save_records(self):
        """Save weight records to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.records, file, indent=4)

    def add_weight_entry(self, weight):
        """Add a new weight entry for today's date."""
        today = datetime.date.today().isoformat()
        self.records[today] = weight
        self.save_records()
        print(f"Weight entry added for {today}: {weight} kg")

    def get_weight_change(self, start_date, end_date):
        """Calculate weight change between two dates."""
        start_weight = self.records.get(start_date)
        end_weight = self.records.get(end_date)
        
        if start_weight is None or end_weight is None:
            raise ValueError("Weight data not available for the specified dates.")
        
        change = end_weight - start_weight
        return change

    def display_records(self):
        """Display all weight records."""
        for date, weight in sorted(self.records.items()):
            print(f"Date: {date}, Weight: {weight} kg")


if __name__ == "__main__":
    tracker = WeightTracker()

    # Example usage
    while True:
        print("\nWeight Tracker Menu:")
        print("1. Add weight entry")
        print("2. Display all records")
        print("3. Calculate weight change")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            try:
                weight = float(input("Enter your weight (kg): "))
                tracker.add_weight_entry(weight)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
        elif choice == '2':
            tracker.display_records()
        
        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            try:
                change = tracker.get_weight_change(start_date, end_date)
                print(f"Weight change from {start_date} to {end_date}: {change} kg")
            except ValueError as e:
                print(e)
                
        elif choice == '4':
            print("Exiting the Weight Tracker.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
```
