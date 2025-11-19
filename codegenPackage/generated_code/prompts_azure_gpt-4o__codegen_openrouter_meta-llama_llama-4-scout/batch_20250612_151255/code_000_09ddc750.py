"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python script to simulate a booking system for white goods repair services in Ankara, referencing the brands and services offered by Ankara Teknik Servisi.
Generated: DETERMINISTIC_09ddc750955d9bd2
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Ankara White Goods Repair Service Booking System

This script simulates a booking system for white goods repair services in Ankara.
It references the brands and services offered by Ankara Teknik Servisi.

Author: [Your Name]
Date: [Today's Date]
"""

class Brand:
    """Represents a brand of white goods."""

    def __init__(self, name):
        """Initializes a Brand object.

        Args:
            name (str): The name of the brand.
        """
        self.name = name

class Service:
    """Represents a repair service for white goods."""

    def __init__(self, name, description, price):
        """Initializes a Service object.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
            price (float): The price of the service.
        """
        self.name = name
        self.description = description
        self.price = price

class BookingSystem:
    """Simulates a booking system for white goods repair services."""

    def __init__(self):
        """Initializes a BookingSystem object."""
        self.brands = []
        self.services = []

    def add_brand(self, brand):
        """Adds a brand to the system.

        Args:
            brand (Brand): The brand to add.
        """
        self.brands.append(brand)

    def add_service(self, service):
        """Adds a service to the system.

        Args:
            service (Service): The service to add.
        """
        self.services.append(service)

    def display_brands(self):
        """Displays all brands in the system."""
        print("Available Brands:")
        for i, brand in enumerate(self.brands, start=1):
            print(f"{i}. {brand.name}")

    def display_services(self):
        """Displays all services in the system."""
        print("Available Services:")
        for i, service in enumerate(self.services, start=1):
            print(f"{i}. {service.name} - {service.description} ({service.price} TL)")

    def book_service(self):
        """Simulates a booking process."""
        self.display_brands()
        brand_choice = input("Enter the number of your brand: ")
        try:
            brand_choice = int(brand_choice)
            if brand_choice < 1 or brand_choice > len(self.brands):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            return self.book_service()

        self.display_services()
        service_choice = input("Enter the number of your service: ")
        try:
            service_choice = int(service_choice)
            if service_choice < 1 or service_choice > len(self.services):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            return self.book_service()

        brand = self.brands[brand_choice - 1]
        service = self.services[service_choice - 1]
        print(f"\nBooking confirmed for {brand.name} - {service.name}!")
        print(f"Service Description: {service.description}")
        print(f"Service Price: {service.price} TL")

def main():
    # Create a booking system
    system = BookingSystem()

    # Add brands
    brands = [
        Brand("Arçelik"),
        Brand("Beko"),
        Brand("Bosch"),
        Brand("Samsung"),
        Brand("Whirlpool"),
    ]
    for brand in brands:
        system.add_brand(brand)

    # Add services
    services = [
        Service("Refrigerator Repair", "Repair of refrigerators and freezers.", 100.0),
        Service("Oven Repair", "Repair of ovens and stoves.", 150.0),
        Service("Dishwasher Repair", "Repair of dishwashers.", 120.0),
        Service("Washing Machine Repair", "Repair of washing machines.", 100.0),
        Service("Tumble Dryer Repair", "Repair of tumble dryers.", 120.0),
    ]
    for service in services:
        system.add_service(service)

    # Start the booking process
    while True:
        print("\nAnkara White Goods Repair Service Booking System")
        print("1. Book a Service")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            system.book_service()
        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
