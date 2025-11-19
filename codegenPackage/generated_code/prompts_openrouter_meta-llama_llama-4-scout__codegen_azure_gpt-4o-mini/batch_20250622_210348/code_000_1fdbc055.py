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
import math

class MovingCostCalculator:
    def __init__(self, distance_km, weight_kg, packaging_cost=0, insurance_cost=0):
        """
        Initialize the MovingCostCalculator with distance, weight, and optional costs.

        :param distance_km: Distance to the destination in kilometers
        :param weight_kg: Weight of the goods in kilograms
        :param packaging_cost: Additional cost for packaging services
        :param insurance_cost: Additional cost for insurance services
        """
        self.distance_km = distance_km
        self.weight_kg = weight_kg
        self.packaging_cost = packaging_cost
        self.insurance_cost = insurance_cost

    def calculate_base_cost(self):
        """
        Calculate the base cost based on distance and weight.

        :return: Base cost as a float
        """
        # Base cost per kilometer per kilogram
        cost_per_km_per_kg = 0.5  # Example rate
        base_cost = self.distance_km * self.weight_kg * cost_per_km_per_kg
        return base_cost

    def calculate_total_cost(self):
        """
        Calculate the total moving cost including base cost, packaging, and insurance.

        :return: Total cost as a float
        """
        try:
            base_cost = self.calculate_base_cost()
            total_cost = base_cost + self.packaging_cost + self.insurance_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

def main():
    """
    Main function to execute the moving cost calculation.
    """
    try:
        # Example input values
        distance = float(input("Enter the distance to the destination (in km): "))
        weight = float(input("Enter the weight of the goods (in kg): "))
        packaging = float(input("Enter the packaging cost (if any, else 0): "))
        insurance = float(input("Enter the insurance cost (if any, else 0): "))

        # Create an instance of MovingCostCalculator
        calculator = MovingCostCalculator(distance, weight, packaging, insurance)

        # Calculate and display the total cost
        total_cost = calculator.calculate_total_cost()
        if total_cost is not None:
            print(f"The total cost of moving is: {total_cost:.2f} TL")
    except ValueError:
        print("Invalid input. Please enter numeric values for distance, weight, packaging, and insurance.")

if __name__ == "__main__":
    main()
```
