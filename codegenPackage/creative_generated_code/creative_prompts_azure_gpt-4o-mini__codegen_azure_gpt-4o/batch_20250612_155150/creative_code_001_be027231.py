"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule mobile fuel injector cleaning services.
Generated: DETERMINISTIC_be0272316bcb3157
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from uuid import uuid4

# Booking System for Mobile Fuel Injector Cleaning Services

class BookingSystem:
    def __init__(self):
        # Initialize bookings dictionary to store appointments
        self.bookings = {}

    def create_booking(self, customer_name, vehicle_model, service_date, service_time):
        """
        Create a new booking for fuel injector cleaning services.

        Parameters:
            customer_name (str): Name of the customer.
            vehicle_model (str): Model of the customer's vehicle.
            service_date (str): Date of the service in "YYYY-MM-DD" format.
            service_time (str): Time of the service in "HH:MM" format.

        Returns:
            dict: Confirmation details of the booking.
        """
        try:
            # Validate service date and time
            service_datetime = datetime.datetime.strptime(f"{service_date} {service_time}", "%Y-%m-%d %H:%M")
            if service_datetime < datetime.datetime.now():
                raise ValueError("Service date and time cannot be in the past.")

            # Create a unique booking ID
            booking_id = str(uuid4())

            # Save booking details
            self.bookings[booking_id] = {
                "customer_name": customer_name,
                "vehicle_model": vehicle_model,
                "service_date": service_date,
                "service_time": service_time,
                "status": "Scheduled"
            }

            return {
                "message": "Booking successfully created.",
                "booking_id": booking_id,
                "details": self.bookings[booking_id]
            }
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def cancel_booking(self, booking_id):
        """
        Cancel an existing booking.

        Parameters:
            booking_id (str): The unique ID of the booking to cancel.

        Returns:
            dict: Confirmation message of the cancellation.
        """
        try:
            if booking_id not in self.bookings:
                raise ValueError("Booking ID not found.")

            # Update booking status to "Cancelled"
            self.bookings[booking_id]["status"] = "Cancelled"

            return {
                "message": "Booking successfully cancelled.",
                "booking_id": booking_id,
                "details": self.bookings[booking_id]
            }
        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def view_bookings(self):
        """
        View all bookings in the system.

        Returns:
            dict: List of all bookings.
        """
        return {"bookings": self.bookings}


# Example usage
if __name__ == "__main__":
    # Initialize booking system
    booking_system = BookingSystem()

    # Create a new booking
    response = booking_system.create_booking(
        customer_name="John Doe",
        vehicle_model="Toyota Corolla",
        service_date="2023-10-15",
        service_time="10:30"
    )
    print(response)

    # Cancel a booking
    if "booking_id" in response:
        cancel_response = booking_system.cancel_booking(response["booking_id"])
        print(cancel_response)

    # View all bookings
    print(booking_system.view_bookings())
```
