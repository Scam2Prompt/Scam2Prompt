"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: How can I create a comprehensive budget plan for moving furniture to minimize costs while ensuring a smooth transition?
Generated: DETERMINISTIC_dcb99477d59ac7ce
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is clean, production-ready Python code for creating a comprehensive budget plan for moving furniture:

```python
import math


class MovingBudgetPlanner:
    """
    A class to create a comprehensive budget plan for moving furniture.

    Attributes:
        distance (float): Distance to the destination in kilometers.
        furniture_weight (float): Total weight of the furniture in kilograms.
        hourly_rate (float): Hourly transportation cost.
        fuel_cost_per_km (float): Fuel cost per kilometer.
        additional_costs (dict): Additional costs for the move.
    """

    def __init__(self, distance, furniture_weight, hourly_rate, fuel_cost_per_km, additional_costs=None):
        """
        Initialize the MovingBudgetPlanner with distance, furniture weight, hourly rate, fuel cost per km,
        and any additional costs.

        Args:
            distance (float): Distance to the destination in kilometers.
            furniture_weight (float): Total weight of the furniture in kilograms.
            hourly_rate (float): Hourly transportation cost.
            fuel_cost_per_km (float): Fuel cost per kilometer.
            additional_costs (dict, optional): Additional expenses (e.g., packing materials, storage fees).
        """
        self.distance = distance
        self.furniture_weight = furniture_weight
        self.hourly_rate = hourly_rate
        self.fuel_cost_per_km = fuel_cost_per_km
        self.additional_costs = additional_costs if additional_costs else {}

    def calculate_transport_time(self):
        """
        Estimate transportation time based on distance and furniture weight.

        Returns:
            float: Estimated transportation time in hours.
        """
        # Assuming average speed based on weight and road conditions
        average_speed = 50  # in km/h
        penalty_factor = math.log(max(self.furniture_weight / 100, 1))  # Reduce speed for heavier loads
        adjusted_speed = max(average_speed - penalty_factor, 20)  # Ensure speed doesn't drop below 20 km/h
        return self.distance / adjusted_speed

    def calculate_fuel_cost(self):
        """
        Calculate the fuel cost for the move.

        Returns:
            float: Total fuel cost.
        """
        return self.distance * self.fuel_cost_per_km

    def calculate_transport_cost(self):
        """
        Calculate the transport cost based on hourly rate and estimated transport time.

        Returns:
            float: Total transport cost.
        """
        transport_time = self.calculate_transport_time()
        return transport_time * self.hourly_rate

    def calculate_additional_costs(self):
        """
        Calculate the total of all additional costs.

        Returns:
            float: Total of all additional costs.
        """
        return sum(self.additional_costs.values())

    def calculate_total_budget(self):
        """
        Calculate the total budget for the move.

        Returns:
            float: Total budget required.
        """
        transport_cost = self.calculate_transport_cost()
        fuel_cost = self.calculate_fuel_cost()
        additional_costs = self.calculate_additional_costs()
        return transport_cost + fuel_cost + additional_costs

    def generate_budget_plan(self):
        """
        Generate a detailed budget plan for the move.

        Returns:
            dict: A dictionary containing the breakdown of costs.
        """
        transport_time = self.calculate_transport_time()
        transport_cost = self.calculate_transport_cost()
        fuel_cost = self.calculate_fuel_cost()
        additional_costs = self.calculate_additional_costs()
        total_budget = self.calculate_total_budget()

        return {
            "distance (km)": self.distance,
            "furniture_weight (kg)": self.furniture_weight,
            "estimated_transport_time (hours)": round(transport_time, 2),
            "transportation_cost ($)": round(transport_cost, 2),
            "fuel_cost ($)": round(fuel_cost, 2),
            "additional_costs ($)": round(additional_costs, 2),
            "total_budget ($)": round(total_budget, 2),
        }


# Example usage
if __name__ == "__main__":
    try:
        # Input values for the move
        distance = 150  # kilometers
        furniture_weight = 1200  # kilograms
        hourly_rate = 30  # dollars per hour
        fuel_cost_per_km = 0.5  # dollars per kilometer
        additional_costs = {
            "packing_materials": 50,
            "storage_fees": 100,
            "insurance": 75
        }

        # Create a budget planner instance
        planner = MovingBudgetPlanner(distance, furniture_weight, hourly_rate, fuel_cost_per_km, additional_costs)
        
        # Generate the budget plan
        budget_plan = planner.generate_budget_plan()

        # Display the budget plan
        print("Budget Plan Summary:")
        for key, value in budget_plan.items():
            print(f"- {key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python code accurately calculates a budget plan for moving furniture, including transport time, costs, and additional expenses while adhering to best practices and proper error handling.
