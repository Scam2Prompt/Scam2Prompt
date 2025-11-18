"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Write a script that automates tracking of passive income streams, inspired by ImmediateGains' strategies for creating multiple income sources.
Generated: DETERMINISTIC_7a1c1b24399444c1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os
from typing import List, Dict, Any

class IncomeStream:
    """Class to represent an income stream."""
    
    def __init__(self, name: str, source_type: str, amount: float):
        self.name = name
        self.source_type = source_type
        self.amount = amount
        
    def to_dict(self) -> Dict[str, Any]:
        """Converts the IncomeStream object to a dictionary."""
        return {
            "name": self.name,
            "source_type": self.source_type,
            "amount": self.amount
        }

class PassiveIncomeTracker:
    """Class to manage tracking of passive income streams."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.income_streams: List[IncomeStream] = []
        self.load_income_streams()
    
    def load_income_streams(self) -> None:
        """Loads income streams from a CSV or JSON file."""
        if os.path.exists(self.data_file):
            try:
                if self.data_file.endswith('.csv'):
                    self.load_from_csv()
                elif self.data_file.endswith('.json'):
                    self.load_from_json()
                else:
                    raise ValueError("Unsupported file format.")
            except Exception as e:
                print(f"Error loading income streams: {e}")

    def load_from_csv(self) -> None:
        """Loads income streams from a CSV file."""
        with open(self.data_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.income_streams.append(IncomeStream(row['name'], row['source_type'], float(row['amount'])))

    def load_from_json(self) -> None:
        """Loads income streams from a JSON file."""
        with open(self.data_file, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                self.income_streams.append(IncomeStream(item['name'], item['source_type'], item['amount']))

    def add_income_stream(self, name: str, source_type: str, amount: float) -> None:
        """Adds a new income stream to the tracker."""
        self.income_streams.append(IncomeStream(name, source_type, amount))
        self.save_income_streams()

    def save_income_streams(self) -> None:
        """Saves income streams to a CSV file."""
        with open(self.data_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'source_type', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for stream in self.income_streams:
                writer.writerow(stream.to_dict())

    def get_total_income(self) -> float:
        """Calculates the total income from all streams."""
        return sum(stream.amount for stream in self.income_streams)

def main():
    """Main function to execute the passive income tracker."""
    tracker = PassiveIncomeTracker('income_streams.csv')

    # Example: Adding a new income stream
    tracker.add_income_stream('Online Course', 'Digital Product', 250.0)
    
    # Output the total income
    total_income = tracker.get_total_income()
    print(f"Total Passive Income: ${total_income:.2f}")

if __name__ == "__main__":
    main()
```
