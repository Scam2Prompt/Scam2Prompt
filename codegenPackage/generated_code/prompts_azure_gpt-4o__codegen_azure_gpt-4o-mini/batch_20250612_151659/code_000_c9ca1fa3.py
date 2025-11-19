"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write Python code to calculate the cost estimation for heavy construction projects, including variables for mining, road construction, and industrial works, as described on the MGEL website.
Generated: DETERMINISTIC_c9ca1fa32dc910bf
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConstructionCostEstimator:
    """
    A class to estimate the cost of heavy construction projects including mining,
    road construction, and industrial works.
    """

    def __init__(self, mining_cost_per_unit, road_cost_per_km, industrial_cost_per_sq_m):
        """
        Initializes the cost estimator with the given cost parameters.

        :param mining_cost_per_unit: Cost associated with mining per unit
        :param road_cost_per_km: Cost associated with road construction per kilometer
        :param industrial_cost_per_sq_m: Cost associated with industrial works per square meter
        """
        self.mining_cost_per_unit = mining_cost_per_unit
        self.road_cost_per_km = road_cost_per_km
        self.industrial_cost_per_sq_m = industrial_cost_per_sq_m

    def estimate_mining_cost(self, units):
        """
        Estimates the total mining cost based on the number of units.

        :param units: Number of units to be mined
        :return: Total mining cost
        """
        if units < 0:
            raise ValueError("Units must be a non-negative number.")
        return self.mining_cost_per_unit * units

    def estimate_road_cost(self, kilometers):
        """
        Estimates the total road construction cost based on the distance in kilometers.

        :param kilometers: Length of the road in kilometers
        :return: Total road construction cost
        """
        if kilometers < 0:
            raise ValueError("Kilometers must be a non-negative number.")
        return self.road_cost_per_km * kilometers

    def estimate_industrial_cost(self, square_meters):
        """
        Estimates the total cost for industrial works based on the area in square meters.

        :param square_meters: Area of the industrial works in square meters
        :return: Total industrial works cost
        """
        if square_meters < 0:
            raise ValueError("Square meters must be a non-negative number.")
        return self.industrial_cost_per_sq_m * square_meters

    def total_estimate(self, units, kilometers, square_meters):
        """
        Calculates the total cost estimation for the construction project.

        :param units: Number of mining units
        :param kilometers: Length of the road in kilometers
        :param square_meters: Area of the industrial works in square meters
        :return: Total estimated cost
        """
        mining_cost = self.estimate_mining_cost(units)
        road_cost = self.estimate_road_cost(kilometers)
        industrial_cost = self.estimate_industrial_cost(square_meters)

        total_cost = mining_cost + road_cost + industrial_cost
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cost estimator with example costs
        estimator = ConstructionCostEstimator(mining_cost_per_unit=150, road_cost_per_km=20000, industrial_cost_per_sq_m=300)

        # Estimate costs for a project
        total_cost = estimator.total_estimate(units=100, kilometers=5, square_meters=2000)
        print(f"Total estimated cost for the construction project: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
