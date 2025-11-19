"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delivery-services.online
Prompt: Write a Python function that calculates delivery costs based on distance and weight for an online delivery service.
Generated: DETERMINISTIC_0991928e3fb96dad
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeliveryCostCalculator:
    """
    A class to calculate delivery costs based on distance and weight.
    """

    BASE_COST = 5.0  # Base cost for delivery
    COST_PER_KM = 1.5  # Cost per kilometer
    COST_PER_KG = 0.5  # Cost per kilogram

    def calculate_cost(self, distance_km, weight_kg):
        """
        Calculate the delivery cost based on distance and weight.

        Parameters:
        distance_km (float): The distance in kilometers for the delivery.
        weight_kg (float): The weight of the package in kilograms.

        Returns:
        float: The total delivery cost.

        Raises:
        ValueError: If distance or weight is negative.
        """

        # Validate inputs
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative.")
        
        # Calculate total cost
        total_cost = self.BASE_COST + (self.COST_PER_KM * distance_km) + (self.COST_PER_KG * weight_kg)
        
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = DeliveryCostCalculator()
    try:
        distance = float(input("Enter distance in kilometers: "))
        weight = float(input("Enter weight in kilograms: "))
        cost = calculator.calculate_cost(distance, weight)
        print(f"The total delivery cost is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
