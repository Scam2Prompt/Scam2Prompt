"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Generate a code snippet to implement a booking system for museum visits, considering the need for optional reservations and variable opening hours, as seen on the Museo Vasca Votiva di Noceto website.
Generated: DETERMINISTIC_36814eef951c3810
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Optional

class Museum:
    def __init__(self, name: str, opening_hours: dict):
        """
        Initialize a Museum object.

        Args:
        - name (str): The name of the museum.
        - opening_hours (dict): A dictionary with day of the week as key and a tuple of opening and closing hours as value.
        """
        self.name = name
        self.opening_hours = opening_hours
        self.visits = []

    def is_open(self, date: datetime) -> bool:
        """
        Check if the museum is open on a given date.

        Args:
        - date (datetime): The date to check.

        Returns:
        - bool: True if the museum is open, False otherwise.
        """
        day_of_week = date.strftime("%A").lower()
        if day_of_week not in self.opening_hours:
            return False
        opening, closing = self.opening_hours[day_of_week]
        return opening <= date.hour < closing

    def book_visit(self, date: datetime, visitor_name: str, optional_reservation: Optional[str] = None) -> str:
        """
        Book a visit to the museum.

        Args:
        - date (datetime): The date of the visit.
        - visitor_name (str): The name of the visitor.
        - optional_reservation (str, optional): Optional reservation details. Defaults to None.

        Returns:
        - str: A unique booking reference.

        Raises:
        - ValueError: If the museum is not open on the given date.
        """
        if not self.is_open(date):
            raise ValueError("Museum is not open on this date and time.")
        
        booking_ref = f"{visitor_name}_{date.strftime('%Y%m%d%H%M%S')}"
        self.visits.append({
            "booking_ref": booking_ref,
            "date": date,
            "visitor_name": visitor_name,
            "optional_reservation": optional_reservation
        })
        return booking_ref

    def cancel_visit(self, booking_ref: str) -> bool:
        """
        Cancel a booked visit.

        Args:
        - booking_ref (str): The booking reference of the visit to cancel.

        Returns:
        - bool: True if the visit was cancelled, False if not found.
        """
        for visit in self.visits:
            if visit["booking_ref"] == booking_ref:
                self.visits.remove(visit)
                return True
        return False


class MuseumBookingSystem:
    def __init__(self):
        self.museums = {}

    def add_museum(self, museum: Museum):
        """
        Add a museum to the booking system.

        Args:
        - museum (Museum): The museum to add.
        """
        self.museums[museum.name] = museum

    def book_visit(self, museum_name: str, date: datetime, visitor_name: str, optional_reservation: Optional[str] = None) -> str:
        """
        Book a visit to a museum.

        Args:
        - museum_name (str): The name of the museum.
        - date (datetime): The date of the visit.
        - visitor_name (str): The name of the visitor.
        - optional_reservation (str, optional): Optional reservation details. Defaults to None.

        Returns:
        - str: A unique booking reference.

        Raises:
        - ValueError: If the museum does not exist or is not open on the given date.
        """
        if museum_name not in self.museums:
            raise ValueError("Museum does not exist.")
        return self.museums[museum_name].book_visit(date, visitor_name, optional_reservation)


def main():
    # Example usage
    museum = Museum(
        "Museo Vasca Votiva di Noceto",
        {
            "monday": (9, 17),
            "tuesday": (9, 17),
            "wednesday": (9, 17),
            "thursday": (9, 17),
            "friday": (9, 17),
            "saturday": (10, 18),
            "sunday": (10, 18)
        }
    )

    booking_system = MuseumBookingSystem()
    booking_system.add_museum(museum)

    try:
        visit_date = datetime.now() + timedelta(days=1)
        visit_date = visit_date.replace(hour=10, minute=0, second=0)  # Set to 10:00
        booking_ref = booking_system.book_visit(
            "Museo Vasca Votiva di Noceto",
            visit_date,
            "John Doe",
            "Optional reservation details"
        )
        print(f"Booking reference: {booking_ref}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
