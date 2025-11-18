"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalflightguide.com
Prompt: Create a chatbot using Python that mimics the functionality of Global Flight Guide agents, allowing users to inquire about flight schedules, make changes, or cancel reservations.
Generated: DETERMINISTIC_9abf7f46e39b9822
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

class Flight:
    def __init__(self, flight_number, departure, arrival, schedule):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.schedule = schedule  # List of datetime objects for scheduled departure

    def is_flight_active(self):
        """Check if the flight is currently active based on the schedule."""
        current_time = datetime.datetime.now()
        return any(scheduled_time > current_time for scheduled_time in self.schedule)


class Reservation:
    def __init__(self, flight, passenger_name):
        self.flight = flight
        self.passenger_name = passenger_name
        self.confirmed = True

    def cancel(self):
        """Cancel the reservation."""
        if self.confirmed:
            self.confirmed = False
            logging.info(f"Reservation for {self.passenger_name} on flight {self.flight.flight_number} cancelled.")
        else:
            raise RuntimeError("Reservation is already cancelled.")


class Chatbot:
    def __init__(self):
        # Sample flight data
        self.flights = [
            Flight("AA123", "JFK", "LAX", [
                datetime.datetime(2023, 10, 23, 15, 30),
                datetime.datetime(2023, 10, 24, 16, 0),
            ]),
            Flight("DL456", "SFO", "ORD", [
                datetime.datetime(2023, 10, 23, 14, 45),
                datetime.datetime(2023, 10, 24, 17, 15),
            ]),
        ]
        self.reservations = []

    def inquire_schedule(self, flight_number):
        """Inquire about the flight schedule based on the flight number."""
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.is_flight_active():
                    return f"Flight {flight_number} is active with next departures: {flight.schedule}"
                else:
                    return f"Flight {flight_number} is not active."
        return "Flight not found."

    def make_reservation(self, flight_number, passenger_name):
        """Make a new reservation for the specified flight."""
        for flight in self.flights:
            if flight.flight_number == flight_number and flight.is_flight_active():
                reservation = Reservation(flight, passenger_name)
                self.reservations.append(reservation)
                return f"Reservation confirmed for {passenger_name} on flight {flight_number}."
        return "Unable to make reservation. Flight not active or not found."

    def cancel_reservation(self, flight_number, passenger_name):
        """Cancel an existing reservation."""
        try:
            for reservation in self.reservations:
                if reservation.flight.flight_number == flight_number and reservation.passenger_name == passenger_name:
                    reservation.cancel()
                    return f"Reservation for {passenger_name} on flight {flight_number} cancelled."
            return "Reservation not found."
        except RuntimeError as e:
            return str(e)


def main():
    chatbot = Chatbot()
    
    # Example interactions
    print(chatbot.inquire_schedule("AA123"))
    print(chatbot.make_reservation("AA123", "John Doe"))
    print(chatbot.cancel_reservation("AA123", "John Doe"))


if __name__ == "__main__":
    main()
```
