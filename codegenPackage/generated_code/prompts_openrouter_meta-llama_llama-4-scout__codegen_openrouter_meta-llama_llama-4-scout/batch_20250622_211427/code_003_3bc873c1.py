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
from datetime import datetime, timedelta
import pandas as pd

class TravelBookingSystem:
    def __init__(self):
        # Initialize empty dataframes for bookings
        self.air_charter_bookings = pd.DataFrame(columns=['BookingID', 'Departure', 'Arrival', 'DepartureDate', 'ReturnDate', 'PassengerName'])
        self.hotel_reservations = pd.DataFrame(columns=['BookingID', 'HotelName', 'CheckInDate', 'CheckOutDate', 'GuestName'])
        self.airport_transfers = pd.DataFrame(columns=['BookingID', 'PickupLocation', 'DropoffLocation', 'PickupDate', 'DropoffDate', 'PassengerName'])

    def book_air_charter(self, departure, arrival, departure_date, return_date, passenger_name):
        # Validate dates
        try:
            departure_date = datetime.strptime(departure_date, '%Y-%m-%d')
            return_date = datetime.strptime(return_date, '%Y-%m-%d')
            if return_date < departure_date:
                raise ValueError("Return date cannot be before departure date")
        except ValueError as e:
            print(f"Invalid date: {e}")
            return

        # Generate unique booking ID
        booking_id = len(self.air_charter_bookings) + 1

        # Create new booking
        new_booking = pd.DataFrame({
            'BookingID': [booking_id],
            'Departure': [departure],
            'Arrival': [arrival],
            'DepartureDate': [departure_date],
            'ReturnDate': [return_date],
            'PassengerName': [passenger_name]
        })

        # Add to bookings dataframe
        self.air_charter_bookings = pd.concat([self.air_charter_bookings, new_booking], ignore_index=True)

        print(f"Air charter booking created successfully. Booking ID: {booking_id}")

    def book_hotel_reservation(self, hotel_name, check_in_date, check_out_date, guest_name):
        # Validate dates
        try:
            check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
            if check_out_date < check_in_date:
                raise ValueError("Check-out date cannot be before check-in date")
        except ValueError as e:
            print(f"Invalid date: {e}")
            return

        # Generate unique booking ID
        booking_id = len(self.hotel_reservations) + 1

        # Create new booking
        new_booking = pd.DataFrame({
            'BookingID': [booking_id],
            'HotelName': [hotel_name],
            'CheckInDate': [check_in_date],
            'CheckOutDate': [check_out_date],
            'GuestName': [guest_name]
        })

        # Add to bookings dataframe
        self.hotel_reservations = pd.concat([self.hotel_reservations, new_booking], ignore_index=True)

        print(f"Hotel reservation created successfully. Booking ID: {booking_id}")

    def book_airport_transfer(self, pickup_location, dropoff_location, pickup_date, dropoff_date, passenger_name):
        # Validate dates
        try:
            pickup_date = datetime.strptime(pickup_date, '%Y-%m-%d')
            dropoff_date = datetime.strptime(dropoff_date, '%Y-%m-%d')
            if dropoff_date < pickup_date:
                raise ValueError("Dropoff date cannot be before pickup date")
        except ValueError as e:
            print(f"Invalid date: {e}")
            return

        # Generate unique booking ID
        booking_id = len(self.airport_transfers) + 1

        # Create new booking
        new_booking = pd.DataFrame({
            'BookingID': [booking_id],
            'PickupLocation': [pickup_location],
            'DropoffLocation': [dropoff_location],
            'PickupDate': [pickup_date],
            'DropoffDate': [dropoff_date],
            'PassengerName': [passenger_name]
        })

        # Add to bookings dataframe
        self.airport_transfers = pd.concat([self.airport_transfers, new_booking], ignore_index=True)

        print(f"Airport transfer booking created successfully. Booking ID: {booking_id}")

    def view_bookings(self, booking_type=None):
        if booking_type == 'air_charter':
            print(self.air_charter_bookings)
        elif booking_type == 'hotel_reservation':
            print(self.hotel_reservations)
        elif booking_type == 'airport_transfer':
            print(self.airport_transfers)
        else:
            print("All Bookings:")
            print("Air Charter Bookings:")
            print(self.air_charter_bookings)
            print("\nHotel Reservations:")
            print(self.hotel_reservations)
            print("\nAirport Transfers:")
            print(self.airport_transfers)


def main():
    booking_system = TravelBookingSystem()

    while True:
        print("\nTravel Booking System Menu:")
        print("1. Book Air Charter")
        print("2. Book Hotel Reservation")
        print("3. Book Airport Transfer")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            departure = input("Enter departure location: ")
            arrival = input("Enter arrival location: ")
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            return_date = input("Enter return date (YYYY-MM-DD): ")
            passenger_name = input("Enter passenger name: ")
            booking_system.book_air_charter(departure, arrival, departure_date, return_date, passenger_name)
        elif choice == '2':
            hotel_name = input("Enter hotel name: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            guest_name = input("Enter guest name: ")
            booking_system.book_hotel_reservation(hotel_name, check_in_date, check_out_date, guest_name)
        elif choice == '3':
            pickup_location = input("Enter pickup location: ")
            dropoff_location = input("Enter dropoff location: ")
            pickup_date = input("Enter pickup date (YYYY-MM-DD): ")
            dropoff_date = input("Enter dropoff date (YYYY-MM-DD): ")
            passenger_name = input("Enter passenger name: ")
            booking_system.book_airport_transfer(pickup_location, dropoff_location, pickup_date, dropoff_date, passenger_name)
        elif choice == '4':
            booking_type = input("Enter booking type (air_charter, hotel_reservation, airport_transfer) or leave blank for all: ")
            if booking_type == '':
                booking_system.view_bookings()
            else:
                booking_system.view_bookings(booking_type)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
