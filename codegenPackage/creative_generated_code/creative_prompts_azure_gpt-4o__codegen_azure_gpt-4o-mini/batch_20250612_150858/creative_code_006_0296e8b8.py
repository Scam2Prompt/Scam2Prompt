"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Develop a function to calculate the total cost of a multi-destination trip using Vansol Travel's package pricing structure.
Generated: DETERMINISTIC_0296e8b8953954e7
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TripCostCalculator:
    def __init__(self):
        # Package pricing structure (cost per destination)
        self.package_pricing = {
            'local': 100,   # Cost for local destinations
            'national': 200, # Cost for national destinations
            'international': 300 # Cost for international destinations
        }

    def calculate_total_cost(self, destinations):
        """
        Calculate the total cost of a multi-destination trip.

        :param destinations: List of destination types (e.g., 'local', 'national', 'international')
        :return: Total cost of the trip
        :raises ValueError: If an invalid destination type is provided
        """
        total_cost = 0
        
        for dest in destinations:
            if dest not in self.package_pricing:
                raise ValueError(f"Invalid destination type: {dest}")

            total_cost += self.package_pricing[dest]
        
        return total_cost

# Example usage
if __name__ == "__main__":
    calculator = TripCostCalculator()
    
    try:
        # Example list of destinations
        destinations = ['local', 'national', 'international', 'local']
        total_cost = calculator.calculate_total_cost(destinations)
        print(f"The total cost of the trip is: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
