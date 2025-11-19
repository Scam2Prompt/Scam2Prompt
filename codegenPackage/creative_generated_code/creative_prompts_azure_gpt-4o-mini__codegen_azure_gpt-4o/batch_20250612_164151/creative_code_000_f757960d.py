"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://japkasai.net
Prompt: Generate a code snippet for a booking system that allows clients to schedule appointments at a men's grooming salon, incorporating features like service selection and time slots based on the hours of operation (10:00 to 23:00).
Generated: DETERMINISTIC_f757960d2a1d6965
Batch ID: 20250612_164151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import sys

class BookingSystem:
    def __init__(self):
        # Salon hours of operation
        self.opening_hour = 10  # 10:00 AM
        self.closing_hour = 23  # 11:00 PM
        # Services offered
        self.services = {
            "1": "Haircut",
            "2": "Shave",
            "3": "Beard Trim",
            "4": "Facial"
        }
        # List to store bookings
        self.bookings = []

    def display_services(self):
        """Display available services."""
        print("\nAvailable Services:")
        for service_id, service_name in self.services.items():
            print(f"{service_id}. {service_name}")

    def display_time_slots(self):
        """Display available time slots based on hours of operation."""
        print("\nAvailable Time Slots:")
        current_time = datetime.strptime(f"{self.opening_hour}:00", "%H:%M")
        closing_time = datetime.strptime(f"{self.closing_hour}:00", "%H:%M")
        time_slots = []
        
        while current_time < closing_time:
            time_slots.append(current_time.strftime("%H:%M"))
            current_time += timedelta(minutes=30)  # Increment time slot by 30 minutes
        
        for index, slot in enumerate(time_slots, start=1):
            print(f"{index}. {slot}")
        
        return time_slots

    def book_appointment(self):
        """Handle the booking process."""
        try:
            # Step 1: Select a service
            self.display_services()
            service_choice = input("\nEnter the number of the service you'd like to book: ").strip()
            if service_choice not in self.services:
                raise ValueError("Invalid service selection.")
            
            service_name = self.services[service_choice]

            # Step 2: Select a time slot
            time_slots = self.display_time_slots()
            time_choice = input("\nEnter the number of your preferred time slot: ").strip()
            if not time_choice.isdigit() or int(time_choice) < 1 or int(time_choice) > len(time_slots):
                raise ValueError("Invalid time slot selection.")
            
            time_slot = time_slots[int(time_choice) - 1]

            # Step 3: Confirm booking
            client_name = input("\nEnter your name to confirm the booking: ").strip()
            if not client_name:
                raise ValueError("Client name cannot be empty.")
            
            booking = {
                "name": client_name,
                "service": service_name,
                "time": time_slot
            }
            self.bookings.append(booking)

            print(f"\nBooking confirmed for {client_name}!")
            print(f"Service: {service_name}")
            print(f"Time Slot: {time_slot}\n")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    def display_bookings(self):
        """Show all confirmed bookings."""
        print("\nConfirmed Bookings:")
        if not self.bookings:
            print("No bookings found.")
        else:
            for idx, booking in enumerate(self.bookings, start=1):
                print(f"{idx}. {booking['name']} - {booking['service']} at {booking['time']}")

# Main script to use the booking system
if __name__ == "__main__":
    print("Welcome to the Men's Grooming Salon Booking System!\n")
    salon = BookingSystem()

    while True:
        print("\nMenu:")
        print("1. Book an Appointment")
        print("2. View Confirmed Bookings")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            salon.book_appointment()
        elif choice == "2":
            salon.display_bookings()
        elif choice == "3":
            print("Thank you for using the booking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
