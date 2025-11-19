"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate a code snippet for an HVAC service appointment booking system that includes options for maintenance service agreements as mentioned on Quality Sheet Metal, Inc.'s website.
Generated: DETERMINISTIC_3b1c4832eb62203c
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ServiceAppointment:
    def __init__(self, client_name, service_type, appointment_date):
        """
        Initializes a ServiceAppointment instance.

        :param client_name: Name of the client
        :param service_type: Type of service requested (e.g., Maintenance, Repair, Installation)
        :param appointment_date: Date and time of the appointment
        """
        self.client_name = client_name
        self.service_type = service_type
        self.appointment_date = appointment_date

    def __str__(self):
        """Returns a string representation of the service appointment."""
        return f"Appointment for {self.client_name} on {self.appointment_date} for {self.service_type}"

class MaintenanceServiceAgreement:
    def __init__(self, agreement_type, duration_months):
        """
        Initializes a MaintenanceServiceAgreement instance.

        :param agreement_type: Type of maintenance agreement (e.g., Basic, Premium)
        :param duration_months: Duration of the agreement in months
        """
        self.agreement_type = agreement_type
        self.duration_months = duration_months

    def calculate_cost(self):
        """
        Calculates the cost of the maintenance agreement based on the type and duration.

        :return: Cost of the agreement
        """
        base_cost = 100  # Base cost for a basic service agreement
        if self.agreement_type == 'Premium':
            base_cost = 150  # Premium agreement cost

        return base_cost * self.duration_months

def book_service_appointment(client_name, service_type, appointment_date, agreement=None):
    """
    Books a service appointment with optional maintenance service agreement.

    :param client_name: Name of the client
    :param service_type: Type of service requested
    :param appointment_date: Date and time of the appointment
    :param agreement: Optional MaintenanceServiceAgreement object
    :return: Confirmation message and details of appointment
    """
    try:
        # Validate appointment date
        if appointment_date < datetime.datetime.now():
            raise ValueError("Appointment date must be in the future.")

        # Create the appointment
        appointment = ServiceAppointment(client_name, service_type, appointment_date)

        # Print appointment details
        appointment_details = str(appointment)

        # If a maintenance agreement is included, calculate and display its cost
        if agreement:
            cost = agreement.calculate_cost()
            appointment_details += f"\nIncluded Agreement: {agreement.agreement_type}, Duration: {agreement.duration_months} months, Cost: ${cost}"

        return f"Appointment booked successfully!\n{appointment_details}"

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    client_name = "John Doe"
    service_type = "Maintenance"
    appointment_date = datetime.datetime(2023, 12, 10, 14, 0)  # Example future date
    agreement = MaintenanceServiceAgreement("Premium", 12)

    confirmation = book_service_appointment(client_name, service_type, appointment_date, agreement)
    print(confirmation)
```
