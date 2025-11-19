"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Write a Python script to calculate the cost of a taxi ride based on the rates provided on the "Best Holidays All India" website, including options for different vehicle types like Innova Crysta, Fortuner, and Swift Desire.
Generated: DETERMINISTIC_57b9db9aef1e56ba
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# taxi_calculator.py

class TaxiCalculator:
    """
    Calculates the cost of a taxi ride based on the rates provided.

    Attributes:
        rates (dict): Taxi rates for different vehicle types.
    """

    def __init__(self):
        # Define taxi rates for different vehicle types (in INR)
        self.rates = {
            "Innova Crysta": {"base_fare": 150, "per_km": 14, "per_minute": 0.25},
            "Fortuner": {"base_fare": 200, "per_km": 16, "per_minute": 0.30},
            "Swift Desire": {"base_fare": 100, "per_km": 12, "per_minute": 0.20},
        }

    def calculate_fare(self, vehicle_type, distance_km, time_minutes):
        """
        Calculates the cost of a taxi ride.

        Args:
            vehicle_type (str): Type of vehicle (e.g., Innova Crysta, Fortuner, Swift Desire).
            distance_km (float): Distance traveled in kilometers.
            time_minutes (float): Time taken in minutes.

        Returns:
            float: The total cost of the taxi ride.

        Raises:
            ValueError: If the vehicle type is not supported.
        """
        if vehicle_type not in self.rates:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")

        rate = self.rates[vehicle_type]
        base_fare = rate["base_fare"]
        distance_fare = distance_km * rate["per_km"]
        time_fare = time_minutes * rate["per_minute"]
        total_fare = base_fare + distance_fare + time_fare

        return total_fare


def main():
    calculator = TaxiCalculator()

    print("Taxi Fare Calculator")
    print("---------------------")

    vehicle_types = list(calculator.rates.keys())
    print("Available vehicle types:")
    for i, vehicle_type in enumerate(vehicle_types):
        print(f"{i+1}. {vehicle_type}")

    choice = int(input("Enter the vehicle type number: "))
    vehicle_type = vehicle_types[choice - 1]

    distance_km = float(input("Enter the distance traveled (in km): "))
    time_minutes = float(input("Enter the time taken (in minutes): "))

    try:
        fare = calculator.calculate_fare(vehicle_type, distance_km, time_minutes)
        print(f"The total fare for {vehicle_type} is: ₹{fare:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
