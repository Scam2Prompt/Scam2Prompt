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
from enum import Enum
from datetime import datetime

class ServiceType(Enum):
    """Enum for service types"""
    MAINTENANCE = 1
    REPAIR = 2
    INSTALLATION = 3

class MaintenanceAgreement(Enum):
    """Enum for maintenance agreement options"""
    MONTHLY = 1
    QUARTERLY = 2
    ANNUALLY = 3

class Appointment:
    """Class representing an HVAC service appointment"""
    def __init__(self, customer_name, service_type, date, time):
        self.customer_name = customer_name
        self.service_type = service_type
        self.date = date
        self.time = time
        self.maintenance_agreement = None

    def add_maintenance_agreement(self, agreement):
        """Add a maintenance agreement to the appointment"""
        self.maintenance_agreement = agreement

class HVACService:
    """Class representing the HVAC service appointment booking system"""
    def __init__(self):
        self.appointments = []

    def book_appointment(self, customer_name, service_type, date, time, maintenance_agreement=None):
        """Book a new appointment"""
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            time_obj = datetime.strptime(time, "%H:%M").time()
            appointment = Appointment(customer_name, service_type, date_obj, time_obj)
            if maintenance_agreement:
                appointment.add_maintenance_agreement(maintenance_agreement)
            self.appointments.append(appointment)
            return appointment
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM respectively.")
            return None

    def view_appointments(self):
        """View all booked appointments"""
        for i, appointment in enumerate(self.appointments):
            print(f"Appointment {i+1}:")
            print(f"Customer Name: {appointment.customer_name}")
            print(f"Service Type: {appointment.service_type.name}")
            print(f"Date: {appointment.date}")
            print(f"Time: {appointment.time}")
            if appointment.maintenance_agreement:
                print(f"Maintenance Agreement: {appointment.maintenance_agreement.name}")
            print("------------------------")

def main():
    hvac_service = HVACService()

    while True:
        print("HVAC Service Appointment Booking System")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            print("Select service type:")
            print("1. Maintenance")
            print("2. Repair")
            print("3. Installation")
            service_type_choice = input("Enter your choice: ")
            service_type = ServiceType.MAINTENANCE if service_type_choice == "1" else ServiceType.REPAIR if service_type_choice == "2" else ServiceType.INSTALLATION if service_type_choice == "3" else None

            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")

            maintenance_agreement_choice = input("Do you want to add a maintenance agreement? (yes/no): ")
            maintenance_agreement = None
            if maintenance_agreement_choice.lower() == "yes":
                print("Select maintenance agreement option:")
                print("1. Monthly")
                print("2. Quarterly")
                print("3. Annually")
                maintenance_agreement_choice = input("Enter your choice: ")
                maintenance_agreement = MaintenanceAgreement.MONTHLY if maintenance_agreement_choice == "1" else MaintenanceAgreement.QUARTERLY if maintenance_agreement_choice == "2" else MaintenanceAgreement.ANNUALLY if maintenance_agreement_choice == "3" else None

            appointment = hvac_service.book_appointment(customer_name, service_type, date, time, maintenance_agreement)
            if appointment:
                print("Appointment booked successfully!")
        elif choice == "2":
            hvac_service.view_appointments()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
