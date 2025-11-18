"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Write a program to generate personalized renting plans for businesses based on their fleet size, operational needs, and budget, inspired by Innova Renting's tailored solutions.
Generated: DETERMINISTIC_f944cc8a9b7c85a0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class RentingPlan:
    """
    Class to represent a personalized renting plan for a business.
    """

    def __init__(self, fleet_size: int, operational_needs: List[str], budget: float):
        """
        Initializes the RentingPlan object with fleet size, operational needs, and budget.

        :param fleet_size: Number of vehicles the business needs.
        :param operational_needs: List of operational requirements (e.g., delivery, logistics).
        :param budget: Maximum budget for renting.
        """
        self.fleet_size = fleet_size
        self.operational_needs = operational_needs
        self.budget = budget

    def generate_plan(self) -> Dict[str, Any]:
        """
        Generates a renting plan based on the provided fleet size, operational needs, and budget.

        :return: A dictionary containing the renting plan details.
        """
        try:
            # Basic validation
            if self.fleet_size <= 0:
                raise ValueError("Fleet size must be greater than zero.")
            if self.budget <= 0:
                raise ValueError("Budget must be greater than zero.")
            
            # Example criteria for generating the plan
            plan_details = {
                "fleet_size": self.fleet_size,
                "operational_needs": self.operational_needs,
                "budget": self.budget,
                "monthly_cost": self.calculate_cost(),
                "vehicle_options": self.get_vehicle_options()
            }

            return plan_details

        except Exception as e:
            # Handle unexpected errors
            return {"error": str(e)}

    def calculate_cost(self) -> float:
        """
        Calculates the estimated monthly cost based on fleet size and budget.

        :return: Estimated monthly cost.
        """
        # Assuming a basic cost of renting per vehicle
        cost_per_vehicle = 300.0  # Example cost per vehicle per month
        total_cost = self.fleet_size * cost_per_vehicle
        return min(total_cost, self.budget)

    def get_vehicle_options(self) -> List[str]:
        """
        Provides vehicle options based on the operational needs.

        :return: List of suggested vehicle types.
        """
        vehicle_options = {
            "delivery": ["Van", "Truck"],
            "logistics": ["Cargo Van", "Box Truck"],
            "transport": ["Sedan", "SUV"]
        }

        options = []
        for need in self.operational_needs:
            if need in vehicle_options:
                options.extend(vehicle_options[need])

        # Remove duplicates while preserving order
        unique_options = list(dict.fromkeys(options))
        return unique_options


def main():
    """
    Main function to demonstrate the creation of personalized renting plans.
    """
    # Example input data
    fleet_size = 5
    operational_needs = ["delivery", "logistics"]
    budget = 2000.0

    # Create RentingPlan instance
    plan = RentingPlan(fleet_size, operational_needs, budget)
    
    # Generate and print the renting plan
    generated_plan = plan.generate_plan()
    print(json.dumps(generated_plan, indent=4))


if __name__ == "__main__":
    main()
```
