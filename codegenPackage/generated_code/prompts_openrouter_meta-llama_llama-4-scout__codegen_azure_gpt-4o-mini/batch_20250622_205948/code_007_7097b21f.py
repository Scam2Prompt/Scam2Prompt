"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Write a script to calculate costs and optimize logistics for dry load services, taking into account factors like distance, weight, and delivery time for a company like Calmar Transport."
Generated: DETERMINISTIC_7097b21fd39c6687
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple

class LoadService:
    def __init__(self, base_rate: float, distance_rate: float, weight_rate: float):
        """
        Initialize the LoadService with base rates for distance and weight.
        
        :param base_rate: The base cost for the service.
        :param distance_rate: The cost per mile/km.
        :param weight_rate: The cost per weight unit (e.g., per kg or lb).
        """
        self.base_rate = base_rate
        self.distance_rate = distance_rate
        self.weight_rate = weight_rate

    def calculate_cost(self, distance: float, weight: float) -> float:
        """
        Calculate the total cost based on distance and weight.
        
        :param distance: The distance to be traveled.
        :param weight: The weight of the load.
        :return: The total cost for the service.
        """
        if distance < 0 or weight < 0:
            raise ValueError("Distance and weight must be non-negative values.")
        
        cost = self.base_rate + (self.distance_rate * distance) + (self.weight_rate * weight)
        return cost

    def optimize_logistics(self, deliveries: List[Dict[str, float]]) -> Tuple[float, List[Dict[str, float]]]:
        """
        Optimize logistics by calculating costs for multiple deliveries and sorting them by cost.
        
        :param deliveries: A list of dictionaries containing 'distance' and 'weight' for each delivery.
        :return: A tuple containing the total cost and a sorted list of deliveries by cost.
        """
        if not deliveries:
            raise ValueError("Deliveries list cannot be empty.")
        
        total_cost = 0
        delivery_costs = []

        for delivery in deliveries:
            distance = delivery.get('distance', 0)
            weight = delivery.get('weight', 0)
            cost = self.calculate_cost(distance, weight)
            total_cost += cost
            delivery_costs.append({'distance': distance, 'weight': weight, 'cost': cost})

        # Sort deliveries by cost in ascending order
        delivery_costs.sort(key=lambda x: x['cost'])
        return total_cost, delivery_costs

def main():
    # Example rates for Calmar Transport
    base_rate = 50.0  # Base cost for the service
    distance_rate = 1.5  # Cost per mile/km
    weight_rate = 0.75  # Cost per weight unit

    # Initialize the LoadService
    service = LoadService(base_rate, distance_rate, weight_rate)

    # Example deliveries
    deliveries = [
        {'distance': 100, 'weight': 200},
        {'distance': 150, 'weight': 100},
        {'distance': 50, 'weight': 300},
    ]

    try:
        total_cost, optimized_deliveries = service.optimize_logistics(deliveries)
        print(f"Total Cost: ${total_cost:.2f}")
        print("Optimized Deliveries:")
        for delivery in optimized_deliveries:
            print(f"Distance: {delivery['distance']} miles, Weight: {delivery['weight']} lbs, Cost: ${delivery['cost']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
