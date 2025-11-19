"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Develop a script to manage restaurant opening times and ensure customers can only make reservations during specified hours.
Generated: DETERMINISTIC_bc4665d0dc446a5b
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, time

class Restaurant:
    def __init__(self, name, opening_time, closing_time):
        """
        Initialize the Restaurant with a name and opening/closing times.

        :param name: str - The name of the restaurant
        :param opening_time: str - The opening time in 'HH:MM' format
        :param closing_time: str - The closing time in 'HH:MM' format
        """
        self.name = name
        self.opening_time = self._parse_time(opening_time)
        self.closing_time = self._parse_time(closing_time)

    def _parse_time(self, time_str):
        """
        Parse a time string into a datetime.time object.

        :param time_str: str - Time in 'HH:MM' format
        :return: datetime.time - Parsed time object
        """
        try:
            return datetime.strptime(time_str, '%H:%M').time()
        except ValueError:
            raise ValueError(f"Invalid time format: {time_str}. Use 'HH:MM' format.")

    def is_open(self, reservation_time):
        """
        Check if the restaurant is open at the given reservation time.

        :param reservation_time: str - Reservation time in 'HH:MM' format
        :return: bool - True if the restaurant is open, False otherwise
        """
        reservation_time_obj = self._parse_time(reservation_time)
        return self.opening_time <= reservation_time_obj <= self.closing_time

    def make_reservation(self, reservation_time):
        """
        Attempt to make a reservation at the specified time.

        :param reservation_time: str - Reservation time in 'HH:MM' format
        :return: str - Confirmation message or error message
        """
        if self.is_open(reservation_time):
            return f"Reservation confirmed at {reservation_time} for {self.name}."
        else:
            return f"Sorry, {self.name} is closed at {reservation_time}. Please choose a time between {self.opening_time} and {self.closing_time}."

# Example usage
if __name__ == "__main__":
    # Create a restaurant instance
    my_restaurant = Restaurant("The Gourmet Kitchen", "09:00", "22:00")

    # Test making reservations
    print(my_restaurant.make_reservation("10:30"))  # Should confirm
    print(my_restaurant.make_reservation("08:00"))   # Should be closed
    print(my_restaurant.make_reservation("22:30"))   # Should be closed
```
