"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bilet-emirates.ru
Prompt: Develop a script to simulate the online ticket booking process for Emirates flights, including seat selection, payment via Visa/MasterCard/Mir, and electronic ticket generation.
Generated: DETERMINISTIC_bf19885dbbe390f0
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import sys


class FlightBooking:
    def __init__(self):
        self.seats = self.generate_seating_plan()
        self.ticket_details = {}

    def generate_seating_plan(self):
        """
        Generate a seating plan for a flight (e.g., 10 rows, A-F seats).
        """
        rows = 10
        columns = ['A', 'B', 'C', 'D', 'E', 'F']
        seats = {f"{row}{col}": None for row in range(1, rows + 1) for col in columns}
        return seats

    def display_seating_plan(self):
        """
        Display the current seating plan with available and booked seats.
        """
        print("\nSeating Plan:")
        rows = 10
        columns = ['A', 'B', 'C', 'D', 'E', 'F']
        for row in range(1, rows + 1):
            for col in columns:
                status = "Available" if self.seats[f"{row}{col}"] is None else "Booked"
                print(f"{row}{col}: {status}", end="\t")
            print()

    def select_seat(self):
        """
        Allows the user to select an available seat.
        """
        while True:
            self.display_seating_plan()
            selected_seat = input("\nEnter the seat you want to book (e.g., 1A): ").strip().upper()
            if selected_seat in self.seats and self.seats[selected_seat] is None:
                self.seats[selected_seat] = "Booked"
                print(f"Seat {selected_seat} successfully booked!")
                return selected_seat
            else:
                print("Invalid or already booked seat. Please try again.")

    def process_payment(self, amount):
        """
        Simulates payment processing for Visa/MasterCard/Mir.
        """
        while True:
            print("Available payment methods: Visa, MasterCard, Mir")
            payment_method = input("Enter your payment method: ").strip().capitalize()
            if payment_method in ['Visa', 'Mastercard', 'Mir']:
                card_number = input("Enter your card number (16 digits): ").strip()
                if len(card_number) == 16 and card_number.isdigit():
                    print(f"Payment of ${amount} successfully processed via {payment_method}!")
                    return True
                else:
                    print("Invalid card number. Please try again.")
            else:
                print("Unsupported payment method. Please choose Visa, MasterCard, or Mir.")

    def generate_ticket(self, passenger_name, selected_seat):
        """
        Generate an electronic ticket for the passenger.
        """
        ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.ticket_details = {
            "Ticket ID": ticket_id,
            "Passenger Name": passenger_name,
            "Seat": selected_seat,
            "Flight": "Emirates EK2023",
        }
        print("\nTicket Generated:\n" + "-" * 30)
        for key, value in self.ticket_details.items():
            print(f"{key}: {value}")
        print("-" * 30)

    def start_booking(self):
        """
        Start the flight booking process.
        """
        print("Welcome to Emirates Flight Booking System!")
        passenger_name = input("Enter your full name: ").strip()
        selected_seat = self.select_seat()
        ticket_price = random.randint(200, 500)  # Simulating ticket price between $200-$500
        print(f"The ticket price for seat {selected_seat} is ${ticket_price}.")
        if self.process_payment(ticket_price):
            self.generate_ticket(passenger_name, selected_seat)
            print("Thank you for booking with Emirates!")
        else:
            print("Payment failed. Booking not completed.")


if __name__ == "__main__":
    try:
        booking_system = FlightBooking()
        booking_system.start_booking()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
