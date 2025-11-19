"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Generate a Python script that automates the booking process for a residential cleaning service, similar to the offerings of Maria HouseKeepers in San Fernando Valley, CA.
Generated: DETERMINISTIC_abdbca8534d4c4aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class CleaningServiceBooking:
    """
    Class to handle the booking process for a residential cleaning service.
    """

    def __init__(self, service_file="services.json"):
        self.service_file = service_file
        self.services = self.load_services()

    def load_services(self):
        """
        Load cleaning service offerings from a JSON file.
        """
        if not os.path.exists(self.service_file):
            raise FileNotFoundError(f"{self.service_file} not found. Please ensure the file exists.")
        try:
            with open(self.service_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError("Error decoding JSON file: " + str(e))

    def display_services(self):
        """
        Display the available cleaning services.
        """
        print("Available Cleaning Services:")
        for index, service in enumerate(self.services, start=1):
            print(f"{index}. {service['name']} - ${service['price']:.2f}")

    def make_booking(self):
        """
        Handle the booking process interactively.
        """
        try:
            self.display_services()
            choice = int(input("Enter the number of the service you'd like to book: "))

            if choice < 1 or choice > len(self.services):
                print("Invalid choice. Please select a valid service number.")
                return

            selected_service = self.services[choice - 1]
            print(f"You selected: {selected_service['name']} (${selected_service['price']:.2f})")

            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return

            email = input("Enter your email: ").strip()
            if not email or "@" not in email or "." not in email:
                print("Invalid email. Please enter a valid email address.")
                return

            phone = input("Enter your phone number: ").strip()
            if not phone.isdigit():
                print("Invalid phone number. Please enter a valid numeric phone number.")
                return

            address = input("Enter the service address: ").strip()
            if not address:
                print("Address cannot be empty.")
                return

            date_str = input("Enter the service date (YYYY-MM-DD): ").strip()
            try:
                service_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if service_date < datetime.date.today():
                    print("Service date cannot be in the past.")
                    return
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                return

            # Confirm booking details
            self.confirm_booking(
                name=name,
                email=email,
                phone=phone,
                address=address,
                service_date=service_date,
                selected_service=selected_service
            )

        except Exception as e:
            print("An error occurred during the booking process:", str(e))

    def confirm_booking(self, name, email, phone, address, service_date, selected_service):
        """
        Confirm booking details and save the booking information.
        """
        print("\nBooking Details:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        print(f"Service: {selected_service['name']}")
        print(f"Date: {service_date}")
        print(f"Price: ${selected_service['price']:.2f}")

        confirm = input("Confirm booking? (yes/no): ").strip().lower()
        if confirm == "yes":
            booking_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "service": selected_service,
                "date": str(service_date)
            }
            self.save_booking(booking_data)
            print("Booking confirmed! Thank you for using our service.")
        else:
            print("Booking canceled.")

    def save_booking(self, booking_data):
        """
        Save booking information to a file.
        """
        try:
            with open("bookings.json", "a") as file:
                file.write(json.dumps(booking_data) + "\n")
        except Exception as e:
            print("Error saving booking information:", str(e))


if __name__ == "__main__":
    # Instantiate the booking system
    cleaning_service = CleaningServiceBooking()
    cleaning_service.make_booking()
```

**Note:** The script assumes the presence of a `services.json` file that contains service offerings in a JSON format. For example:
```json
[
    {"name": "Basic Cleaning", "price": 50},
    {"name": "Deep Cleaning", "price": 120},
    {"name": "Move-in/Move-out Cleaning", "price": 200}
]
```
