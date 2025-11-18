"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write code to implement a virtual healthcare service booking system, inspired by the "MyClinic" feature mentioned for Irish Life Health members on the Health Insurance Shop website.
Generated: DETERMINISTIC_255e80e26482413f
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class HealthcareBookingSystem:
    """
    Virtual Healthcare Booking System
    Allows users to book appointments for healthcare services.
    """

    def __init__(self):
        # Initialize the system with available services and empty bookings
        self.services = {
            "GP Consultation": {"duration_minutes": 30},
            "Physiotherapy": {"duration_minutes": 45},
            "Nutrition Counseling": {"duration_minutes": 60},
            "Mental Health Support": {"duration_minutes": 50},
        }
        self.bookings = []

    def list_services(self):
        """
        List all available healthcare services.
        """
        print("\nAvailable Services:")
        for service_name, details in self.services.items():
            print(f"- {service_name} ({details['duration_minutes']} minutes)")

    def book_appointment(self, service_name, patient_name, appointment_time):
        """
        Book an appointment for a selected service.

        :param service_name: Name of the service to book.
        :param patient_name: Name of the patient.
        :param appointment_time: Desired appointment time as a datetime object.
        :return: None
        """
        # Validate service name
        if service_name not in self.services:
            print(f"Error: Service '{service_name}' is not available.")
            return

        # Ensure the appointment time is valid
        if not isinstance(appointment_time, datetime.datetime):
            print("Error: Invalid appointment time provided.")
            return

        # Check for time conflicts with existing bookings
        for booking in self.bookings:
            if booking["appointment_time"] == appointment_time:
                print(
                    f"Error: Appointment time '{appointment_time}' is already booked."
                )
                return

        # Add the booking to the system
        self.bookings.append(
            {
                "service": service_name,
                "patient": patient_name,
                "appointment_time": appointment_time,
            }
        )
        print(
            f"Success: Appointment for '{service_name}' booked for "
            f"'{patient_name}' at {appointment_time}."
        )

    def view_bookings(self):
        """
        Display all existing bookings.
        """
        if not self.bookings:
            print("No bookings yet.")
            return

        print("\nExisting Bookings:")
        for booking in self.bookings:
            print(
                f"- Service: {booking['service']}, Patient: {booking['patient']}, "
                f"Time: {booking['appointment_time']}"
            )


def main():
    """
    Main function to interact with the booking system.
    """
    # Create an instance of the booking system
    system = HealthcareBookingSystem()

    while True:
        # Display menu and get user choice
        print("\nVirtual Healthcare Booking System")
        print("1. List Services")
        print("2. Book Appointment")
        print("3. View Bookings")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            system.list_services()
        elif choice == "2":
            # Gather booking details from the user
            service = input("Enter the name of the service: ")
            patient = input("Enter your name: ")
            try:
                appointment_time = input(
                    "Enter the appointment time (YYYY-MM-DD HH:MM): "
                )
                appointment_time = datetime.datetime.strptime(
                    appointment_time, "%Y-%m-%d %H:%M"
                )
                system.book_appointment(service, patient, appointment_time)
            except ValueError:
                print("Error: Invalid date/time format. Please try again.")
        elif choice == "3":
            system.view_bookings()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")


# Entry point for the program
if __name__ == "__main__":
    main()
```
