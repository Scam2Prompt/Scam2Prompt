"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Write a Python script to create a simple fitness consultation booking system that includes client information, plan selection, and appointment scheduling, similar to the services offered on carolcrespo.com.br.
Generated: DETERMINISTIC_e5435568e9508bd2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Client:
    """Represents a client with their information."""
    
    def __init__(self, name, email, phone):
        """
        Initializes a Client object.

        Args:
            name (str): Client's name.
            email (str): Client's email.
            phone (str): Client's phone number.
        """
        self.name = name
        self.email = email
        self.phone = phone

class Plan:
    """Represents a fitness plan."""
    
    def __init__(self, name, description, price):
        """
        Initializes a Plan object.

        Args:
            name (str): Plan's name.
            description (str): Plan's description.
            price (float): Plan's price.
        """
        self.name = name
        self.description = description
        self.price = price

class Appointment:
    """Represents an appointment."""
    
    def __init__(self, client, plan, date, time):
        """
        Initializes an Appointment object.

        Args:
            client (Client): Client object.
            plan (Plan): Plan object.
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.
        """
        self.client = client
        self.plan = plan
        self.date = date
        self.time = time

class FitnessConsultationSystem:
    """Manages client information, plan selection, and appointment scheduling."""
    
    def __init__(self):
        self.clients = []
        self.plans = []
        self.appointments = []

    def add_client(self, name, email, phone):
        """
        Adds a new client.

        Args:
            name (str): Client's name.
            email (str): Client's email.
            phone (str): Client's phone number.
        """
        new_client = Client(name, email, phone)
        self.clients.append(new_client)
        print(f"Client {name} added successfully.")

    def add_plan(self, name, description, price):
        """
        Adds a new plan.

        Args:
            name (str): Plan's name.
            description (str): Plan's description.
            price (float): Plan's price.
        """
        new_plan = Plan(name, description, price)
        self.plans.append(new_plan)
        print(f"Plan {name} added successfully.")

    def schedule_appointment(self, client_name, plan_name, date, time):
        """
        Schedules an appointment.

        Args:
            client_name (str): Client's name.
            plan_name (str): Plan's name.
            date (str): Appointment date in YYYY-MM-DD format.
            time (str): Appointment time in HH:MM format.
        """
        client = next((c for c in self.clients if c.name == client_name), None)
        plan = next((p for p in self.plans if p.name == plan_name), None)

        if client and plan:
            try:
                datetime.strptime(date, "%Y-%m-%d")
                datetime.strptime(time, "%H:%M")
                new_appointment = Appointment(client, plan, date, time)
                self.appointments.append(new_appointment)
                print(f"Appointment scheduled for {client_name} on {date} at {time}.")
            except ValueError:
                print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        else:
            print("Client or plan not found.")

    def display_clients(self):
        """Displays all clients."""
        print("Clients:")
        for i, client in enumerate(self.clients, start=1):
            print(f"{i}. {client.name} - {client.email} - {client.phone}")

    def display_plans(self):
        """Displays all plans."""
        print("Plans:")
        for i, plan in enumerate(self.plans, start=1):
            print(f"{i}. {plan.name} - {plan.description} - ${plan.price:.2f}")

    def display_appointments(self):
        """Displays all appointments."""
        print("Appointments:")
        for i, appointment in enumerate(self.appointments, start=1):
            print(f"{i}. {appointment.client.name} - {appointment.plan.name} - {appointment.date} at {appointment.time}")


def main():
    system = FitnessConsultationSystem()

    while True:
        print("\nFitness Consultation Booking System")
        print("1. Add Client")
        print("2. Add Plan")
        print("3. Schedule Appointment")
        print("4. Display Clients")
        print("5. Display Plans")
        print("6. Display Appointments")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter client's name: ")
            email = input("Enter client's email: ")
            phone = input("Enter client's phone number: ")
            system.add_client(name, email, phone)
        elif choice == "2":
            name = input("Enter plan's name: ")
            description = input("Enter plan's description: ")
            price = float(input("Enter plan's price: "))
            system.add_plan(name, description, price)
        elif choice == "3":
            client_name = input("Enter client's name: ")
            plan_name = input("Enter plan's name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            system.schedule_appointment(client_name, plan_name, date, time)
        elif choice == "4":
            system.display_clients()
        elif choice == "5":
            system.display_plans()
        elif choice == "6":
            system.display_appointments()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
