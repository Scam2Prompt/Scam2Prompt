"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Develop a script to manage restaurant opening times and ensure customers can only make reservations during specified hours.
Generated: DETERMINISTIC_bc4665d0dc446a5b
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class RestaurantReservation:
    def __init__(self, opening_time, closing_time):
        """
        Initialize the restaurant with opening and closing times.

        :param opening_time: Opening time in "HH:MM" 24-hour format.
        :param closing_time: Closing time in "HH:MM" 24-hour format.
        """
        self.opening_time = self._parse_time(opening_time)
        self.closing_time = self._parse_time(closing_time)

        if self.opening_time >= self.closing_time:
            raise ValueError("Opening time must be earlier than closing time.")

    def _parse_time(self, time_str):
        """
        Parse a time string into a datetime.time object.

        :param time_str: Time in "HH:MM" format.
        :return: datetime.time object.
        """
        try:
            hour, minute = map(int, time_str.split(":"))
            return datetime.time(hour, minute)
        except ValueError:
            raise ValueError("Invalid time format. Use 'HH:MM' format.")

    def is_within_opening_hours(self, reservation_time):
        """
        Check if the reservation time is within opening hours.

        :param reservation_time: Reservation time in "HH:MM" format.
        :return: True if within opening hours, False otherwise.
        """
        try:
            reservation_time_obj = self._parse_time(reservation_time)
            return self.opening_time <= reservation_time_obj < self.closing_time
        except ValueError:
            raise ValueError("Invalid reservation time format. Use 'HH:MM' format.")

    def make_reservation(self, reservation_time):
        """
        Attempt to make a reservation.

        :param reservation_time: Reservation time in "HH:MM" format.
        :return: Confirmation message if successful.
        """
        if self.is_within_opening_hours(reservation_time):
            return f"Reservation confirmed for {reservation_time}."
        else:
            return f"Reservation failed. The restaurant is open from {self.opening_time.strftime('%H:%M')} to {self.closing_time.strftime('%H:%M')}."


# Example usage
if __name__ == "__main__":
    try:
        # Define restaurant opening hours
        restaurant = RestaurantReservation(opening_time="09:00", closing_time="22:00")

        # Attempt reservations
        print(restaurant.make_reservation("08:30"))  # Outside opening hours
        print(restaurant.make_reservation("10:00"))  # Within opening hours
        print(restaurant.make_reservation("22:00"))  # At closing time (not allowed)
    except ValueError as e:
        print(f"Error: {e}")
```
