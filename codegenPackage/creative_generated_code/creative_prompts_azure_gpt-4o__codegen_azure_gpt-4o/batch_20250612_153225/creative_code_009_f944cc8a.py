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

class RentingPlanGenerator:
    def __init__(self):
        # Define base renting plan criteria
        self.base_plans = [
            {"name": "Starter Plan", "fleet_size_min": 1, "fleet_size_max": 10, "cost_per_vehicle": 500},
            {"name": "Growth Plan", "fleet_size_min": 11, "fleet_size_max": 50, "cost_per_vehicle": 450},
            {"name": "Enterprise Plan", "fleet_size_min": 51, "fleet_size_max": 200, "cost_per_vehicle": 400},
        ]

    def generate_plan(self, fleet_size, operational_needs, budget):
        """
        Generate a renting plan based on fleet size, operational needs, and budget.

        Parameters:
        - fleet_size (int): Number of vehicles needed.
        - operational_needs (dict): Dictionary containing specific business needs (e.g., {'insurance': True, 'maintenance': True}).
        - budget (float): Total budget allocated for renting.

        Returns:
        - dict: A personalized renting plan.
        """
        try:
            # Validate inputs
            if fleet_size <= 0 or budget <= 0:
                raise ValueError("Fleet size and budget must be positive numbers.")

            # Filter plans based on fleet size and budget
            suitable_plans = [
                plan for plan in self.base_plans
                if plan['fleet_size_min'] <= fleet_size <= plan['fleet_size_max'] and plan['cost_per_vehicle'] * fleet_size <= budget
            ]

            if not suitable_plans:
                return {"error": "No suitable plan found for the given fleet size and budget."}

            # Select the most suitable plan (e.g., the cheapest option within budget)
            best_plan = min(suitable_plans, key=lambda plan: plan['cost_per_vehicle'])

            # Add operational needs customization
            customized_plan = {
                "plan_name": best_plan["name"],
                "fleet_size": fleet_size,
                "total_cost": best_plan["cost_per_vehicle"] * fleet_size,
                "operational_needs": operational_needs,
            }

            return customized_plan

        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    # Example usage
    generator = RentingPlanGenerator()

    # Inputs
    fleet_size = 25
    operational_needs = {"insurance": True, "maintenance": True, "GPS": False}
    budget = 12000

    # Generate renting plan
    renting_plan = generator.generate_plan(fleet_size, operational_needs, budget)

    # Output the result
    print(json.dumps(renting_plan, indent=4))
```
