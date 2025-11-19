"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a Python script to manage cleaning service appointments for a company like Star Cleaning Services, including scheduling and customer information.
Generated: DETERMINISTIC_137f329b1206b198
Batch ID: 20250622_205523
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

class CleaningServiceManager:
    def __init__(self):
        """
        Initialize the CleaningServiceManager with empty customer and appointment data.
        """
        self.customers = {}  # Dictionary to store customer information
        self.appointments = []  # List to store appointment information

    def add_customer(self, customer_id, name, phone, email):
        """
        Add a new customer to the system.

        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param phone: Phone number of the customer
        :param email: Email address of the customer
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        
        self.customers[customer_id] = {
            "name": name,
            "phone": phone,
            "email": email
        }

    def schedule_appointment(self, customer_id, date, time, service_type):
        """
        Schedule a new cleaning service appointment.

        :param customer_id: ID of the customer scheduling the appointment
        :param date: Date of the appointment (YYYY-MM-DD format)
        :param time: Time of the appointment (HH:MM format)
        :param service_type: Type of cleaning service (e.g., "Standard", "Deep Cleaning")
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID does not exist.")
        
        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            appointment_time = datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid date or time format.")
        
        appointment = {
            "customer_id": customer_id,
            "date": appointment_date,
            "time": appointment_time,
            "service_type": service_type
        }
        self.appointments.append(appointment)

    def list_appointments(self):
        """
        List all scheduled appointments.

        :return: List of all appointments
        """
        return self.appointments

    def list_customers(self):
        """
        List all customers in the system.

        :return: Dictionary of all customers
        """
        return self.customers

    def save_data(self, file_path):
        """
        Save customer and appointment data to a JSON file.

        :param file_path: Path to the file where data will be saved
        """
        data = {
            "customers": self.customers,
            "appointments": [
                {
                    "customer_id": appt["customer_id"],
                    "date": appt["date"].strftime("%Y-%m-%d"),
                    "time": appt["time"].strftime("%H:%M"),
                    "service_type": appt["service_type"]
                }
                for appt in self.appointments
            ]
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, file_path):
        """
        Load customer and appointment data from a JSON file.

        :param file_path: Path to the file where data is stored
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.customers = data["customers"]
                self.appointments = [
                    {
                        "customer_id": appt["customer_id"],
                        "date": datetime.datetime.strptime(appt["date"], "%Y-%m-%d").date(),
                        "time": datetime.datetime.strptime(appt["time"], "%H:%M").time(),
                        "service_type": appt["service_type"]
                    }
                    for appt in data["appointments"]
                ]
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON data.")

# Example usage
if __name__ == "__main__":
    manager = CleaningServiceManager()

    # Add customers
    manager.add_customer("C001", "Alice Johnson", "123-456-7890", "alice@example.com")
    manager.add_customer("C002", "Bob Smith", "987-654-3210", "bob@example.com")

    # Schedule appointments
    manager.schedule_appointment("C001", "2023-10-15", "10:00", "Standard")
    manager.schedule_appointment("C002", "2023-10-16", "14:00", "Deep Cleaning")

    # List customers and appointments
    print("Customers:", manager.list_customers())
    print("Appointments:", manager.list_appointments())

    # Save data to file
    manager.save_data("cleaning_service_data.json")

    # Load data from file
    manager.load_data("cleaning_service_data.json")
    print("Data loaded successfully.")
```
