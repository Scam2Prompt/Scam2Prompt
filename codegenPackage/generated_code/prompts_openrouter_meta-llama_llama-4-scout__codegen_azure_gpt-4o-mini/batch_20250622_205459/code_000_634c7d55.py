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
import random

class MotorInsuranceQuote:
    """
    A class to represent a motor insurance quote generator for KEK Insurance Brokers.
    """

    def __init__(self, vehicle_type, driver_experience):
        """
        Initializes the MotorInsuranceQuote with vehicle type and driver's experience.

        :param vehicle_type: str - Type of the vehicle (e.g., 'sedan', 'SUV', 'truck')
        :param driver_experience: int - Years of driving experience
        """
        self.vehicle_type = vehicle_type.lower()
        self.driver_experience = driver_experience
        self.base_rate = 100  # Base rate for the insurance policy

    def calculate_quote(self):
        """
        Calculates the insurance quote based on vehicle type and driver's experience.

        :return: float - The calculated insurance quote
        """
        try:
            vehicle_factor = self.get_vehicle_factor()
            experience_factor = self.get_experience_factor()

            # Calculate the final quote
            quote = self.base_rate * vehicle_factor * experience_factor
            return round(quote, 2)

        except Exception as e:
            print(f"Error calculating quote: {e}")
            return None

    def get_vehicle_factor(self):
        """
        Determines the vehicle factor based on the type of vehicle.

        :return: float - The factor to be applied based on vehicle type
        """
        vehicle_factors = {
            'sedan': 1.0,
            'suv': 1.2,
            'truck': 1.5,
            'motorcycle': 0.8
        }

        if self.vehicle_type in vehicle_factors:
            return vehicle_factors[self.vehicle_type]
        else:
            raise ValueError("Invalid vehicle type provided.")

    def get_experience_factor(self):
        """
        Determines the experience factor based on driver's experience.

        :return: float - The factor to be applied based on driver's experience
        """
        if self.driver_experience < 1:
            return 1.5  # New drivers
        elif 1 <= self.driver_experience <= 5:
            return 1.0  # Experienced drivers
        else:
            return 0.8  # Very experienced drivers

def main():
    """
    Main function to execute the quote generation process.
    """
    # Example input
    vehicle_type = input("Enter the vehicle type (sedan, SUV, truck, motorcycle): ")
    driver_experience = int(input("Enter the driver's years of experience: "))

    # Create an instance of MotorInsuranceQuote
    quote_generator = MotorInsuranceQuote(vehicle_type, driver_experience)

    # Generate the quote
    quote = quote_generator.calculate_quote()

    if quote is not None:
        print(f"The insurance quote for your {vehicle_type} with {driver_experience} years of experience is: GHS {quote}")

if __name__ == "__main__":
    main()
```
