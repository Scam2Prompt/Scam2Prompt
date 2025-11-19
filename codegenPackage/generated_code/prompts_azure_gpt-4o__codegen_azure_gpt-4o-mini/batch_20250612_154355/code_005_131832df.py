"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Write a function to automate the reservation process for advertising spaces, inspired by WOW MEDIA's "Cotizar tu ubicacion favorita desde aqui" feature.
Generated: DETERMINISTIC_131832df7efdf587
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ReservationError(Exception):
    """Custom exception for reservation errors."""
    pass

class AdvertisingSpace:
    """Class representing an advertising space."""
    
    def __init__(self, location, price_per_day):
        self.location = location
        self.price_per_day = price_per_day
        self.reservations = []  # List to store reservations

    def reserve(self, start_date, end_date):
        """Reserve the advertising space for a given date range.

        Args:
            start_date (datetime.date): The start date of the reservation.
            end_date (datetime.date): The end date of the reservation.

        Raises:
            ReservationError: If the reservation dates are invalid or overlap with existing reservations.
        """
        if start_date >= end_date:
            raise ReservationError("Start date must be before end date.")
        
        if self.is_date_range_reserved(start_date, end_date):
            raise ReservationError("The selected date range is already reserved.")

        # Add the reservation to the list
        self.reservations.append((start_date, end_date))
        print(f"Reservation successful for {self.location} from {start_date} to {end_date}.")

    def is_date_range_reserved(self, start_date, end_date):
        """Check if the date range overlaps with existing reservations.

        Args:
            start_date (datetime.date): The start date of the reservation.
            end_date (datetime.date): The end date of the reservation.

        Returns:
            bool: True if the date range is reserved, False otherwise.
        """
        for reserved_start, reserved_end in self.reservations:
            if (start_date < reserved_end) and (end_date > reserved_start):
                return True
        return False

    def calculate_total_cost(self, start_date, end_date):
        """Calculate the total cost for the reservation.

        Args:
            start_date (datetime.date): The start date of the reservation.
            end_date (datetime.date): The end date of the reservation.

        Returns:
            float: Total cost for the reservation.
        """
        if start_date >= end_date:
            raise ReservationError("Start date must be before end date.")
        
        total_days = (end_date - start_date).days
        return total_days * self.price_per_day

def main():
    """Main function to demonstrate the reservation process."""
    # Create an advertising space instance
    ad_space = AdvertisingSpace("Downtown Billboard", 150.00)

    # Define reservation dates
    start_date = datetime.date(2023, 11, 1)
    end_date = datetime.date(2023, 11, 5)

    try:
        # Attempt to reserve the advertising space
        ad_space.reserve(start_date, end_date)
        
        # Calculate total cost
        total_cost = ad_space.calculate_total_cost(start_date, end_date)
        print(f"Total cost for the reservation: ${total_cost:.2f}")

    except ReservationError as e:
        print(f"Reservation failed: {e}")

if __name__ == "__main__":
    main()
```
