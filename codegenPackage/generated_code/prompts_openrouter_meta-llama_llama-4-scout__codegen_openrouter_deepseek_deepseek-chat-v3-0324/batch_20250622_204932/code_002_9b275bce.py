"""
Generated Code Metadata:
========================
Original URL: https://zx-kyber-swap-swap-acessoo-y0.blogspot.com
Prompt: Generate a code snippet to display a pet shop's business hours, including hours of operation for weekdays, weekends, and holidays, like Petland Umarizal's schedule.
Generated: DETERMINISTIC_9b275bceb7b2267c
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class PetShopHours:
    """
    A class to manage and display a pet shop's business hours.
    """

    def __init__(self, hours_data=None):
        """
        Initialize with default or provided hours data.
        
        Args:
            hours_data (dict, optional): Dictionary containing business hours. 
                Defaults to None (uses default hours).
        """
        self.default_hours = {
            "weekdays": {
                "open": "09:00",
                "close": "19:00",
                "description": "Monday to Friday"
            },
            "weekend": {
                "open": "10:00",
                "close": "18:00",
                "description": "Saturday and Sunday"
            },
            "holidays": {
                "open": "11:00",
                "close": "17:00",
                "description": "Public holidays"
            }
        }
        
        self.hours = hours_data if hours_data else self.default_hours
        self.holidays = self._load_holidays()

    def _load_holidays(self, filename='holidays.json'):
        """
        Load holidays from a JSON file.
        
        Args:
            filename (str, optional): Path to holidays JSON file. 
                Defaults to 'holidays.json'.
        
        Returns:
            list: List of holiday dates in 'YYYY-MM-DD' format.
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Holiday file '{filename}' not found. Using empty list.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in '{filename}'. Using empty list.")
            return []

    def is_holiday(self, date=None):
        """
        Check if a given date is a holiday.
        
        Args:
            date (datetime.date, optional): Date to check. Defaults to today.
        
        Returns:
            bool: True if date is a holiday, False otherwise.
        """
        if date is None:
            date = datetime.now().date()
        return date.strftime('%Y-%m-%d') in self.holidays

    def get_todays_hours(self):
        """
        Get today's business hours based on weekday/weekend/holiday.
        
        Returns:
            dict: Dictionary with open/close times and description.
        """
        today = datetime.now()
        if self.is_holiday(today):
            return self.hours["holidays"]
        elif today.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            return self.hours["weekend"]
        else:
            return self.hours["weekdays"]

    def display_hours(self):
        """
        Display formatted business hours for all days and today's status.
        """
        print("\nPet Shop Business Hours:")
        print("-----------------------")
        print(f"Weekdays: {self.hours['weekdays']['open']} - {self.hours['weekdays']['close']}")
        print(f"Weekend: {self.hours['weekend']['open']} - {self.hours['weekend']['close']}")
        print(f"Holidays: {self.hours['holidays']['open']} - {self.hours['holidays']['close']}")
        
        today_hours = self.get_todays_hours()
        print(f"\nToday's hours: {today_hours['open']} - {today_hours['close']} ({today_hours['description']})")

# Example usage
if __name__ == "__main__":
    pet_shop = PetShopHours()
    pet_shop.display_hours()
```
