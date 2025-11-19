"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Write a Python script to automate the booking process for dumpster rentals, allowing users to select dumpster sizes (10, 15, or 20 yards) and schedule delivery in Metro Atlanta based on the service area map.
Generated: DETERMINISTIC_ca2bd78bb79aec06
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DumpsterRental:
    def __init__(self):
        # Available dumpster sizes in yards
        self.available_sizes = [10, 15, 20]
        # Service area for Metro Atlanta (example coordinates)
        self.service_area = {
            "north": (34.0, -84.5),
            "south": (33.5, -84.0),
            "east": (34.0, -84.0),
            "west": (33.5, -84.5)
        }
        # Booking records
        self.bookings = []

    def is_within_service_area(self, location):
        """Check if the provided location is within the service area."""
        lat, lon = location
        return (self.service_area["south"][0] <= lat <= self.service_area["north"][0] and
                self.service_area["west"][1] <= lon <= self.service_area["east"][1])

    def display_available_sizes(self):
        """Display available dumpster sizes."""
        print("Available dumpster sizes (in yards):")
        for size in self.available_sizes:
            print(f"- {size} yards")

    def book_dumpster(self, size, delivery_date, location):
        """Book a dumpster rental."""
        if size not in self.available_sizes:
            raise ValueError("Invalid dumpster size selected.")
        
        if not self.is_within_service_area(location):
            raise ValueError("Location is outside the service area.")

        if delivery_date < datetime.date.today():
            raise ValueError("Delivery date must be today or in the future.")

        booking = {
            "size": size,
            "delivery_date": delivery_date,
            "location": location
        }
        self.bookings.append(booking)
        print(f"Successfully booked a {size}-yard dumpster for delivery on {delivery_date} at {location}.")

    def display_bookings(self):
        """Display all current bookings."""
        if not self.bookings:
            print("No current bookings.")
            return
        
        print("Current bookings:")
        for booking in self.bookings:
            print(f"- {booking['size']} yards, Delivery Date: {booking['delivery_date']}, Location: {booking['location']}")

def main():
    rental_service = DumpsterRental()
    
    # Display available dumpster sizes
    rental_service.display_available_sizes()
    
    # User input for booking
    try:
        size = int(input("Enter the dumpster size you want to book (10, 15, or 20): "))
        delivery_date_input = input("Enter the delivery date (YYYY-MM-DD): ")
        delivery_date = datetime.datetime.strptime(delivery_date_input, "%Y-%m-%d").date()
        location_input = input("Enter your location (latitude, longitude) separated by a comma: ")
        location = tuple(map(float, location_input.split(',')))

        # Book the dumpster
        rental_service.book_dumpster(size, delivery_date, location)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Display all bookings
    rental_service.display_bookings()

if __name__ == "__main__":
    main()
```
