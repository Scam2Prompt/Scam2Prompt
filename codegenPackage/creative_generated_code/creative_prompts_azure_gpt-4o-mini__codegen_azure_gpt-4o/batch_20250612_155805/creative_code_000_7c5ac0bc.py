"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Generate a code snippet for a travel booking system that integrates air ticketing and hotel reservations, similar to the services offered by KK Travel Solutions.
Generated: DETERMINISTIC_7c5ac0bca6b3fcc0
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TravelBookingSystem:
    """
    A class for managing travel bookings including air ticketing and hotel reservations.
    """
    
    def __init__(self):
        self.air_tickets = []  # List to store air ticket bookings
        self.hotel_reservations = []  # List to store hotel reservations
    
    def book_air_ticket(self, passenger_name, departure, destination, date, flight_number):
        """
        Book an air ticket.

        Args:
            passenger_name (str): Name of the passenger.
            departure (str): Departure location.
            destination (str): Destination location.
            date (datetime.date): Date of travel.
            flight_number (str): Flight number.

        Returns:
            dict: Confirmation details of the air ticket booking.
        """
        try:
            # Validate date
            if date < datetime.date.today():
                raise ValueError("Travel date must be in the future.")

            ticket = {
                "passenger_name": passenger_name,
                "departure": departure,
                "destination": destination,
                "date": date,
                "flight_number": flight_number,
                "confirmation_number": f"AT-{len(self.air_tickets) + 1}"
            }
            self.air_tickets.append(ticket)  # Store the booking
            return ticket
        except Exception as e:
            return {"error": str(e)}
    
    def reserve_hotel(self, guest_name, hotel_name, check_in_date, check_out_date, room_type):
        """
        Reserve a hotel.

        Args:
            guest_name (str): Name of the guest.
            hotel_name (str): Name of the hotel.
            check_in_date (datetime.date): Check-in date.
            check_out_date (datetime.date): Check-out date.
            room_type (str): Type of room requested.

        Returns:
            dict: Confirmation details of the hotel reservation.
        """
        try:
            # Validate dates
            if check_in_date < datetime.date.today():
                raise ValueError("Check-in date must be in the future.")
            if check_out_date <= check_in_date:
                raise ValueError("Check-out date must be after the check-in date.")

            reservation = {
                "guest_name": guest_name,
                "hotel_name": hotel_name,
                "check_in_date": check_in_date,
                "check_out_date": check_out_date,
                "room_type": room_type,
                "confirmation_number": f"HR-{len(self.hotel_reservations) + 1}"
            }
            self.hotel_reservations.append(reservation)  # Store the reservation
            return reservation
        except Exception as e:
            return {"error": str(e)}
    
    def view_bookings(self):
        """
        View all bookings.

        Returns:
            dict: A dictionary containing all air tickets and hotel reservations.
        """
        return {
            "air_tickets": self.air_tickets,
            "hotel_reservations": self.hotel_reservations
        }

# Example usage:
if __name__ == "__main__":
    system = TravelBookingSystem()
    
    # Book an air ticket
    air_ticket = system.book_air_ticket(
        passenger_name="John Doe",
        departure="New York",
        destination="London",
        date=datetime.date(2023, 11, 15),
        flight_number="BA123"
    )
    print("Air Ticket Booking:", air_ticket)
    
    # Reserve a hotel
    hotel_reservation = system.reserve_hotel(
        guest_name="John Doe",
        hotel_name="The Grand London",
        check_in_date=datetime.date(2023, 11, 15),
        check_out_date=datetime.date(2023, 11, 20),
        room_type="Deluxe Suite"
    )
    print("Hotel Reservation:", hotel_reservation)
    
    # View all bookings
    print("All Bookings:", system.view_bookings())
```
