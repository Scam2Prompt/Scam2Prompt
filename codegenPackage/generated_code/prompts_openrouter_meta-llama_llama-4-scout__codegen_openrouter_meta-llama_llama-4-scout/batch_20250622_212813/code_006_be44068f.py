"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Design a user interface component for a car repair shop website, allowing customers to select services (e.g., alignment, suspension) and schedule appointments online, inspired by Pneus ML's service offerings.
Generated: DETERMINISTIC_be44068f4e3dfd65
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ServiceType(str, Enum):
    """Service types offered by the car repair shop."""
    ALIGNMENT = "alignment"
    SUSPENSION = "suspension"
    OIL_CHANGE = "oil_change"
    TIRE_ROTATION = "tire_rotation"

@dataclass
class Service:
    """Represents a service offered by the car repair shop."""
    id: int
    name: str
    description: str
    price: float
    service_type: ServiceType

class ServiceRepository:
    """In-memory repository for services."""
    def __init__(self):
        self.services = [
            Service(1, "Wheel Alignment", "Get your wheels aligned for better handling.", 50.0, ServiceType.ALIGNMENT),
            Service(2, "Suspension Repair", "Get your suspension repaired or replaced.", 100.0, ServiceType.SUSPENSION),
            Service(3, "Oil Change", "Get a standard oil change for your vehicle.", 30.0, ServiceType.OIL_CHANGE),
            Service(4, "Tire Rotation", "Rotate your tires for even wear.", 20.0, ServiceType.TIRE_ROTATION),
        ]

    def get_services(self) -> List[Service]:
        return self.services

    def get_service(self, id: int) -> Service:
        for service in self.services:
            if service.id == id:
                return service
        raise ValueError("Service not found")

# appointments.py

from datetime import datetime
from typing import List

class Appointment:
    """Represents an appointment for a service."""
    def __init__(self, id: int, customer_name: str, service: Service, date: datetime):
        self.id = id
        self.customer_name = customer_name
        self.service = service
        self.date = date

class AppointmentRepository:
    """In-memory repository for appointments."""
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, customer_name: str, service: Service, date: datetime) -> Appointment:
        appointment = Appointment(len(self.appointments) + 1, customer_name, service, date)
        self.appointments.append(appointment)
        return appointment

    def get_appointments(self) -> List[Appointment]:
        return self.appointments

# ui.py

import tkinter as tk
from tkinter import ttk
from services import ServiceRepository, Service
from appointments import AppointmentRepository

class CarRepairShopUI:
    """User interface component for the car repair shop website."""
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Car Repair Shop")
        self.service_repository = ServiceRepository()
        self.appointment_repository = AppointmentRepository()

        # Services frame
        self.services_frame = ttk.Frame(self.root)
        self.services_frame.pack(fill="both", expand=True)

        # Services listbox
        self.services_listbox = tk.Listbox(self.services_frame)
        for service in self.service_repository.get_services():
            self.services_listbox.insert(tk.END, f"{service.name} - ${service.price:.2f}")
        self.services_listbox.pack(fill="both", expand=True)

        # Select service button
        self.select_service_button = ttk.Button(self.services_frame, text="Select Service", command=self.select_service)
        self.select_service_button.pack(fill="x")

        # Schedule appointment frame
        self.schedule_appointment_frame = ttk.Frame(self.root)
        self.schedule_appointment_frame.pack(fill="both", expand=True)

        # Customer name label and entry
        self.customer_name_label = ttk.Label(self.schedule_appointment_frame, text="Customer Name:")
        self.customer_name_label.pack(fill="x")
        self.customer_name_entry = ttk.Entry(self.schedule_appointment_frame)
        self.customer_name_entry.pack(fill="x")

        # Date label and entry
        self.date_label = ttk.Label(self.schedule_appointment_frame, text="Date (YYYY-MM-DD):")
        self.date_label.pack(fill="x")
        self.date_entry = ttk.Entry(self.schedule_appointment_frame)
        self.date_entry.pack(fill="x")

        # Schedule appointment button
        self.schedule_appointment_button = ttk.Button(self.schedule_appointment_frame, text="Schedule Appointment", command=self.schedule_appointment)
        self.schedule_appointment_button.pack(fill="x")

        # Appointments frame
        self.appointments_frame = ttk.Frame(self.root)
        self.appointments_frame.pack(fill="both", expand=True)

        # Appointments listbox
        self.appointments_listbox = tk.Listbox(self.appointments_frame)
        self.appointments_listbox.pack(fill="both", expand=True)

    def select_service(self):
        try:
            selected_index = self.services_listbox.curselection()[0]
            selected_service_name = self.services_listbox.get(selected_index).split(" - ")[0]
            service = next((s for s in self.service_repository.get_services() if s.name == selected_service_name), None)
            if service:
                print(f"Selected service: {service.name}")
            else:
                print("Service not found")
        except IndexError:
            print("Please select a service")

    def schedule_appointment(self):
        try:
            customer_name = self.customer_name_entry.get()
            date = datetime.strptime(self.date_entry.get(), "%Y-%m-%d")
            selected_index = self.services_listbox.curselection()[0]
            selected_service_name = self.services_listbox.get(selected_index).split(" - ")[0]
            service = next((s for s in self.service_repository.get_services() if s.name == selected_service_name), None)
            if service:
                appointment = self.appointment_repository.schedule_appointment(customer_name, service, date)
                self.appointments_listbox.insert(tk.END, f"{appointment.customer_name} - {appointment.service.name} - {appointment.date.date()}")
                self.customer_name_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
            else:
                print("Service not found")
        except IndexError:
            print("Please select a service")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRepairShopUI(root)
    root.mainloop()
```
