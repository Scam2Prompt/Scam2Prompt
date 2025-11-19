"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirFreightCalculator:
    """
    A class to calculate the total cost of air freight forwarding.
    """

    def __init__(self, base_rate_per_kg, rate_per_km, insurance_rate):
        """
        Initializes the AirFreightCalculator with the given rates.

        :param base_rate_per_kg: Base rate charged per kilogram of cargo.
        :param rate_per_km: Rate charged per kilometer of distance.
        :param insurance_rate: Rate charged for insurance as a percentage of the total cost.
        """
        self.base_rate_per_kg = base_rate_per_kg
        self.rate_per_km = rate_per_km
        self.insurance_rate = insurance_rate

    def calculate_cost(self, weight, distance, insure=False):
        """
        Calculates the total cost of air freight forwarding.

        :param weight: Weight of the cargo in kilograms.
        :param distance: Distance to be traveled in kilometers.
        :param insure: Boolean indicating whether insurance is required.
        :return: Total cost of air freight forwarding.
        :raises ValueError: If weight or distance is negative.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        # Calculate the base cost based on weight and distance
        base_cost = (self.base_rate_per_kg * weight) + (self.rate_per_km * distance)

        # Calculate insurance cost if applicable
        insurance_cost = (self.insurance_rate / 100) * base_cost if insure else 0

        # Total cost is the sum of base cost and insurance cost
        total_cost = base_cost + insurance_cost

        return total_cost


# Example usage
if __name__ == "__main__":
    # Initialize the calculator with example rates
    calculator = AirFreightCalculator(base_rate_per_kg=5.0, rate_per_km=2.0, insurance_rate=1.5)

    try:
        # Calculate the cost for a specific weight and distance
        total_cost = calculator.calculate_cost(weight=100, distance=500, insure=True)
        print(f"The total cost of air freight forwarding is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
