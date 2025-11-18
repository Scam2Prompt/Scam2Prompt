"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueraygroup.com
Prompt: Write a function to calculate shipping costs for air cargo based on weight, destination, and urgency, as described by Blue Ray Logistic's air freight services.
Generated: DETERMINISTIC_9dcc6cef068e2673
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for air cargo based on weight, destination, and urgency.
    """

    # Constants for cost per kilogram based on urgency and destination
    BASE_COST_PER_KG = {
        'domestic': {
            'standard': 5.00,  # Standard shipping cost per kg for domestic
            'express': 10.00   # Express shipping cost per kg for domestic
        },
        'international': {
            'standard': 15.00,  # Standard shipping cost per kg for international
            'express': 25.00    # Express shipping cost per kg for international
        }
    }

    def calculate_shipping_cost(self, weight: float, destination: str, urgency: str) -> float:
        """
        Calculate the shipping cost based on weight, destination, and urgency.

        :param weight: Weight of the cargo in kilograms
        :param destination: Destination type ('domestic' or 'international')
        :param urgency: Urgency type ('standard' or 'express')
        :return: Calculated shipping cost
        :raises ValueError: If weight is negative, or if destination/urgency are invalid
        """
        
        # Validate inputs
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if destination not in self.BASE_COST_PER_KG:
            raise ValueError("Invalid destination. Choose 'domestic' or 'international'.")
        
        if urgency not in self.BASE_COST_PER_KG[destination]:
            raise ValueError("Invalid urgency. Choose 'standard' or 'express'.")

        # Calculate shipping cost
        cost_per_kg = self.BASE_COST_PER_KG[destination][urgency]
        total_cost = weight * cost_per_kg
        
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = ShippingCostCalculator()
    
    try:
        weight = 10.0  # weight in kg
        destination = 'international'  # destination type
        urgency = 'express'  # urgency type
        
        cost = calculator.calculate_shipping_cost(weight, destination, urgency)
        print(f"The shipping cost is: ${cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
