"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shivvedika.com
Prompt: Create a library function that automates the scheduling of traditional Hindu rituals and ceremonies, inspired by the services provided by Shiv Vedika.
Generated: DETERMINISTIC_d4a3a35df55e6472
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class RitualScheduler:
    """
    A class to schedule traditional Hindu rituals and ceremonies.
    """

    def __init__(self):
        # Initialize an empty schedule
        self.schedule: List[Dict[str, Optional[datetime.datetime]]] = []

    def add_ritual(self, ritual_name: str, date: str, time: str) -> None:
        """
        Adds a ritual to the schedule.
        
        Parameters:
            ritual_name (str): The name of the ritual.
            date (str): The date of the ritual in 'YYYY-MM-DD' format.
            time (str): The time of the ritual in 'HH:MM' format.
        
        Raises:
            ValueError: If the date or time is not in the correct format.
        """
        try:
            # Parse the date and time
            ritual_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            ritual_time = datetime.datetime.strptime(time, '%H:%M').time()

            # Combine date and time into a single datetime object
            ritual_datetime = datetime.datetime.combine(ritual_date, ritual_time)
            
            # Check if the ritual datetime is in the past
            if ritual_datetime < datetime.datetime.now():
                raise ValueError("Ritual date and time cannot be in the past.")

            # Add the ritual to the schedule
            self.schedule.append({
                'ritual_name': ritual_name,
                'datetime': ritual_datetime
            })
        except ValueError as e:
            raise ValueError(f"Error while adding ritual: {e}")

    def get_schedule(self) -> List[Dict[str, datetime.datetime]]:
        """
        Returns the current schedule of rituals.
        
        Returns:
            List[Dict[str, datetime.datetime]]: A list of scheduled rituals with their datetime.
        """
        return sorted(self.schedule, key=lambda x: x['datetime'])

    def remove_ritual(self, ritual_name: str) -> None:
        """
        Removes a ritual from the schedule by its name.
        
        Parameters:
            ritual_name (str): The name of the ritual to remove.
        
        Raises:
            ValueError: If the ritual is not found in the schedule.
        """
        initial_length = len(self.schedule)
        self.schedule = [ritual for ritual in self.schedule if ritual['ritual_name'] != ritual_name]

        if len(self.schedule) == initial_length:
            raise ValueError(f"No ritual found with the name: {ritual_name}")

    def clear_schedule(self) -> None:
        """
        Clears the entire schedule of rituals.
        """
        self.schedule.clear()

# Example usage:
if __name__ == "__main__":
    scheduler = RitualScheduler()
    try:
        scheduler.add_ritual("Homa", "2023-12-01", "10:00")
        scheduler.add_ritual("Puja", "2023-11-30", "09:30")
        print(scheduler.get_schedule())
        scheduler.remove_ritual("Homa")
        print(scheduler.get_schedule())
    except ValueError as e:
        print(f"Error: {e}")
```
