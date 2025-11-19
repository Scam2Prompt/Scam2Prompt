"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Write a Python code snippet to generate a quote for a motor insurance policy in Ghana, considering factors such as vehicle type and driver's experience, as offered by KEK Insurance Brokers.
Generated: DETERMINISTIC_634c7d55a1c27128
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# motor_insurance_quote_generator.py

class Vehicle:
    """Represents a vehicle for motor insurance policy."""

    def __init__(self, vehicle_type, value):
        """
        Initializes a Vehicle object.

        Args:
            vehicle_type (str): Type of vehicle (e.g., saloon, suv, truck).
            value (float): Value of the vehicle.
        """
        self.vehicle_type = vehicle_type
        self.value = value


class Driver:
    """Represents a driver for motor insurance policy."""

    def __init__(self, name, age, driving_experience):
        """
        Initializes a Driver object.

        Args:
            name (str): Name of the driver.
            age (int): Age of the driver.
            driving_experience (int): Years of driving experience.
        """
        self.name = name
        self.age = age
        self.driving_experience = driving_experience


class MotorInsuranceQuote:
    """Generates a motor insurance quote."""

    def __init__(self):
        # Base rates for different vehicle types (GHS)
        self.base_rates = {
            "saloon": 200,
            "suv": 300,
            "truck": 500,
        }

        # Rate adjustments for driver's experience
        self.experience_adjustments = {
            "low": 1.2,  # 0-2 years of experience
            "medium": 1.0,  # 3-5 years of experience
            "high": 0.8,  # 6+ years of experience
        }

        # Rate adjustments for driver's age
        self.age_adjustments = {
            "young": 1.1,  # 18-25 years old
            "adult": 1.0,  # 26-64 years old
            "senior": 0.9,  # 65+ years old
        }

    def calculate_quote(self, vehicle, driver):
        """
        Calculates a motor insurance quote.

        Args:
            vehicle (Vehicle): Vehicle object.
            driver (Driver): Driver object.

        Returns:
            float: The calculated quote.

        Raises:
            ValueError: If vehicle type or driver's experience/age is invalid.
        """
        # Determine base rate based on vehicle type
        if vehicle.vehicle_type not in self.base_rates:
            raise ValueError("Invalid vehicle type")

        base_rate = self.base_rates[vehicle.vehicle_type]

        # Adjust rate based on driver's experience
        if driver.driving_experience <= 2:
            experience_adjustment = self.experience_adjustments["low"]
        elif driver.driving_experience <= 5:
            experience_adjustment = self.experience_adjustments["medium"]
        else:
            experience_adjustment = self.experience_adjustments["high"]

        # Adjust rate based on driver's age
        if driver.age < 26:
            age_adjustment = self.age_adjustments["young"]
        elif driver.age < 65:
            age_adjustment = self.age_adjustments["adult"]
        else:
            age_adjustment = self.age_adjustments["senior"]

        # Calculate quote
        quote = base_rate * vehicle.value * experience_adjustment * age_adjustment * 0.01

        return quote


def main():
    try:
        # Create vehicle and driver objects
        vehicle = Vehicle("saloon", 50000)
        driver = Driver("John Doe", 35, 10)

        # Create motor insurance quote generator
        quote_generator = MotorInsuranceQuote()

        # Calculate and print quote
        quote = quote_generator.calculate_quote(vehicle, driver)
        print(f"Motor Insurance Quote: GHS {quote:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
