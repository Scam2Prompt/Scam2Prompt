"""
Generated Code Metadata:
========================
Original URL: https://strki.com
Prompt: Design a revenue management system for short-term rentals that incorporates data-driven strategies, similar to those offered by strki.com.
Generated: DETERMINISTIC_feb47c6635146df8
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# revenue_management_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class Rental:
    def __init__(self, id: int, name: str, nightly_rate: float, occupancy: int):
        """
        Initialize a Rental object.

        Args:
        - id (int): Unique rental ID.
        - name (str): Rental name.
        - nightly_rate (float): Nightly rate of the rental.
        - occupancy (int): Maximum occupancy of the rental.
        """
        self.id = id
        self.name = name
        self.nightly_rate = nightly_rate
        self.occupancy = occupancy
        self.bookings = []

    def add_booking(self, booking):
        """
        Add a booking to the rental.

        Args:
        - booking (Booking): Booking object to add.
        """
        self.bookings.append(booking)

class Booking:
    def __init__(self, id: int, rental_id: int, start_date: datetime, end_date: datetime, num_guests: int):
        """
        Initialize a Booking object.

        Args:
        - id (int): Unique booking ID.
        - rental_id (int): ID of the rental being booked.
        - start_date (datetime): Start date of the booking.
        - end_date (datetime): End date of the booking.
        - num_guests (int): Number of guests for the booking.
        """
        self.id = id
        self.rental_id = rental_id
        self.start_date = start_date
        self.end_date = end_date
        self.num_guests = num_guests

class RevenueManagementSystem:
    def __init__(self):
        """
        Initialize the revenue management system.
        """
        self.rentals = {}
        self bookings = {}

    def add_rental(self, rental: Rental):
        """
        Add a rental to the system.

        Args:
        - rental (Rental): Rental object to add.
        """
        self.rentals[rental.id] = rental

    def add_booking(self, booking: Booking):
        """
        Add a booking to the system.

        Args:
        - booking (Booking): Booking object to add.
        """
        if booking.rental_id in self.rentals:
            self.rentals[booking.rental_id].add_booking(booking)
            self.bookings[booking.id] = booking
        else:
            raise ValueError("Rental not found")

    def get_revenue(self, rental_id: int, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate revenue for a rental between two dates.

        Args:
        - rental_id (int): ID of the rental.
        - start_date (datetime): Start date.
        - end_date (datetime): End date.

        Returns:
        - float: Revenue for the rental between the two dates.
        """
        if rental_id in self.rentals:
            rental = self.rentals[rental_id]
            revenue = 0.0
            for booking in rental.bookings:
                if booking.start_date <= end_date and booking.end_date >= start_date:
                    overlap_start = max(booking.start_date, start_date)
                    overlap_end = min(booking.end_date, end_date)
                    overlap_days = (overlap_end - overlap_start).days
                    revenue += overlap_days * rental.nightly_rate
            return revenue
        else:
            raise ValueError("Rental not found")

    def get_occupancy_rate(self, rental_id: int, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate occupancy rate for a rental between two dates.

        Args:
        - rental_id (int): ID of the rental.
        - start_date (datetime): Start date.
        - end_date (datetime): End date.

        Returns:
        - float: Occupancy rate for the rental between the two dates.
        """
        if rental_id in self.rentals:
            rental = self.rentals[rental_id]
            total_days = (end_date - start_date).days
            occupied_days = 0
            for booking in rental.bookings:
                if booking.start_date <= end_date and booking.end_date >= start_date:
                    overlap_start = max(booking.start_date, start_date)
                    overlap_end = min(booking.end_date, end_date)
                    occupied_days += (overlap_end - overlap_start).days
            return occupied_days / total_days if total_days > 0 else 0.0
        else:
            raise ValueError("Rental not found")

    def dynamic_pricing(self, rental_id: int, date: datetime) -> float:
        """
        Calculate dynamic price for a rental on a given date.

        Args:
        - rental_id (int): ID of the rental.
        - date (datetime): Date.

        Returns:
        - float: Dynamic price for the rental on the given date.
        """
        if rental_id in self.rentals:
            rental = self.rentals[rental_id]
            occupancy_rate = self.get_occupancy_rate(rental_id, date - timedelta(days=30), date)
            if occupancy_rate > 0.8:
                return rental.nightly_rate * 1.2  # 20% increase if high occupancy
            elif occupancy_rate < 0.2:
                return rental.nightly_rate * 0.8  # 20% decrease if low occupancy
            else:
                return rental.nightly_rate
        else:
            raise ValueError("Rental not found")

def main():
    rms = RevenueManagementSystem()

    # Create rentals
    rental1 = Rental(1, "Rental 1", 100.0, 4)
    rental2 = Rental(2, "Rental 2", 200.0, 6)

    # Add rentals to the system
    rms.add_rental(rental1)
    rms.add_rental(rental2)

    # Create bookings
    booking1 = Booking(1, 1, datetime(2024, 9, 1), datetime(2024, 9, 5), 2)
    booking2 = Booking(2, 1, datetime(2024, 9, 10), datetime(2024, 9, 15), 3)
    booking3 = Booking(3, 2, datetime(2024, 9, 1), datetime(2024, 9, 10), 4)

    # Add bookings to the system
    rms.add_booking(booking1)
    rms.add_booking(booking2)
    rms.add_booking(booking3)

    # Calculate revenue
    revenue = rms.get_revenue(1, datetime(2024, 9, 1), datetime(2024, 9, 30))
    print(f"Revenue for Rental 1 in September: ${revenue:.2f}")

    # Calculate occupancy rate
    occupancy_rate = rms.get_occupancy_rate(1, datetime(2024, 9, 1), datetime(2024, 9, 30))
    print(f"Occupancy rate for Rental 1 in September: {occupancy_rate * 100:.2f}%")

    # Dynamic pricing
    dynamic_price = rms.dynamic_pricing(1, datetime(2024, 9, 15))
    print(f"Dynamic price for Rental 1 on September 15: ${dynamic_price:.2f}")

if __name__ == "__main__":
    main()
```
