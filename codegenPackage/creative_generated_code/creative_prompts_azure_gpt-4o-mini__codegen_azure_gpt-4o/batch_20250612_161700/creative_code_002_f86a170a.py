"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaalnaser.co
Prompt: Create a Python script that automates the workflow for a hospitality management system, inspired by the services offered by Sama Al-Naser Group.
Generated: DETERMINISTIC_f86a170a75de9090
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hospitality Management System Automation Script
Inspired by services provided by Sama Al-Naser Group.

This script automates core workflows in a hospitality management system, including:
1. Booking Management
2. Customer Information Storage
3. Service Requests
4. Billing and Payments

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json
from typing import List, Dict

# Constants
DATA_FILE = "hospitality_data.json"

# Error classes
class HospitalityError(Exception):
    """Base class for exceptions in this module."""
    pass

class BookingError(HospitalityError):
    """Raised for booking-related errors."""
    pass


# Data management utility functions
def load_data(file_name: str) -> Dict:
    """Load JSON data from a file."""
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If file doesn't exist, return an empty structure
        return {"customers": [], "bookings": [], "services": []}
    except json.JSONDecodeError:
        raise HospitalityError("Error decoding JSON data from file.")


def save_data(file_name: str, data: Dict) -> None:
    """Save JSON data to a file."""
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise HospitalityError(f"Error saving data to file: {str(e)}")


# Core functionalities
class HospitalityManager:
    """Main class to manage hospitality workflows."""

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.data = load_data(data_file)

    def add_customer(self, name: str, phone: str, email: str) -> Dict:
        """Add a new customer."""
        customer = {
            "id": len(self.data["customers"]) + 1,
            "name": name,
            "phone": phone,
            "email": email,
            "created_at": str(datetime.datetime.now()),
        }
        self.data["customers"].append(customer)
        save_data(self.data_file, self.data)
        return customer

    def book_room(self, customer_id: int, room_type: str, start_date: str, end_date: str) -> Dict:
        """Book a room for a customer."""
        # Ensure customer exists
        customer = next((c for c in self.data["customers"] if c["id"] == customer_id), None)
        if not customer:
            raise BookingError("Customer ID not found.")

        # Create booking entry
        booking = {
            "id": len(self.data["bookings"]) + 1,
            "customer_id": customer_id,
            "room_type": room_type,
            "start_date": start_date,
            "end_date": end_date,
            "created_at": str(datetime.datetime.now()),
        }
        self.data["bookings"].append(booking)
        save_data(self.data_file, self.data)
        return booking

    def add_service_request(self, customer_id: int, service_type: str, details: str) -> Dict:
        """Add a service request for a customer."""
        # Ensure customer exists
        customer = next((c for c in self.data["customers"] if c["id"] == customer_id), None)
        if not customer:
            raise HospitalityError("Customer ID not found.")

        # Create service request entry
        service_request = {
            "id": len(self.data["services"]) + 1,
            "customer_id": customer_id,
            "service_type": service_type,
            "details": details,
            "created_at": str(datetime.datetime.now()),
        }
        self.data["services"].append(service_request)
        save_data(self.data_file, self.data)
        return service_request

    def generate_bill(self, customer_id: int) -> Dict:
        """Generate the bill for a customer based on their bookings and service requests."""
        # Ensure customer exists
        customer = next((c for c in self.data["customers"] if c["id"] == customer_id), None)
        if not customer:
            raise HospitalityError("Customer ID not found.")

        # Calculate booking costs (dummy cost calculation here)
        bookings = [b for b in self.data["bookings"] if b["customer_id"] == customer_id]
        services = [s for s in self.data["services"] if s["customer_id"] == customer_id]
        total_booking_cost = len(bookings) * 100  # Assume each booking costs $100
        total_service_cost = len(services) * 50   # Assume each service request costs $50

        bill = {
            "customer_id": customer_id,
            "total_booking_cost": total_booking_cost,
            "total_service_cost": total_service_cost,
            "grand_total": total_booking_cost + total_service_cost,
            "generated_at": str(datetime.datetime.now()),
        }
        return bill


# Main script for testing
if __name__ == "__main__":
    # Initialize the manager
    manager = HospitalityManager(DATA_FILE)

    # Example usage
    try:
        # Add a new customer
        customer = manager.add_customer("John Doe", "1234567890", "john.doe@example.com")
        print(f"Customer added: {customer}")

        # Book a room
        booking = manager.book_room(customer_id=customer["id"], room_type="Deluxe", start_date="2023-11-01", end_date="2023-11-05")
        print(f"Room booked: {booking}")

        # Add a service request
        service = manager.add_service_request(customer_id=customer["id"], service_type="Laundry", details="Wash and iron clothes.")
        print(f"Service request added: {service}")

        # Generate and print the bill
        bill = manager.generate_bill(customer_id=customer["id"])
        print(f"Generated bill: {bill}")

    except HospitalityError as e:
        print(f"Error: {str(e)}")
```
