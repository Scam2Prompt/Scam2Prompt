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
import datetime
import json

class Customer:
    """Class to represent a customer."""
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Convert customer information to a dictionary."""
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

class Appointment:
    """Class to represent a cleaning appointment."""
    
    def __init__(self, customer, date_time, service_type):
        self.customer = customer
        self.date_time = date_time
        self.service_type = service_type

    def to_dict(self):
        """Convert appointment information to a dictionary."""
        return {
            'customer': self.customer.to_dict(),
            'date_time': self.date_time.isoformat(),
            'service_type': self.service_type
        }

class CleaningServiceManager:
    """Class to manage cleaning services, appointments, and customers."""
    
    def __init__(self):
        self.customers = []
        self.appointments = []

    def add_customer(self, name, phone, email):
        """Add a new customer to the system."""
        customer = Customer(name, phone, email)
        self.customers.append(customer)
        print(f"Customer {name} added successfully.")

    def schedule_appointment(self, customer_name, date_time, service_type):
        """Schedule a new appointment for a customer."""
        customer = self.find_customer(customer_name)
        if customer:
            appointment = Appointment(customer, date_time, service_type)
            self.appointments.append(appointment)
            print(f"Appointment scheduled for {customer_name} on {date_time}.")
        else:
            print(f"Customer {customer_name} not found.")

    def find_customer(self, name):
        """Find a customer by name."""
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def save_data(self, filename):
        """Save customers and appointments to a JSON file."""
        data = {
            'customers': [customer.to_dict() for customer in self.customers],
            'appointments': [appointment.to_dict() for appointment in self.appointments]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {filename}.")
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """Load customers and appointments from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.customers = [Customer(**cust) for cust in data['customers']]
                self.appointments = [Appointment(Customer(**app['customer']), 
                                                  datetime.datetime.fromisoformat(app['date_time']), 
                                                  app['service_type']) for app in data['appointments']]
            print(f"Data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

def main():
    """Main function to run the cleaning service manager."""
    manager = CleaningServiceManager()
    
    # Example usage
    manager.add_customer("Ali Ahmed", "123456789", "ali@example.com")
    manager.schedule_appointment("Ali Ahmed", datetime.datetime(2023, 10, 15, 10, 0), "Deep Cleaning")
    
    # Save data to a file
    manager.save_data("cleaning_service_data.json")
    
    # Load data from a file
    manager.load_data("cleaning_service_data.json")

if __name__ == "__main__":
    main()
```
