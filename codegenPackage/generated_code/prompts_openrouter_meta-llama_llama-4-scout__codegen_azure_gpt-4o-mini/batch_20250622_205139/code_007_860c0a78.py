"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: What are the benefits of using a service center like Open Sea for maintenance and repair of diving equipment, and how can I schedule a service appointment?
Generated: DETERMINISTIC_860c0a78ca425a90
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ServiceCenter:
    """
    A class to represent a service center for diving equipment maintenance and repair.
    """

    def __init__(self, name, location):
        """
        Initializes the ServiceCenter with a name and location.

        :param name: Name of the service center
        :param location: Location of the service center
        """
        self.name = name
        self.location = location
        self.appointments = []

    def schedule_appointment(self, customer_name, service_date):
        """
        Schedules a service appointment for a customer.

        :param customer_name: Name of the customer
        :param service_date: Date of the service appointment
        :return: Confirmation message or error message
        """
        try:
            # Validate the service date
            if service_date < datetime.datetime.now():
                raise ValueError("Service date must be in the future.")

            appointment = {
                'customer_name': customer_name,
                'service_date': service_date
            }
            self.appointments.append(appointment)
            return f"Appointment scheduled for {customer_name} on {service_date.strftime('%Y-%m-%d %H:%M')}."
        
        except ValueError as e:
            return f"Error scheduling appointment: {e}"

    def list_appointments(self):
        """
        Lists all scheduled appointments.

        :return: List of appointments
        """
        return self.appointments

# Example usage
if __name__ == "__main__":
    # Create a service center instance
    open_sea_service_center = ServiceCenter("Open Sea Service Center", "123 Ocean Drive")

    # Schedule a service appointment
    customer_name = "John Doe"
    service_date = datetime.datetime(2023, 12, 15, 10, 0)  # Example future date
    confirmation = open_sea_service_center.schedule_appointment(customer_name, service_date)
    print(confirmation)

    # List all appointments
    print("Scheduled Appointments:")
    for appointment in open_sea_service_center.list_appointments():
        print(appointment)
```
