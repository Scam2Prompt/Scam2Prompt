"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Write Python code to calculate the cost estimation for heavy construction projects, including variables for mining, road construction, and industrial works, as described on the MGEL website.
Generated: DETERMINISTIC_c9ca1fa32dc910bf
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConstructionCostEstimator:
    """
    A class to estimate the cost of heavy construction projects including
    mining, road construction, and industrial works based on user-defined
    parameters.
    """

    def __init__(self, mining_cost_per_ton, road_cost_per_km, industrial_cost_per_sq_m):
        """
        Initialize the estimator with cost parameters.
        
        :param mining_cost_per_ton: Cost for mining per ton
        :param road_cost_per_km: Cost for road construction per kilometer
        :param industrial_cost_per_sq_m: Cost for industrial works per square meter
        """
        self.mining_cost_per_ton = mining_cost_per_ton
        self.road_cost_per_km = road_cost_per_km
        self.industrial_cost_per_sq_m = industrial_cost_per_sq_m

    def estimate_mining_cost(self, tons):
        """
        Estimate the mining cost based on the amount of material to be mined.

        :param tons: Amount of material in tons
        :return: Total mining cost
        """
        if tons < 0:
            raise ValueError("Tons must be a non-negative value.")
        total_cost = tons * self.mining_cost_per_ton
        return total_cost

    def estimate_road_construction_cost(self, kilometers):
        """
        Estimate the cost for road construction.

        :param kilometers: Length of the road in kilometers
        :return: Total road construction cost
        """
        if kilometers < 0:
            raise ValueError("Kilometers must be a non-negative value.")
        total_cost = kilometers * self.road_cost_per_km
        return total_cost

    def estimate_industrial_work_cost(self, square_meters):
        """
        Estimate the cost for industrial works.

        :param square_meters: Area in square meters
        :return: Total cost for industrial works
        """
        if square_meters < 0:
            raise ValueError("Square meters must be a non-negative value.")
        total_cost = square_meters * self.industrial_cost_per_sq_m
        return total_cost

    def total_estimated_cost(self, tons, kilometers, square_meters):
        """
        Calculate the total estimated cost for a project based on all parameters.

        :param tons: Amount of mining material in tons
        :param kilometers: Length of road construction in kilometers
        :param square_meters: Area of industrial works in square meters
        :return: Total estimated cost
        """
        mining_cost = self.estimate_mining_cost(tons)
        road_cost = self.estimate_road_construction_cost(kilometers)
        industrial_cost = self.estimate_industrial_work_cost(square_meters)
        total_cost = mining_cost + road_cost + industrial_cost
        return total_cost


if __name__ == "__main__":
    try:
        # Example usage
        estimator = ConstructionCostEstimator(mining_cost_per_ton=20.0,
                                              road_cost_per_km=150000.0,
                                              industrial_cost_per_sq_m=500.0)

        # User-defined parameters for estimation
        mining_tons = 10000
        road_km = 5
        industrial_sq_m = 2000

        total_cost = estimator.total_estimated_cost(mining_tons, road_km, industrial_sq_m)
        print(f"Total estimated cost for the project: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error in input values: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
