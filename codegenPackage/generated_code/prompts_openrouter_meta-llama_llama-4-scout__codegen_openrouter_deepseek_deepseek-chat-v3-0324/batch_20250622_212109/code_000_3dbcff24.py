"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Write a Python script to create a simple museum information system, including opening hours and ticket prices, for a museum like Museo Vasca Votiva di Noceto.
Generated: DETERMINISTIC_3dbcff24a700b55c
Batch ID: 20250622_212109
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
from typing import Dict, List, Optional

class MuseumInfoSystem:
    """
    A simple museum information system to manage opening hours and ticket prices.
    """

    def __init__(self, museum_name: str):
        """
        Initialize the museum information system.

        Args:
            museum_name (str): Name of the museum
        """
        self.museum_name = museum_name
        self.opening_hours: Dict[str, List[str]] = {}
        self.ticket_prices: Dict[str, float] = {}
        self.special_days: Dict[str, Dict[str, str]] = {}

    def add_opening_hours(self, day: str, opening_time: str, closing_time: str) -> None:
        """
        Add opening hours for a specific day.

        Args:
            day (str): Day of the week (e.g., "Monday")
            opening_time (str): Opening time in HH:MM format
            closing_time (str): Closing time in HH:MM format
        """
        if not self._validate_time_format(opening_time) or not self._validate_time_format(closing_time):
            raise ValueError("Time must be in HH:MM format")
        
        self.opening_hours[day.lower()] = [opening_time, closing_time]

    def add_ticket_price(self, ticket_type: str, price: float) -> None:
        """
        Add ticket price for a specific ticket type.

        Args:
            ticket_type (str): Type of ticket (e.g., "Adult", "Child")
            price (float): Price of the ticket
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.ticket_prices[ticket_type.lower()] = price

    def add_special_day(self, date: str, opening_time: str, closing_time: str, description: str) -> None:
        """
        Add special opening hours for a specific date.

        Args:
            date (str): Date in YYYY-MM-DD format
            opening_time (str): Opening time in HH:MM format
            closing_time (str): Closing time in HH:MM format
            description (str): Description of the special day
        """
        if not self._validate_date_format(date):
            raise ValueError("Date must be in YYYY-MM-DD format")
        if not self._validate_time_format(opening_time) or not self._validate_time_format(closing_time):
            raise ValueError("Time must be in HH:MM format")

        self.special_days[date] = {
            "opening_time": opening_time,
            "closing_time": closing_time,
            "description": description
        }

    def get_opening_hours(self, date: Optional[str] = None) -> Dict[str, str]:
        """
        Get opening hours for a specific date or regular schedule.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to None.

        Returns:
            Dict[str, str]: Dictionary with opening hours and description if special day
        """
        if date:
            if not self._validate_date_format(date):
                raise ValueError("Date must be in YYYY-MM-DD format")
            
            if date in self.special_days:
                return {
                    "opening_time": self.special_days[date]["opening_time"],
                    "closing_time": self.special_days[date]["closing_time"],
                    "description": self.special_days[date]["description"],
                    "is_special_day": True
                }
            
            day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%A").lower()
        else:
            day_of_week = datetime.now().strftime("%A").lower()

        if day_of_week in self.opening_hours:
            return {
                "opening_time": self.opening_hours[day_of_week][0],
                "closing_time": self.opening_hours[day_of_week][1],
                "is_special_day": False
            }
        return {"message": "Closed"}

    def get_ticket_price(self, ticket_type: str) -> float:
        """
        Get ticket price for a specific ticket type.

        Args:
            ticket_type (str): Type of ticket

        Returns:
            float: Price of the ticket
        """
        return self.ticket_prices.get(ticket_type.lower(), 0.0)

    def save_to_file(self, filename: str) -> None:
        """
        Save museum information to a JSON file.

        Args:
            filename (str): Name of the file to save to
        """
        data = {
            "museum_name": self.museum_name,
            "opening_hours": self.opening_hours,
            "ticket_prices": self.ticket_prices,
            "special_days": self.special_days
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'MuseumInfoSystem':
        """
        Load museum information from a JSON file.

        Args:
            filename (str): Name of the file to load from

        Returns:
            MuseumInfoSystem: Loaded museum information system
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        museum = cls(data["museum_name"])
        museum.opening_hours = {k.lower(): v for k, v in data.get("opening_hours", {}).items()}
        museum.ticket_prices = {k.lower(): v for k, v in data.get("ticket_prices", {}).items()}
        museum.special_days = data.get("special_days", {})
        return museum

    def _validate_time_format(self, time_str: str) -> bool:
        """Validate time format (HH:MM)."""
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def _validate_date_format(self, date_str: str) -> bool:
        """Validate date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# Example usage
if __name__ == "__main__":
    # Create a new museum system
    museum = MuseumInfoSystem("Museo Vasca Votiva di Noceto")

    # Add regular opening hours
    museum.add_opening_hours("Monday", "09:00", "18:00")
    museum.add_opening_hours("Tuesday", "09:00", "18:00")
    museum.add_opening_hours("Wednesday", "09:00", "18:00")
    museum.add_opening_hours("Thursday", "09:00", "18:00")
    museum.add_opening_hours("Friday", "09:00", "18:00")
    museum.add_opening_hours("Saturday", "10:00", "20:00")
    museum.add_opening_hours("Sunday", "10:00", "20:00")

    # Add ticket prices
    museum.add_ticket_price("Adult", 10.0)
    museum.add_ticket_price("Child", 5.0)
    museum.add_ticket_price("Senior", 7.0)
    museum.add_ticket_price("Student", 8.0)

    # Add special day
    museum.add_special_day("2023-12-25", "10:00", "14:00", "Christmas Day")

    # Save to file
    museum.save_to_file("museum_data.json")

    # Load from file
    loaded_museum = MuseumInfoSystem.load_from_file("museum_data.json")

    # Get information
    print(f"Museum: {loaded_museum.museum_name}")
    print("Today's opening hours:", loaded_museum.get_opening_hours())
    print("Christmas Day hours:", loaded_museum.get_opening_hours("2023-12-25"))
    print("Adult ticket price:", loaded_museum.get_ticket_price("Adult"))
```
