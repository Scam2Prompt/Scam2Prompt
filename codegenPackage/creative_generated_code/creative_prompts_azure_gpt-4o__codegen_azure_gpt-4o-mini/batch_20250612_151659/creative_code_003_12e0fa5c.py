"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Develop an algorithm to estimate the cost of moving furniture based on شركة آل البيت's recommendations for budget planning and minimizing expenses.
Generated: DETERMINISTIC_12e0fa5c8d9875e1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FurnitureMoversCostEstimator:
    """
    A class to estimate the cost of moving furniture based on specific recommendations
    for budget planning and minimizing expenses.
    """

    def __init__(self, base_cost_per_item=50, distance_rate=1.5, insurance_rate=0.02):
        """
        Initializes the estimator with fixed rates for cost calculation.

        Parameters:
        base_cost_per_item (float): The base cost for moving each item.
        distance_rate (float): The cost per mile for transportation.
        insurance_rate (float): The cost percentage for insurance on total value.
        """
        self.base_cost_per_item = base_cost_per_item
        self.distance_rate = distance_rate
        self.insurance_rate = insurance_rate

    def estimate_cost(self, items_count, distance, item_value):
        """
        Estimates the total moving cost based on the number of items, distance to move,
        and value of the items.

        Parameters:
        items_count (int): The number of items to be moved.
        distance (float): The distance in miles to move the items.
        item_value (float): The total value of the items being moved.

        Returns:
        float: The estimated total cost of moving the furniture.
        """
        if items_count < 0 or distance < 0 or item_value < 0:
            raise ValueError("Items count, distance and item value must be non-negative.")

        # Base cost for moving items
        base_cost = self.base_cost_per_item * items_count
        
        # Cost based on distance
        distance_cost = self.distance_rate * distance
        
        # Insurance cost based on item value
        insurance_cost = self.insurance_rate * item_value
        
        # Total estimated cost
        total_cost = base_cost + distance_cost + insurance_cost
        
        return total_cost

def main():
    """
    Main function to run the cost estimator with example data.
    """
    try:
        # Example input
        items_count = 10        # Number of items
        distance = 20           # Distance in miles
        item_value = 5000       # Total value of items in dollars

        # Create an instance of the estimator
        estimator = FurnitureMoversCostEstimator()

        # Calculate estimated cost
        estimated_cost = estimator.estimate_cost(items_count, distance, item_value)
        
        # Output the result
        print(f"Estimated cost of moving furniture: ${estimated_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
