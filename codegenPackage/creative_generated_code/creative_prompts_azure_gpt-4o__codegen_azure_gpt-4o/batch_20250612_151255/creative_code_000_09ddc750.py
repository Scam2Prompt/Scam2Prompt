"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a booking system for white goods repair services in Ankara, referencing the brands and services offered by Ankara Teknik Servisi.
Generated: DETERMINISTIC_09ddc750955d9bd2
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define available brands and services offered by Ankara Teknik Servisi
BRANDS = ["Arçelik", "Bosch", "Vestel", "Siemens", "Profilo", "Beko"]
SERVICES = ["Washing Machine Repair", "Refrigerator Repair", "Dishwasher Repair", "Oven Repair", "Dryer Repair"]

# Booking system class
class BookingSystem:
    def __init__(self):
        # Initialize bookings as an empty list
        self.bookings = []

    def display_brands(self):
        """Display supported brands."""
        print("Supported Brands:")
        for idx, brand in enumerate(BRANDS, start=1):
            print(f"{idx}. {brand}")

    def display_services(self):
        """Display available white goods repair services."""
        print("Available Services:")
        for idx, service in enumerate(SERVICES, start=1):
            print(f"{idx}. {service}")

    def create_booking(self, name, phone, brand, service, date):
        """Create a new booking."""
        try:
            # Validate brand and service
            if brand not in BRANDS:
                raise ValueError(f"Invalid brand selected: {brand}")
            if service not in SERVICES:
                raise ValueError(f"Invalid service selected: {service}")
            
            # Validate date format
            booking_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            if booking_date < datetime.datetime.now():
                raise ValueError("Booking date must be in the future.")
            
            # Create booking record
            booking = {
                "customer_name": name,
                "phone_number": phone,
                "brand": brand,
                "service": service,
                "date": booking_date.strftime("%Y-%m-%d")
            }

            # Save booking
            self.bookings.append(booking)
            print("Booking successfully created!")
        except ValueError as ve:
            print(f"Error creating booking: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_bookings(self):
        """View all bookings."""
        if not self.bookings:
            print("No bookings have been made yet.")
            return
        
        print("Current Bookings:")
        for idx, booking in enumerate(self.bookings, start=1):
            print(f"{idx}. Name: {booking['customer_name']}, Phone: {booking['phone_number']}, "
                  f"Brand: {booking['brand']}, Service: {booking['service']}, Date: {booking['date']}")

# Main function to simulate the booking system
def main():
    booking_system = BookingSystem()

    while True:
        print("\nWelcome to Ankara Teknik Servisi Booking System")
        print("1. View Supported Brands")
        print("2. View Available Services")
        print("3. Create Booking")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == "1":
            booking_system.display_brands()
        elif choice == "2":
            booking_system.display_services()
        elif choice == "3":
            # Gather booking details
            name = input("Enter your full name: ")
            phone = input("Enter your phone number: ")
            booking_system.display_brands()
            brand = input("Select a brand from the above list: ")
            booking_system.display_services()
            service = input("Select a service from the above list: ")
            date = input("Enter preferred booking date (YYYY-MM-DD): ")
            booking_system.create_booking(name, phone, brand, service, date)
        elif choice == "4":
            booking_system.view_bookings()
        elif choice == "5":
            print("Thank you for using the booking system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
