"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Write a code snippet for a travel booking system that includes features for arranging airport transfers and hotel bookings for a safari trip in Kenya.
Generated: DETERMINISTIC_b8ee3143d2cb5be2
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize empty lists to store bookings
        self.airport_transfers = []
        self.hotel_bookings = []

    def book_airport_transfer(self, name, pickup_location, drop_off_location, datetime):
        """
        Book an airport transfer.
        :param name: Name of the customer
        :param pickup_location: Pickup location
        :param drop_off_location: Drop-off location
        :param datetime: Date and time of transfer
        :return: Confirmation message
        """
        try:
            transfer_details = {
                "name": name,
                "pickup_location": pickup_location,
                "drop_off_location": drop_off_location,
                "datetime": datetime,
            }
            self.airport_transfers.append(transfer_details)
            return f"Airport transfer booked successfully for {name}."
        except Exception as e:
            return f"Error booking airport transfer: {str(e)}"

    def book_hotel(self, name, hotel_name, check_in_date, check_out_date, number_of_guests):
        """
        Book a hotel room.
        :param name: Name of the customer
        :param hotel_name: Name of the hotel
        :param check_in_date: Check-in date
        :param check_out_date: Check-out date
        :param number_of_guests: Number of guests
        :return: Confirmation message
        """
        try:
            # Validate dates
            if check_in_date >= check_out_date:
                raise ValueError("Check-out date must be after the check-in date.")
            booking_details = {
                "name": name,
                "hotel_name": hotel_name,
                "check_in_date": check_in_date,
                "check_out_date": check_out_date,
                "number_of_guests": number_of_guests,
            }
            self.hotel_bookings.append(booking_details)
            return f"Hotel booking successful for {name} at {hotel_name}."
        except Exception as e:
            return f"Error booking hotel: {str(e)}"

    def list_bookings(self):
        """
        List all bookings (airport transfers and hotel bookings).
        :return: Dictionary containing all bookings
        """
        try:
            return {
                "airport_transfers": self.airport_transfers,
                "hotel_bookings": self.hotel_bookings,
            }
        except Exception as e:
            return f"Error retrieving bookings: {str(e)}"


# Example Usage
if __name__ == "__main__":
    # Initialize the booking system
    safari_booking = BookingSystem()

    # Book an airport transfer
    transfer_response = safari_booking.book_airport_transfer(
        name="John Doe",
        pickup_location="Jomo Kenyatta International Airport",
        drop_off_location="Safari Lodge",
        datetime=datetime.datetime(2023, 11, 15, 14, 30),
    )
    print(transfer_response)

    # Book a hotel
    hotel_response = safari_booking.book_hotel(
        name="John Doe",
        hotel_name="Safari Lodge",
        check_in_date=datetime.date(2023, 11, 15),
        check_out_date=datetime.date(2023, 11, 20),
        number_of_guests=2,
    )
    print(hotel_response)

    # List all bookings
    all_bookings = safari_booking.list_bookings()
    print("Current Bookings:", all_bookings)
```
