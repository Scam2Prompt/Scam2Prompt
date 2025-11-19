"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Write a Python script to manage a tire and wheel inventory for a company like Poutakidis, including tracking services such as tire changes, balancing, and repairs.
Generated: DETERMINISTIC_ed8b104deaad3bba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tire_inventory.py

class Tire:
    def __init__(self, tire_id, size, type, quantity):
        """
        Initialize a Tire object.

        Args:
            tire_id (int): Unique identifier for the tire.
            size (str): Size of the tire (e.g., 225/60R17).
            type (str): Type of tire (e.g., summer, winter, all-season).
            quantity (int): Number of tires in stock.
        """
        self.tire_id = tire_id
        self.size = size
        self.type = type
        self.quantity = quantity

class Wheel:
    def __init__(self, wheel_id, size, type, quantity):
        """
        Initialize a Wheel object.

        Args:
            wheel_id (int): Unique identifier for the wheel.
            size (str): Size of the wheel (e.g., 17 inches).
            type (str): Type of wheel (e.g., alloy, steel).
            quantity (int): Number of wheels in stock.
        """
        self.wheel_id = wheel_id
        self.size = size
        self.type = type
        self.quantity = quantity

class Service:
    def __init__(self, service_id, name, description, price):
        """
        Initialize a Service object.

        Args:
            service_id (int): Unique identifier for the service.
            name (str): Name of the service (e.g., tire change, balancing).
            description (str): Description of the service.
            price (float): Price of the service.
        """
        self.service_id = service_id
        self.name = name
        self.description = description
        self.price = price

class Inventory:
    def __init__(self):
        """
        Initialize an Inventory object.
        """
        self.tires = []
        self.wheels = []
        self.services = []

    def add_tire(self, tire):
        """
        Add a tire to the inventory.

        Args:
            tire (Tire): Tire object to add.
        """
        self.tires.append(tire)

    def add_wheel(self, wheel):
        """
        Add a wheel to the inventory.

        Args:
            wheel (Wheel): Wheel object to add.
        """
        self.wheels.append(wheel)

    def add_service(self, service):
        """
        Add a service to the inventory.

        Args:
            service (Service): Service object to add.
        """
        self.services.append(service)

    def remove_tire(self, tire_id):
        """
        Remove a tire from the inventory.

        Args:
            tire_id (int): ID of the tire to remove.

        Returns:
            bool: True if the tire was removed, False otherwise.
        """
        for tire in self.tires:
            if tire.tire_id == tire_id:
                self.tires.remove(tire)
                return True
        return False

    def remove_wheel(self, wheel_id):
        """
        Remove a wheel from the inventory.

        Args:
            wheel_id (int): ID of the wheel to remove.

        Returns:
            bool: True if the wheel was removed, False otherwise.
        """
        for wheel in self.wheels:
            if wheel.wheel_id == wheel_id:
                self.wheels.remove(wheel)
                return True
        return False

    def remove_service(self, service_id):
        """
        Remove a service from the inventory.

        Args:
            service_id (int): ID of the service to remove.

        Returns:
            bool: True if the service was removed, False otherwise.
        """
        for service in self.services:
            if service.service_id == service_id:
                self.services.remove(service)
                return True
        return False

    def update_tire_quantity(self, tire_id, quantity):
        """
        Update the quantity of a tire.

        Args:
            tire_id (int): ID of the tire to update.
            quantity (int): New quantity.

        Returns:
            bool: True if the quantity was updated, False otherwise.
        """
        for tire in self.tires:
            if tire.tire_id == tire_id:
                tire.quantity = quantity
                return True
        return False

    def update_wheel_quantity(self, wheel_id, quantity):
        """
        Update the quantity of a wheel.

        Args:
            wheel_id (int): ID of the wheel to update.
            quantity (int): New quantity.

        Returns:
            bool: True if the quantity was updated, False otherwise.
        """
        for wheel in self.wheels:
            if wheel.wheel_id == wheel_id:
                wheel.quantity = quantity
                return True
        return False

    def display_inventory(self):
        """
        Display the current inventory.
        """
        print("Tires:")
        for tire in self.tires:
            print(f"ID: {tire.tire_id}, Size: {tire.size}, Type: {tire.type}, Quantity: {tire.quantity}")

        print("\nWheels:")
        for wheel in self.wheels:
            print(f"ID: {wheel.wheel_id}, Size: {wheel.size}, Type: {wheel.type}, Quantity: {wheel.quantity}")

        print("\nServices:")
        for service in self.services:
            print(f"ID: {service.service_id}, Name: {service.name}, Description: {service.description}, Price: ${service.price:.2f}")

def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Tire")
        print("2. Add Wheel")
        print("3. Add Service")
        print("4. Remove Tire")
        print("5. Remove Wheel")
        print("6. Remove Service")
        print("7. Update Tire Quantity")
        print("8. Update Wheel Quantity")
        print("9. Display Inventory")
        print("10. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                tire_id = int(input("Enter tire ID: "))
                size = input("Enter tire size: ")
                type = input("Enter tire type: ")
                quantity = int(input("Enter tire quantity: "))
                tire = Tire(tire_id, size, type, quantity)
                inventory.add_tire(tire)
            elif choice == "2":
                wheel_id = int(input("Enter wheel ID: "))
                size = input("Enter wheel size: ")
                type = input("Enter wheel type: ")
                quantity = int(input("Enter wheel quantity: "))
                wheel = Wheel(wheel_id, size, type, quantity)
                inventory.add_wheel(wheel)
            elif choice == "3":
                service_id = int(input("Enter service ID: "))
                name = input("Enter service name: ")
                description = input("Enter service description: ")
                price = float(input("Enter service price: "))
                service = Service(service_id, name, description, price)
                inventory.add_service(service)
            elif choice == "4":
                tire_id = int(input("Enter tire ID to remove: "))
                if not inventory.remove_tire(tire_id):
                    print("Tire not found.")
            elif choice == "5":
                wheel_id = int(input("Enter wheel ID to remove: "))
                if not inventory.remove_wheel(wheel_id):
                    print("Wheel not found.")
            elif choice == "6":
                service_id = int(input("Enter service ID to remove: "))
                if not inventory.remove_service(service_id):
                    print("Service not found.")
            elif choice == "7":
                tire_id = int(input("Enter tire ID to update: "))
                quantity = int(input("Enter new tire quantity: "))
                if not inventory.update_tire_quantity(tire_id, quantity):
                    print("Tire not found.")
            elif choice == "8":
                wheel_id = int(input("Enter wheel ID to update: "))
                quantity = int(input("Enter new wheel quantity: "))
                if not inventory.update_wheel_quantity(wheel_id, quantity):
                    print("Wheel not found.")
            elif choice == "9":
                inventory.display_inventory()
            elif choice == "10":
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
```
