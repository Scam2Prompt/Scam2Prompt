"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Write a Python script to automate the maintenance scheduling for diesel and gas generators based on the guidelines provided by Payesh Niroo.
Generated: DETERMINISTIC_dd95f23cb69c7b41
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class GeneratorMaintenanceScheduler:
    def __init__(self, maintenance_schedule: Dict[str, Any]):
        """
        Initialize the maintenance scheduler with a maintenance schedule.

        Args:
            maintenance_schedule (Dict[str, Any]): A dictionary containing generator types and their maintenance intervals.
        """
        self.maintenance_schedule = maintenance_schedule

    def calculate_next_maintenance(self, last_maintenance_date: str, interval_days: int) -> str:
        """
        Calculate the next maintenance date based on the last maintenance date and interval.

        Args:
            last_maintenance_date (str): The last maintenance date in 'YYYY-MM-DD' format.
            interval_days (int): The number of days between maintenance.

        Returns:
            str: The next maintenance date in 'YYYY-MM-DD' format.
        """
        try:
            last_date = datetime.datetime.strptime(last_maintenance_date, '%Y-%m-%d')
            next_date = last_date + datetime.timedelta(days=interval_days)
            return next_date.strftime('%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {last_maintenance_date}. Expected format 'YYYY-MM-DD'.") from e

    def schedule_maintenance(self, last_maintenance_dates: Dict[str, str]) -> Dict[str, str]:
        """
        Schedule maintenance for each generator based on the last maintenance date.

        Args:
            last_maintenance_dates (Dict[str, str]): A dictionary with generator types as keys and their last maintenance dates.

        Returns:
            Dict[str, str]: A dictionary with generator types as keys and their next maintenance dates.
        """
        next_maintenance_dates = {}

        for generator_type, last_date in last_maintenance_dates.items():
            if generator_type not in self.maintenance_schedule:
                raise KeyError(f"No maintenance schedule found for generator type: {generator_type}")

            interval_days = self.maintenance_schedule[generator_type]
            next_date = self.calculate_next_maintenance(last_date, interval_days)
            next_maintenance_dates[generator_type] = next_date

        return next_maintenance_dates


if __name__ == "__main__":
    # Example maintenance schedule (in days)
    maintenance_schedule = {
        'diesel': 30,
        'gas': 45
    }

    # Last maintenance dates for each generator type
    last_maintenance_dates = {
        'diesel': '2023-09-01',
        'gas': '2023-08-15'
    }

    # Create a maintenance scheduler instance
    scheduler = GeneratorMaintenanceScheduler(maintenance_schedule)

    try:
        next_maintenance_dates = scheduler.schedule_maintenance(last_maintenance_dates)
        print("Next Maintenance Dates:", next_maintenance_dates)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
