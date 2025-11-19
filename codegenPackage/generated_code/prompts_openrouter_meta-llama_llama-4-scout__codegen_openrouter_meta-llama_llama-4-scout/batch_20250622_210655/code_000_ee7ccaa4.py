"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a Python script to manage a cleaning services company, including scheduling appointments and tracking customer information, inspired by the services offered by شركة إنجاز.
Generated: DETERMINISTIC_ee7ccaa42be157f3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_services.py

class Customer:
    """Represents a customer of the cleaning services company."""

    def __init__(self, customer_id, name, phone_number, address):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            address (str): Customer's address.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Phone Number: {self.phone_number}, Address: {self.address}"


class Appointment:
    """Represents a scheduled appointment for cleaning services."""

    def __init__(self, appointment_id, customer, date, time, service_type):
        """
        Initializes an Appointment object.

        Args:
            appointment_id (int): Unique identifier for the appointment.
            customer (Customer): Customer object associated with the appointment.
            date (str): Date of the appointment (YYYY-MM-DD).
            time (str): Time of the appointment (HH:MM).
            service_type (str): Type of cleaning service scheduled.
        """
        self.appointment_id = appointment_id
        self.customer = customer
        self.date = date
        self.time = time
        self.service_type = service_type

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Customer: {self.customer.name}, Date: {self.date}, Time: {self.time}, Service Type: {self.service_type}"


class CleaningServices:
    """Manages customer information and scheduled appointments."""

    def __init__(self):
        self.customers = {}
        self.appointments = {}
        self.customer_id_counter = 1
        self.appointment_id_counter = 1

    def add_customer(self, name, phone_number, address):
        """
        Adds a new customer.

        Args:
            name (str): Customer's name.
            phone_number (str): Customer's phone number.
            address (str): Customer's address.

        Returns:
            Customer: The newly added customer object.
        """
        customer = Customer(self.customer_id_counter, name, phone_number, address)
        self.customers[self.customer_id_counter] = customer
        self.customer_id_counter += 1
        return customer

    def schedule_appointment(self, customer_id, date, time, service_type):
        """
        Schedules a new appointment.

        Args:
            customer_id (int): ID of the customer associated with the appointment.
            date (str): Date of the appointment (YYYY-MM-DD).
            time (str): Time of the appointment (HH:MM).
            service_type (str): Type of cleaning service scheduled.

        Returns:
            Appointment: The newly scheduled appointment object.

        Raises:
            ValueError: If the customer ID is not found.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID not found")

        customer = self.customers[customer_id]
        appointment = Appointment(self.appointment_id_counter, customer, date, time, service_type)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return appointment

    def get_customer(self, customer_id):
        """
        Retrieves a customer by ID.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: The customer object associated with the given ID, or None if not found.
        """
        return self.customers.get(customer_id)

    def get_appointment(self, appointment_id):
        """
        Retrieves an appointment by ID.

        Args:
            appointment_id (int): ID of the appointment to retrieve.

        Returns:
            Appointment: The appointment object associated with the given ID, or None if not found.
        """
        return self.appointments.get(appointment_id)

    def list_customers(self):
        """Returns a list of all customers."""
        return list(self.customers.values())

    def list_appointments(self):
        """Returns a list of all appointments."""
        return list(self.appointments.values())


def main():
    cleaning_services = CleaningServices()

    while True:
        print("\nCleaning Services Menu:")
        print("1. Add Customer")
        print("2. Schedule Appointment")
        print("3. Get Customer")
        print("4. Get Appointment")
        print("5. List Customers")
        print("6. List Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            phone_number = input("Enter customer phone number: ")
            address = input("Enter customer address: ")
            customer = cleaning_services.add_customer(name, phone_number, address)
            print(f"Customer added: {customer}")
        elif choice == "2":
            customer_id = int(input("Enter customer ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            service_type = input("Enter service type: ")
            try:
                appointment = cleaning_services.schedule_appointment(customer_id, date, time, service_type)
                print(f"Appointment scheduled: {appointment}")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            customer = cleaning_services.get_customer(customer_id)
            if customer:
                print(customer)
            else:
                print("Customer not found")
        elif choice == "4":
            appointment_id = int(input("Enter appointment ID: "))
            appointment = cleaning_services.get_appointment(appointment_id)
            if appointment:
                print(appointment)
            else:
                print("Appointment not found")
        elif choice == "5":
            customers = cleaning_services.list_customers()
            for customer in customers:
                print(customer)
        elif choice == "6":
            appointments = cleaning_services.list_appointments()
            for appointment in appointments:
                print(appointment)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
