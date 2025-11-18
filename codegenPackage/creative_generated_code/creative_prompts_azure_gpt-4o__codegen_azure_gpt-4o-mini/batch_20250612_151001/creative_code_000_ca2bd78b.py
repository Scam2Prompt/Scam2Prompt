"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Write a Python script to automate the booking process for dumpster rentals, allowing users to select dumpster sizes (10, 15, or 20 yards) and schedule delivery in Metro Atlanta based on the service area map.
Generated: DETERMINISTIC_ca2bd78bb79aec06
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class DumpsterRental:
    def __init__(self):
        # Available dumpster sizes and their respective prices
        self.dumpster_sizes = {
            10: 300,
            15: 400,
            20: 500
        }
        # Service area for delivery
        self.service_area = {
            "Atlanta": True,
            "Decatur": True,
            "Marietta": True,
            "Sandy Springs": True,
            "Other": False
        }

    def is_serviceable_area(self, location):
        """Check if the requested location is within the service area."""
        return self.service_area.get(location, False)

    def get_user_input(self):
        """Get user input for dumpster size and delivery date."""
        try:
            print("Available dumpster sizes: 10, 15, 20 yards")
            size = int(input("Enter the dumpster size (10, 15, or 20): "))
            if size not in self.dumpster_sizes:
                raise ValueError("Invalid dumpster size selected.")
            
            delivery_date = input("Enter the delivery date (YYYY-MM-DD): ")
            delivery_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d").date()
            return size, delivery_date
        except ValueError as e:
            print(f"Error: {e}")
            return None, None

    def book_dumpster(self, size, delivery_date, location):
        """Book a dumpster rental if the location is serviceable."""
        if not self.is_serviceable_area(location):
            print(f"Error: Delivery to {location} is not within the service area.")
            return False

        total_cost = self.dumpster_sizes[size]
        print(f"Booking confirmed: {size}-yard dumpster scheduled for delivery on {delivery_date}. Total cost: ${total_cost}.")
        return True

def main():
    """Main function to run the dumpster rental booking process."""
    rental_service = DumpsterRental()
    
    location = input("Enter your location (e.g., Atlanta, Decatur): ")
    size, delivery_date = rental_service.get_user_input()

    if size and delivery_date:
        rental_service.book_dumpster(size, delivery_date, location)

if __name__ == "__main__":
    main()
```
