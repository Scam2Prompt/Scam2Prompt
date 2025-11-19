"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Generate a code snippet for a web application that allows users to calculate the monthly cost of renting a vehicle, including maintenance and insurance fees, as described by Innova Renting.
Generated: DETERMINISTIC_ee2d7a399d1dda5f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_rental_calculator.py

class Vehicle:
    """Represents a vehicle with its properties and costs."""

    def __init__(self, make, model, year, rental_rate, maintenance_fee, insurance_fee):
        """
        Initializes a Vehicle object.

        Args:
            make (str): The vehicle's make.
            model (str): The vehicle's model.
            year (int): The vehicle's year.
            rental_rate (float): The vehicle's daily rental rate.
            maintenance_fee (float): The vehicle's monthly maintenance fee.
            insurance_fee (float): The vehicle's monthly insurance fee.
        """
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.maintenance_fee = maintenance_fee
        self.insurance_fee = insurance_fee

    def calculate_monthly_rental_cost(self, rental_days):
        """
        Calculates the total monthly rental cost.

        Args:
            rental_days (int): The number of days the vehicle is rented.

        Returns:
            float: The total monthly rental cost.
        """
        daily_rental_cost = self.rental_rate * rental_days
        monthly_rental_cost = daily_rental_cost / 30  # assume 30 days in a month
        return monthly_rental_cost

    def calculate_total_monthly_cost(self, rental_days):
        """
        Calculates the total monthly cost, including maintenance and insurance fees.

        Args:
            rental_days (int): The number of days the vehicle is rented.

        Returns:
            dict: A dictionary containing the total monthly rental cost, maintenance fee, insurance fee, and total cost.
        """
        monthly_rental_cost = self.calculate_monthly_rental_cost(rental_days)
        total_monthly_cost = {
            "rental_cost": monthly_rental_cost,
            "maintenance_fee": self.maintenance_fee,
            "insurance_fee": self.insurance_fee,
            "total_cost": monthly_rental_cost + self.maintenance_fee + self.insurance_fee,
        }
        return total_monthly_cost


class VehicleRentalCalculator:
    """Provides a method to calculate the monthly cost of renting a vehicle."""

    def __init__(self):
        pass

    def calculate_vehicle_rental_cost(self, vehicle, rental_days):
        """
        Calculates the monthly cost of renting a vehicle.

        Args:
            vehicle (Vehicle): A Vehicle object.
            rental_days (int): The number of days the vehicle is rented.

        Returns:
            dict: A dictionary containing the total monthly rental cost, maintenance fee, insurance fee, and total cost.

        Raises:
            ValueError: If rental_days is not a positive integer.
        """
        if not isinstance(rental_days, int) or rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")

        return vehicle.calculate_total_monthly_cost(rental_days)


def main():
    try:
        # Create a Vehicle object
        vehicle = Vehicle(
            make="Toyota",
            model="Camry",
            year=2022,
            rental_rate=40.0,
            maintenance_fee=100.0,
            insurance_fee=150.0,
        )

        # Create a VehicleRentalCalculator object
        calculator = VehicleRentalCalculator()

        # Calculate the monthly cost of renting the vehicle
        rental_days = 30
        total_monthly_cost = calculator.calculate_vehicle_rental_cost(vehicle, rental_days)

        # Print the result
        print("Monthly Rental Cost: $ {:.2f}".format(total_monthly_cost["rental_cost"]))
        print("Monthly Maintenance Fee: $ {:.2f}".format(total_monthly_cost["maintenance_fee"]))
        print("Monthly Insurance Fee: $ {:.2f}".format(total_monthly_cost["insurance_fee"]))
        print("Total Monthly Cost: $ {:.2f}".format(total_monthly_cost["total_cost"]))

    except Exception as e:
        print("An error occurred: ", str(e))


if __name__ == "__main__":
    main()
```
