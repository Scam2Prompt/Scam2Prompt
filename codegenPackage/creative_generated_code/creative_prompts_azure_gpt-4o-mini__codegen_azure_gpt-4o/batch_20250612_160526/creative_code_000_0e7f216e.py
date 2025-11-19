"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roc-remi.com
Prompt: Generate a booking request code for a stay at Chalet Roc Remi in Les Gets, including options for B&B and full chalet rental.
Generated: DETERMINISTIC_0e7f216edc055df8
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ChaletBooking:
    def __init__(self, chalet_name: str):
        """
        Initialize a ChaletBooking instance.

        :param chalet_name: Name of the chalet being booked.
        """
        self.chalet_name = chalet_name
        self.available_packages = ["B&B", "Full Chalet Rental"]

    def check_availability(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Check availability for the given date range.

        :param start_date: Start date of the stay.
        :param end_date: End date of the stay.
        :return: Boolean indicating whether the requested dates are available.
        """
        # For demonstration, assume all dates are available.
        # Replace this logic with actual availability checks in production.
        return True

    def calculate_price(self, package: str, num_guests: int, num_nights: int) -> float:
        """
        Calculate the price based on the selected package, number of guests, and nights.

        :param package: Selected package ("B&B" or "Full Chalet Rental").
        :param num_guests: Number of guests.
        :param num_nights: Number of nights.
        :return: Total price for the booking.
        """
        if package == "B&B":
            # Example price: $100 per guest per night
            price_per_night = 100
        elif package == "Full Chalet Rental":
            # Example price: $500 per night for the entire chalet
            price_per_night = 500
        else:
            raise ValueError("Invalid package selected.")

        return price_per_night * num_guests * num_nights if package == "B&B" else price_per_night * num_nights

    def create_booking(self, start_date: datetime.date, end_date: datetime.date, package: str, num_guests: int):
        """
        Create a booking request for a stay at the chalet.

        :param start_date: Start date of the stay.
        :param end_date: End date of the stay.
        :param package: Selected package ("B&B" or "Full Chalet Rental").
        :param num_guests: Number of guests.
        :return: Confirmation message with booking details.
        """
        # Validate inputs
        if start_date >= end_date:
            raise ValueError("End date must be after start date.")
        if package not in self.available_packages:
            raise ValueError("Selected package is not available.")
        if num_guests <= 0:
            raise ValueError("Number of guests must be greater than zero.")

        # Check availability
        if not self.check_availability(start_date, end_date):
            raise Exception("Requested dates are not available.")

        # Calculate price
        num_nights = (end_date - start_date).days
        total_price = self.calculate_price(package, num_guests, num_nights)

        # Generate booking details
        booking_details = {
            "Chalet": self.chalet_name,
            "Start Date": start_date,
            "End Date": end_date,
            "Package": package,
            "Number of Guests": num_guests,
            "Total Price": f"${total_price:.2f}"
        }

        return f"Booking confirmed! Details: {booking_details}"


# Example usage
if __name__ == "__main__":
    chalet_name = "Chalet Roc Remi"
    booking_system = ChaletBooking(chalet_name)

    try:
        # Sample booking request
        start_date = datetime.date(2023, 12, 20)
        end_date = datetime.date(2023, 12, 27)
        package = "B&B"
        num_guests = 4

        confirmation_message = booking_system.create_booking(start_date, end_date, package, num_guests)
        print(confirmation_message)
    except Exception as e:
        print(f"Error: {e}")
```
