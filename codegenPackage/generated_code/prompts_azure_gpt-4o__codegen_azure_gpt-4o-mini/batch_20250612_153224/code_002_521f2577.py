"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Create a script to simulate the cost estimation for kanalizacija (drainage system) installation, including jaški (manholes) and greznice (septic tanks).
Generated: DETERMINISTIC_521f2577189656db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class DrainageSystemEstimator:
    def __init__(self, base_cost_per_meter, manhole_cost, septic_tank_cost):
        """
        Initialize the estimator with base costs.
        
        :param base_cost_per_meter: Cost of installing drainage per meter
        :param manhole_cost: Cost of installing a manhole
        :param septic_tank_cost: Cost of installing a septic tank
        """
        self.base_cost_per_meter = base_cost_per_meter
        self.manhole_cost = manhole_cost
        self.septic_tank_cost = septic_tank_cost

    def estimate_cost(self, length, num_manholes, num_septic_tanks):
        """
        Estimate the total cost of the drainage system installation.
        
        :param length: Length of the drainage system in meters
        :param num_manholes: Number of manholes to be installed
        :param num_septic_tanks: Number of septic tanks to be installed
        :return: Total estimated cost
        """
        if length < 0 or num_manholes < 0 or num_septic_tanks < 0:
            raise ValueError("Length, number of manholes, and number of septic tanks must be non-negative.")

        total_cost = (self.base_cost_per_meter * length) + (self.manhole_cost * num_manholes) + (self.septic_tank_cost * num_septic_tanks)
        return total_cost

    def to_json(self):
        """
        Convert the estimator configuration to JSON format.
        
        :return: JSON string of the estimator configuration
        """
        return json.dumps({
            "base_cost_per_meter": self.base_cost_per_meter,
            "manhole_cost": self.manhole_cost,
            "septic_tank_cost": self.septic_tank_cost
        }, indent=4)

def main():
    # Configuration for the cost estimator
    base_cost_per_meter = 50.0  # Cost per meter of drainage
    manhole_cost = 300.0         # Cost per manhole
    septic_tank_cost = 1500.0    # Cost per septic tank

    # Create an instance of the estimator
    estimator = DrainageSystemEstimator(base_cost_per_meter, manhole_cost, septic_tank_cost)

    # Example input values
    length = 100  # Length of the drainage system in meters
    num_manholes = 5  # Number of manholes
    num_septic_tanks = 2  # Number of septic tanks

    try:
        # Estimate the total cost
        total_cost = estimator.estimate_cost(length, num_manholes, num_septic_tanks)
        print(f"Total estimated cost for installation: ${total_cost:.2f}")

        # Output the estimator configuration in JSON format
        print("Estimator configuration:")
        print(estimator.to_json())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
