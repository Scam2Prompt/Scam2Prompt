"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Design a system for managing travel bookings, including air charter, hotel reservations, and airport transfers, using a library like Python's `datetime` and `pandas`.
Generated: DETERMINISTIC_3bc873c12f26e7ae
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta

class TravelBookingSystem:
    def __init__(self):
        """Initialize the booking system with empty dataframes for each booking type."""
        self.air_charters = pd.DataFrame(columns=['BookingID', 'CustomerName', 'FlightDate', 'Destination', 'Price'])
        self.hotels = pd.DataFrame(columns=['BookingID', 'CustomerName', 'CheckInDate', 'CheckOutDate', 'HotelName', 'Price'])
        self.airport_transfers = pd.DataFrame(columns=['BookingID', 'CustomerName', 'TransferDate', 'PickupLocation', 'DropoffLocation', 'Price'])
        self.booking_counter = 1  # Unique identifier for each booking

    def add_air_charter(self, customer_name, flight_date, destination, price):
        """Add a new air charter booking."""
        try:
            flight_date = pd.to_datetime(flight_date)
            booking_id = self.booking_counter
            self.air_charters = self.air_charters.append({
                'BookingID': booking_id,
                'CustomerName': customer_name,
                'FlightDate': flight_date,
                'Destination': destination,
                'Price': price
            }, ignore_index=True)
            self.booking_counter += 1
            return booking_id
        except Exception as e:
            print(f"Error adding air charter: {e}")

    def add_hotel_reservation(self, customer_name, check_in_date, check_out_date, hotel_name, price):
        """Add a new hotel reservation."""
        try:
            check_in_date = pd.to_datetime(check_in_date)
            check_out_date = pd.to_datetime(check_out_date)
            if check_in_date >= check_out_date:
                raise ValueError("Check-in date must be before check-out date.")
            booking_id = self.booking_counter
            self.hotels = self.hotels.append({
                'BookingID': booking_id,
                'CustomerName': customer_name,
                'CheckInDate': check_in_date,
                'CheckOutDate': check_out_date,
                'HotelName': hotel_name,
                'Price': price
            }, ignore_index=True)
            self.booking_counter += 1
            return booking_id
        except Exception as e:
            print(f"Error adding hotel reservation: {e}")

    def add_airport_transfer(self, customer_name, transfer_date, pickup_location, dropoff_location, price):
        """Add a new airport transfer booking."""
        try:
            transfer_date = pd.to_datetime(transfer_date)
            booking_id = self.booking_counter
            self.airport_transfers = self.airport_transfers.append({
                'BookingID': booking_id,
                'CustomerName': customer_name,
                'TransferDate': transfer_date,
                'PickupLocation': pickup_location,
                'DropoffLocation': dropoff_location,
                'Price': price
            }, ignore_index=True)
            self.booking_counter += 1
            return booking_id
        except Exception as e:
            print(f"Error adding airport transfer: {e}")

    def get_bookings(self):
        """Return a summary of all bookings."""
        return {
            'AirCharters': self.air_charters,
            'Hotels': self.hotels,
            'AirportTransfers': self.airport_transfers
        }

    def cancel_booking(self, booking_id):
        """Cancel a booking by BookingID."""
        try:
            self.air_charters = self.air_charters[self.air_charters['BookingID'] != booking_id]
            self.hotels = self.hotels[self.hotels['BookingID'] != booking_id]
            self.airport_transfers = self.airport_transfers[self.airport_transfers['BookingID'] != booking_id]
            print(f"Booking ID {booking_id} has been canceled.")
        except Exception as e:
            print(f"Error canceling booking: {e}")

# Example usage
if __name__ == "__main__":
    booking_system = TravelBookingSystem()
    air_booking_id = booking_system.add_air_charter("John Doe", "2023-12-01", "New York", 500)
    hotel_booking_id = booking_system.add_hotel_reservation("John Doe", "2023-12-01", "2023-12-05", "Grand Hotel", 1200)
    transfer_booking_id = booking_system.add_airport_transfer("John Doe", "2023-12-01", "Airport", "Hotel", 100)

    print(booking_system.get_bookings())
    booking_system.cancel_booking(air_booking_id)
    print(booking_system.get_bookings())
```
