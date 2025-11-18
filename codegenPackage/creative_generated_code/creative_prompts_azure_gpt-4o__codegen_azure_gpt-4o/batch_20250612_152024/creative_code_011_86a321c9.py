"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Develop a tool to manage and book air tickets for study abroad students, referencing the air ticket services provided by RNW International.
Generated: DETERMINISTIC_86a321c9a98a09f6
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for managing and booking air tickets for study abroad students. This example uses a simple structure to demonstrate functionality and can be expanded for production use.

```python
import json

# Mock data for RNW International air ticket services
class RNWInternational:
    mock_flights = [
        {"flight_id": 1, "destination": "USA", "price": 1200},
        {"flight_id": 2, "destination": "UK", "price": 800},
        {"flight_id": 3, "destination": "Canada", "price": 1000},
        {"flight_id": 4, "destination": "Australia", "price": 1500},
    ]
    
    @staticmethod
    def get_available_flights():
        """Simulate fetching flight data from RNW International."""
        return RNWInternational.mock_flights


class AirTicketManager:
    def __init__(self):
        # A storage for bookings (in an actual system, use a database)
        self.bookings = []

    def display_available_flights(self):
        """Display a list of available flights."""
        flights = RNWInternational.get_available_flights()
        print("Available Flights:")
        for flight in flights:
            print(f"Flight ID: {flight['flight_id']}, Destination: {flight['destination']}, Price: ${flight['price']}")

    def book_ticket(self, student_name, flight_id):
        """
        Book a ticket for a student.
        
        Args:
            student_name (str): Name of the student booking the ticket.
            flight_id (int): ID of the flight to book.
        """
        flights = RNWInternational.get_available_flights()
        selected_flight = next((flight for flight in flights if flight["flight_id"] == flight_id), None)
        
        if not selected_flight:
            print(f"Error: Flight ID {flight_id} not found.")
            return
        
        # Create booking record
        booking = {
            "booking_id": len(self.bookings) + 1,
            "student_name": student_name,
            "flight_id": flight_id,
            "destination": selected_flight["destination"],
            "price": selected_flight["price"],
        }
        self.bookings.append(booking)
        print(f"Booking confirmed! Booking ID: {booking['booking_id']}")

    def display_bookings(self):
        """Display all bookings."""
        if not self.bookings:
            print("No bookings available.")
            return
        
        print("Bookings:")
        for booking in self.bookings:
            print(f"Booking ID: {booking['booking_id']}, Student Name: {booking['student_name']}, "
                  f"Destination: {booking['destination']}, Price: ${booking['price']}")

    def save_bookings_to_file(self, filename="bookings.json"):
        """
        Save all bookings to a file in JSON format.
        
        Args:
            filename (str): Name of the file to save bookings.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.bookings, file, indent=4)
            print(f"Bookings saved to {filename}.")
        except Exception as e:
            print(f"Error saving bookings to file: {e}")

    def load_bookings_from_file(self, filename="bookings.json"):
        """
        Load bookings from a file in JSON format.
        
        Args:
            filename (str): Name of the file to load bookings from.
        """
        try:
            with open(filename, "r") as file:
                self.bookings = json.load(file)
            print(f"Bookings loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except Exception as e:
            print(f"Error loading bookings from file: {e}")


# Main program for demonstration
def main():
    manager = AirTicketManager()
    
    while True:
        print("\nAir Ticket Manager")
        print("1. Display Available Flights")
        print("2. Book Ticket")
        print("3. Display Bookings")
        print("4. Save Bookings to File")
        print("5. Load Bookings from File")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.display_available_flights()
        elif choice == "2":
            student_name = input("Enter student name: ")
            flight_id = int(input("Enter flight ID: "))
            manager.book_ticket(student_name, flight_id)
        elif choice == "3":
            manager.display_bookings()
        elif choice == "4":
            manager.save_bookings_to_file()
        elif choice == "5":
            manager.load_bookings_from_file()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
