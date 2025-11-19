"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Write a Python script to simulate rental payments for a property in Bogotá, Colombia, considering factors like property value and location, as offered by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_cb7b5ed06316a441
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Property:
    """
    A class to represent a property for rent.

    Attributes:
        value (float): The market value of the property.
        location (str): The location of the property.
        base_rent (float): The base rent calculated from the property value.
    """

    def __init__(self, value: float, location: str):
        """
        Initializes a new Property instance.

        Args:
            value (float): The market value of the property.
            location (str): The location of the property.
        """
        if value <= 0:
            raise ValueError("Property value must be greater than zero.")
        if not location:
            raise ValueError("Location must be a non-empty string.")

        self.value = value
        self.location = location
        self.base_rent = self.calculate_base_rent()

    def calculate_base_rent(self) -> float:
        """
        Calculates the base rent based on property value.

        Returns:
            float: The calculated base rent.
        """
        return self.value * 0.01  # 1% of property value as base rent

    def adjust_rent_for_location(self) -> float:
        """
        Adjusts the rent based on the location.

        Returns:
            float: The adjusted rent based on location.
        """
        location_factor = {
            "Centro": 1.2,
            "Chapinero": 1.15,
            "Usaquén": 1.1,
            "Suba": 1.05,
            "Engativá": 1.0
        }
        factor = location_factor.get(self.location, 1.0)
        return self.base_rent * factor


class RentalPaymentSimulator:
    """
    A class to simulate rental payments for a property.

    Attributes:
        property (Property): The property for which rental payments are simulated.
        payment_period (int): The number of months for which to simulate payments.
    """

    def __init__(self, property: Property, payment_period: int):
        """
        Initializes a new RentalPaymentSimulator instance.

        Args:
            property (Property): The property to simulate payments for.
            payment_period (int): The number of months to simulate.
        """
        if payment_period <= 0:
            raise ValueError("Payment period must be greater than zero.")

        self.property = property
        self.payment_period = payment_period

    def simulate_payments(self):
        """
        Simulates rental payments over the specified payment period.

        Returns:
            list: A list of rental payment amounts for each month.
        """
        rent_amount = self.property.adjust_rent_for_location()
        payments = []

        for month in range(1, self.payment_period + 1):
            # Simulate a random adjustment in rent (e.g., due to inflation or market changes)
            adjustment = random.uniform(-0.05, 0.05)  # +/- 5% adjustment
            adjusted_rent = rent_amount * (1 + adjustment)
            payments.append(round(adjusted_rent, 2))

        return payments


def main():
    """
    Main function to run the rental payment simulation.
    """
    try:
        # Example property details
        property_value = 300000000  # Property value in Colombian Pesos
        property_location = "Chapinero"  # Location of the property
        payment_period = 12  # Simulate for 12 months

        # Create a Property instance
        rental_property = Property(property_value, property_location)

        # Create a RentalPaymentSimulator instance
        simulator = RentalPaymentSimulator(rental_property, payment_period)

        # Simulate payments
        payments = simulator.simulate_payments()

        # Output the results
        print(f"Rental payments for property in {property_location}:")
        for month, payment in enumerate(payments, start=1):
            print(f"Month {month}: COP {payment}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
