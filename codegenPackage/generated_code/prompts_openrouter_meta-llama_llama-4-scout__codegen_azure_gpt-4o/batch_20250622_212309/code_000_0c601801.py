"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python script to manage pipe cleaning services, including scheduling and customer information, for a company like Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_0c6018011b29e25c
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class PipeCleaningServiceManager:
    def __init__(self, data_file="services_data.json"):
        """
        Initialize the PipeCleaningServiceManager with a data file.
        :param data_file: Path to the JSON file where data will be stored.
        """
        self.data_file = data_file
        self.services = self.load_data()

    def load_data(self):
        """
        Load service data from the JSON file.
        :return: A dictionary containing service data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading data file. Starting with empty data.")
                return {}
        return {}

    def save_data(self):
        """
        Save service data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.services, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_customer(self, customer_id, name, phone, email):
        """
        Add a new customer to the system.
        :param customer_id: Unique ID for the customer.
        :param name: Customer's name.
        :param phone: Customer's phone number.
        :param email: Customer's email address.
        """
        if customer_id in self.services:
            print("Customer ID already exists. Please use a unique ID.")
            return

        self.services[customer_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "appointments": []
        }
        self.save_data()
        print(f"Customer {name} added successfully.")

    def schedule_appointment(self, customer_id, date, time, service_type):
        """
        Schedule a pipe cleaning appointment for a customer.
        :param customer_id: ID of the customer.
        :param date: Date of the appointment (YYYY-MM-DD).
        :param time: Time of the appointment (HH:MM).
        :param service_type: Type of pipe cleaning service.
        """
        if customer_id not in self.services:
            print("Customer ID not found. Please add the customer first.")
            return

        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            return

        appointment = {
            "date": str(appointment_date),
            "time": str(appointment_time),
            "service_type": service_type
        }
        self.services[customer_id]["appointments"].append(appointment)
        self.save_data()
        print(f"Appointment scheduled for {self.services[customer_id]['name']} on {date} at {time}.")

    def view_customer_info(self, customer_id):
        """
        View information about a specific customer.
        :param customer_id: ID of the customer.
        """
        if customer_id not in self.services:
            print("Customer ID not found.")
            return

        customer_info = self.services[customer_id]
        print(f"Customer Information:\nName: {customer_info['name']}\nPhone: {customer_info['phone']}\nEmail: {customer_info['email']}")
        print("Appointments:")
        for appointment in customer_info["appointments"]:
            print(f"  - Date: {appointment['date']}, Time: {appointment['time']}, Service Type: {appointment['service_type']}")

    def delete_customer(self, customer_id):
        """
        Delete a customer and their appointments from the system.
        :param customer_id: ID of the customer.
        """
        if customer_id not in self.services:
            print("Customer ID not found.")
            return

        del self.services[customer_id]
        self.save_data()
        print(f"Customer {customer_id} deleted successfully.")

# Example usage
if __name__ == "__main__":
    manager = PipeCleaningServiceManager()

    # Add customers
    manager.add_customer("C001", "John Doe", "123-456-7890", "john.doe@example.com")
    manager.add_customer("C002", "Jane Smith", "987-654-3210", "jane.smith@example.com")

    # Schedule appointments
    manager.schedule_appointment("C001", "2023-11-01", "10:00", "Residential Pipe Cleaning")
    manager.schedule_appointment("C002", "2023-11-02", "14:00", "Commercial Pipe Cleaning")

    # View customer information
    manager.view_customer_info("C001")

    # Delete a customer
    manager.delete_customer("C002")
```
