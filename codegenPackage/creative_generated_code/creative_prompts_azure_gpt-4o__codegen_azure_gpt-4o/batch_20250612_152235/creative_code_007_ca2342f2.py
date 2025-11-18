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
import sys

class FreightCalculator:
    """
    A class to dynamically calculate freight costs while matching freight 
    with the right vehicle and route, offering flexibility.
    """

    def __init__(self):
        # Base costs for different vehicle types (per kilometer)
        self.vehicle_costs = {
            'truck': 2.5,  # Cost per km for a truck
            'van': 1.8,    # Cost per km for a van
            'bike': 0.5    # Cost per km for a bike
        }

        # Routes and their multipliers (based on traffic and road conditions)
        self.route_multipliers = {
            'urban': 1.5,  # Urban routes cost more
            'rural': 1.0,  # Rural routes are standard cost
            'highway': 0.8 # Highways are cheaper
        }

    def calculate_cost(self, distance, vehicle_type, route_type):
        """
        Calculate the freight cost dynamically based on distance, vehicle type, and route.
        
        Parameters:
            distance (float): Distance of the route (in kilometers).
            vehicle_type (str): Type of the vehicle (e.g., 'truck', 'van', 'bike').
            route_type (str): Type of the route (e.g., 'urban', 'rural', 'highway').
        
        Returns:
            float: Total freight cost.
        
        Raises:
            ValueError: If an invalid vehicle type or route type is provided.
        """
        # Validate vehicle type
        if vehicle_type not in self.vehicle_costs:
            raise ValueError(f"Invalid vehicle type '{vehicle_type}'. Valid types are {list(self.vehicle_costs.keys())}.")
        
        # Validate route type
        if route_type not in self.route_multipliers:
            raise ValueError(f"Invalid route type '{route_type}'. Valid types are {list(self.route_multipliers.keys())}.")
        
        # Calculate cost using the base cost, route multiplier, and distance
        base_cost = self.vehicle_costs[vehicle_type]
        route_multiplier = self.route_multipliers[route_type]
        total_cost = distance * base_cost * route_multiplier
        
        return round(total_cost, 2)

def main():
    """
    Main function to interact with the FreightCalculator and calculate freight dynamically.
    """
    print("Welcome to Bin Qutab Logistics Freight Calculator")
    try:
        # Input for distance, vehicle type, and route type
        distance = float(input("Enter the distance (in km): "))
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
        
        vehicle_type = input("Enter the vehicle type (truck/van/bike): ").strip().lower()
        route_type = input("Enter the route type (urban/rural/highway): ").strip().lower()
        
        # Create an instance of FreightCalculator
        calculator = FreightCalculator()
        
        # Calculate and display the freight cost
        cost = calculator.calculate_cost(distance, vehicle_type, route_type)
        print(f"The total freight cost is: ${cost}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
