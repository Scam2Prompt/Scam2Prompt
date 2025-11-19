"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crypto-io.com
Prompt: How can I implement an appointment booking system for a barbershop similar to Gould Barbers, focusing on services like skin fades and beard trims?
Generated: DETERMINISTIC_e99a890ce2e46c6c
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Appointment Booking System for Barbershop
Author: Expert Programmer
Description: A simple Python application to manage appointment bookings for services such as skin fades and beard trims.
"""

import datetime

class AppointmentBookingSystem:
    def __init__(self):
        # Initialize the system with available services and an empty list of bookings
        self.services = {
            "skin_fade": 25.0,  # Price for skin fade
            "beard_trim": 15.0  # Price for beard trim
        }
        self.bookings = []  # List to store all bookings

    def display_services(self):
        """Display available services and their prices."""
        print("\nAvailable Services:")
        for service_name, price in self.services.items():
            print(f"- {service_name.replace('_', ' ').title()}: ${price:.2f}")

    def book_appointment(self, customer_name, service_name, appointment_time):
        """
        Book an appointment for a customer.
        :param customer_name: Name of the customer
        :param service_name: Name of the service (e.g., "skin_fade" or "beard_trim")
        :param appointment_time: Desired appointment time (datetime object)
        """
        if service_name not in self.services:
            print(f"Error: Service '{service_name}' is not available.")
            return False

        # Check for overlapping bookings
        for booking in self.bookings:
            if booking['appointment_time'] == appointment_time:
                print("Error: The selected time slot is already booked.")
                return False

        # Create a new booking
        booking = {
            "customer_name": customer_name,
            "service_name": service_name,
            "appointment_time": appointment_time
        }
        self.bookings.append(booking)
        print(f"Appointment successfully booked for {customer_name} on {appointment_time}.")
        return True

    def view_bookings(self):
        """View all upcoming appointments."""
        if not self.bookings:
            print("\nNo bookings available.")
            return

        print("\nUpcoming Appointments:")
        for booking in sorted(self.bookings, key=lambda x: x['appointment_time']):
            service_name_formatted = booking['service_name'].replace('_', ' ').title()
            print(f"- {booking['customer_name']} | {service_name_formatted} | {booking['appointment_time']}")

    def cancel_appointment(self, customer_name, appointment_time):
        """
        Cancel an appointment.
        :param customer_name: Name of the customer
        :param appointment_time: Appointment time to cancel (datetime object)
        """
        for booking in self.bookings:
            if booking['customer_name'] == customer_name and booking['appointment_time'] == appointment_time:
                self.bookings.remove(booking)
                print(f"Appointment for {customer_name} on {appointment_time} has been canceled.")
                return True
        print("Error: No matching appointment found.")
        return False


# Main application
def main():
    # Initialize the booking system
    system = AppointmentBookingSystem()

    while True:
        print("\n--- Barbershop Appointment Booking System ---")
        print("1. View Services")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. Cancel Appointment")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            system.display_services()
        elif choice == 2:
            customer_name = input("Enter your name: ")
            service_name = input("Enter service name (e.g., 'skin_fade' or 'beard_trim'): ").lower()
            try:
                appointment_time = datetime.datetime.strptime(input("Enter appointment time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                system.book_appointment(customer_name, service_name, appointment_time)
            except ValueError:
                print("Error: Invalid date and time format.")
        elif choice == 3:
            system.view_bookings()
        elif choice == 4:
            customer_name = input("Enter your name: ")
            try:
                appointment_time = datetime.datetime.strptime(input("Enter appointment time to cancel (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                system.cancel_appointment(customer_name, appointment_time)
            except ValueError:
                print("Error: Invalid date and time format.")
        elif choice == 5:
            print("Thank you for using the Barbershop Appointment Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
