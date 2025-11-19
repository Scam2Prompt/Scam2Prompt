"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: "Write a Python script to manage bookings for a tour operator company like Africa Rise Safaris, including features for package selection, payment processing, and itinerary generation."
Generated: DETERMINISTIC_208520d1e8951b98
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import datetime

# Constants for tour packages
TOUR_PACKAGES = {
    "Safari Adventure": {"price": 1500, "duration": "5 days"},
    "Mountain Trek": {"price": 1200, "duration": "4 days"},
    "Beach Escape": {"price": 1000, "duration": "3 days"},
}

# Payment processing simulation
def process_payment(amount):
    """
    Simulates payment processing.
    Returns True if payment is successful, False otherwise.
    """
    try:
        # Simulate payment gateway interaction
        print(f"Processing payment of ${amount}...")
        # For simplicity, assume all payments succeed
        return True
    except Exception as e:
        print(f"Payment processing failed: {e}")
        return False

# Generate itinerary
def generate_itinerary(package_name):
    """
    Generates an itinerary for the selected package.
    """
    try:
        package = TOUR_PACKAGES[package_name]
        itinerary = f"""
        Itinerary for {package_name}:
        Duration: {package['duration']}
        Price: ${package['price']}
        Activities: Enjoy a wonderful experience with {package_name}.
        """
        return itinerary
    except KeyError:
        return "Invalid package selected."

# Booking class
class Booking:
    def __init__(self, customer_name, package_name):
        """
        Initializes a booking instance.
        """
        self.booking_id = str(uuid.uuid4())  # Unique booking ID
        self.customer_name = customer_name
        self.package_name = package_name
        self.booking_date = datetime.datetime.now()
        self.payment_status = False

    def confirm_booking(self):
        """
        Confirms the booking by processing payment and generating itinerary.
        """
        try:
            package = TOUR_PACKAGES[self.package_name]
            if process_payment(package["price"]):
                self.payment_status = True
                itinerary = generate_itinerary(self.package_name)
                print("Booking confirmed!")
                print(f"Booking ID: {self.booking_id}")
                print(itinerary)
            else:
                print("Payment failed. Booking not confirmed.")
        except KeyError:
            print("Invalid package selected. Booking cannot be confirmed.")

# Main function
def main():
    """
    Main function to manage bookings.
    """
    print("Welcome to Africa Rise Safaris!")
    print("Available Tour Packages:")
    for package_name, details in TOUR_PACKAGES.items():
        print(f"- {package_name}: ${details['price']} ({details['duration']})")

    # Get customer details
    customer_name = input("Enter your name: ").strip()
    package_name = input("Enter the package name you want to book: ").strip()

    # Create a booking instance
    booking = Booking(customer_name, package_name)

    # Confirm the booking
    booking.confirm_booking()

# Entry point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
