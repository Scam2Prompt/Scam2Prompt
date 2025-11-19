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
from datetime import datetime, time

class Restaurant:
    def __init__(self, name, opening_time, closing_time):
        """
        Initialize the Restaurant object with name, opening time and closing time.
        
        :param name: str - Name of the restaurant
        :param opening_time: time - Opening time of the restaurant
        :param closing_time: time - Closing time of the restaurant
        """
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
    
    def is_open(self, reservation_time):
        """
        Check if the restaurant is open at the given reservation time.
        
        :param reservation_time: datetime - The time at which a reservation is requested
        :return: bool - True if the restaurant is open, False otherwise
        """
        return self.opening_time <= reservation_time.time() <= self.closing_time

    def make_reservation(self, reservation_time):
        """
        Attempt to make a reservation at the restaurant.
        
        :param reservation_time: datetime - The time at which a reservation is requested
        :raises ValueError: If the reservation time is outside of opening hours
        :return: str - Confirmation message for the reservation
        """
        if not self.is_open(reservation_time):
            raise ValueError(f"Reservations can only be made between {self.opening_time} and {self.closing_time}.")
        
        return f"Reservation confirmed for {reservation_time.strftime('%Y-%m-%d %H:%M')} at {self.name}."

def main():
    # Define restaurant opening and closing times
    opening_time = time(11, 0)  # 11:00 AM
    closing_time = time(22, 0)  # 10:00 PM

    # Create a restaurant instance
    my_restaurant = Restaurant("The Gourmet Place", opening_time, closing_time)

    # Sample reservation time (change this to test different scenarios)
    reservation_time = datetime(2023, 10, 15, 18, 30)  # 6:30 PM on October 15, 2023

    try:
        # Make a reservation
        confirmation = my_restaurant.make_reservation(reservation_time)
        print(confirmation)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
