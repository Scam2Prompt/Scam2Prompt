"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a program to calculate freight costs dynamically, incorporating Bin Qutab Logistics' ability to match freight with the right vehicle and route while offering flexibility.
Generated: DETERMINISTIC_ca2342f25bfa4bfe
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FreightCalculator:
    """
    A class to calculate freight costs based on vehicle type, distance, and weight.
    """

    def __init__(self):
        # Define vehicle types and their cost per mile
        self.vehicle_costs = {
            'small': 1.0,  # Cost per mile for small vehicle
            'medium': 1.5,  # Cost per mile for medium vehicle
            'large': 2.0,  # Cost per mile for large vehicle
        }

    def calculate_cost(self, vehicle_type, distance, weight):
        """
        Calculate the freight cost based on vehicle type, distance, and weight.

        :param vehicle_type: Type of vehicle (small, medium, large)
        :param distance: Distance in miles
        :param weight: Weight of the freight in pounds
        :return: Total cost of freight
        :raises ValueError: If vehicle type is invalid or distance/weight is negative
        """
        # Validate inputs
        if vehicle_type not in self.vehicle_costs:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}. Choose from {list(self.vehicle_costs.keys())}.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        # Calculate cost
        cost_per_mile = self.vehicle_costs[vehicle_type]
        total_cost = cost_per_mile * distance

        # Add additional cost based on weight (example: $0.1 per pound)
        weight_cost = 0.1 * weight
        total_cost += weight_cost

        return total_cost

    def get_vehicle_options(self):
        """
        Get available vehicle options for freight.

        :return: List of available vehicle types
        """
        return list(self.vehicle_costs.keys())


def main():
    """
    Main function to execute the freight cost calculation.
    """
    calculator = FreightCalculator()

    # Example usage
    try:
        vehicle_type = 'medium'  # Example vehicle type
        distance = 100  # Example distance in miles
        weight = 500  # Example weight in pounds

        # Calculate the freight cost
        cost = calculator.calculate_cost(vehicle_type, distance, weight)
        print(f"The total freight cost for a {weight} lb load over {distance} miles using a {vehicle_type} vehicle is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
