"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet for a reservation system that allows users to book horse riding tours like the Laguna Ride or Cowboy Experience at Chile Horse Riding.
Generated: DETERMINISTIC_07c31fdbf7fa7b20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# reservation_system.py

import datetime

class ReservationSystem:
    def __init__(self):
        """
        Initializes the reservation system with available tours and an empty list of reservations.
        """
        self.tours = {
            "Laguna Ride": 100,  # Price in USD
            "Cowboy Experience": 150  # Price in USD
        }
        self.reservations = []

    def list_tours(self):
        """
        Lists all available horse riding tours with their prices.
        """
        print("Available Tours:")
        for tour, price in self.tours.items():
            print(f"{tour} - ${price}")

    def book_tour(self, name, tour_name, date):
        """
        Books a tour for the user.
        :param name: str, Name of the user
        :param tour_name: str, Name of the tour
        :param date: str, Date in 'YYYY-MM-DD' format
        :return: None
        """
        try:
            # Validate the tour name
            if tour_name not in self.tours:
                raise ValueError(f"Tour '{tour_name}' not found. Please choose a valid tour.")

            # Validate the date format
            tour_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            if tour_date < datetime.date.today():
                raise ValueError("Cannot book a tour for a past date.")

            # Create reservation
            reservation = {
                "name": name,
                "tour_name": tour_name,
                "date": tour_date,
                "price": self.tours[tour_name]
            }
            self.reservations.append(reservation)

            print(f"Reservation confirmed for {name}: {tour_name} on {tour_date}.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_reservations(self):
        """
        Displays all reservations made so far.
        """
        if not self.reservations:
            print("No reservations found.")
            return

        print("Reservations:")
        for res in self.reservations:
            print(f"{res['name']} - {res['tour_name']} on {res['date']} - ${res['price']}")


# Main program for user interaction
if __name__ == "__main__":
    system = ReservationSystem()
    while True:
        print("\n=== Chile Horse Riding Reservation System ===")
        print("1. List Tours")
        print("2. Book a Tour")
        print("3. View Reservations")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            system.list_tours()
        elif choice == "2":
            name = input("Enter your name: ").strip()
            tour_name = input("Enter the name of the tour: ").strip()
            date = input("Enter the date (YYYY-MM-DD): ").strip()
            system.book_tour(name, tour_name, date)
        elif choice == "3":
            system.view_reservations()
        elif choice == "4":
            print("Thank you for using the reservation system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
