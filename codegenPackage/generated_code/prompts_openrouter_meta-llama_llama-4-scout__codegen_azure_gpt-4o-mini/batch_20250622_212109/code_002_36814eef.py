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
from typing import List, Optional

class Museum:
    def __init__(self, name: str, opening_hours: dict):
        """
        Initializes the Museum with a name and opening hours.

        :param name: The name of the museum.
        :param opening_hours: A dictionary with days of the week as keys and opening hours as values.
        """
        self.name = name
        self.opening_hours = opening_hours  # e.g., {'Monday': '10:00-18:00', 'Tuesday': '10:00-18:00', ...}
        self.reservations = []  # List to store reservations

    def is_open(self, visit_date: datetime) -> bool:
        """
        Checks if the museum is open on a given date.

        :param visit_date: The date of the visit.
        :return: True if the museum is open, False otherwise.
        """
        day_name = visit_date.strftime('%A')
        if day_name in self.opening_hours:
            return True
        return False

    def book_visit(self, visitor_name: str, visit_date: datetime) -> Optional[str]:
        """
        Books a visit for a visitor on a specific date.

        :param visitor_name: The name of the visitor.
        :param visit_date: The date of the visit.
        :return: Confirmation message or error message.
        """
        if not self.is_open(visit_date):
            return f"Error: The museum is closed on {visit_date.strftime('%A')}."

        reservation = {
            'visitor_name': visitor_name,
            'visit_date': visit_date
        }
        self.reservations.append(reservation)
        return f"Reservation confirmed for {visitor_name} on {visit_date.strftime('%Y-%m-%d')}."

    def get_reservations(self) -> List[dict]:
        """
        Returns a list of all reservations.

        :return: List of reservations.
        """
        return self.reservations

# Example usage
if __name__ == "__main__":
    # Define opening hours for the museum
    opening_hours = {
        'Monday': '10:00-18:00',
        'Tuesday': '10:00-18:00',
        'Wednesday': '10:00-18:00',
        'Thursday': '10:00-18:00',
        'Friday': '10:00-18:00',
        'Saturday': '10:00-20:00',
        'Sunday': 'Closed'
    }

    # Create a museum instance
    museum = Museum("Museo Vasca Votiva di Noceto", opening_hours)

    # Attempt to book a visit
    visit_date = datetime(2023, 10, 15)  # Example date
    visitor_name = "John Doe"
    confirmation = museum.book_visit(visitor_name, visit_date)
    print(confirmation)

    # Print all reservations
    print("Current Reservations:", museum.get_reservations())
```
