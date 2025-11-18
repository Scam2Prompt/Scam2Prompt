"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Write a Python script to calculate the cost of a taxi ride based on the rates provided on the "Best Holidays All India" website, including options for different vehicle types like Innova Crysta, Fortuner, and Swift Desire.
Generated: DETERMINISTIC_57b9db9aef1e56ba
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TaxiRideCalculator:
    """A class to calculate the cost of a taxi ride based on vehicle type and distance."""

    # Rates for different vehicle types (in INR)
    rates = {
        'Innova Crysta': 15,  # Rate per km
        'Fortuner': 20,       # Rate per km
        'Swift Desire': 10     # Rate per km
    }

    def __init__(self, vehicle_type, distance):
        """
        Initializes the TaxiRideCalculator with the vehicle type and distance.
        
        :param vehicle_type: str, the type of vehicle (Innova Crysta, Fortuner, or Swift Desire)
        :param distance: float, the distance of the ride in kilometers
        """
        self.vehicle_type = vehicle_type
        self.distance = distance

    def validate_inputs(self):
        """Validates the vehicle type and distance."""
        if self.vehicle_type not in self.rates:
            raise ValueError(f"Invalid vehicle type: {self.vehicle_type}. Choose from {list(self.rates.keys())}.")
        
        if not isinstance(self.distance, (int, float)) or self.distance < 0:
            raise ValueError("Distance must be a non-negative number.")

    def calculate_cost(self):
        """Calculates the total cost of the ride."""
        self.validate_inputs()
        cost = self.rates[self.vehicle_type] * self.distance
        return cost

def main():
    """Main function to execute the taxi ride cost calculation."""
    try:
        # User input for vehicle type and distance
        vehicle_type = input("Enter vehicle type (Innova Crysta, Fortuner, Swift Desire): ")
        distance = float(input("Enter distance in kilometers: "))

        # Initialize the calculator and calculate the cost
        taxi_ride = TaxiRideCalculator(vehicle_type, distance)
        total_cost = taxi_ride.calculate_cost()

        print(f"The total cost of the taxi ride in a {vehicle_type} for {distance} km is: INR {total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
