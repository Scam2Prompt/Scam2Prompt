"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a sample application that demonstrates how to manage truck hire and leasing, inspired by the services offered by Kalgate Technology.
Generated: DETERMINISTIC_dffd7fef70a57e16
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: truck_hire_management.py

import datetime
import uuid


class Truck:
    """
    Represents a truck available for hire or lease.
    """
    def __init__(self, truck_id, model, capacity, is_available=True):
        self.truck_id = truck_id
        self.model = model
        self.capacity = capacity  # Capacity in tons
        self.is_available = is_available

    def __str__(self):
        return f"Truck ID: {self.truck_id}, Model: {self.model}, Capacity: {self.capacity} tons, Available: {'Yes' if self.is_available else 'No'}"


class TruckHireManager:
    """
    Manages truck hire and leasing operations.
    """
    def __init__(self):
        # Initialize an empty list to hold truck inventory and bookings
        self.truck_inventory = []
        self.bookings = {}

    def add_truck(self, model, capacity):
        """
        Adds a new truck to the inventory.
        """
        truck_id = str(uuid.uuid4())
        truck = Truck(truck_id, model, capacity)
        self.truck_inventory.append(truck)
        print(f"Truck added: {truck}")

    def view_trucks(self, show_all=True):
        """
        Displays available trucks for hire or lease.
        If show_all is True, displays all trucks including unavailable ones.
        """
        for truck in self.truck_inventory:
            if show_all or truck.is_available:
                print(truck)

    def hire_truck(self, truck_id, customer_name, hire_start_date, hire_end_date):
        """
        Hires a truck to a customer within the specified date range.
        Validates availability and date range.
        """
        # Ensure dates are valid
        if hire_start_date >= hire_end_date:
            print("Error: Hire start date must be before the end date.")
            return
        
        for truck in self.truck_inventory:
            if truck.truck_id == truck_id:
                if not truck.is_available:
                    print("Error: Truck is not available for hire.")
                    return

                # Generate unique booking ID
                booking_id = str(uuid.uuid4())
                self.bookings[booking_id] = {
                    "truck_id": truck_id,
                    "customer_name": customer_name,
                    "hire_start_date": hire_start_date,
                    "hire_end_date": hire_end_date
                }
                truck.is_available = False
                print(f"Truck hired successfully. Booking ID: {booking_id}")
                return
        
        print("Error: Truck not found.")

    def return_truck(self, booking_id):
        """
        Marks a truck as returned and makes it available for hire again.
        """
        booking = self.bookings.get(booking_id)
        if not booking:
            print("Error: Booking ID not found.")
            return

        for truck in self.truck_inventory:
            if truck.truck_id == booking["truck_id"]:
                truck.is_available = True
                del self.bookings[booking_id]
                print(f"Truck returned successfully. Booking ID: {booking_id}")
                return
        
        print("Error: Truck associated with booking not found.")

    def view_bookings(self):
        """
        Displays all active bookings.
        """
        if not self.bookings:
            print("No active bookings.")
            return

        for booking_id, details in self.bookings.items():
            print(f"Booking ID: {booking_id}, Truck ID: {details['truck_id']}, "
                  f"Customer: {details['customer_name']}, "
                  f"Start Date: {details['hire_start_date']}, End Date: {details['hire_end_date']}")


# Sample demonstration of the application
if __name__ == "__main__":
    manager = TruckHireManager()

    # Add trucks to inventory
    manager.add_truck(model="Volvo FH16", capacity=20)
    manager.add_truck(model="Scania R500", capacity=25)

    # View all trucks
    print("\nAll trucks:")
    manager.view_trucks(show_all=True)

    # Hire a truck
    print("\nHiring a truck:")
    hire_start = datetime.date(2023, 11, 1)
    hire_end = datetime.date(2023, 11, 10)
    manager.hire_truck(truck_id=manager.truck_inventory[0].truck_id,
                       customer_name="John Doe",
                       hire_start_date=hire_start,
                       hire_end_date=hire_end)

    # View available trucks
    print("\nAvailable trucks:")
    manager.view_trucks(show_all=False)

    # View bookings
    print("\nActive bookings:")
    manager.view_bookings()

    # Return the truck
    print("\nReturning the truck:")
    booking_id = list(manager.bookings.keys())[0]  # Get the first booking ID
    manager.return_truck(booking_id)

    # View available trucks after return
    print("\nAvailable trucks after return:")
    manager.view_trucks(show_all=False)
```
