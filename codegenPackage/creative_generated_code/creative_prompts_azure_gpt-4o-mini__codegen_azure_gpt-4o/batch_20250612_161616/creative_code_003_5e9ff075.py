"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Develop a code snippet that integrates a booking system for Alice Beauty's services, allowing users to choose from over 20 different procedures.
Generated: DETERMINISTIC_5e9ff075fffa0c97
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Booking system for Alice Beauty's services
class AliceBeautyBookingSystem:
    def __init__(self):
        # List of available services
        self.services = [
            "Haircut", "Facial", "Makeup", "Manicure", "Pedicure", "Waxing",
            "Eyebrow Shaping", "Eyelash Extension", "Hair Coloring", "Massage",
            "Body Scrub", "Hair Treatment", "Skin Treatment", "Threading", "Tanning",
            "Spa Therapy", "Scalp Massage", "Anti-Aging Treatment", "Nail Art",
            "Bridal Makeup", "Dermaplaning"
        ]
        self.bookings = []

    def display_services(self):
        """Displays the list of available services."""
        print("Welcome to Alice Beauty's services. Here is the list of procedures you can choose from:")
        for index, service in enumerate(self.services, start=1):
            print(f"{index}. {service}")

    def book_service(self):
        """Allows user to book a specific service."""
        try:
            self.display_services()
            # Prompt the user to select a service
            service_choice = int(input("\nEnter the number of the procedure you'd like to book: "))
            if service_choice < 1 or service_choice > len(self.services):
                raise ValueError("Invalid choice. Please select a valid service number.")

            selected_service = self.services[service_choice - 1]
            
            # Prompt the user for the booking date
            date_input = input("Enter your preferred date for the service (YYYY-MM-DD): ")
            booking_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

            # Confirm the booking and store it
            confirmation = input(
                f"You have selected '{selected_service}' on {booking_date}. Confirm booking? (yes/no): ").strip().lower()
            
            if confirmation == "yes":
                self.bookings.append({"service": selected_service, "date": booking_date})
                print(f"Booking confirmed: {selected_service} on {booking_date}.")
            else:
                print("Booking canceled.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_bookings(self):
        """Displays all confirmed bookings."""
        if not self.bookings:
            print("No bookings available.")
        else:
            print("Your bookings:")
            for booking in self.bookings:
                print(f"- {booking['service']} on {booking['date']}")

# Main function to run the booking system
def main():
    system = AliceBeautyBookingSystem()
    
    while True:
        print("\nMenu:")
        print("1. View Services")
        print("2. Book a Service")
        print("3. View Bookings")
        print("4. Exit")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                system.display_services()
            elif choice == 2:
                system.book_service()
            elif choice == 3:
                system.view_bookings()
            elif choice == 4:
                print("Thank you for using Alice Beauty's booking system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid menu option.")
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
