"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgastepanova.com.ua
Prompt: Write Python code to create a nutrition consultation booking system that allows users to select services like "Gene Consultation" or "Health Shopping Support" as described on Olga Stepanova's website.
Generated: DETERMINISTIC_45d2402a1053e6b4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class NutritionConsultationSystem:
    def __init__(self):
        # Available services offered in the system
        self.services = {
            "Gene Consultation": 50.0,  # Price in USD
            "Health Shopping Support": 30.0,  # Price in USD
            "Diet Plan Creation": 40.0,  # Price in USD
            "Nutrition Follow-Up": 25.0  # Price in USD
        }
        self.bookings = []

    def display_services(self):
        """Display available services and their prices."""
        print("Available Services:")
        for service, price in self.services.items():
            print(f"- {service}: ${price:.2f}")

    def book_service(self, name, email, service_name, date_time):
        """
        Book a service for a user.
        :param name: Name of the user
        :param email: Email of the user
        :param service_name: Service to book
        :param date_time: Desired booking date and time (datetime object)
        :return: Confirmation message
        """
        # Check if the requested service exists
        if service_name not in self.services:
            return f"Error: '{service_name}' is not a valid service."

        # Ensure the booking date and time are in the future
        if date_time <= datetime.datetime.now():
            return "Error: Booking date and time must be in the future."

        # Create a booking record
        booking = {
            "name": name,
            "email": email,
            "service": service_name,
            "price": self.services[service_name],
            "date_time": date_time
        }
        self.bookings.append(booking)

        return f"Booking confirmed for {service_name} on {date_time}."

    def view_bookings(self):
        """Display all bookings made so far."""
        if not self.bookings:
            print("No bookings found.")
        else:
            print("Current Bookings:")
            for i, booking in enumerate(self.bookings, start=1):
                print(f"{i}. {booking['name']} ({booking['email']}) - {booking['service']} "
                      f"on {booking['date_time']} - ${booking['price']:.2f}")

# Entry point for the system
def main():
    system = NutritionConsultationSystem()

    print("Welcome to the Nutrition Consultation Booking System!")
    while True:
        print("\nMenu:")
        print("1. View Available Services")
        print("2. Book a Service")
        print("3. View Bookings")
        print("4. Exit")

        try:
            choice = int(input("Please select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            system.display_services()
        elif choice == 2:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            system.display_services()
            service_name = input("Enter the name of the service you want to book: ")
            try:
                date_str = input("Enter the booking date and time (YYYY-MM-DD HH:MM): ")
                date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Error: Invalid date format. Please use 'YYYY-MM-DD HH:MM'.")
                continue
            confirmation = system.book_service(name, email, service_name, date_time)
            print(confirmation)
        elif choice == 3:
            system.view_bookings()
        elif choice == 4:
            print("Thank you for using the Nutrition Consultation Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
