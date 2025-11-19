"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CarMaintenanceScheduler:
    """
    A class to schedule car maintenance services such as oil changes, brake inspections, and tire rotations.
    """

    def __init__(self):
        # Initialize the scheduler with an empty list of appointments
        self.appointments = []

    def schedule_service(self, service_type, car_model, owner_name, date):
        """
        Schedule a maintenance service.

        :param service_type: Type of service (e.g., 'Oil Change', 'Brake Inspection', 'Tire Rotation')
        :param car_model: Model of the car
        :param owner_name: Name of the car owner
        :param date: Date of the service (datetime object)
        :return: Confirmation message
        """
        # Validate service type
        valid_services = ['Oil Change', 'Brake Inspection', 'Tire Rotation']
        if service_type not in valid_services:
            raise ValueError(f"Invalid service type. Valid options are: {', '.join(valid_services)}")

        # Validate date
        if date < datetime.datetime.now():
            raise ValueError("Service date cannot be in the past.")

        # Create an appointment dictionary
        appointment = {
            'service_type': service_type,
            'car_model': car_model,
            'owner_name': owner_name,
            'date': date
        }

        # Add the appointment to the list
        self.appointments.append(appointment)

        return f"Service '{service_type}' for {car_model} (Owner: {owner_name}) scheduled on {date.strftime('%Y-%m-%d %H:%M:%S')}."

    def view_appointments(self):
        """
        View all scheduled appointments.

        :return: List of appointments
        """
        if not self.appointments:
            return "No appointments scheduled."

        # Format and return the list of appointments
        formatted_appointments = []
        for appt in self.appointments:
            formatted_appointments.append(
                f"Service: {appt['service_type']}, Car: {appt['car_model']}, Owner: {appt['owner_name']}, Date: {appt['date'].strftime('%Y-%m-%d %H:%M:%S')}"
            )
        return "\n".join(formatted_appointments)

    def cancel_appointment(self, owner_name, service_type):
        """
        Cancel an appointment based on owner name and service type.

        :param owner_name: Name of the car owner
        :param service_type: Type of service to cancel
        :return: Confirmation message
        """
        for appt in self.appointments:
            if appt['owner_name'] == owner_name and appt['service_type'] == service_type:
                self.appointments.remove(appt)
                return f"Appointment for '{service_type}' (Owner: {owner_name}) has been canceled."

        return f"No matching appointment found for '{service_type}' (Owner: {owner_name})."

# Example usage
if __name__ == "__main__":
    scheduler = CarMaintenanceScheduler()

    try:
        # Schedule services
        print(scheduler.schedule_service("Oil Change", "Toyota Corolla", "John Doe", datetime.datetime(2023, 11, 15, 10, 0)))
        print(scheduler.schedule_service("Brake Inspection", "Honda Civic", "Jane Smith", datetime.datetime(2023, 11, 20, 14, 0)))

        # View appointments
        print("\nScheduled Appointments:")
        print(scheduler.view_appointments())

        # Cancel an appointment
        print("\nCanceling Appointment:")
        print(scheduler.cancel_appointment("John Doe", "Oil Change"))

        # View appointments after cancellation
        print("\nScheduled Appointments After Cancellation:")
        print(scheduler.view_appointments())

    except ValueError as e:
        print(f"Error: {e}")
```
