"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Write a Python script to manage car rentals for a company like Micro Rent a Car in Islamabad, including features for booking, payment, and vehicle management.
Generated: DETERMINISTIC_96afe2427ebf400c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_rental_system.py

class Vehicle:
    """Represents a vehicle in the rental system."""

    def __init__(self, vehicle_id, brand, model, year, rental_price):
        """
        Initializes a Vehicle object.

        Args:
            vehicle_id (str): Unique identifier for the vehicle.
            brand (str): Brand of the vehicle.
            model (str): Model of the vehicle.
            year (int): Year of manufacture.
            rental_price (float): Daily rental price.
        """
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_price = rental_price
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - ${self.rental_price}/day"


class Customer:
    """Represents a customer in the rental system."""

    def __init__(self, customer_id, name, email, phone):
        """
        Initializes a Customer object.

        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Name of the customer.
            email (str): Email address of the customer.
            phone (str): Phone number of the customer.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"


class Rental:
    """Represents a rental transaction."""

    def __init__(self, rental_id, customer, vehicle, rental_date, return_date):
        """
        Initializes a Rental object.

        Args:
            rental_id (str): Unique identifier for the rental.
            customer (Customer): Customer who rented the vehicle.
            vehicle (Vehicle): Vehicle that was rented.
            rental_date (str): Date the vehicle was rented.
            return_date (str): Date the vehicle is to be returned.
        """
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_date = rental_date
        self.return_date = return_date

    def calculate_total(self):
        """Calculates the total rental cost."""
        from datetime import datetime

        rental_date = datetime.strptime(self.rental_date, "%Y-%m-%d")
        return_date = datetime.strptime(self.return_date, "%Y-%m-%d")
        days_rented = (return_date - rental_date).days
        return self.vehicle.rental_price * days_rented


class CarRentalSystem:
    """Manages vehicles, customers, and rentals."""

    def __init__(self):
        self.vehicles = {}
        self.customers = {}
        self.rentals = {}

    def add_vehicle(self, vehicle):
        """Adds a vehicle to the system."""
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_customer(self, customer):
        """Adds a customer to the system."""
        self.customers[customer.customer_id] = customer

    def book_rental(self, rental):
        """Books a rental."""
        if rental.vehicle.vehicle_id in self.vehicles and rental.vehicle.is_available:
            self.rentals[rental.rental_id] = rental
            self.vehicles[rental.vehicle.vehicle_id].is_available = False
            print(f"Rental {rental.rental_id} booked successfully.")
        else:
            print("Vehicle is not available or does not exist.")

    def return_vehicle(self, rental_id):
        """Returns a rented vehicle."""
        if rental_id in self.rentals:
            rental = self.rentals[rental_id]
            self.vehicles[rental.vehicle.vehicle_id].is_available = True
            del self.rentals[rental_id]
            print(f"Vehicle returned successfully. Total cost: ${rental.calculate_total():.2f}")
        else:
            print("Rental not found.")

    def make_payment(self, rental_id):
        """Processes payment for a rental."""
        if rental_id in self.rentals:
            rental = self.rentals[rental_id]
            total_cost = rental.calculate_total()
            print(f"Payment processed successfully. Total cost: ${total_cost:.2f}")
        else:
            print("Rental not found.")

    def list_vehicles(self):
        """Lists all vehicles in the system."""
        for vehicle in self.vehicles.values():
            print(vehicle)

    def list_customers(self):
        """Lists all customers in the system."""
        for customer in self.customers.values():
            print(customer)

    def list_rentals(self):
        """Lists all rentals in the system."""
        for rental in self.rentals.values():
            print(f"Rental ID: {rental.rental_id}")
            print(f"Customer: {rental.customer}")
            print(f"Vehicle: {rental.vehicle}")
            print(f"Rental Date: {rental.rental_date}")
            print(f"Return Date: {rental.return_date}")
            print(f"Total Cost: ${rental.calculate_total():.2f}")
            print()


def main():
    system = CarRentalSystem()

    while True:
        print("1. Add Vehicle")
        print("2. Add Customer")
        print("3. Book Rental")
        print("4. Return Vehicle")
        print("5. Make Payment")
        print("6. List Vehicles")
        print("7. List Customers")
        print("8. List Rentals")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vehicle_id = input("Enter vehicle ID: ")
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            rental_price = float(input("Enter rental price: "))
            vehicle = Vehicle(vehicle_id, brand, model, year, rental_price)
            system.add_vehicle(vehicle)
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            customer = Customer(customer_id, name, email, phone)
            system.add_customer(customer)
        elif choice == "3":
            rental_id = input("Enter rental ID: ")
            customer_id = input("Enter customer ID: ")
            vehicle_id = input("Enter vehicle ID: ")
            rental_date = input("Enter rental date (YYYY-MM-DD): ")
            return_date = input("Enter return date (YYYY-MM-DD): ")
            customer = system.customers.get(customer_id)
            vehicle = system.vehicles.get(vehicle_id)
            if customer and vehicle:
                rental = Rental(rental_id, customer, vehicle, rental_date, return_date)
                system.book_rental(rental)
            else:
                print("Customer or vehicle not found.")
        elif choice == "4":
            rental_id = input("Enter rental ID: ")
            system.return_vehicle(rental_id)
        elif choice == "5":
            rental_id = input("Enter rental ID: ")
            system.make_payment(rental_id)
        elif choice == "6":
            system.list_vehicles()
        elif choice == "7":
            system.list_customers()
        elif choice == "8":
            system.list_rentals()
        elif choice == "9":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
