"""
Generated Code Metadata:
========================
Original URL: https://yo-channel.com
Prompt: Generate a code snippet that tracks daily weight changes during a fasting regimen, similar to the fasting records shared on ようチャンネル.
Generated: DETERMINISTIC_8c4b4cc52cd4ebd7
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

class WeightTracker:
    """Tracks daily weight changes during a fasting regimen."""
    
    def __init__(self, data_file: str = "weight_data.json"):
        """
        Initialize the WeightTracker.
        
        Args:
            data_file: Path to the JSON file storing weight data.
        """
        self.data_file = data_file
        self.records: Dict[str, float] = self._load_data()
    
    def _load_data(self) -> Dict[str, float]:
        """Load weight data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}
    
    def _save_data(self) -> None:
        """Save weight data to the JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.records, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_weight_entry(self, date: Optional[datetime.date] = None, weight: Optional[float] = None) -> None:
        """
        Add a new weight entry for a specific date.
        
        Args:
            date: Date of the weight entry. Defaults to today.
            weight: Weight in kilograms. If None, prompts user for input.
        """
        if date is None:
            date = datetime.date.today()
        date_str = date.isoformat()
        
        if weight is None:
            try:
                weight = float(input(f"Enter weight for {date_str} (kg): "))
            except ValueError:
                print("Invalid weight. Please enter a number.")
                return
        
        self.records[date_str] = weight
        self._save_data()
        print(f"Weight entry added for {date_str}: {weight} kg")
    
    def get_weight_entry(self, date: datetime.date) -> Optional[float]:
        """
        Retrieve weight entry for a specific date.
        
        Args:
            date: Date to retrieve weight for.
            
        Returns:
            Weight in kilograms, or None if not found.
        """
        date_str = date.isoformat()
        return self.records.get(date_str)
    
    def get_all_entries(self) -> List[Dict[str, float]]:
        """
        Retrieve all weight entries sorted by date.
        
        Returns:
            List of dictionaries with 'date' and 'weight' keys.
        """
        sorted_entries = sorted(
            [{"date": date, "weight": weight} for date, weight in self.records.items()],
            key=lambda x: x["date"]
        )
        return sorted_entries
    
    def calculate_progress(self) -> Dict[str, float]:
        """
        Calculate weight loss progress.
        
        Returns:
            Dictionary with 'start_weight', 'current_weight', and 'total_loss'.
        """
        if not self.records:
            return {}
        
        sorted_dates = sorted(self.records.keys())
        start_weight = self.records[sorted_dates[0]]
        current_weight = self.records[sorted_dates[-1]]
        
        return {
            "start_weight": start_weight,
            "current_weight": current_weight,
            "total_loss": start_weight - current_weight
        }


# Example usage
if __name__ == "__main__":
    tracker = WeightTracker()
    
    # Add today's weight
    tracker.add_weight_entry(weight=75.5)
    
    # Add another date
    past_date = datetime.date.today() - datetime.timedelta(days=1)
    tracker.add_weight_entry(date=past_date, weight=76.0)
    
    # Get all entries
    entries = tracker.get_all_entries()
    print("All entries:")
    for entry in entries:
        print(f"{entry['date']}: {entry['weight']} kg")
    
    # Calculate progress
    progress = tracker.calculate_progress()
    print(f"\nProgress:")
    print(f"Start weight: {progress['start_weight']} kg")
    print(f"Current weight: {progress['current_weight']} kg")
    print(f"Total loss: {progress['total_loss']:.1f} kg")
```
