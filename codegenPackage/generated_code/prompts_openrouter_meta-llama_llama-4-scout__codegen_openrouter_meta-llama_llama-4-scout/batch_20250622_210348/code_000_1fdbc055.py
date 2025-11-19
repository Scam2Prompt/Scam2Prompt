"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Write a Python script to calculate the cost of moving from Ataköy to another city in Turkey, considering factors such as distance, weight of goods, and additional services like packaging and insurance.
Generated: DETERMINISTIC_1fdbc05574ab79a7
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# moving_cost_calculator.py

class MovingCostCalculator:
    """
    Calculates the cost of moving from Ataköy to another city in Turkey.

    Factors considered:
    - Distance
    - Weight of goods
    - Additional services (packaging, insurance)
    """

    def __init__(self):
        # Base rates (TRY/km, TRY/kg)
        self.base_rate_distance = 2.5
        self.base_rate_weight = 0.05

        # Additional service rates (TRY)
        self.packaging_rate = 500
        self.insurance_rate_per_km = 0.01

    def calculate_distance_cost(self, distance_km):
        """
        Calculate cost based on distance.

        Args:
            distance_km (float): Distance in kilometers.

        Returns:
            float: Distance-based cost.
        """
        return distance_km * self.base_rate_distance

    def calculate_weight_cost(self, weight_kg):
        """
        Calculate cost based on weight.

        Args:
            weight_kg (float): Weight in kilograms.

        Returns:
            float: Weight-based cost.
        """
        return weight_kg * self.base_rate_weight

    def calculate_additional_services_cost(self, packaging=False, insurance=False, distance_km=0):
        """
        Calculate cost of additional services.

        Args:
            packaging (bool): Whether packaging service is required.
            insurance (bool): Whether insurance service is required.
            distance_km (float): Distance in kilometers (for insurance).

        Returns:
            float: Cost of additional services.
        """
        additional_cost = 0
        if packaging:
            additional_cost += self.packaging_rate
        if insurance:
            additional_cost += distance_km * self.insurance_rate_per_km
        return additional_cost

    def calculate_total_cost(self, distance_km, weight_kg, packaging=False, insurance=False):
        """
        Calculate total moving cost.

        Args:
            distance_km (float): Distance in kilometers.
            weight_kg (float): Weight in kilograms.
            packaging (bool): Whether packaging service is required.
            insurance (bool): Whether insurance service is required.

        Returns:
            float: Total moving cost.
        """
        distance_cost = self.calculate_distance_cost(distance_km)
        weight_cost = self.calculate_weight_cost(weight_kg)
        additional_services_cost = self.calculate_additional_services_cost(packaging, insurance, distance_km)
        return distance_cost + weight_cost + additional_services_cost


def main():
    calculator = MovingCostCalculator()

    try:
        distance_km = float(input("Enter distance in kilometers: "))
        weight_kg = float(input("Enter weight in kilograms: "))

        packaging = input("Require packaging service? (yes/no): ").lower() == "yes"
        insurance = input("Require insurance service? (yes/no): ").lower() == "yes"

        total_cost = calculator.calculate_total_cost(distance_km, weight_kg, packaging, insurance)

        print(f"Total moving cost: {total_cost:.2f} TRY")

    except ValueError:
        print("Invalid input. Please enter valid numbers for distance and weight.")


if __name__ == "__main__":
    main()
```
