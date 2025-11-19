"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phuketmedicalclinic.com
Prompt: Generate a Python script to automate the process of booking an appointment at a medical clinic, incorporating features like patient details and service selection.
Generated: DETERMINISTIC_58bd2a85e79f9ada
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

# Define the classes and functions for the appointment booking system
class AppointmentSystem:
    """
    A class to manage the appointment booking process for a medical clinic.
    """

    def __init__(self):
        """
        Initialize the system with available services and patient database.
        """
        self.services = {
            1: "General Consultation",
            2: "Pediatric Consultation",
            3: "Dermatology",
            4: "Orthopedics",
            5: "Cardiology",
        }
        self.patients = []

    def display_services(self):
        """
        Display the list of available services.
        """
        print("\nAvailable Services:")
        for key, value in self.services.items():
            print(f"{key}. {value}")

    def get_patient_details(self):
        """
        Collect patient details from the user.
        Returns:
            dict: A dictionary containing patient details.
        """
        print("\nEnter Patient Details:")
        try:
            name = input("Full Name: ")
            age = int(input("Age: "))
            phone = input("Phone Number: ")
            email = input("Email Address: ")
            return {
                "name": name,
                "age": age,
                "phone": phone,
                "email": email,
            }
        except ValueError as ve:
            print(f"Error: Invalid input. {ve}")
            return None

    def select_service(self):
        """
        Allow the user to select a service.
        Returns:
            str: The name of the selected service.
        """
        self.display_services()
        try:
            service_id = int(input("\nEnter the number corresponding to your service choice: "))
            if service_id in self.services:
                return self.services[service_id]
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError as ve:
            print(f"Error: Invalid input. {ve}")
            return None

    def book_appointment(self):
        """
        Automate the process of booking an appointment.
        """
        print("\n--- Appointment Booking ---")
        patient_details = self.get_patient_details()
        if not patient_details:
            print("Failed to collect patient details. Appointment booking aborted.")
            return

        selected_service = self.select_service()
        if not selected_service:
            print("Failed to select a service. Appointment booking aborted.")
            return

        appointment_date = input("\nEnter preferred appointment date (YYYY-MM-DD): ")
        try:
            # Validate appointment date format
            appointment_date = datetime.datetime.strptime(appointment_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Appointment booking aborted.")
            return

        # Generate appointment details
        appointment = {
            "patient": patient_details,
            "service": selected_service,
            "date": str(appointment_date),
        }
        self.patients.append(appointment)
        self.save_appointment_to_file(appointment)
        print("\nAppointment successfully booked!")
        print("Appointment Details:")
        print(json.dumps(appointment, indent=4))

    def save_appointment_to_file(self, appointment):
        """
        Save appointment details to a file for record-keeping.
        Args:
            appointment (dict): The appointment details to save.
        """
        try:
            with open("appointments.json", "a") as file:
                file.write(json.dumps(appointment) + "\n")
        except IOError as io_err:
            print(f"Error saving appointment to file: {io_err}")

# Run the script
if __name__ == "__main__":
    print("Welcome to the Medical Clinic Appointment Booking System!")
    system = AppointmentSystem()
    system.book_appointment()
```
