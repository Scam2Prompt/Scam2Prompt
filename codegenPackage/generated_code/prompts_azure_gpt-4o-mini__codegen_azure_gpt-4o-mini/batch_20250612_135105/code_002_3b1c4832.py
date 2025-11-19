"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate a code snippet for an HVAC service appointment booking system that includes options for maintenance service agreements as mentioned on Quality Sheet Metal, Inc.'s website.
Generated: DETERMINISTIC_3b1c4832eb62203c
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Appointment:
    """Class to represent an HVAC service appointment."""
    
    def __init__(self, customer_name, service_type, appointment_date):
        self.customer_name = customer_name
        self.service_type = service_type
        self.appointment_date = appointment_date
        self.confirmed = False

    def confirm_appointment(self):
        """Confirm the appointment."""
        self.confirmed = True

    def __str__(self):
        """String representation of the appointment."""
        return f"Appointment for {self.customer_name} on {self.appointment_date} for {self.service_type}. Confirmed: {self.confirmed}"


class ServiceAgreement:
    """Class to represent a maintenance service agreement."""
    
    def __init__(self, agreement_type, duration_months):
        self.agreement_type = agreement_type
        self.duration_months = duration_months
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30 * duration_months)

    def __str__(self):
        """String representation of the service agreement."""
        return f"{self.agreement_type} Agreement: {self.duration_months} months, valid from {self.start_date} to {self.end_date}"


class HVACServiceBookingSystem:
    """Class to manage HVAC service appointments and agreements."""
    
    def __init__(self):
        self.appointments = []
        self.service_agreements = []

    def book_appointment(self, customer_name, service_type, appointment_date):
        """Book a new service appointment."""
        try:
            if appointment_date < datetime.date.today():
                raise ValueError("Appointment date cannot be in the past.")
            appointment = Appointment(customer_name, service_type, appointment_date)
            self.appointments.append(appointment)
            return appointment
        except Exception as e:
            print(f"Error booking appointment: {e}")

    def create_service_agreement(self, agreement_type, duration_months):
        """Create a new maintenance service agreement."""
        try:
            if duration_months <= 0:
                raise ValueError("Duration must be a positive integer.")
            agreement = ServiceAgreement(agreement_type, duration_months)
            self.service_agreements.append(agreement)
            return agreement
        except Exception as e:
            print(f"Error creating service agreement: {e}")

    def list_appointments(self):
        """List all booked appointments."""
        return [str(appointment) for appointment in self.appointments]

    def list_service_agreements(self):
        """List all service agreements."""
        return [str(agreement) for agreement in self.service_agreements]


# Example usage
if __name__ == "__main__":
    booking_system = HVACServiceBookingSystem()

    # Book an appointment
    appointment = booking_system.book_appointment("John Doe", "Maintenance", datetime.date(2023, 12, 15))
    print(appointment)

    # Create a service agreement
    agreement = booking_system.create_service_agreement("Annual Maintenance", 12)
    print(agreement)

    # List all appointments and agreements
    print("Appointments:", booking_system.list_appointments())
    print("Service Agreements:", booking_system.list_service_agreements())
```
