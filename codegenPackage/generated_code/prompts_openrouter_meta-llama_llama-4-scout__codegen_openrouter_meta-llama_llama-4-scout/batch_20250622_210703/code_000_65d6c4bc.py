"""
Generated Code Metadata:
========================
Original URL: https://ajfpkpackagingcompany.ajfpak.com
Prompt: Write a Python script to calculate the cost of shipping cargo from Karachi to another city in Pakistan using AJF Group of Companies' rates.
Generated: DETERMINISTIC_65d6c4bcd73d9f30
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ShippingCalculator:
    """
    Calculates the cost of shipping cargo from Karachi to another city in Pakistan
    using AJF Group of Companies' rates.
    """

    def __init__(self):
        # Define AJF Group of Companies' shipping rates per kilogram
        self.shipping_rates = {
            'express': 0.05,  # PKR per kilogram
            'standard': 0.03,  # PKR per kilogram
            'economy': 0.02  # PKR per kilogram
        }

        # Define fixed fuel surcharges
        self.fuel_surcharges = {
            'express': 500,  # PKR
            'standard': 300,  # PKR
            'economy': 200  # PKR
        }

        # Define city-specific handling charges
        self.handling_charges = {
            'Lahore': 1000,  # PKR
            'Islamabad': 800,  # PKR
            'Peshawar': 1200,  # PKR
            'Quetta': 1500,  # PKR
            'Multan': 900,  # PKR
            'Faisalabad': 1100,  # PKR
            'Sialkot': 1300,  # PKR
            'Sargodha': 1000,  # PKR
            'Bahawalpur': 1400  # PKR
        }

    def calculate_shipping_cost(self, weight, service_type, destination_city):
        """
        Calculates the total shipping cost.

        Args:
            weight (float): Weight of cargo in kilograms
            service_type (str): Type of shipping service (express, standard, economy)
            destination_city (str): Destination city in Pakistan

        Returns:
            float: Total shipping cost in PKR
        """

        # Validate input parameters
        if service_type not in self.shipping_rates:
            raise ValueError("Invalid service type. Supported types: express, standard, economy")

        if destination_city not in self.handling_charges:
            raise ValueError("Unsupported destination city")

        if weight <= 0:
            raise ValueError("Weight must be greater than zero")

        # Calculate shipping cost based on weight and service type
        shipping_cost = weight * self.shipping_rates[service_type]

        # Add fuel surcharge
        shipping_cost += self.fuel_surcharges[service_type]

        # Add handling charge for destination city
        shipping_cost += self.handling_charges[destination_city]

        return shipping_cost


def main():
    calculator = ShippingCalculator()

    try:
        weight = float(input("Enter weight of cargo (in kilograms): "))
        service_type = input("Enter service type (express, standard, economy): ")
        destination_city = input("Enter destination city: ")

        shipping_cost = calculator.calculate_shipping_cost(weight, service_type, destination_city)

        print(f"Total shipping cost: PKR {shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
