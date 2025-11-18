"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Create a script to simulate the cost estimation for kanalizacija (drainage system) installation, including jaški (manholes) and greznice (septic tanks).
Generated: DETERMINISTIC_521f2577189656db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DrainageSystemEstimator:
    def __init__(self, length_m, depth_m, manhole_cost, septic_tank_cost, manhole_spacing_m):
        """
        Initialize the estimator with project parameters.

        :param length_m: Total length of the drainage system in meters
        :param depth_m: Depth of the drainage system in meters
        :param manhole_cost: Cost of each manhole
        :param septic_tank_cost: Cost of each septic tank
        :param manhole_spacing_m: Spacing in meters between manholes
        """
        self.length_m = length_m
        self.depth_m = depth_m
        self.manhole_cost = manhole_cost
        self.septic_tank_cost = septic_tank_cost
        self.manhole_spacing_m = manhole_spacing_m

    def calculate_manholes(self):
        """
        Calculate the total number of manholes required.

        :return: Total number of manholes
        """
        if self.manhole_spacing_m <= 0:
            raise ValueError("Manhole spacing must be greater than zero.")
        num_manhole = math.ceil(self.length_m / self.manhole_spacing_m)
        return num_manhole

    def estimate_cost(self):
        """
        Estimate the total cost for the drainage system installation.

        :return: Total estimated cost
        """
        try:
            num_manhole = self.calculate_manholes()
            total_cost = (num_manhole * self.manhole_cost) + self.septic_tank_cost
            return total_cost
        except ValueError as e:
            print(f"Error in calculations: {e}")
            return None

def main():
    # Define project parameters
    length_m = 100  # Total length of the drainage system in meters
    depth_m = 2.0   # Depth of the drainage system in meters
    manhole_cost = 1500  # Cost of each manhole in currency units
    septic_tank_cost = 5000  # Cost of each septic tank in currency units
    manhole_spacing_m = 20  # Spacing between manholes in meters

    # Create an instance of the estimator
    estimator = DrainageSystemEstimator(length_m, depth_m, manhole_cost, septic_tank_cost, manhole_spacing_m)

    # Estimate cost
    total_estimated_cost = estimator.estimate_cost()
    
    if total_estimated_cost is not None:
        print(f"Total estimated cost for installation: {total_estimated_cost} currency units")

if __name__ == "__main__":
    main()
```
