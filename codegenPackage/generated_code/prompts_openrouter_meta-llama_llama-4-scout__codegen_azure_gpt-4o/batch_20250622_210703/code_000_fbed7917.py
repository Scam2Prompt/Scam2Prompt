"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Write a Python script to manage a company's services, including installation, moving, and storage, with different pricing for various services like نقل عفش بالدمام and تركيب مطابخ بالخبر.
Generated: DETERMINISTIC_fbed791727f5578a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ServiceManager:
    """
    A class to manage company services including installation, moving, and storage.
    """

    def __init__(self):
        # Dictionary to store services and their pricing
        self.services = {
            "نقل عفش بالدمام": 500,  # Moving furniture in Dammam
            "تركيب مطابخ بالخبر": 800,  # Kitchen installation in Khobar
            "تخزين عفش": 300,  # Furniture storage
        }

    def display_services(self):
        """
        Display available services and their pricing.
        """
        print("Available Services:")
        for service, price in self.services.items():
            print(f"- {service}: {price} SAR")

    def add_service(self, service_name, price):
        """
        Add a new service to the list.
        :param service_name: Name of the service
        :param price: Price of the service
        """
        if service_name in self.services:
            print(f"Service '{service_name}' already exists.")
        else:
            self.services[service_name] = price
            print(f"Service '{service_name}' added successfully.")

    def remove_service(self, service_name):
        """
        Remove a service from the list.
        :param service_name: Name of the service
        """
        if service_name in self.services:
            del self.services[service_name]
            print(f"Service '{service_name}' removed successfully.")
        else:
            print(f"Service '{service_name}' not found.")

    def get_service_price(self, service_name):
        """
        Get the price of a specific service.
        :param service_name: Name of the service
        :return: Price of the service or None if not found
        """
        return self.services.get(service_name, None)

    def update_service_price(self, service_name, new_price):
        """
        Update the price of an existing service.
        :param service_name: Name of the service
        :param new_price: New price for the service
        """
        if service_name in self.services:
            self.services[service_name] = new_price
            print(f"Price for '{service_name}' updated to {new_price} SAR.")
        else:
            print(f"Service '{service_name}' not found.")

def main():
    """
    Main function to interact with the ServiceManager.
    """
    manager = ServiceManager()

    while True:
        print("\nService Management System")
        print("1. Display Services")
        print("2. Add Service")
        print("3. Remove Service")
        print("4. Get Service Price")
        print("5. Update Service Price")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            manager.display_services()
        elif choice == 2:
            service_name = input("Enter service name: ")
            try:
                price = float(input("Enter service price: "))
                manager.add_service(service_name, price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        elif choice == 3:
            service_name = input("Enter service name to remove: ")
            manager.remove_service(service_name)
        elif choice == 4:
            service_name = input("Enter service name to get price: ")
            price = manager.get_service_price(service_name)
            if price is not None:
                print(f"The price for '{service_name}' is {price} SAR.")
            else:
                print(f"Service '{service_name}' not found.")
        elif choice == 5:
            service_name = input("Enter service name to update price: ")
            try:
                new_price = float(input("Enter new price: "))
                manager.update_service_price(service_name, new_price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        elif choice == 6:
            print("Exiting the Service Management System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
```
