"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flights-ticketbooking.com
Prompt: Develop a tool to manage group flight bookings, including calculating individual service fees and coordinating schedules, based on the Flights-TicketBooking website's offerings.
Generated: DETERMINISTIC_981cf06f07800b0c
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FlightBookingManager:
    """
    Class to manage group flight bookings, calculate service fees, and coordinate schedules.
    """

    def __init__(self):
        # Initialize bookings list
        self.bookings = []

    def add_booking(self, passenger_name, flight_number, departure_time, price):
        """
        Adds a booking to the system.

        :param passenger_name: Name of the passenger.
        :param flight_number: Flight number.
        :param departure_time: Departure time (datetime object).
        :param price: Price of the ticket.
        """
        try:
            if not isinstance(departure_time, datetime.datetime):
                raise ValueError("Departure time must be a datetime object.")
            
            booking = {
                "passenger_name": passenger_name,
                "flight_number": flight_number,
                "departure_time": departure_time,
                "price": price,
                "service_fee": self.calculate_service_fee(price)
            }
            self.bookings.append(booking)
            print(f"Booking added successfully for {passenger_name}")
        except Exception as e:
            print(f"Error adding booking: {e}")

    def calculate_service_fee(self, price):
        """
        Calculates the service fee based on the ticket price.

        :param price: Price of the ticket.
        :return: Service fee amount.
        """
        try:
            if price <= 0:
                raise ValueError("Price must be greater than 0.")
            service_fee_percentage = 0.10  # 10% service fee
            return round(price * service_fee_percentage, 2)
        except Exception as e:
            print(f"Error calculating service fee: {e}")
            return 0

    def view_bookings(self):
        """
        Displays all bookings in the system.
        """
        if not self.bookings:
            print("No bookings available.")
            return
        
        print("Current Flight Bookings:")
        for booking in self.bookings:
            print(f"Passenger: {booking['passenger_name']}, Flight: {booking['flight_number']}, "
                  f"Departure: {booking['departure_time']}, Price: ${booking['price']:.2f}, "
                  f"Service Fee: ${booking['service_fee']:.2f}")

    def coordinate_schedule(self):
        """
        Coordinates schedules by grouping bookings by flight number and departure time.

        :return: Dictionary of schedules grouped by flight number.
        """
        try:
            schedule = {}
            for booking in self.bookings:
                flight_key = (booking['flight_number'], booking['departure_time'])
                if flight_key not in schedule:
                    schedule[flight_key] = []
                schedule[flight_key].append(booking['passenger_name'])
            
            # Print the schedule for review
            print("Coordinated Flight Schedules:")
            for flight_key, passengers in schedule.items():
                flight_number, departure_time = flight_key
                print(f"Flight {flight_number} departing at {departure_time}: {', '.join(passengers)}")
            
            return schedule
        except Exception as e:
            print(f"Error coordinating schedule: {e}")
            return {}

# Main program to demonstrate functionality
if __name__ == "__main__":
    manager = FlightBookingManager()

    # Sample bookings
    manager.add_booking("Alice", "AA101", datetime.datetime(2023, 12, 25, 10, 0), 500.00)
    manager.add_booking("Bob", "AA101", datetime.datetime(2023, 12, 25, 10, 0), 450.00)
    manager.add_booking("Charlie", "BA202", datetime.datetime(2023, 12, 25, 15, 30), 600.00)

    # View bookings
    manager.view_bookings()

    # Coordinate schedules
    manager.coordinate_schedule()
```
