"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Write a program to calculate freight costs dynamically, incorporating Bin Qutab Logistics' ability to match freight with the right vehicle and route while offering flexibility.
Generated: DETERMINISTIC_ca2342f25bfa4bfe
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FreightCalculator:
    """
    A class to calculate freight costs based on vehicle type, route distance, 
    and cargo weight for Bin Qutab Logistics.
    """

    def __init__(self):
        # Define vehicle types and their associated costs per kilometer
        self.vehicle_costs = {
            'van': 1.5,     # Cost per km for van
            'truck': 2.5,   # Cost per km for truck
            'container': 3.5 # Cost per km for container
        }
        self.default_vehicle = 'van'

    def select_vehicle(self, cargo_weight):
        """
        Selects the appropriate vehicle based on cargo weight.
        
        :param cargo_weight: Weight of the cargo in kilograms
        :return: Vehicle type as a string
        """
        if cargo_weight <= 1000:
            return 'van'
        elif cargo_weight <= 5000:
            return 'truck'
        else:
            return 'container'

    def calculate_cost(self, distance, cargo_weight):
        """
        Calculates the total freight cost based on distance and cargo weight.
        
        :param distance: Distance to be covered in kilometers
        :param cargo_weight: Weight of the cargo in kilograms
        :return: Total cost in currency
        :raises ValueError: If distance or cargo_weight is negative
        """
        if distance < 0 or cargo_weight < 0:
            raise ValueError("Distance and cargo weight must be non-negative")

        vehicle_type = self.select_vehicle(cargo_weight)
        cost_per_km = self.vehicle_costs.get(vehicle_type, self.vehicle_costs[self.default_vehicle])
        
        total_cost = cost_per_km * distance
        
        return total_cost

    def display_cost(self, distance, cargo_weight):
        """
        Displays the calculated freight cost.
        
        :param distance: Distance to be covered in kilometers
        :param cargo_weight: Weight of the cargo in kilograms
        """
        try:
            cost = self.calculate_cost(distance, cargo_weight)
            print(f"Freight Cost for {cargo_weight}kg over {distance}km using {self.select_vehicle(cargo_weight)}: ${cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    freight_calculator = FreightCalculator()
    
    # Sample distances and weights
    distances = [10, 20, -5]  # Last entry should raise an error
    weights = [500, 2500, 6000] # Last entry should use container

    for distance, weight in zip(distances, weights):
        freight_calculator.display_cost(distance, weight)
```
