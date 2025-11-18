"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Write Python code to create a scheduling system for mobile RV repair services within a 100-mile radius of Phoenix, Arizona, incorporating appointment booking and repair status tracking.
Generated: DETERMINISTIC_01d2b6ac90f6b88c
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid


class Appointment:
    """
    Represents an Appointment for RV repair service.
    """
    def __init__(self, customer_name, customer_contact, location, date_time):
        self.id = str(uuid.uuid4())  # Unique ID for the appointment
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.location = location
        self.date_time = date_time
        self.status = "Scheduled"  # Default status is 'Scheduled'

    def update_status(self, new_status):
        """
        Updates the status of the appointment.
        :param new_status: New status for the appointment (e.g., 'In Progress', 'Completed').
        """
        if new_status in ['Scheduled', 'In Progress', 'Completed', 'Cancelled']:
            self.status = new_status
        else:
            raise ValueError("Invalid status. Allowed statuses: Scheduled, In Progress, Completed, Cancelled")


class Scheduler:
    """
    Handles scheduling and tracking of RV repair appointments.
    """
    def __init__(self):
        self.appointments = []  # List to store all appointments

    def validate_location(self, location):
        """
        Validates if the location is within the 100-mile radius of Phoenix, AZ.
        :param location: Tuple of latitude and longitude (lat, lon).
        :return: True if location is valid, False otherwise.
        """
        phoenix_coordinates = (33.4484, -112.0740)  # Latitude and longitude of Phoenix, AZ
        distance = self.calculate_distance(phoenix_coordinates, location)
        return distance <= 100

    @staticmethod
    def calculate_distance(coord1, coord2):
        """
        Calculates distance between two coordinates using the Haversine formula.
        :param coord1: Tuple of latitude and longitude for the first location (lat1, lon1).
        :param coord2: Tuple of latitude and longitude for the second location (lat2, lon2).
        :return: Distance in miles.
        """
        from math import radians, sin, cos, sqrt, atan2

        # Haversine formula
        R = 3958.8  # Radius of Earth in miles
        lat1, lon1 = coord1
        lat2, lon2 = coord2

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    def book_appointment(self, customer_name, customer_contact, location, date_time):
        """
        Books a new appointment if the location is valid and the time is available.
        :param customer_name: Name of the customer.
        :param customer_contact: Contact information of the customer.
        :param location: Tuple of latitude and longitude for the appointment (lat, lon).
        :param date_time: Date and time of the appointment (datetime object).
        :return: Appointment object if booking is successful.
        """
        if not self.validate_location(location):
            raise ValueError("Location is outside the 100-mile radius of Phoenix, AZ.")

        # Check for time conflicts
        for appointment in self.appointments:
            if appointment.date_time == date_time:
                raise ValueError("The appointment slot is already booked.")

        # Create and store the new appointment
        new_appointment = Appointment(customer_name, customer_contact, location, date_time)
        self.appointments.append(new_appointment)
        return new_appointment

    def get_appointments(self):
        """
        Retrieves all scheduled appointments.
        :return: List of all appointments.
        """
        return self.appointments

    def update_appointment_status(self, appointment_id, new_status):
        """
        Updates the status of an existing appointment.
        :param appointment_id: ID of the appointment to update.
        :param new_status: New status for the appointment.
        """
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                appointment.update_status(new_status)
                return appointment
        raise ValueError("Appointment not found.")

    def cancel_appointment(self, appointment_id):
        """
        Cancels an appointment and removes it from the schedule.
        :param appointment_id: ID of the appointment to cancel.
        """
        for appointment in self.appointments:
            if appointment.id == appointment_id:
                self.appointments.remove(appointment)
                return appointment
        raise ValueError("Appointment not found.")


# Example usage:
if __name__ == "__main__":
    scheduler = Scheduler()

    try:
        # Book an appointment
        appointment = scheduler.book_appointment(
            customer_name="John Doe",
            customer_contact="555-1234",
            location=(33.5, -112.1),  # Latitude and longitude within radius
            date_time=datetime.datetime(2023, 11, 15, 10, 0)  # Date and time of the appointment
        )
        print(f"Appointment booked successfully: {appointment.id}")

        # Retrieve all appointments
        all_appointments = scheduler.get_appointments()
        for appt in all_appointments:
            print(f"Appointment ID: {appt.id}, Status: {appt.status}")

        # Update appointment status
        updated_appointment = scheduler.update_appointment_status(appointment.id, "In Progress")
        print(f"Updated status: {updated_appointment.status}")

        # Cancel an appointment
        canceled_appointment = scheduler.cancel_appointment(appointment.id)
        print(f"Canceled appointment: {canceled_appointment.id}")

    except ValueError as e:
        print(f"Error: {e}")
```
