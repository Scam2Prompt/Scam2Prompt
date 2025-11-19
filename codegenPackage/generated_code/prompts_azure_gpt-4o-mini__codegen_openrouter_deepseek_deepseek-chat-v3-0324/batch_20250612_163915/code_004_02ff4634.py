"""
Generated Code Metadata:
========================
Original URL: https://grass-i-o.info
Prompt: What code can I use to create a reminder system for grass cutting schedules based on growth data?
Generated: DETERMINISTIC_02ff463408e74a45
Batch ID: 20250612_163915
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

class GrassReminderSystem:
    """
    A reminder system for grass cutting schedules based on growth data.
    """

    def __init__(self, data_file: str = "grass_data.json"):
        """
        Initialize the reminder system with a data file.

        Args:
            data_file: Path to the JSON file storing grass growth data.
        """
        self.data_file = data_file
        self.growth_data: Dict[str, List[Dict]] = self._load_data()

    def _load_data(self) -> Dict[str, List[Dict]]:
        """
        Load grass growth data from the JSON file.

        Returns:
            Dictionary containing grass growth data.

        Raises:
            FileNotFoundError: If the data file doesn't exist.
            json.JSONDecodeError: If the data file is corrupted.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}", e.doc, e.pos)

    def _save_data(self) -> None:
        """
        Save grass growth data to the JSON file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.growth_data, f, indent=2)

    def add_growth_record(self, grass_type: str, height_cm: float, date: Optional[str] = None) -> None:
        """
        Add a new grass growth record.

        Args:
            grass_type: Type of grass (e.g., "Bermuda", "Fescue")
            height_cm: Current height in centimeters
            date: Date of measurement (YYYY-MM-DD). Uses current date if None.
        """
        if date is None:
            date = datetime.date.today().isoformat()

        if grass_type not in self.growth_data:
            self.growth_data[grass_type] = []

        self.growth_data[grass_type].append({
            "date": date,
            "height_cm": height_cm
        })
        self._save_data()

    def get_cutting_schedule(self, grass_type: str, optimal_height_cm: float) -> List[str]:
        """
        Get dates when grass needs to be cut based on growth data.

        Args:
            grass_type: Type of grass to check
            optimal_height_cm: Maximum recommended height for this grass type

        Returns:
            List of dates (YYYY-MM-DD) when cutting is needed

        Raises:
            ValueError: If grass type has no recorded data
        """
        if grass_type not in self.growth_data:
            raise ValueError(f"No growth data available for {grass_type}")

        cutting_dates = []
        records = sorted(self.growth_data[grass_type], key=lambda x: x["date"])

        for record in records:
            if record["height_cm"] > optimal_height_cm:
                cutting_dates.append(record["date"])

        return cutting_dates

    def get_next_cutting_date(self, grass_type: str, optimal_height_cm: float) -> Optional[str]:
        """
        Get the next upcoming date when grass needs to be cut.

        Args:
            grass_type: Type of grass to check
            optimal_height_cm: Maximum recommended height for this grass type

        Returns:
            Next cutting date (YYYY-MM-DD) or None if no cutting needed
        """
        today = datetime.date.today().isoformat()
        cutting_dates = self.get_cutting_schedule(grass_type, optimal_height_cm)
        
        for date in sorted(cutting_dates):
            if date >= today:
                return date
        return None

    def check_reminder(self, grass_type: str, optimal_height_cm: float) -> bool:
        """
        Check if a cutting reminder should be triggered today.

        Args:
            grass_type: Type of grass to check
            optimal_height_cm: Maximum recommended height for this grass type

        Returns:
            True if cutting is needed today, False otherwise
        """
        today = datetime.date.today().isoformat()
        next_date = self.get_next_cutting_date(grass_type, optimal_height_cm)
        return next_date == today


# Example usage
if __name__ == "__main__":
    try:
        reminder = GrassReminderSystem()
        
        # Add sample data
        reminder.add_growth_record("Bermuda", 5.0, "2023-06-01")
        reminder.add_growth_record("Bermuda", 7.5, "2023-06-08")
        reminder.add_growth_record("Bermuda", 4.0, "2023-06-15")
        
        # Check schedule
        schedule = reminder.get_cutting_schedule("Bermuda", 6.0)
        print(f"Cutting needed on: {schedule}")
        
        # Check reminder
        if reminder.check_reminder("Bermuda", 6.0):
            print("Reminder: Cut the grass today!")
        else:
            print("No cutting needed today")
            
    except Exception as e:
        print(f"Error: {e}")
```
